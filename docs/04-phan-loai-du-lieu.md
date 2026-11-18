# Phân loại dữ liệu

v0.1.0 – pilot, chưa COO duyệt

[CHỜ COO DUYỆT – D-02]

Ý kiến mới đề xuất mở phạm vi dữ liệu khi dùng Claude Team/doanh nghiệp được ghi tại [đề xuất D-02/D-09](de-xuat-d02-d09-mo-du-lieu-va-tu-chu.md). Bảng và quy tắc chặn bên dưới vẫn là hướng dẫn đang áp dụng cho tới khi phạm vi D-02 được chốt và các Skill/Project instructions được cập nhật, kiểm thử đồng bộ.

**Bảng thay thế được đề xuất, chưa áp dụng:** Giữ tên lớp Đỏ để nhận diện rủi ro; đề xuất cho phép xử lý từng mục đích trên môi trường Claude Team/Enterprise đã được tổ chức phê duyệt, đúng quyền hồ sơ. Phạm vi người yêu cầu chọn gồm CCCD, số tài khoản, ảnh giấy tờ tùy thân, mật khẩu, OTP và token. Trước khi mở nhóm bí mật xác thực phải có quyết định riêng của chủ hệ thống/an ninh thông tin và quy trình cấp/thu hồi; không dùng AI để đăng nhập hoặc nhập bí mật vào CMS. Không đưa dữ liệu Đỏ vào repo, tracker, log hay bộ SIM. Nhân viên chỉ gửi trường cần cho việc đã được duyệt, không copy nguyên hồ sơ. Nếu chưa xác minh được điều kiện của một nhóm, tiếp tục chặn nhóm đó theo bảng hiện hành.

| Nhóm | Nội dung | Quy tắc |
|---|---|---|
| Xanh | Chính sách đã duyệt, checklist, mẫu tin, hướng dẫn giao diện | Chỉ bản APPROVED hiện hành; bản pilot không tự thành APPROVED |
| Vàng | Loại hình, ngành hàng, trạng thái, mục thiếu, tên shop, nội dung sản phẩm | [CHỜ COO DUYỆT – D-03] Chỉ dùng trên gói Claude Team/Enterprise được cho phép; tên người/SĐT thay placeholder |
| Đỏ | CCCD, STK ngân hàng, OTP, mật khẩu, token, ảnh giấy tờ tuỳ thân | Không bao giờ đưa vào AI hoặc repo |

[CHỜ COO DUYỆT – D-02] Nếu input chứa giá trị CCCD, số tài khoản ngân hàng, OTP, mật khẩu, token hoặc ảnh giấy tờ tuỳ thân: dừng ngay, không lặp lại giá trị, không xử lý hay lưu; nhắc người dùng xoá khỏi hội thoại và ghi sự cố qua người phụ trách, chỉ ghi mã SIM-xxx/loại sự cố, không ghi dữ liệu Đỏ. Tên loại tài liệu và cờ có/không không phải nội dung giấy tờ.

Dùng [Tên NB], [Tên nhân viên], [SĐT], [Mã hồ sơ], [kênh chính thức], [thời điểm]. Ví dụ chỉ SIM-xxx, không dùng số giả giống dữ liệu thật. Che dữ liệu trước khi nạp; không đưa ảnh giấy tờ vào để nhờ AI che. Mã merchant_id vận hành chỉ được dùng theo phân quyền; repo chỉ có SIM-xxx. Không lưu bản nguồn/ảnh/link chứa bí mật. Sự cố được người ghi tại nơi được phép, không lặp lại giá trị bị lộ.

Ghi chú nguồn L2: HI1-P1A-SOL-001 v0.1 §4 xếp SĐT/liên hệ vào RED; Architecture Review v1.3 đã chốt thay bằng placeholder. Theo kết quả kiểm định, giữ phân loại repo/v1.3, không đổi SĐT thành dữ liệu Đỏ. Token vẫn bị chặn theo guardrails đã audit.
