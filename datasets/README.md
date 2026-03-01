# Datasets

## Mô tả

Thư mục này chứa dataset huấn luyện cho module nhận diện quân cờ tướng.

## Dataset nhận diện quân cờ

- **Số lượng ảnh**: TBD
- **Số class**: 14 (7 quân đỏ + 7 quân đen)
- **Format**: YOLO format (txt annotations)
- **Augmentation**: Có (xem `30_CV/Chessrobot/dataAugment.py`)

### Các class quân cờ

| ID | Quân (Đỏ) | Quân (Đen) |
|----|-----------|-----------|
| 0  | Tướng (帥) | Tướng (將) |
| 1  | Sĩ (仕)   | Sĩ (士)   |
| 2  | Tượng (相) | Tượng (象) |
| 3  | Xe (俥)   | Xe (車)   |
| 4  | Pháo (炮) | Pháo (砲) |
| 5  | Mã (傌)   | Mã (馬)   |
| 6  | Tốt (兵)  | Tốt (卒)  |

## Download

> Dataset quá lớn để lưu trên GitHub. Tải tại link sau:
> - Google Drive: TBD
> - Hoặc liên hệ nhóm Lab307

## Cấu trúc dataset

```
datasets/
├── README.md
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```
