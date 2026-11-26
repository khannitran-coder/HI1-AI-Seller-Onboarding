# Quy trình 12 bước

v0.2.0 – pilot, chưa COO duyệt

Thay đổi so với v0.1.0: AI tham gia cả 12 bước ở mức cao nhất mà guardrails hiện cho phép; chạy trên Claude Cowork (lớp điều phối, xem [README](../README.md)); chuyển cấp còn 2 cấp. Mức tự chủ (M) theo [docs/12](12-ma-tran-tu-chu-va-rui-ro.md). Không bước nào vượt M3 cho thao tác ghi: AI chuẩn bị đến sát nút cuối, người bấm.

## Nguyên tắc chung

- AI làm toàn bộ phần đọc, đối chiếu, điền nháp; người làm phần quyết định và phần ghi (gửi tin, bấm Tạo mới/Lưu/Duyệt, cập nhật tracker).
- Một lệnh cho Claude = một hồ sơ, gọi đúng Skill. Mọi đầu ra theo output contract, kết thúc “Cần người duyệt trước khi gửi/lưu: Có”.
- Bước 2, 6, 8, 10 dùng CMS qua Claude in Chrome (A01 xem, A05 điền trước Tạo mới) là đề xuất pilot, chờ COO duyệt D-07a/D-07b; trước khi duyệt, nhân viên tự thao tác CMS, AI chỉ nháp từ dữ liệu được dán vào.
- Khoá cứng (không bước nào mở): A07 bấm Lưu/Tạo mới/Duyệt/Kích hoạt/Đăng/Xoá/Gộp; A08 nhập mật khẩu/OTP, sửa giá/tồn/xuất xứ/thông tin pháp lý, cam kết ngày duyệt/doanh thu.
- Chuyển cấp: **Cấp 1 – Nghiệp vụ** (Trưởng nhóm hoặc bộ phận chuyên môn đúng vướng mắc); **Cấp 2 – COO** (chính sách, quyền AI, nguồn, ngoại lệ, sự cố nghiêm trọng hoặc Cấp 1 không xử lý được).

## Bảng 12 bước

