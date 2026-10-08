"""TV4 - Route xóa sách (chỉ nhận POST)."""
from flask import Blueprint, redirect, flash
from xoa_sach import xoa

bp = Blueprint("xoa", __name__)


@bp.route("/delete/<ma_sach>", methods=["POST"])
def xoa_moi(ma_sach):
    ok, thong_bao = xoa.xoa_sach(ma_sach)
    flash(thong_bao, "ok" if ok else "loi")
    return redirect("/books")
