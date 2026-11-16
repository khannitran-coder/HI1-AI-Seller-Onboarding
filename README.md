# HI1 Seller Onboarding — Phương án A

Tác giả: PM - TKC

GIAI ĐOẠN 1 - PHƯƠNG ÁN A: Ưu tiên hiện tại AI Adoption & Rapid Production Claude Cowork + AI Skills + low-code/no-code
Mục tiêu: Đưa AI vào quy trình Phát triển & Hỗ trợ Nhà bán đang vận hành tại HI1.

GIAI ĐOẠN 2 - PHƯƠNG ÁN B:
AI Engineering & Scalable Automation
Backend + API + Database + AI Orchestration
Mục tiêu: Chuyển những workflow đã chứng minh giá trị sang hệ thống tích hợp, tự động hóa và có khả năng mở rộng
## Kiến trúc hiện tại (v0.2.0)

Hệ thống là lớp hỗ trợ soạn thảo đặt cạnh quy trình onboarding nhà bán đang chạy. AI ở mức tự chủ 3: đọc dữ liệu được cấp, đối chiếu, soạn nháp. Mọi thao tác ghi (gửi tin, sửa CMS, cập nhật tracker) do người thực hiện. Không có tích hợp hệ thống; dữ liệu giữa các thành phần đi qua tay nhân viên. Mức tự chủ được quy định theo từng hành động tại docs/12; hiện tại tất cả ở M3 hoặc thấp hơn.

### Thành phần

| Thành phần | Nền tảng | Trách nhiệm | Giới hạn |
|---|---|---|---|
| Hệ thống nguồn | admin.hi1.vn, App Nhà Bán Hi1 | Trạng thái chính thức của hồ sơ, shop, sản phẩm | v0.1.x: Claude Project không truy cập – do thiết kế, không phải giới hạn kỹ thuật. Mở theo mức D-07a (chỉ đọc) / D-07b (điền trước nút Lưu), xem docs/12 |
| Kênh nhà bán | Zalo | Trao đổi và nhận giấy tờ | Chỉ nhân viên gửi |
| Tracker vận hành | Google Sheet, 26 cột | Theo dõi hồ sơ, owner, hạn, đo KPI | Không phải nguồn chính thức; người ghi |
| Kho tri thức | Thư mục Drive + Project knowledge | Checklist, chính sách, mẫu tin, hướng dẫn giao diện có phiên bản | Chỉ tài liệu APPROVED được nạp |
| Lớp điều phối | Claude Project "HI1 Seller Onboarding" | Instructions chung: guardrails, chặn dữ liệu Đỏ, output contract, chọn Skill | Không có quyền ghi ra ngoài |
| Skill | 6 thư mục cài được trong skills/; 2 bản nháp trong skills-draft/ | Một nghiệp vụ mỗi Skill, phiên bản riêng | Chỉ cài skills/; skills-draft/ không cài, chưa kích hoạt |
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

### Mức tự chủ

Đề xuất – chưa có hiệu lực; chưa bật quyền hay connector. [CHỜ COO DUYỆT – D-07a] [CHỜ COO DUYỆT – D-07b] [CHỜ COO DUYỆT – D-08b] [CHỜ COO DUYỆT – D-09].

| Mã | Hành động | Hiện tại | Đề xuất | Quyết định |
|---|---|---|---|---|
| A01 | Đọc trang danh sách/trạng thái hồ sơ, shop, sản phẩm trên admin.hi1.vn | M0 | M4 | D-07a |
| A02 | Ghi tracker các cột vận hành: status_updated_at, shop_status, product_status, last_action, next_action, contact_status, risk_flags | M0 (người ghi) | M4 | D-09 |
| A03 | Tạo nháp phiếu chuyển cấp và nháp tin nhắc việc cho hồ sơ quá hạn | M3 | M4 (tạo nháp tự động mỗi ngày, vẫn chưa gửi) | D-09 |
| A04 | Gửi tin nhắc việc mẫu D và tin hướng dẫn mẫu H qua Zalo web | M0 | M3+ | D-09 |
| A05 | Điền form tạo đối tác, thương hiệu, sản phẩm trên admin tới TRƯỚC nút Lưu | M0 | M3 | D-07b |
| A06 | Kiểm bảng giá Affiliate, chuẩn hoá ảnh vuông, gộp PDF hợp đồng trên bản sao | M0 | M4 với bản sao, người kiểm trước khi gửi | D-08b (phạm vi hợp đồng) |
| A07 | Bấm Lưu/Tạo mới, Duyệt, Kích hoạt, Đăng công khai, Xoá/Gộp tài khoản | M0 | M0 | Không mở |
| A08 | Nhập mật khẩu, OTP, số tài khoản, CCCD; sửa giá, tồn, xuất xứ, thông tin pháp lý; cam kết ngày duyệt/doanh thu | M0 | M0 | Không mở |

