// Hộp xác nhận trước khi xóa sách
function xacNhanXoa(form) {
  return confirm("Bạn có chắc muốn xóa sách \"" + form.dataset.ten + "\"?");
}
