# Sơ đồ đấu nối điện - Wiring Diagram

## Tổng quan kết nối

```
┌──────────────┐         Serial/USB          ┌──────────────┐
│              │◄───────────────────────────► │              │
│ Raspberry Pi │                              │   Arduino    │
│     4B       │         USB Camera           │  Mega 2560   │
│              │◄──── Camera ────             │              │
└──────────────┘                              └──────┬───────┘
                                                     │
                                              ┌──────┴───────┐
                                              │              │
                                        ┌─────┴─┐      ┌────┴────┐
                                        │Driver │      │ Driver  │
                                        │  #1   │      │   #2    │
                                        └───┬───┘      └────┬────┘
                                            │               │
                                        ┌───┴───┐      ┌────┴────┐
                                        │Motor  │      │ Motor   │
                                        │  #1   │      │   #2    │
                                        └───────┘      └─────────┘
```

## Chi tiết kết nối Arduino

### Stepper Motor Driver #1 (Joint 1)
| Arduino Pin | Driver Pin | Mô tả |
|-------------|------------|--------|
| TBD | STEP | Xung step |
| TBD | DIR | Hướng quay |
| TBD | EN | Enable |

### Stepper Motor Driver #2 (Joint 2)
| Arduino Pin | Driver Pin | Mô tả |
|-------------|------------|--------|
| TBD | STEP | Xung step |
| TBD | DIR | Hướng quay |
| TBD | EN | Enable |

### Servo (Gripper)
| Arduino Pin | Mô tả |
|-------------|--------|
| TBD | PWM signal |

### Endstop / Limit Switch
| Arduino Pin | Mô tả |
|-------------|--------|
| TBD | Home sensor Joint 1 |
| TBD | Home sensor Joint 2 |

## Nguồn điện

| Thiết bị | Điện áp | Dòng tối đa |
|----------|---------|-------------|
| Raspberry Pi | 5V / 3A | USB-C |
| Arduino | 5V (qua USB) | - |
| Stepper Motors | 12V / 24V | TBD |
| Servo | 5V | TBD |

> **Lưu ý**: Sơ đồ chi tiết sẽ được cập nhật khi thiết kế mạch hoàn chỉnh. Ảnh sơ đồ sẽ nằm tại `docs/images/`.
