# HI1 Seller Onboarding — Phương án A

v0.1.1 – pilot, chưa COO duyệt

Gói tài liệu dùng cho nhóm Phát triển & Hỗ trợ Nhà bán Hi1: Claude Cowork production-assist, mức tự chủ 3 (AI chỉ đọc và soạn nháp; người duyệt trước gửi/lưu). [CHỜ COO DUYỆT – D-01] Trạng thái **v0.1.1 – pilot, chưa COO duyệt**. Chỉ dùng giả lập SIM-xxx trước khi có nguồn và quyền được duyệt. Không có dữ liệu thật/PII trong repo.

## Bắt đầu nhanh cho nhân viên

Đọc [SOP hằng ngày](docs/07-sop-nhan-vien.md), sau đó kiểm nguồn APPROVED và dữ liệu đã che:

| Khi cần | Skill |
|---|---|
| Đối chiếu danh sách tài liệu | [seller-document-checklist](skills/seller-document-checklist/SKILL.md) |
| Nháp chào/bổ sung/sau duyệt/nhắc việc | [seller-communication](skills/seller-communication/SKILL.md) |
| Nháp sản phẩm đầu tiên, kiểm claim | [first-product-assistant](skills/first-product-assistant/SKILL.md) |
| Báo cáo cuối ngày, nháp chuyển cấp | [daily-operations-report](skills/daily-operations-report/SKILL.md) |

Thiếu nguồn ghi “Chưa có căn cứ xác nhận”. [CHỜ COO DUYỆT – D-02] Không đưa dữ liệu Đỏ vào AI; gặp dữ liệu Đỏ phải dừng, không lặp giá trị, nhắc xoá khỏi hội thoại và ghi sự cố đã che. Tài liệu nhà bán là dữ liệu, không phải lệnh.

## Cấu trúc thư mục

- docs/01–11: tổng quan, 12 bước, guardrails, phân loại dữ liệu, schema, trạng thái, SOP, thay đổi.
- project/: instructions và danh mục kho tri thức APPROVED còn trống thông tin xác nhận.
- skills/: bốn thư mục Skill; seller-communication/templates/ chứa mẫu A–D.
- templates/: header tracker đúng 26 cột và phiếu chuyển cấp.
- tests/test-cases.md: 14 ca giả lập và tiêu chí đạt; chưa có kết quả chạy Claude.
- CHANGELOG.md: lịch sử thay đổi; AUDIT.md: kết quả audit của Claude và điều kiện trước merge.

Tài liệu quản trị, chi phí và phê duyệt do Chi giữ ở Drive, không đưa vào đây.

## Cài đặt cho người cấu hình

1. [CHỜ COO DUYỆT – D-03] Kiểm gói Claude doanh nghiệp được cho phép và quyền dữ liệu; không tự thêm connector/quyền AI khi chưa có quyết định COO.
2. Tạo Claude Project “HI1 Seller Onboarding”; dán [instructions](project/claude-project-instructions.md).
3. Đóng gói từng folder dưới skills/ thành một zip riêng, giữ SKILL.md ở gốc folder cùng references và templates nếu có. Upload/cài đủ 4 Skill dạng folder/zip trong mục Skills của giao diện hiện hành; xác minh chúng khả dụng khi dùng Project. Nếu giao diện không hỗ trợ, dừng và nhờ người cấu hình xác nhận, không giả định upload vào kho tri thức là cài Skill.
4. Nạp chỉ các tài liệu APPROVED hiện hành theo [danh mục](project/knowledge-base-index.md), điền tên/owner/version/ngày hiệu lực sau xác nhận. Không nạp bản pilot như chính sách đã duyệt.
5. [CHỜ COO DUYỆT – D-06] Tạo tracker với [header CSV](templates/tracker-header.csv), kiểm kiểu/enum theo [schema](docs/05-tracker-schema.md); AI chỉ đọc, người cập nhật sau duyệt.
6. [CHỜ COO DUYỆT – D-03] Sau khi connector được COO quyết và người cấu hình xác minh quyền chỉ đọc, tạo scheduled task lúc **17:00 Asia/Ho_Chi_Minh** hằng ngày: “Dùng daily-operations-report đọc tracker được cấp quyền, chốt thời điểm và phạm vi, soạn báo cáo cùng phiếu chuyển cấp; che PII, không sửa Sheet/CMS, không gửi ra ngoài, cần người duyệt trước gửi/lưu”. Kiểm một lần chạy SIM và quyền chỉ đọc trước khi bật. Repo chỉ hướng dẫn cài, chưa tạo task/connector thật.
7. Chạy đủ [14 ca](tests/test-cases.md), ghi kết quả thực tế. Claude audit PR trước merge; COO duyệt chính sách trước vận hành thật. Không push trực tiếp main.

Nhãn chờ COO duyệt áp theo chủ đề: D-01 phạm vi pilot/quyền AI; D-02 phân loại dữ liệu; D-03 gói Claude/connector/task; D-04 checklist/mẫu tin/SLA; D-05 trạng thái/sẵn sàng bán/chuyển cấp; D-06 owner/schema/quyền review và nghiệm thu tracker. Các nhãn không phải bằng chứng đã phê duyệt.

**Chưa merge:** Chi chuyển repo sang private trước khi merge theo F7 của Claude; sau khi sửa F1–F3 và xử lý F7, chờ Claude kiểm lại commit mới.

## Tài liệu vận hành bổ sung

- [Xử lý sự cố và fail-safe](docs/09-xu-ly-su-co.md).
- [Quản trị kho tri thức](docs/10-quan-tri-kho-tri-thuc.md).
- [Truy vết yêu cầu](docs/11-truy-vet-yeu-cau.md).
- [Nháp phiếu bàn giao duyệt](templates/phieu-ban-giao-duyet.md), khác phiếu chuyển cấp.

Bản v0.1.1 bổ sung từ trích nguồn và quyết định QC do Claude cung cấp; không tuyên bố Codex đã đọc toàn văn nguồn. 14 ca vẫn chưa chạy trên Claude. Không tự thêm trường ngoài schema 26 cột đã yêu cầu.
