# Form CMS

Tác giả: PM - TKC

v0.1.0 – pilot; A01/A05 chờ COO duyệt D-07a/D-07b, trước đó chỉ dùng dữ liệu SIM.

Tên menu cần kiểm lại theo giao diện được phê duyệt. Chỉ người có quyền thực hiện các ô nhạy cảm/ghi; dữ liệu Đỏ không đưa vào AI. Nếu trang có trường Đỏ, AI dừng, không đọc giá trị. Không được hiểu bảng này là quyền sửa trường đang bị guardrails cấm.

## Quản trị → Đối tác, Quản trị → Thương hiệu

Dùng skill hi1-mo-shop (AI điền tới trước Tạo mới, gồm số tài khoản công ty và logo; người nhập mật khẩu và tải ảnh giấy tờ).

## Quản trị → Quản lý sản phẩm

| Trường | Nguồn dữ liệu | Ai điền |
|---|---|---|
| Đối tác | Hồ sơ đúng merchant_id, chọn trước Danh mục/Thương hiệu | AI điền, người duyệt từng lần |
| Danh mục, Thương hiệu | Danh mục đã có, đúng dữ kiện | AI đề xuất, không tự tạo mới; không thấy đúng thì dừng |
| Tên, mô tả ngắn, mô tả, HDSD, hashtag | Nháp đã người duyệt, hồ sơ công bố hiện hành | AI điền, người duyệt từng lần |
| Ảnh chính/slide, chọn tệp | File đã kiểm | Người; AI không upload |
| Giá gốc, giá hội viên, giá liên hệ, tồn | Bảng giá/dữ kiện được nhà bán xác nhận | Người; AI không sửa |
| Xuất xứ, chứng nhận, thời hạn | Hồ sơ chính thức được xác nhận | Người |
| Khối lượng gam, quy cách, biến thể, chủng loại | Dữ kiện xác nhận, thuộc tính đã có | Người; AI chỉ chuẩn bị nháp, không tạo thuộc tính mới |
| Trạng thái, vận chuyển, hot, miễn phí vận chuyển, giới hạn tỉnh, affiliate/tỷ lệ | Chính sách và phụ lục đã duyệt | Người; không mặc định bật/tắt |
| Hỗ trợ/CSKH | Kênh được xác nhận | Người, không đưa PII vào AI |
| Lưu/Tạo mới | Người kiểm bảng tóm tắt trước lưu | Người |

Tìm trùng trước tạo; tải lại khi mở form tạo mới; không mở chế độ sửa rồi lưu. AI dừng trước Lưu và báo trường, nguồn, điểm chưa xác nhận, người thực hiện. A01 vào M3 trước theo lệnh từng lần; A05 tối đa M3. Không tự nâng mức.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ
