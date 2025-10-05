# Mô hình hồi quy tuyến tính đơn

Dự án này cung cấp một script Python (`regression.py`) để ước lượng mô hình hồi quy tuyến tính đơn giữa điểm SAT và GPA đại học.

## Cài đặt

Script yêu cầu Python 3.8+ cùng với các thư viện phụ thuộc:

```bash
pip install pandas scikit-learn
```

## Sử dụng

Chạy mô hình bằng cách cung cấp đường dẫn tới tệp CSV chứa dữ liệu với hai cột bắt buộc: `sat` và `colgpa`.

```bash
python regression.py path/to/data.csv
```

Nếu một trong hai cột bị thiếu, chương trình sẽ hiển thị thông báo lỗi mô tả rõ cột nào còn thiếu.

### Ví dụ

```bash
python regression.py data/college_scores.csv
```

Đầu ra bao gồm hệ số chặn, hệ số góc (slope), hệ số xác định R² và một diễn giải ngắn gọn về ý nghĩa của hệ số góc.
