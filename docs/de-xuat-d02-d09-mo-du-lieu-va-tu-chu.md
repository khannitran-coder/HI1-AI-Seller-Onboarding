# Đề xuất D-02/D-09: dữ liệu nhạy cảm và một bước tự chủ

Tác giả: PM - TKC  
Trạng thái: Đề xuất để COO/Trưởng nhóm review; **chưa cấu hình hoặc cấp quyền vận hành**. Nguồn yêu cầu: ý kiến ngày 18/11/2026 về việc dùng Claude Team/doanh nghiệp để mở rộng dữ liệu và tăng tự chủ AI một bậc. Người yêu cầu đã chọn **toàn bộ dữ liệu Đỏ, kể cả mật khẩu/OTP/token**; đây là phạm vi đề xuất, chưa là quyết định D-02 có hiệu lực.

## D-02 — Phạm vi dữ liệu đề xuất

| Nhóm | Đề xuất xử lý trên Claude Team/Enterprise được tổ chức cho phép | Điều kiện |
|---|---|---|
| Xanh/Vàng | Giữ quy tắc hiện hành. | Tài liệu APPROVED, đúng phân quyền, đúng mục đích; dùng merchant_id và chỉ các trường cần thiết. |
| CCCD, số tài khoản, ảnh giấy tờ tùy thân | **Đề xuất cho phép có điều kiện** cho từng mục đích kiểm tra hồ sơ cụ thể. | COO/người phụ trách dữ liệu xác nhận loại dữ liệu, quyền truy cập, điều khoản xử lý, nơi lưu, thời gian lưu, kiểm thử rò rỉ và xử lý sự cố. Không đưa vào repo, tracker, log hoặc mẫu test. |
| Mật khẩu, OTP, token | **Người yêu cầu muốn đưa vào phạm vi mở D-02. Chưa cho phép vận hành.** | Đây là bí mật xác thực có thể dùng để truy cập hoặc thay đổi tài khoản. Cần chủ hệ thống/an ninh thông tin xác định mục đích cần AI xử lý, luồng cấp/thu hồi, khả năng AI không lưu hoặc lặp lại, quyền truy cập và phương án thay thế an toàn; COO quyết sau khi có đánh giá đó. Không dùng gói Team như bằng chứng đủ để bật. |

Đăng ký gói Team/Enterprise không tự xác nhận quyền xử lý mọi loại dữ liệu. Nếu D-02 được duyệt cho từng nhóm dữ liệu, phải sửa đồng bộ `docs/03`, `docs/04`, Project instructions, guardrails của từng Skill, SOP, ca test và bản đóng gói; hiện các thành phần đó **vẫn chặn** dữ liệu Đỏ. Không bỏ yêu cầu chỉ đưa trường cần thiết hoặc quyền theo hồ sơ. Mở dữ liệu để phân tích không tự cấp quyền A08 nhập bí mật vào CMS hoặc đăng nhập thay người.

## D-09 — Bước tự chủ đề xuất

Đề xuất **A03: tạo lô nháp phiếu chuyển cấp và tin nhắc việc** đi từ **M3 hiện tại lên M3+**. M3 là mỗi nháp được người duyệt riêng; M3+ là nhân viên xem trước đầy đủ danh sách merchant_id, nguồn và nội dung lô, duyệt một lần cho đúng lô, rồi AI tạo các **bản nháp** trong phạm vi đã duyệt. Không gửi tin, không sửa CMS/tracker. Hành động khác giữ nguyên mức hiện tại; M3+ không cấp quyền A04 gửi Zalo, A02 ghi tracker hoặc A07/A08.

Trước khi bật: D-09 và D-03 được người có thẩm quyền duyệt; có connector/quyền đúng phạm vi, tab nhật ký AI, nút dừng và bằng chứng kiểm thử. Áp dụng ngưỡng tại `docs/12`: ít nhất 30 lượt thật ở M3, ít nhất 90% duyệt nguyên/sửa nhỏ và không có sự cố; Trưởng nhóm đề xuất, COO duyệt bằng văn bản. Chưa đạt thì tiếp tục M3. Không coi tài liệu này là phê duyệt hoặc kết quả kiểm thử.

## Câu hỏi chốt trước khi triển khai

1. D-02: COO và người phụ trách an ninh/dữ liệu có chấp thuận từng nhóm trong phạm vi toàn bộ lớp Đỏ không, cho mục đích nào và theo điều khoản xử lý nào? Đặc biệt cần giải quyết bí mật xác thực trước khi sửa quy tắc vận hành.
2. D-09: COO có chọn A03 để lên M3+ không? Nếu chọn hành động khác, phải sửa ma trận và ca kiểm thử theo hành động đó.
3. Ai xác nhận quyền truy cập, lưu giữ, sự cố và kết quả chạy lại test trước khi phát SOP mới?
