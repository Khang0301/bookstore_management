# Quản lý cửa hàng sách (Python + Flask + CSV)

Website nhỏ quản lý sách với 4 chức năng: **Đọc (xem danh sách), Thêm, Sửa, Xóa**.
Dữ liệu lưu trong file `data/books.csv` (không dùng database).

## Công nghệ
Python 3, Flask, module `csv` có sẵn, HTML + CSS thuần + JavaScript cơ bản.

## Cài đặt và chạy (Windows)
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```
Mở trình duyệt: http://127.0.0.1:5000  (luôn chạy từ thư mục gốc của project)

## Cấu trúc thư mục
```
app/main.py            Khởi tạo Flask, đăng ký các route
doc_sach/              Đọc: file_io.py (đọc/ghi CSV), routes.py (trang danh sách)
them_sach/             Thêm: them.py (thêm + kiểm tra hợp lệ), routes.py
sua_sach/              Sửa:  sua.py, routes.py
xoa_sach/              Xóa:  xoa.py, routes.py
templates/             Giao diện HTML (base, books, add, edit, _form)
static/                style.css, script.js
data/books.csv         Dữ liệu
docs/                  Báo cáo
```

## Quy ước dữ liệu
Mỗi sách là một dictionary:
`{"ma_sach": "S001", "ten_sach": "Nhà Giả Kim", "tac_gia": "Paulo Coelho", "gia": 79000, "so_luong": 15}`
CSV có tiêu đề `ma_sach,ten_sach,tac_gia,gia,so_luong`. Giá và số lượng là số nguyên.
Các hàm thêm/sửa/xóa/ghi trả về `(True/False, "thông báo tiếng Việt")`.

## Phân công
| Thành viên | Chức năng | File |
|---|---|---|
| TV1 | Thêm sách + kiểm tra hợp lệ | `them_sach/` |
| TV2 | Đọc: đọc/ghi CSV, danh sách | `doc_sach/`, `app/main.py` |
| TV3 | Sửa sách | `sua_sach/` |
| TV4 | Xóa sách | `xoa_sach/` |
| TV5 | Báo cáo, giao diện chung | `docs/`, `templates/base.html`, `static/` |
