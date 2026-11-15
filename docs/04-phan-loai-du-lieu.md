# Phân loại dữ liệu

v0.1.0 – pilot, chưa COO duyệt

[CHỜ COO DUYỆT – D-02]

| Nhóm | Nội dung | Quy tắc |
|---|---|---|
| Xanh | Chính sách đã duyệt, checklist, mẫu tin, hướng dẫn giao diện | Chỉ bản APPROVED hiện hành; bản pilot không tự thành APPROVED |
| Vàng | Loại hình, ngành hàng, trạng thái, mục thiếu, tên shop, nội dung sản phẩm | [CHỜ COO DUYỆT – D-03] Chỉ dùng trên gói Claude Team/Enterprise được cho phép; tên người/SĐT thay placeholder |
| Đỏ | CCCD, STK ngân hàng, OTP, mật khẩu, token, ảnh giấy tờ tuỳ thân | Không bao giờ đưa vào AI hoặc repo |

[CHỜ COO DUYỆT – D-02] Nếu input chứa giá trị CCCD, số tài khoản ngân hàng, OTP, mật khẩu, token hoặc ảnh giấy tờ tuỳ thân: dừng ngay, không lặp lại giá trị, không xử lý hay lưu; nhắc người dùng xoá khỏi hội thoại và ghi sự cố qua người phụ trách, chỉ ghi mã SIM-xxx/loại sự cố, không ghi dữ liệu Đỏ. Tên loại tài liệu và cờ có/không không phải nội dung giấy tờ.

Dùng [Tên NB], [Tên nhân viên], [SĐT], [Mã hồ sơ], [kênh chính thức], [thời điểm]. Ví dụ chỉ SIM-xxx, không dùng số giả giống dữ liệu thật. Che dữ liệu trước khi nạp; không đưa ảnh giấy tờ vào để nhờ AI che. Mã merchant_id vận hành chỉ được dùng theo phân quyền; repo chỉ có SIM-xxx. Không lưu bản nguồn/ảnh/link chứa bí mật. Sự cố được người ghi tại nơi được phép, không lặp lại giá trị bị lộ.

Ghi chú nguồn L2: HI1-P1A-SOL-001 v0.1 §4 xếp SĐT/liên hệ vào RED; Architecture Review v1.3 đã chốt thay bằng placeholder. Theo kết quả kiểm định, giữ phân loại repo/v1.3, không đổi SĐT thành dữ liệu Đỏ. Token vẫn bị chặn theo guardrails đã audit.
