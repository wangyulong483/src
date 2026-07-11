#!/bin/bash
# toggle_keepout.sh — 手动标定路点时临时禁用/恢复禁区
# 用法:
#   bash toggle_keepout.sh off   → 禁用keepout (标定用, 车可自由行驶)
#   bash toggle_keepout.sh on    → 恢复keepout (标定完成后)
#   bash toggle_keepout.sh status → 查看当前状态
#
# 原理解释: 弯道上Ackermann车无法完美跟随路径, 转弯时车头/车尾会切过禁区边缘.
# 禁区边缘就是通道边界 (binary mask 原边界), LETHAL 像素紧邻通道,
# 任何转弯误差 >0.10m 就让足迹撞进 LETHAL → 卡死.
# 标定期间禁用辖区, 标定完再恢复.

ACTION=${1:-status}

if [ "$ACTION" = "off" ]; then
    echo "[KEEPOUT] 禁用禁区 (标定模式) ..."
    ros2 topic pub /costmap_ctrl nav2_msgs/msg/CostmapFilterInfo \
      "{type: 0, filter_mask_topic: '/keepout_disabled', base: 100.0, multiplier: -1.0}" --once
    # 同时清空 costmap 中残留的禁区成本
    ros2 service call /global_costmap/clear_entirely_global_costmap nav2_msgs/srv/ClearEntireCostmap "{}" 2>/dev/null
    ros2 service call /local_costmap/clear_entirely_local_costmap nav2_msgs/srv/ClearEntireCostmap "{}" 2>/dev/null
    echo "[KEEPOUT] ✓ 已禁用. 标定完成后运行: bash toggle_keepout.sh on"

elif [ "$ACTION" = "on" ]; then
    echo "[KEEPOUT] 恢复禁区 ..."
    ros2 topic pub /costmap_ctrl nav2_msgs/msg/CostmapFilterInfo \
      "{type: 0, filter_mask_topic: '/keepout_mask', base: 100.0, multiplier: -1.0}" --once
    ros2 service call /global_costmap/clear_entirely_global_costmap nav2_msgs/srv/ClearEntireCostmap "{}" 2>/dev/null
    ros2 service call /local_costmap/clear_entirely_local_costmap nav2_msgs/srv/ClearEntireCostmap "{}" 2>/dev/null
    echo "[KEEPOUT] ✓ 已恢复"

elif [ "$ACTION" = "status" ]; then
    echo "[KEEPOUT] 当前 /costmap_ctrl 最后一条消息:"
    ros2 topic echo /costmap_ctrl nav2_msgs/msg/CostmapFilterInfo --once 2>/dev/null || \
      echo "  (无法读取, 可能没有发布者)"
else
    echo "用法: bash toggle_keepout.sh [off|on|status]"
fi
