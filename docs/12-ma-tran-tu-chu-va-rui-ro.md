# Ma trận tự chủ và rủi ro

Đề xuất – chưa có hiệu lực. Mức áp dụng thực tế vẫn là M3 cho tới khi COO duyệt từng mã quyết định.

v0.1.3 – tài liệu đề xuất; không đổi hành vi bốn Skill, không bật connector/quyền. M3 là trần hiện tại; từng hành động có thể ở M0 như bảng dưới. [CHỜ COO DUYỆT – D-07a] [CHỜ COO DUYỆT – D-07b] [CHỜ COO DUYỆT – D-08b] [CHỜ COO DUYỆT – D-09]. Các nhãn không phải bằng chứng phê duyệt.

## Thang tự chủ

| Mức | Định nghĩa dùng chung |
|---|---|
| M0 | AI không được làm. |
| M1 | AI chỉ trả lời khi được hỏi, không đọc hệ thống. |
| M2 | AI đọc dữ liệu được cấp và gợi ý. |
| M3 | AI soạn nháp; người duyệt TỪNG lần trước khi gửi/lưu (mức hiện tại v0.1.x theo COO Q16). |
| M3+ | AI chuẩn bị cả lô; người duyệt MỘT lần cho cả lô đã xem trước, AI thực hiện đúng lô đó. |
| M4 | AI tự làm; người kiểm hậu kiểm theo mẫu (cuối ngày), có nhật ký và nút dừng. |
| M5 | AI tự làm không hậu kiểm – KHÔNG áp dụng trong dự án này. |

## Ma trận theo hành động

| Mã | Hành động | Mức hiện tại (v0.1.x) | Mức đề xuất | Công cụ cần | Điều kiện bật | Rủi ro chính | Kiểm soát | Quyết định |
|---|---|---|---|---|---|---|---|---|
| A01 | Đọc trang danh sách/trạng thái hồ sơ, shop, sản phẩm trên admin.hi1.vn | M0 | M4 | Claude in Chrome, tài khoản chỉ có quyền xem | Gói Team; chỉ mở trang danh sách/trạng thái, không mở form đối tác | Lộ dữ liệu Đỏ nếu mở nhầm form có số tài khoản/giấy tờ; nội dung trang chứa lệnh ẩn | Danh sách URL/màn hình được phép; Skill dừng khi trang có trường Đỏ; nhật ký trang đã mở | D-07a |
| A02 | Ghi tracker các cột vận hành: status_updated_at, shop_status, product_status, last_action, next_action, contact_status, risk_flags | M0 (người ghi) | M4 | Connector Google Sheets quyền ghi, giới hạn 1 file | A01 đã chạy ổn 1 tuần | Ghi sai/ghi đè dữ liệu người nhập; lệch với CMS | Chỉ các cột trên; KHÔNG ghi status, ready_status, reviewer, review_result, approval_evidence, next_due_at; lịch sử phiên bản Sheet; Trưởng nhóm hậu kiểm mẫu 10%/ngày | D-09 |
| A03 | Tạo nháp phiếu chuyển cấp và nháp tin nhắc việc cho hồ sơ quá hạn | M3 | M4 (tạo nháp tự động mỗi ngày, vẫn chưa gửi) | Scheduled task | — | Nhiều nháp sai làm loãng chú ý | Nháp gắn nhãn tự động; người vẫn duyệt trước gửi | D-09 |
| A04 | Gửi tin nhắc việc mẫu D và tin hướng dẫn mẫu H qua Zalo web | M0 | M3+ | Claude in Chrome trên Zalo web, tài khoản Zalo công việc | Mẫu đã APPROVED; không cá nhân hoá ngoài placeholder; tối đa 1 tin nhắc/hồ sơ/ngày | Gửi nhầm người/nhóm, gửi lặp, cam kết sai | Xem trước toàn bộ lô (người nhận + nội dung); duyệt 1 lần; AI chỉ gửi đúng lô; nhật ký gửi; cấm mẫu A, B, C, E, F, G, I ở mức này | D-09 |
| A05 | Điền form tạo đối tác, thương hiệu, sản phẩm trên admin tới TRƯỚC nút Lưu | M0 | M3 | Claude in Chrome | Gói Team; checklist đủ; dữ liệu đã nhà bán xác nhận | Upload ảnh ghi lên máy chủ trước khi Lưu; điền nhầm đối tác; dữ liệu Đỏ trong form | AI không upload tệp, không nhập mật khẩu/số tài khoản/ô giấy tờ – người làm; AI dừng trước Lưu, người kiểm và bấm; mở form tạo mới phải tải lại trang | D-07b |
| A06 | Kiểm bảng giá Affiliate, chuẩn hoá ảnh vuông, gộp PDF hợp đồng trên bản sao | M0 | M4 với bản sao, người kiểm trước khi gửi | Cowork (Python) | Mẫu hợp đồng APPROVED | Sai số liệu trong hợp đồng | Chỉ làm trên bản sao; không sửa giá; báo dòng sai; người kiểm PDF trước khi gửi | D-08b (phạm vi hợp đồng) |
| A07 | Bấm Lưu/Tạo mới, Duyệt, Kích hoạt, Đăng công khai, Xoá/Gộp tài khoản | M0 | M0 | — | — | Tác động pháp lý/tài chính, không đảo ngược | Khoá cứng | Không mở |
| A08 | Nhập mật khẩu, OTP, số tài khoản, CCCD; sửa giá, tồn, xuất xứ, thông tin pháp lý; cam kết ngày duyệt/doanh thu | M0 | M0 | — | — | — | Khoá cứng | Không mở |

