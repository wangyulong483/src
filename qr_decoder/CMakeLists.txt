cmake_minimum_required(VERSION 3.5)
project(qr_decoder)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(OpenCV REQUIRED)

add_executable(qr_decoder src/qr_decoder.cpp)
ament_target_dependencies(qr_decoder rclcpp sensor_msgs nav_msgs geometry_msgs std_msgs cv_bridge)

# link zbar library
find_package(PkgConfig REQUIRED)
pkg_search_module(ZBAR REQUIRED zbar)
target_link_libraries(qr_decoder ${ZBAR_LIBRARIES})
target_include_directories(qr_decoder PUBLIC ${ZBAR_INCLUDE_DIRS})

target_link_libraries(qr_decoder
  ${OpenCV_LIBS}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(TARGETS
  qr_decoder
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  qr_decision.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
