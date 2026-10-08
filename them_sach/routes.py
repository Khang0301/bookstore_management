"""TV1 - Trang thêm sách."""
from flask import Blueprint, render_template, request, redirect, flash
from them_sach import them

bp = Blueprint("them", __name__)


@bp.route("/add", methods=["GET", "POST"])
def them_moi():
    if request.method == "POST":
        sach = {
            "ma_sach": request.form.get("ma_sach", ""),
            "ten_sach": request.form.get("ten_sach", ""),
            "tac_gia": request.form.get("tac_gia", ""),
            "gia": request.form.get("gia", ""),
            "so_luong": request.form.get("so_luong", ""),
        }
        ok, thong_bao = them.them_sach(sach)
        if ok:
            flash(thong_bao, "ok")
            return redirect("/books")
        flash(thong_bao, "loi")
        return render_template("add.html", sach=sach)   # giữ lại dữ liệu đã nhập
    return render_template("add.html", sach={})
