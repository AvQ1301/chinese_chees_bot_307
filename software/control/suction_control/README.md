# Suction Control Module

ROS 2 module điều khiển giác hút chân không cho robot chơi cờ tướng CCR3.

## Chức năng

- **pick(x, y, z)**: Gắp quân cờ tại vị trí (x, y, z)
- **place(x, y, z)**: Đặt quân cờ tại vị trí (x, y, z)
- **check_suction()**: Kiểm tra trạng thái hút
- **pump_on/off**: Bật/tắt bơm chân không

## Cấu trúc

```
suction_control/
├── __init__.py
├── suction_control.py      # ROS 2 Node chính
├── suction_control_standalone.py  # Test không cần ROS
├── srv/
│   ├── PickChessPiece.srv
│   ├── PlaceChessPiece.srv
│   └── CheckSuction.srv
└── test/
    └── test_suction.py
```

## Cài đặt

1. **Build ROS 2 package:**
```bash
cd ~/ros2_ws
colcon build --packages-select ccr3_suction_control
source install/setup.bash
```

2. **Upload firmware lên Arduino:**
```bash
# Upload file firmware/src/suction_control.cpp lên Arduino
```

3. **Chạy Node:**
```bash
ros2 run ccr3_suction_control suction_control
```

## Test

### Với ROS 2:
```bash
ros2 run ccr3_suction_control test_suction
```

### Không cần ROS (standalone):
```bash
python3 suction_control_standalone.py /dev/ttyUSB0
```

## Kết nối Arduino

| Arduino Pin | Chức năng |
|------------|-----------|
| D2 | Điều khiển relay bơm |
| D3 | Điều khiển van xả |
| A0 | Cảm biến áp suất (optional) |

## Services

```bash
# Gắp quân cờ
ros2 service call /suction_control/pick ccr3_suction_control/srv/PickChessPiece "{x: 0.0, y: 0.0, z: 0.0}"

# Đặt quân cờ
ros2 service call /suction_control/place ccr3_suction_control/srv/PlaceChessPiece "{x: 1.0, y: 1.0, z: 0.0}"

# Kiểm tra trạng thái hút
ros2 service call /suction_control/check_suction ccr3_suction_control/srv/CheckSuction

# Bật/tắt bơm
ros2 service call /suction_control/pump_on std_srvs/srv/Trigger
ros2 service call /suction_control/pump_off std_srvs/srv/Trigger
```
