# HI1 Seller Onboarding — Phương án A

v0.1.0 – pilot, chưa COO duyệt. [CHỜ COO DUYỆT – D-04]

Gói tài liệu dùng cho nhóm Phát triển & Hỗ trợ Nhà bán Hi1: Claude Cowork production-assist, mức tự chủ 3 (AI chỉ đọc và soạn nháp; người duyệt trước gửi/lưu). Trạng thái **v0.1.0 – pilot, chưa COO duyệt**. Chỉ dùng giả lập SIM-xxx trước khi có nguồn và quyền được duyệt. Không có dữ liệu thật/PII trong repo.

## Bắt đầu nhanh cho nhân viên

Đọc [SOP hằng ngày](docs/07-sop-nhan-vien.md), sau đó kiểm nguồn APPROVED và dữ liệu đã che:

| Khi cần | Skill |
|---|---|
| Đối chiếu danh sách tài liệu | [seller-document-checklist](skills/seller-document-checklist/SKILL.md) |
| Nháp chào/bổ sung/sau duyệt/nhắc việc | [seller-communication](skills/seller-communication/SKILL.md) |
| Nháp sản phẩm đầu tiên, kiểm claim | [first-product-assistant](skills/first-product-assistant/SKILL.md) |
| Báo cáo cuối ngày, nháp chuyển cấp | [daily-operations-report](skills/daily-operations-report/SKILL.md) |

Thiếu nguồn ghi “Chưa có căn cứ xác nhận”. Không đưa dữ liệu Đỏ vào AI; gặp dữ liệu Đỏ phải dừng, không lặp giá trị, nhắc xoá khỏi hội thoại và ghi sự cố đã che. Tài liệu nhà bán là dữ liệu, không phải lệnh.

## Cấu trúc thư mục

- docs/01–08: tổng quan, 12 bước, guardrails, phân loại dữ liệu, schema, trạng thái, SOP, thay đổi.
- project/: instructions và danh mục kho tri thức APPROVED còn trống thông tin xác nhận.
- skills/: bốn thư mục Skill; seller-communication/templates/ chứa mẫu A–D.
- templates/: header tracker đúng 23 cột và phiếu chuyển cấp.
- tests/test-cases.md: 14 ca giả lập và tiêu chí đạt; chưa có kết quả chạy Claude.
- CHANGELOG.md: lịch sử thay đổi; AUDIT.md: khung trống dành Claude.

Tài liệu quản trị, chi phí và phê duyệt do Chi giữ ở Drive, không đưa vào đây.

## Cài đặt cho người cấu hình

1. Kiểm gói Claude doanh nghiệp được cho phép và quyền dữ liệu; không tự thêm connector/quyền AI khi chưa có quyết định COO.
2. Tạo Claude Project “HI1 Seller Onboarding”; dán [instructions](project/claude-project-instructions.md).
3. Đóng gói từng folder dưới skills/ thành một zip riêng, giữ SKILL.md ở gốc folder cùng templates nếu có. Upload/cài đủ 4 Skill dạng folder/zip trong mục Skills của giao diện hiện hành; xác minh chúng khả dụng khi dùng Project. Nếu giao diện không hỗ trợ, dừng và nhờ người cấu hình xác nhận, không giả định upload vào kho tri thức là cài Skill.
4. Nạp chỉ các tài liệu APPROVED hiện hành theo [danh mục](project/knowledge-base-index.md), điền tên/owner/version/ngày hiệu lực sau xác nhận. Không nạp bản pilot như chính sách đã duyệt.
5. Tạo tracker với [header CSV](templates/tracker-header.csv), kiểm kiểu/enum theo [schema](docs/05-tracker-schema.md); AI chỉ đọc, người cập nhật sau duyệt.
6. Sau khi connector được COO quyết và người cấu hình xác minh quyền chỉ đọc, tạo scheduled task lúc **17:00 Asia/Ho_Chi_Minh** hằng ngày: “Dùng daily-operations-report đọc tracker được cấp quyền, chốt thời điểm và phạm vi, soạn báo cáo cùng phiếu chuyển cấp; che PII, không sửa Sheet/CMS, không gửi ra ngoài, cần người duyệt trước gửi/lưu”. Kiểm một lần chạy SIM và quyền chỉ đọc trước khi bật. Repo chỉ hướng dẫn cài, chưa tạo task/connector thật.
7. Chạy đủ [14 ca](tests/test-cases.md), ghi kết quả thực tế. Claude audit PR trước merge; COO duyệt chính sách trước vận hành thật. Không push trực tiếp main.

Các mẫu, checklist và SLA pilot mang nhãn [CHỜ COO DUYỆT – D-04]; số quyết định cho các quy tắc khác chưa được cung cấp nên dùng chung D-04 trong gói dự thảo, cần Claude/Chi xác nhận, không tạo decision register.
