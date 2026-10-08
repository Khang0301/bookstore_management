"""TV4 - Xóa sách."""
from doc_sach import file_io


def xoa_sach(ma_sach):
    """Xóa cuốn sách theo mã. Trả về (True/False, thông báo)."""
    ds = file_io.doc_sach()
    ds_moi = [s for s in ds if s["ma_sach"] != ma_sach]
    if len(ds_moi) == len(ds):
        return False, "Không tìm thấy sách cần xóa."
    ok, tb = file_io.ghi_sach(ds_moi)
    if not ok:
        return False, tb
    return True, "Xóa sách thành công."
