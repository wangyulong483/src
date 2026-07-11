#!/usr/bin/env bash
# health_check.sh — RDK X5 Stage3 关键话题 / 节点 / 锥桶绕行状态 健康检查
#
# 用法:
#   source /opt/ros/humble/setup.bash
#   bash health_check.sh            # 快速检查 (一次性)
#   bash health_check.sh --watch    # 持续监控 (每5s刷新)
#   bash health_check.sh --json     # JSON 输出 (供外部脚本解析)
#
# 检查范围:
#   - 关键话题存活 + 预期频率
#   - 关键节点存活
#   - 锥桶绕行状态 (/cone_bypass_debug)
#   - keepout 控制状态 (/costmap_ctrl)
#   - CPU / 内存 / 温度

set -euo pipefail

WATCH="${1:-}"
TIMEOUT=3  # ros2 topic hz 超时

# ── 期望频率 (Hz) ──────────────────────────────────────────────
declare -A EXPECTED_RATES=(
    ["/scan"]="4-6"
    ["/odom"]="15-25"
    ["/cmd_vel"]="5-25"
    ["/plan"]="0.5-3"
    ["/amcl_pose"]="2-10"
    ["/racing_obstacle_detection"]="5-20"
    ["/speed_limit"]="5-25"
    ["/aurora/rgb/image_raw"]="10-20"
    ["/local_costmap/costmap"]="1-3"
    ["/global_costmap/costmap"]="0.5-2"
    ["/cone_bypass_debug"]="0.5-5"
)

# ── 关键节点 (至少需要这些) ─────────────────────────────────────
CRITICAL_NODES=(
    "competition_master_stage3"
    "controller_server"
    "planner_server"
    "bt_navigator"
    "velocity_smoother"
)

check_topic_rate() {
    local topic="$1"
    local range="$2"
    local min_hz="${range%-*}"; local max_hz="${range#*-}"

    # 获取实际频率
    local hz_out
    hz_out=$(ros2 topic hz "$topic" --timeout "$TIMEOUT" 2>/dev/null | tail -1 | awk '{print $2}') || true
    if [[ -z "$hz_out" || "$hz_out" == "0.0" ]]; then
        echo "  ❌ $topic: NO DATA (expected $range Hz)"
        return 1
    fi
    hz_out="${hz_out%.*}"

    local status="✅"
    if (( hz_out < min_hz )); then status="⚠️ SLOW"; fi
    if (( hz_out > max_hz )); then status="⚠️ FAST"; fi
    printf "  %-4s %-45s ~%s Hz (expected %s Hz)\n" "$status" "$topic" "$hz_out" "$range"
}

check_nodes() {
    echo ""
    echo "── 关键节点存活 ──"
    local all_nodes
    all_nodes=$(ros2 node list 2>/dev/null) || true
    for node in "${CRITICAL_NODES[@]}"; do
        if echo "$all_nodes" | grep -q "$node"; then
            echo "  ✅ $node"
        else
            echo "  ❌ $node: NOT FOUND"
        fi
    done
}

check_cone_bypass() {
    echo ""
    echo "── 锥桶绕行状态 ──"
    local last_msg
    last_msg=$(ros2 topic echo /cone_bypass_debug --once --timeout 3 2>/dev/null) || true
    if [[ -z "$last_msg" ]]; then
        echo "  ⚠️  /cone_bypass_debug: NO DATA (competition_master 可能未激活)"
        return
    fi
    echo "  📡 最后消息: $last_msg"

    # 检查 keepout 是 ON 还是 OFF
    if echo "$last_msg" | grep -q '"keepout_disabled": false'; then
        echo "  🔒 keepout: ON (正常通道行驶)"
    elif echo "$last_msg" | grep -q '"keepout_disabled": true'; then
        echo "  🔓 keepout: OFF (锥桶绕行中!)"
    fi

    # 检查自由区域
    if echo "$last_msg" | grep -q '"in_free_zone": "True"'; then
        echo "  📍 机器人位置: 通道自由区内 ✅"
    elif echo "$last_msg" | grep -q '"in_free_zone": "False"'; then
        echo "  📍 机器人位置: 禁区/未知 ⚠️"
    fi
}

check_hw() {
    echo ""
    echo "── 硬件资源 ──"
    local cpu freq temp mem
    cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2+$4}' 2>/dev/null || echo "N/A")
    freq=$(cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq 2>/dev/null || echo "N/A")
    temp=$(cat /sys/class/hwmon/hwmon0/temp3_input 2>/dev/null || echo "0")
    mem=$(free | grep Mem | awk '{printf "%.0f", $3/$2*100}' 2>/dev/null || echo "N/A")

    printf "  CPU: %s%%  Freq: %s MHz  Temp: %s°C  Mem: %s%%\n" \
        "$cpu" "$((freq / 1000))" "$((temp / 1000))" "$mem"
}

check_all() {
    local start_time
    start_time=$(date +%s)
    echo "══════════════════════════════════════════════════════════"
    echo "  RDK X5 Stage3 健康检查"
    echo "  时间: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "══════════════════════════════════════════════════════════"

    check_nodes

    echo ""
    echo "── 关键话题频率 (${TIMEOUT}s 超时) ──"
    local failed=0
    for topic in "${!EXPECTED_RATES[@]}"; do
        check_topic_rate "$topic" "${EXPECTED_RATES[$topic]}" || ((failed++)) || true
    done
    if (( failed > 0 )); then
        echo "  ⚠️  $failed 个话题异常"
    fi

    check_cone_bypass
    check_hw

    local elapsed
    elapsed=$(($(date +%s) - start_time))
    echo ""
    echo "══════════════════════════════════════════════════════════"
    echo "  检查完成 (耗时 ${elapsed}s)"
    echo "══════════════════════════════════════════════════════════"
}

# ── 主入口 ───────────────────────────────────────────────────────
case "$WATCH" in
    --watch)
        echo "🔁 持续监控模式 (Ctrl+C 退出)..."
        while true; do
            clear 2>/dev/null || true
            check_all
            sleep 5
        done
        ;;
    --json)
        # 最小 JSON 摘要 (供外部脚本解析)
        echo "{"
        echo "  \"time\": \"$(date -Iseconds)\","
        for topic in "${!EXPECTED_RATES[@]}"; do
            local hz
            hz=$(ros2 topic hz "$topic" --timeout "$TIMEOUT" 2>/dev/null | tail -1 | awk '{print $2}' || echo "0.0")
            echo "  \"${topic//\//_}\": ${hz:-0.0},"
        done
        echo "  \"nodes\": {"
        for node in "${CRITICAL_NODES[@]}"; do
            local alive="false"
            ros2 node list 2>/dev/null | grep -q "$node" && alive="true"
            echo "    \"$node\": $alive,"
        done
        echo "  }"
        echo "}"
        ;;
    *)
        check_all
        ;;
esac
