"""TV2 - Trang danh sách sách."""
from flask import Blueprint, render_template, redirect
from doc_sach import file_io

bp = Blueprint("doc", __name__)


@bp.route("/")
def trang_chu():
    return redirect("/books")


@bp.route("/books")
def danh_sach():
    return render_template("books.html", ds=file_io.doc_sach())