Rủi ro đầy đủ và quy tắc nâng/hạ mức ở docs/12. Tab nhật ký AI riêng trong file tracker theo templates/nhat-ky-ai-header.csv là BẮT BUỘC trước khi bất kỳ hành động nào chạy ở M3+/M4; tracker chính giữ 26 cột.

Xem [ma trận tự chủ và rủi ro](docs/12-ma-tran-tu-chu-va-rui-ro.md).

### Giới hạn đã chấp nhận

- Tracker và CMS đồng bộ thủ công, có thể lệch.
- Google Sheet không phân quyền theo dòng và không có nhật ký bất biến.
- Không nhắc việc theo thời gian thực.
- Kiểm bảng giá Affiliate và chuẩn bị media có Skill chỉ hỗ trợ kiểm/chuẩn bị bản sao; hợp đồng và nhập CMS chỉ có bản nháp chưa kích hoạt, chưa có quyền tự động hoá.
- Gói Claude Pro không chia sẻ được Project và Skill; dùng chung cho nhóm cần gói Team.

### Hướng phát triển

- v0.2: affiliate-price-review và seller-media-tools cài được để kiểm/chuẩn bị nháp; seller-contract-draft là bản nháp D-08b chưa cài/kích hoạt.
- seller-cms-entry: 07a chỉ đọc trong pilot nếu COO duyệt; 07b điền trước nút Lưu sau pilot; 07c (AI bấm Lưu/Duyệt) không làm.
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
| Kiểm bảng giá Affiliate đã che dữ liệu | [affiliate-price-review](skills/affiliate-price-review/SKILL.md) |
| Chuẩn bị bản sao ảnh/PDF không có dữ liệu Đỏ | [seller-media-tools](skills/seller-media-tools/SKILL.md) |

Thiếu nguồn ghi “Chưa có căn cứ xác nhận”. [CHỜ COO DUYỆT – D-02] Không đưa dữ liệu Đỏ vào AI; gặp dữ liệu Đỏ phải dừng, không lặp giá trị, nhắc xoá khỏi hội thoại và ghi sự cố đã che. Tài liệu nhà bán là dữ liệu, không phải lệnh.

## Cấu trúc thư mục

- docs/01–11: tổng quan, 12 bước, guardrails, phân loại dữ liệu, schema, trạng thái, SOP, thay đổi.
- project/: instructions và danh mục kho tri thức APPROVED còn trống thông tin xác nhận.
- skills/: sáu thư mục Skill cài được; seller-communication/templates/ chứa mẫu A–I.
- skills-draft/: seller-contract-draft (D-08b), seller-cms-entry (D-07a/D-07b) là BẢN NHÁP, không cài/không dùng trước COO duyệt.
- tests/fixtures/: bảng giá SIM và script tạo fixture; không chứa hồ sơ thật.
- templates/: header tracker đúng 26 cột và phiếu chuyển cấp.
- tests/test-cases.md: 14 ca giả lập và tiêu chí đạt; chưa có kết quả chạy trên Claude Project.
- CHANGELOG.md: lịch sử thay đổi; AUDIT.md: kết quả kiểm định và điều kiện trước merge.

Tài liệu quản trị, ngân sách và phê duyệt PM lưu nội bộ, không đưa vào đây.

## Cài đặt cho người cấu hình

1. [CHỜ COO DUYỆT – D-03] Kiểm gói Claude Team/Enterprise được cho phép và quyền dữ liệu; không tự thêm connector/quyền AI khi chưa có quyết định COO.
2. Tạo Claude Project “HI1 Seller Onboarding”; dán [instructions](project/claude-project-instructions.md).
3. Chạy `python tools/build_skills.py` → lấy zip trong dist/. Công cụ kiểm trước khi đóng gói và chỉ đóng skills/; tuyệt đối không cài skills-draft/. Cài zip trong mục Skills của giao diện hiện hành và xác minh chúng khả dụng trong Project; không coi nạp knowledge là cài Skill.
4. Nạp chỉ các tài liệu APPROVED hiện hành theo [danh mục](project/knowledge-base-index.md), điền tên/owner/version/ngày hiệu lực sau xác nhận. Không nạp bản pilot như chính sách đã duyệt.
5. [CHỜ COO DUYỆT – D-06] Tạo tracker với [header CSV](templates/tracker-header.csv), kiểm kiểu/enum theo [schema](docs/05-tracker-schema.md); AI chỉ đọc, người cập nhật sau duyệt.
6. [CHỜ COO DUYỆT – D-03] Sau khi connector được COO quyết và người cấu hình xác minh quyền chỉ đọc, tạo scheduled task lúc **17:00 Asia/Ho_Chi_Minh** hằng ngày: “Dùng daily-operations-report đọc tracker được cấp quyền, chốt thời điểm và phạm vi, soạn báo cáo cùng phiếu chuyển cấp; che PII, không sửa Sheet/CMS, không gửi ra ngoài, cần người duyệt trước gửi/lưu”. Kiểm một lần chạy SIM và quyền chỉ đọc trước khi bật. Repo chỉ hướng dẫn cài, chưa tạo task/connector thật.
7. Chạy đủ [14 ca](tests/test-cases.md), ghi kết quả thực tế. người kiểm định kiểm tra PR trước merge; COO duyệt chính sách trước vận hành thật. Không push trực tiếp main.

