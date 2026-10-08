"""TV1 - Thêm sách và kiểm tra dữ liệu hợp lệ (dùng chung cho cả nhóm)."""
from doc_sach import file_io


def _la_so_nguyen_khong_am(gia_tri):
    """'15' -> True ; '-5', '8.5', 'abc', '' -> False"""
    return str(gia_tri).strip().isdigit()


def kiem_tra_hop_le(sach, ds, bo_qua_ma=None):
    """Kiểm tra 1 cuốn sách. Trả về (True/False, thông báo).
    bo_qua_ma: dùng khi sửa, để không báo trùng với chính cuốn đang sửa."""
    ma = str(sach.get("ma_sach", "")).strip()
    if not ma:
        return False, "Mã sách không được để trống."
    if any(s["ma_sach"].lower() == ma.lower() and s["ma_sach"] != bo_qua_ma for s in ds):
        return False, "Mã sách đã tồn tại."
    if not str(sach.get("ten_sach", "")).strip():
        return False, "Tên sách không được để trống."
    if not str(sach.get("tac_gia", "")).strip():
        return False, "Tác giả không được để trống."
    if not _la_so_nguyen_khong_am(sach.get("gia", "")):
        return False, "Giá phải là số nguyên từ 0 trở lên (ví dụ 79000)."
    if not _la_so_nguyen_khong_am(sach.get("so_luong", "")):
        return False, "Số lượng phải là số nguyên từ 0 trở lên."
    return True, "Hợp lệ."


def chuan_hoa(sach):
    """Cắt khoảng trắng, đổi giá và số lượng sang int (gọi SAU khi đã kiểm tra hợp lệ)."""
    return {
        "ma_sach": str(sach["ma_sach"]).strip(),
        "ten_sach": str(sach["ten_sach"]).strip(),
        "tac_gia": str(sach["tac_gia"]).strip(),
        "gia": int(str(sach["gia"]).strip()),
        "so_luong": int(str(sach["so_luong"]).strip()),
    }


def them_sach(sach):
    """Thêm 1 cuốn sách vào CSV. Trả về (True/False, thông báo)."""
    ds = file_io.doc_sach()
    hop_le, thong_bao = kiem_tra_hop_le(sach, ds)
    if not hop_le:
        return False, thong_bao
    ds.append(chuan_hoa(sach))
    ok, tb = file_io.ghi_sach(ds)
    if not ok:
        return False, tb
    return True, "Thêm sách thành công."
