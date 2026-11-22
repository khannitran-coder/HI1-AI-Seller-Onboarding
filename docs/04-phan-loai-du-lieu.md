# Phân loại dữ liệu

v0.1.1 – pilot, chưa COO duyệt

[CHỜ COO DUYỆT – D-02]

| Nhóm | Nội dung | Quy tắc |
|---|---|---|
| Xanh | Chính sách đã duyệt, checklist, mẫu tin, hướng dẫn giao diện | Chỉ bản APPROVED hiện hành; bản pilot không tự thành APPROVED |
| Vàng | Loại hình, ngành hàng, trạng thái, mục thiếu, tên shop, nội dung sản phẩm | [CHỜ COO DUYỆT – D-03] Chỉ dùng trên gói Claude Team/Enterprise được cho phép; tên người/SĐT thay placeholder |
| Đỏ | CCCD, STK ngân hàng, OTP, mật khẩu, token, ảnh giấy tờ tuỳ thân | Không bao giờ đưa vào AI hoặc repo |

[CHỜ COO DUYỆT – D-02] Nếu input chứa giá trị CCCD, số tài khoản ngân hàng, OTP, mật khẩu, token hoặc ảnh giấy tờ tuỳ thân: dừng ngay, không lặp lại giá trị, không xử lý hay lưu; nhắc người dùng xoá khỏi hội thoại và ghi sự cố qua người phụ trách, chỉ ghi mã SIM-xxx/loại sự cố, không ghi dữ liệu Đỏ. Tên loại tài liệu và cờ có/không không phải nội dung giấy tờ.

Dùng [Tên NB], [Tên nhân viên], [SĐT], [Mã hồ sơ], [kênh chính thức], [thời điểm]. Ví dụ chỉ SIM-xxx, không dùng số giả giống dữ liệu thật. Che dữ liệu trước khi nạp; không đưa ảnh giấy tờ vào để nhờ AI che. Mã merchant_id vận hành chỉ được dùng theo phân quyền; repo chỉ có SIM-xxx. [CHỜ COO DUYỆT – D-02] Theo kiến trúc Data Pipeline v1.0, merchant_id thuộc nhóm Vàng vì truy ngược được nhà bán: mặc định thay [Mã hồ sơ], chỉ dùng mã thật khi COO quyết định. Không lưu bản nguồn/ảnh/link chứa bí mật. Sự cố được người ghi tại nơi được phép, không lặp lại giá trị bị lộ.

## Gate 0 trước mọi xử lý AI

[CHỜ COO DUYỆT – D-02] Đề xuất theo kiến trúc Data Pipeline v1.0, chưa có hiệu lực: người nạp tài liệu (owner) đánh dấu từng file khi tải lên là có hay không chứa dữ liệu Đỏ (số tài khoản, CCCD, hợp đồng có chữ ký). Có: bản gốc vào thư mục hạn chế quyền “T0-restricted” (chỉ owner và COO), tạo bản che có người thứ hai kiểm; chỉ bản che đi tiếp vào trích xuất và biên tập. Mỗi file một dòng trong sổ Gate 0 (mã Gate 0, nhãn Đỏ/Vàng/Xanh, người kiểm) do PM giữ nội bộ, không lưu trong repo. Công cụ biên tập tri thức không tự xác nhận Gate 0 và dừng file khi còn thấy dấu hiệu Đỏ. Tài liệu có khối thông tin các bên trong hợp đồng (số tài khoản, chữ ký) phải che trước khi xử lý.

Ghi chú nguồn L2: HI1-P1A-SOL-001 v0.1 §4 xếp SĐT/liên hệ vào RED; Architecture Review v1.3 đã chốt thay bằng placeholder. Theo kết quả kiểm định, giữ phân loại repo/v1.3, không đổi SĐT thành dữ liệu Đỏ. Token vẫn bị chặn theo guardrails đã audit.
