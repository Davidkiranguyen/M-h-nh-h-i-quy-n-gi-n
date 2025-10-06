# Mô hình hồi quy tuyến tính đơn

Dự án này cung cấp một script Python (`regression.py`) để ước lượng mô hình hồi quy tuyến tính đơn giữa điểm SAT và GPA đại học.

## Cài đặt

Script yêu cầu Python 3.8+ cùng với các thư viện phụ thuộc:

```bash
pip install pandas scikit-learn
```

## Sử dụng

### Chạy trực tiếp trong VS Code

1. Mở thư mục dự án trong VS Code.
2. Đảm bảo đã cài đặt tiện ích mở rộng **Python** của Microsoft.
3. Mở tab **Run and Debug** (hoặc nhấn `Ctrl+Shift+D`) và chọn cấu hình **Run regression.py**.
4. Nhấn **Start Debugging** (`F5`). VS Code sẽ yêu cầu bạn nhập đường dẫn tới tệp CSV chứa dữ liệu với hai cột bắt buộc: `sat` và `colgpa`. Hãy nhập đường dẫn đến tệp của chính bạn (ví dụ: `C:/Users/ban/Documents/dataset.csv`).
5. Sau khi cung cấp đường dẫn và nhấn Enter, script sẽ chạy trong terminal tích hợp của VS Code.

Nếu một trong hai cột bị thiếu, chương trình sẽ hiển thị thông báo lỗi mô tả rõ cột nào còn thiếu.

### Chạy bằng dòng lệnh

Bạn cũng có thể chạy script trong terminal nếu muốn:

```bash
python regression.py path/to/data.csv
```

Nếu bạn không truyền đối số đường dẫn, script sẽ hỏi trực tiếp trong terminal:

```bash
python regression.py
```

```
Enter the path to the CSV file: /duong/dan/toi/du-lieu.csv
```

Đầu ra bao gồm hệ số chặn, hệ số góc (slope), hệ số xác định R² và một diễn giải ngắn gọn về ý nghĩa của hệ số góc.
