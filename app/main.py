"""Điểm khởi chạy website. Chạy từ thư mục gốc:  python -m app.main"""
from pathlib import Path
from flask import Flask

from doc_sach.routes import bp as bp_doc
from them_sach.routes import bp as bp_them
from sua_sach.routes import bp as bp_sua
from xoa_sach.routes import bp as bp_xoa

GOC = Path(__file__).resolve().parent.parent

app = Flask(__name__, template_folder=str(GOC / "templates"), static_folder=str(GOC / "static"))
app.secret_key = "cua-hang-sach-do-an-python"   # cần cho flash()

for bp in (bp_doc, bp_them, bp_sua, bp_xoa):
    app.register_blueprint(bp)


@app.template_filter("tien")
def dinh_dang_tien(so):
    """79000 -> '79.000 đ'"""
    return f"{so:,}".replace(",", ".") + " đ"


if __name__ == "__main__":
    app.run(debug=True)
