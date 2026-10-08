"""TV3 - Sửa thông tin sách."""
from doc_sach import file_io
from them_sach import them   # dùng lại hàm kiểm tra của TV1, không tự viết lại


def lay_sach(ma_sach):
    """Trả về dict của cuốn sách, hoặc None nếu không tồn tại."""
    for s in file_io.doc_sach():
        if s["ma_sach"] == ma_sach:
            return dict(s)
    return None


def sua_sach(ma_sach, thong_tin_moi):
    """Sửa tên, tác giả, giá, số lượng (KHÔNG cho đổi mã sách).
    Trả về (True/False, thông báo)."""
    ds = file_io.doc_sach()
    vi_tri = next((i for i, s in enumerate(ds) if s["ma_sach"] == ma_sach), None)
    if vi_tri is None:
        return False, "Không tìm thấy sách cần sửa."
    sach_moi = {
        "ma_sach": ma_sach,
        "ten_sach": thong_tin_moi.get("ten_sach", ""),
        "tac_gia": thong_tin_moi.get("tac_gia", ""),
        "gia": thong_tin_moi.get("gia", ""),
        "so_luong": thong_tin_moi.get("so_luong", ""),
    }
    hop_le, thong_bao = them.kiem_tra_hop_le(sach_moi, ds, bo_qua_ma=ma_sach)
    if not hop_le:
        return False, thong_bao
    ds[vi_tri] = them.chuan_hoa(sach_moi)
    ok, tb = file_io.ghi_sach(ds)
    if not ok:
        return False, tb
    return True, "Cập nhật sách thành công."
