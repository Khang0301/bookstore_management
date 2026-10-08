"""TV2 - Đọc và ghi file CSV. Mọi module khác chỉ đọc/ghi qua 2 hàm ở đây."""
import csv
from pathlib import Path

# Đường dẫn tính từ vị trí file này, không phụ thuộc thư mục đang chạy
DUONG_DAN_CSV = Path(__file__).resolve().parent.parent / "data" / "books.csv"
TIEU_DE = ["ma_sach", "ten_sach", "tac_gia", "gia", "so_luong"]


def doc_sach():
    """Đọc books.csv, trả về list dictionary (sắp theo mã sách).
    File chưa có, file rỗng hoặc sai tiêu đề -> trả về list rỗng.
    Dòng bị lỗi định dạng (giá/số lượng không phải số) -> bỏ qua dòng đó."""
    if not DUONG_DAN_CSV.exists():
        return []
    ds = []
    try:
        with open(DUONG_DAN_CSV, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None or not set(TIEU_DE).issubset(reader.fieldnames):
                return []
            for dong in reader:
                try:
                    ds.append({
                        "ma_sach": (dong["ma_sach"] or "").strip(),
                        "ten_sach": (dong["ten_sach"] or "").strip(),
                        "tac_gia": (dong["tac_gia"] or "").strip(),
                        "gia": int(dong["gia"]),
                        "so_luong": int(dong["so_luong"]),
                    })
                except (ValueError, TypeError):
                    continue
    except (OSError, csv.Error):
        return []
    ds.sort(key=lambda s: s["ma_sach"])
    return ds


def ghi_sach(ds):
    """Ghi toàn bộ danh sách vào books.csv. Trả về (True/False, thông báo)."""
    try:
        DUONG_DAN_CSV.parent.mkdir(parents=True, exist_ok=True)
        with open(DUONG_DAN_CSV, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=TIEU_DE)
            writer.writeheader()
            for s in ds:
                writer.writerow({k: s[k] for k in TIEU_DE})
        return True, "Ghi file thành công."
    except OSError:
        return False, "Không ghi được file. Hãy đóng file books.csv nếu đang mở bằng Excel rồi thử lại."
