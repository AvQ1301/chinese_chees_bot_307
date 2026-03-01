# Kiến trúc hệ thống - System Architecture

## Tổng quan

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CHINESE CHESS ROBOT                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────┐              │
│  │  Camera   │───►│ Vision Module │───►│  FEN Export   │             │
│  └──────────┘    └──────────────┘    └──────┬───────┘              │
│                                             │                       │
│                                             ▼                       │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────┐              │
│  │  Robot    │◄───│   Motion     │◄───│ Chess Engine  │             │
│  │  Arm      │    │  Planning    │    │ (Pikafish)    │             │
│  └──────────┘    └──────────────┘    └──────────────┘              │
│       │                                     ▲                       │
│       ▼                                     │                       │
│  ┌──────────┐                        ┌──────────────┐              │
│  │ Arduino  │                        │ Game Manager  │              │
│  │ (MCU)    │                        │ State Machine │              │
│  └──────────┘                        └──────────────┘              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Các module chính

### 1. Vision Module (`software/vision/`)
- **Detection**: Nhận diện quân cờ sử dụng YOLOv8
- **Calibration**: Hiệu chuẩn camera
- **FEN Export**: Chuyển đổi trạng thái bàn cờ sang ký hiệu FEN

### 2. Chess Engine (`software/chess_engine/`)
- Tích hợp Pikafish (Chinese Chess engine)
- Giao tiếp qua UCI protocol

### 3. Control Module (`software/control/`)
- **Kinematics**: Tính toán động học thuận/ngược cho SCARA
- **Motion Planning**: Lập quỹ đạo di chuyển
- **Serial Communication**: Giao tiếp Raspberry Pi ↔ Arduino

### 4. Firmware (`firmware/`)
- Điều khiển stepper motors
- Điều khiển gripper
- Nhận lệnh từ Pi qua Serial

### 5. Game Manager (`software/game_manager/`)
- Quản lý trạng thái ván cờ
- State machine: IDLE → DETECT → THINK → MOVE → WAIT

## Luồng xử lý chính

1. Camera chụp ảnh bàn cờ
2. Vision module nhận diện vị trí quân cờ
3. FEN export tạo chuỗi FEN
4. Gửi FEN cho Pikafish → nhận best move
5. Motion planning tính quỹ đạo
6. Gửi lệnh cho Arduino → robot di chuyển quân
7. Chờ người chơi đi → lặp lại