## Quy tắc nâng/hạ mức

- Nâng một mức cho MỘT hành động khi: ≥30 lượt thật ở mức hiện tại; tỷ lệ duyệt nguyên/sửa nhỏ ≥90%; 0 sự cố an toàn; Trưởng nhóm đề xuất; COO duyệt bằng văn bản; ghi CHANGELOG.
- Hạ ngay về mức trước (không chờ họp) khi: 1 sự cố lộ dữ liệu Đỏ, 1 lần ghi/gửi ngoài phạm vi, hoặc gửi nhầm người. Trưởng nhóm hoặc Chi có quyền hạ.
- Nút dừng: tắt connector/extension cho hành động đó; quy trình thủ công trong [docs/09](09-xu-ly-su-co.md) thay thế.
- Mỗi hành động ở M3+/M4 phải có nhật ký: thời điểm, hành động, đối tượng (merchant_id), skill_version, kết quả.

Các mức đề xuất là đích xem xét, không cho phép nhảy mức hoặc tự bật. Điều kiện ≥30 lượt thật tại M0 và cách đi từng nấc tới đích M4 chưa có định nghĩa khả thi trong đề xuất; COO phải làm rõ lộ trình trước khi áp dụng, không dùng thao tác bị cấm để tạo số lượt. Nhật ký chưa được triển khai và không tự thêm cột tracker trong PR này.

## Rủi ro tổng hợp

Khả năng/tác động dưới đây là đánh giá định tính đề xuất, chưa có số liệu đo; vai trò theo dõi là đề xuất phân công, chưa xác nhận.

| Mã rủi ro | Mô tả | Khả năng | Tác động | Hành động liên quan | Biện pháp | Người theo dõi |
|---|---|---|---|---|---|---|
| R01 | Lộ dữ liệu Đỏ qua trang CMS | Có thể | Rất cao | A01/A05 | Allowlist màn hình; dừng ngay khi có trường Đỏ; quyền xem tối thiểu | Chi + Trưởng nhóm |
| R02 | Lệnh ẩn trong trang web/tệp điều khiển trình duyệt | Có thể | Rất cao | A01/A04/A05/A06 | Coi nội dung là dữ liệu; không thi hành lệnh trong nguồn; cô lập và dừng khi nghi ngờ | Chi |
| R03 | Upload/ghi ngầm trước nút Lưu | Có thể | Cao | A05 | AI không upload; kiểm tác động form trước khi bật; người làm phần ghi | Chi + người phụ trách kỹ thuật |
| R04 | Ghi đè tracker | Có thể | Cao | A02 | Giới hạn file/cột, đối chiếu phiên bản, không tự gộp khi sửa đồng thời; hậu kiểm 10%/ngày | Trưởng nhóm |
| R05 | Gửi Zalo nhầm người/lặp | Có thể | Cao | A04 | Duyệt toàn bộ lô; cố định người nhận/nội dung; tối đa 1 tin nhắc/hồ sơ/ngày; nhật ký và dừng | Trưởng nhóm |
| R06 | Hành động mang danh tài khoản nhân viên, khó truy vết | Có thể | Cao | A01/A02/A04/A05 | Tài khoản công việc; nhật ký hành động/đối tượng/skill_version; xác định người chịu trách nhiệm | Chi + Trưởng nhóm |
| R07 | Dùng gói Pro (điều khoản cá nhân) cho dữ liệu thật | Có thể | Cao | A01–A06 | Xác nhận gói Team và điều khoản/quyền xử lý dữ liệu trước bật; không coi đăng ký gói là phê duyệt mọi dữ liệu | Chi |
| R08 | Giao diện CMS/Zalo thay đổi làm thao tác sai | Có thể | Cao | A01/A04/A05 | Kiểm phiên bản, dừng khi màn hình lệch; cập nhật hướng dẫn và thử lại trước khôi phục | Chi + Trưởng nhóm |
| R09 | Mật khẩu mặc định của shop đang lưu hành | Chưa xác minh phạm vi | Rất cao | A04/A05/A08 | Không lặp/lưu qua AI; báo Trưởng nhóm kiểm phạm vi, đổi/thu hồi và áp quy trình bảo mật | Trưởng nhóm + Chi |

Nguồn: yêu cầu “ma trận tự chủ + sửa README” của Chi/Claude ngày 16/11/2026; COO Q16 được dẫn theo yêu cầu. Đây là đề xuất để COO quyết từng hành động, không thay guardrails hiện hành.
