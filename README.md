# CCR3 - Chinese Chess Robot 🤖♟️

> Robot chơi cờ tướng tự động sử dụng Computer Vision, AI Engine và cánh tay SCARA – Dự án của nhóm Lab307.

## Tổng quan

**Chinese Chess Robot (CCR3)** là hệ thống robot có khả năng:
- 📷 Nhận diện bàn cờ tướng và các quân cờ qua camera (YOLO)
- 🧠 Tính toán nước đi tối ưu bằng engine Pikafish
- 🦾 Điều khiển cánh tay robot SCARA để gắp và di chuyển quân cờ
- 🎮 Chơi đối kháng với người chơi trong thời gian thực

## Kiến trúc hệ thống

```
Camera  ──►  Vision Module  ──►  FEN Export  ──►  Chess Engine (Pikafish)
                                                         │
                                                         ▼
Player  ◄──  Robot Arm (SCARA)  ◄──  Motion Planning  ◄──  Best Move
```

## Cấu trúc thư mục

```
CCR3-ChineseChessRobot/
├── docs/              # Tài liệu dự án
├── hardware/          # Thiết kế phần cứng (CAD, PCB, BOM)
├── firmware/          # Code Arduino/MCU (PlatformIO)
├── software/          # Code chính (Vision, Control, Engine, UI)
├── simulation/        # Mô phỏng (URDF, MATLAB, Gazebo)
├── datasets/          # Dataset huấn luyện
├── tests/             # Unit tests & Integration tests
└── scripts/           # Scripts tiện ích (setup, run)
```

## Yêu cầu hệ thống

### Phần cứng
- Raspberry Pi 4B (hoặc PC)
- Arduino Mega 2560
- Camera (USB hoặc Pi Camera)
- Cánh tay SCARA (custom)
- Stepper motors + drivers

### Phần mềm
- Python 3.9+
- OpenCV
- YOLOv8 (Ultralytics)
- Pikafish chess engine
- PlatformIO (firmware)

## Cài đặt nhanh

```bash
# Clone repository
git clone https://github.com/AvQ1301/chinese_chees_bot_307.git
cd chinese_chees_bot_307

# Chạy script cài đặt
chmod +x scripts/setup.sh
./scripts/setup.sh

# Chạy hệ thống
./scripts/run.sh
```

## Thành viên nhóm

| Tên | Vai trò |
|-----|---------|
| TBD | Vision / CV |
| TBD | Control / Kinematics |
| TBD | Hardware / Mechanical |
| TBD | Firmware / Electronics |

## License

Dự án này được phân phối theo giấy phép [MIT](LICENSE).

## Liên hệ

- **Lab307** – Hanoi University of Science and Technology (HUST)
- GitHub: [AvQ1301](https://github.com/AvQ1301)
CCR3 - Chinese Chess Robot project by Lab307 team. A robotic system that plays Chinese Chess (Xiangqi) using computer vision, AI engine, and SCARA robot arm.
