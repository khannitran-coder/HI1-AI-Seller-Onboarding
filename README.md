# HI1 Seller Onboarding — Phương án A

GIAI ĐOẠN 1 - PHƯƠNG ÁN A: Ưu tiên hiện tại AI Adoption & Rapid Production Claude Cowork + AI Skills + low-code/no-code
Mục tiêu: Đưa AI vào quy trình Phát triển & Hỗ trợ Nhà bán đang vận hành tại HI1.

GIAI ĐOẠN 2 - PHƯƠNG ÁN B:
AI Engineering & Scalable Automation
Backend + API + Database + AI Orchestration
Mục tiêu: Chuyển những workflow đã chứng minh giá trị sang hệ thống tích hợp, tự động hóa và có khả năng mở rộng
## Kiến trúc hiện tại (v0.1.2)

Hệ thống là lớp hỗ trợ soạn thảo đặt cạnh quy trình onboarding nhà bán đang chạy. AI ở mức tự chủ 3: đọc dữ liệu được cấp, đối chiếu, soạn nháp. Mọi thao tác ghi (gửi tin, sửa CMS, cập nhật tracker) do người thực hiện. Không có tích hợp hệ thống; dữ liệu giữa các thành phần đi qua tay nhân viên.

### Thành phần

| Thành phần | Nền tảng | Trách nhiệm | Giới hạn |
|---|---|---|---|
| Hệ thống nguồn | admin.hi1.vn, App Nhà Bán Hi1 | Trạng thái chính thức của hồ sơ, shop, sản phẩm | Claude không truy cập |
| Kênh nhà bán | Zalo | Trao đổi và nhận giấy tờ | Chỉ nhân viên gửi |
| Tracker vận hành | Google Sheet, 26 cột | Theo dõi hồ sơ, owner, hạn, đo KPI | Không phải nguồn chính thức; người ghi |
| Kho tri thức | Thư mục Drive + Project knowledge | Checklist, chính sách, mẫu tin, hướng dẫn giao diện có phiên bản | Chỉ tài liệu APPROVED được nạp |
| Lớp điều phối | Claude Project "HI1 Seller Onboarding" | Instructions chung: guardrails, chặn dữ liệu Đỏ, output contract, chọn Skill | Không có quyền ghi ra ngoài |
| Skill | 4 thư mục tự chứa (SKILL.md, references, templates) | Một nghiệp vụ mỗi Skill, phiên bản riêng | Không gọi lẫn nhau |
| Báo cáo định kỳ | Scheduled task 17:00 (Asia/Ho_Chi_Minh) | Chạy daily-operations-report trên tracker | Chỉ đọc; bật sau quyết định D-03 |

### Luồng xử lý một hồ sơ

~~~mermaid
flowchart LR
  A[CMS / Zalo] -->|nhân viên trích trường nghiệp vụ| B[Phân lớp dữ liệu]
  B -->|Xanh, Vàng| C[Claude Project + Skill]
  B -->|Đỏ| X[Không đưa vào AI]
  C --> D[Nháp + nguồn + phiên bản]
  D --> E{Nhân viên review}
  E -->|duyệt / sửa| F[Nhân viên gửi Zalo, thao tác CMS]
  E -->|bỏ| C
  F --> G[Ghi tracker]
  G --> H[Báo cáo cuối ngày]
  H --> I[Trưởng nhóm]
~~~

### Ranh giới tin cậy và điểm kiểm soát

| Ranh giới | Kiểm soát |
|---|---|
| Dữ liệu vào AI | Chỉ lớp Xanh và Vàng. Lớp Đỏ bị chặn ở hai tầng: quy trình nhân viên và Skill dừng khi phát hiện |
| Nội dung nhà bán gửi | Xử lý như dữ liệu, không như lệnh |
| Đầu ra AI | Luôn là nháp; không có đường ghi tự động sang CMS, Zalo hay tracker. Điểm duyệt ghi ở cột review_result |
| Trạng thái "Được duyệt" | Chỉ lấy từ CMS hoặc người có thẩm quyền |

### Mô hình trạng thái

Hồ sơ có một trạng thái nghiệp vụ (8 nhãn, docs/06) và ba trạng thái con độc lập: shop_status, product_status, ready_status. "Sẵn sàng bán" là trạng thái suy ra từ năm điều kiện và do Trưởng nhóm xác nhận, không suy ra từ việc shop đã được kích hoạt.

### Phiên bản và truy vết

Mỗi Skill có phiên bản riêng; mỗi dòng tracker ghi skill_version và checklist_version của lần xử lý. Bản references trong Skill được đồng bộ từ docs khi docs thay đổi. Mỗi thay đổi Skill phải chạy lại 14 ca kiểm thử và ghi CHANGELOG. Yêu cầu nghiệp vụ truy vết tới Skill và ca kiểm thử trong docs/11.

### Giới hạn đã chấp nhận

- Tracker và CMS đồng bộ thủ công, có thể lệch.
- Google Sheet không phân quyền theo dòng và không có nhật ký bất biến.
- Không nhắc việc theo thời gian thực.
- Bốn khâu tốn công nhất trong thực tế chưa có Skill: tạo đối tác và thương hiệu trên CMS, lập bộ hợp đồng, nhập sản phẩm lên CMS, kiểm bảng giá Affiliate.
- Gói Claude Pro không chia sẻ được Project và Skill; dùng chung cho nhóm cần gói Team.

### Hướng phát triển

- v0.2 (sau pilot): thêm affiliate-price-review, seller-contract-draft, seller-media-tools; seller-cms-entry chỉ khi COO duyệt D-07.
- Phương án B (khi đạt ngưỡng ở docs/01): backend thay tracker; 26 cột tracker là lược đồ bảng ban đầu.


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