| Bước | AI làm (Claude Cowork) | M | Người làm / duyệt | Skill, công cụ | Chuyển cấp khi |
|---|---|---|---|---|---|
| 1. Nhận lead | Đọc nhóm Zalo PC và thư mục NHÀ BÁN của nhà bán; trích trường, lập danh sách thiếu; nháp tin chào (mẫu A/E) và tin xin SĐT quản trị | M3 | Phân công người phụ trách; duyệt và tự gửi | seller-communication; hi1-mo-shop (bước 1–2); thư mục kết nối, computer use đọc Zalo PC | Lead ngoài phạm vi (cá nhân tự do, ngành cấm) → Cấp 1 Trưởng nhóm |
| 2. Kiểm trùng | Tra danh sách Đối tác trên CMS theo tên, MST, SĐT; báo nghi trùng kèm bằng chứng | M3 (A01, người ra lệnh từng lần) | Xác minh; không giao AI gộp/xoá | hi1-mo-shop (tìm trùng); Claude in Chrome chỉ xem | Nghi trùng → Cấp 1 Trưởng nhóm |
| 3. Phân loại | Đề xuất chủ thể (DN/HTX/HKD), ngành hàng, loại hình DN theo doanh thu, mảng phụ trách; gắn cờ ngành có điều kiện | M3 | Xác nhận phân loại | seller-document-checklist | Ngành có điều kiện → Cấp 1 ngành hàng-pháp chế |
| 4. Đối chiếu hồ sơ | Đọc ĐKKD, giấy tờ trong thư mục nhà bán; bảng Đủ/Thiếu/Cần xác minh theo biểu mẫu hiện hành | M3 | Kiểm chứng bản gốc và hệ thống chính thức | seller-document-checklist | Mâu thuẫn giấy tờ → Cấp 1 kiểm duyệt nhà bán |
| 5. Yêu cầu bổ sung | Nháp tin xin bổ sung đúng mục thiếu (mẫu B/F) | M3 | Duyệt và tự gửi | seller-communication | Nhà bán không bổ sung sau nhắc → Cấp 1 Trưởng nhóm |
| 6. Mở shop + hướng dẫn gian hàng | Điền form Đối tác và Thương hiệu trên CMS tới TRƯỚC nút Tạo mới; lấy toạ độ GPS; nháp chuỗi tin gửi tài khoản (không mật khẩu), giới thiệu App, mã hội viên, nhờ đăng nhập thử (mẫu G/H/I) | M3 (A05) | Nhập mật khẩu và trường khoá; kiểm form; bấm Tạo mới; tự gửi và ghim tin | hi1-mo-shop; seller-communication; Claude in Chrome | Lỗi CMS/đăng nhập → Cấp 1 kỹ thuật |
| 7. Sản phẩm đầu tiên | Kiểm bảng giá Affiliate nhà bán gửi; nháp tiêu đề/mô tả, gắn cờ claim; làm ảnh vuông, gộp PDF trên bản sao | M3 (A06 đề xuất M4 trên bản sao) | Nhà bán xác nhận giá/tồn/xuất xứ; người có quyền nhập/đăng | affiliate-price-review; first-product-assistant; seller-media-tools | Claim/chứng nhận cần xác minh → Cấp 1 ngành hàng-pháp chế |
| 8. Chuyển duyệt | Nháp [phiếu bàn giao duyệt](../templates/phieu-ban-giao-duyet.md); xem danh sách “Sản phẩm chờ duyệt” trên CMS, báo sản phẩm còn treo | M3 (A01 chỉ xem) | Người có quyền chuyển và duyệt trên CMS | seller-document-checklist; Claude in Chrome chỉ xem | Treo quá hạn → Cấp 1 kiểm duyệt nhà bán |
| 9. Hướng dẫn vận hành đơn | Nháp hướng dẫn xử lý đơn/thanh toán từ KU APPROVED đúng phiên bản; không có KU thì “Chưa có căn cứ xác nhận” | M3 | Hướng dẫn, xác nhận nhà bán biết xử lý đơn | seller-communication | Hỏi phí/đối soát chưa có căn cứ → Cấp 1 owner tri thức; ngoại lệ chính sách → Cấp 2 COO |
| 10. Kiểm tra sẵn sàng bán | Tổng hợp bằng chứng đủ/thiếu theo điều kiện tại [docs/06](06-trang-thai.md) từ tracker và CMS (chỉ xem) | M3 | Trưởng nhóm xác nhận Sẵn sàng bán | daily-operations-report | Thiếu điều kiện quá hạn → Cấp 1 Trưởng nhóm |
| 11. Bàn giao + hẹn chăm sóc | Nháp tin bàn giao, mốc chăm sóc; nháp nhắc việc tự động cho hồ sơ đến hạn (chưa gửi) | M3; A03 đề xuất M4 (tạo nháp tự động) | Bàn giao, chốt mốc, tự gửi | seller-communication (D); scheduled task | Nhà bán khiếu nại → Cấp 1 CSKH |
| 12. Báo cáo cuối ngày | Scheduled task 17:00 chạy báo cáo từ tracker; nháp phiếu chuyển cấp | M3; A03 đề xuất M4 (tạo nháp tự động) | Trưởng nhóm duyệt báo cáo và phiếu; người cập nhật tracker | daily-operations-report; scheduled task Cowork | Theo phiếu: Cấp 1 hoặc Cấp 2 COO |

## Phần AI chưa làm (và lý do)

| Việc | Lý do | Điều kiện mở |
|---|---|---|
| Tự gửi tin Zalo (A04) | Rủi ro gửi nhầm/lặp (R05) | COO duyệt D-09; ≥30 lượt M3, ≥90% duyệt nguyên/sửa nhỏ |
| Ghi tracker (A02) | Rủi ro ghi đè (R04) | COO duyệt D-09; A01 chạy ổn 1 tuần; có tab nhật ký AI |
| Bấm Tạo mới/Lưu/Duyệt (A07), nhập mật khẩu (A08) | Không đảo ngược, trách nhiệm pháp lý | Không mở |

seller-contract-draft và seller-cms-entry nằm trong skills-draft/, KHÔNG cài hoặc dùng trước quyết định tương ứng.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ; skills/hi1-mo-shop (26/11/2026); docs/12 v0.2.0.
