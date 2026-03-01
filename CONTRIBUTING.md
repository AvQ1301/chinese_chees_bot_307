# Hướng dẫn đóng góp - Contributing Guide

Cảm ơn bạn đã quan tâm đến dự án **CCR3 - Chinese Chess Robot**! 🎉

## Quy trình đóng góp

### 1. Fork & Clone
```bash
git clone https://github.com/<your-username>/chinese_chees_bot_307.git
cd chinese_chees_bot_307
```

### 2. Tạo branch mới
```bash
git checkout -b feature/ten-tinh-nang
# hoặc
git checkout -b fix/ten-loi
```

### 3. Quy tắc đặt tên branch
- `feature/` – Tính năng mới
- `fix/` – Sửa lỗi
- `docs/` – Cập nhật tài liệu
- `refactor/` – Tái cấu trúc code

### 4. Commit message
Sử dụng format:
```
<type>: <mô tả ngắn>

<mô tả chi tiết (nếu cần)>
```

Ví dụ:
```
feat: thêm module nhận diện quân cờ bằng YOLOv8
fix: sửa lỗi tính toán động học ngược
docs: cập nhật sơ đồ đấu nối điện
```

### 5. Pull Request
- Mô tả rõ ràng thay đổi
- Đính kèm ảnh/video nếu có
- Tag reviewer phù hợp

## Quy tắc code

- **Python**: Tuân thủ PEP 8
- **C/C++ (firmware)**: Sử dụng camelCase cho biến, PascalCase cho class
- Comment bằng tiếng Việt hoặc tiếng Anh đều được
- Viết unit test cho các module quan trọng

## Cấu trúc thư mục

Vui lòng đặt file đúng thư mục theo cấu trúc đã quy định trong README.

## Liên hệ

Nếu có thắc mắc, vui lòng tạo Issue hoặc liên hệ trực tiếp qua nhóm Lab307.
