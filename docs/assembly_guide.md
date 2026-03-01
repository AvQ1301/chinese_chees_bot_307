# Hướng dẫn lắp ráp - Assembly Guide

## Yêu cầu dụng cụ

- Bộ cờ lê Allen
- Tua vít
- Kìm cắt
- Mỏ hàn (cho mạch điện)
- Máy in 3D (cho các chi tiết in)

## Các bước lắp ráp

### Bước 1: Chuẩn bị chi tiết
- [ ] In 3D các chi tiết từ thư mục `hardware/3d_models/stl/`
- [ ] Kiểm tra BOM và chuẩn bị đầy đủ linh kiện

### Bước 2: Lắp ráp khung robot
- [ ] Lắp base frame
- [ ] Lắp khớp 1 (Joint 1)
- [ ] Lắp link 1
- [ ] Lắp khớp 2 (Joint 2)
- [ ] Lắp link 2
- [ ] Lắp end-effector / gripper

### Bước 3: Lắp motor và truyền động
- [ ] Gắn stepper motors vào các khớp
- [ ] Lắp pulley và belt
- [ ] Căn chỉnh belt tension

### Bước 4: Lắp điện tử
- [ ] Kết nối theo sơ đồ `docs/wiring_diagram.md`
- [ ] Lắp Arduino và drivers
- [ ] Lắp Raspberry Pi
- [ ] Lắp camera

### Bước 5: Kiểm tra
- [ ] Test từng motor riêng lẻ
- [ ] Test gripper
- [ ] Test camera
- [ ] Chạy calibration

> **Chi tiết hình ảnh minh họa sẽ được thêm vào `docs/images/`**