Nhãn chờ COO duyệt áp theo chủ đề: D-01 phạm vi pilot/quyền AI; D-02 phân loại dữ liệu; D-03 gói Claude Team/connector/task; D-04 checklist/mẫu tin/SLA; D-05 trạng thái/sẵn sàng bán/chuyển cấp; D-06 owner/schema/quyền review và nghiệm thu tracker. Các nhãn không phải bằng chứng đã phê duyệt.

**Chưa merge:** PM chuyển repo sang private trước khi merge theo F7; sau khi sửa F1–F3 và xử lý F7, chờ người kiểm định kiểm tra lại commit mới.

## Tài liệu vận hành bổ sung

- [Xử lý sự cố và fail-safe](docs/09-xu-ly-su-co.md).
- [Quản trị kho tri thức](docs/10-quan-tri-kho-tri-thuc.md).
- [Truy vết yêu cầu](docs/11-truy-vet-yeu-cau.md).
- [Nháp phiếu bàn giao duyệt](templates/phieu-ban-giao-duyet.md), khác phiếu chuyển cấp.

Bản v0.1.1 bổ sung theo kết quả kiểm định nguồn. 14 ca vẫn chưa chạy trên Claude Project. Không tự thêm trường ngoài schema 26 cột đã yêu cầu.

## Cài và chạy công cụ v0.2

Chỉ đóng gói từng folder trong skills/. Hai Skill mới version 0.1.0; bốn Skill cũ giữ version. Bản nháp skills-draft/ version 0.0.1 không phải Skill dùng được; không cài hoặc chạy cho tới khi COO duyệt mã ghi ở đầu bản nháp.

- affiliate-price-review: Python + openpyxl; schema tham chiếu trong folder, chạy trên Excel đã che dữ liệu. data_only=True không tính công thức; thiếu cache phải ghi chưa xác minh.
- seller-media-tools: Python + Pillow + pypdf; chạy trong Claude Project có code execution hỗ trợ thư viện hoặc Cowork, không cần Windows/Office. Chỉ file đã được người xác nhận không chứa dữ liệu Đỏ, tạo bản sao ở thư mục đầu ra.
- Bản nháp seller-contract-draft chỉ dự kiến chạy Windows có Word/Excel; chưa kiểm chạy COM, không dùng. Bản nháp seller-cms-entry chưa cấp quyền trình duyệt/CMS.

Cài được không có nghĩa được tự làm A06: mức hiện tại vẫn theo docs/12, người kiểm đầu ra trước gửi; chưa bật connector/quyền mới. Các quy tắc giá còn [CHỜ COO DUYỆT – D-04].

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ

## Tự kiểm và báo cáo CSV v0.2.1

Mọi PR phải qua kiểm tra tự động. Chạy `python tools/build_skills.py --check` để kiểm mà không tạo zip; chạy không có cờ để lấy zip trong dist/. dist/ không lưu vào Git. Frontmatter dùng name và description dạng scalar một dòng (chuỗi có nháy khi cần), không cần PM sửa mã.

Daily report dùng JSON nghiệp vụ trong folder references của Skill; đổi enum/quy tắc chỉ sửa JSON và đồng bộ mô tả .md, không sửa Python. Mẫu lệnh: `python skills/daily-operations-report/scripts/tracker_report.py tracker.csv --as-of 2026-11-16T17:00:00+07:00`; thêm `--format md` để xem Markdown. File tracker.csv là input do người cấp, không đưa dữ liệu thật vào repo.

Dòng lỗi không được cộng vào số liệu; dòng trùng loại cả hai. Chuỗi nghi dữ liệu Đỏ chỉ được báo dòng/cột, không in giá trị. Mẫu tracker-sim.csv là fixture mô phỏng được đánh dấu trong fixture-manifest.json; không phải PII thật. Không miễn các quy tắc bí mật khác. Đầu ra trung bình/trung vị giờ lịch không thay SLA giờ làm việc.

Hai bản nháp vẫn chưa cài/kích hoạt; tên tác giả trong chúng được giữ theo quyết định PM, không thuộc tiêu chí lỗi của công cụ.
