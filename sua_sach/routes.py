"""TV3 - Trang sửa sách."""
from flask import Blueprint, render_template, request, redirect, flash
from sua_sach import sua

bp = Blueprint("sua", __name__)


@bp.route("/edit/<ma_sach>", methods=["GET", "POST"])
def sua_moi(ma_sach):
    sach = sua.lay_sach(ma_sach)
    if sach is None:
        flash("Không tìm thấy sách cần sửa.", "loi")
        return redirect("/books")
    if request.method == "POST":
        thong_tin = {
            "ten_sach": request.form.get("ten_sach", ""),
            "tac_gia": request.form.get("tac_gia", ""),
            "gia": request.form.get("gia", ""),
            "so_luong": request.form.get("so_luong", ""),
        }
        ok, thong_bao = sua.sua_sach(ma_sach, thong_tin)
        if ok:
            flash(thong_bao, "ok")
            return redirect("/books")
        flash(thong_bao, "loi")
        thong_tin["ma_sach"] = ma_sach
        return render_template("edit.html", sach=thong_tin)
    return render_template("edit.html", sach=sach)
