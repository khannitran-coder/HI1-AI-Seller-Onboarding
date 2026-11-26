# SOP hằng ngày cho nhân viên

v0.3.0 – pilot, chưa COO duyệt

| Mục | Nội dung |
|---|---|
| Mã | SOP-SEL-01 |
| Áp dụng | Nhóm Phát triển & Hỗ trợ Nhà bán Hi1, giai đoạn pilot từ 24/11/2026 |
| Chủ sở hữu | Trưởng nhóm (vận hành); Bắc (owner tri thức); Huyền (duyệt KU) |
| Liên quan | [Quy trình 12 bước](02-quy-trinh-12-buoc.md), [guardrails](03-guardrails.md), [trạng thái](06-trang-thai.md), [sự cố](09-xu-ly-su-co.md), [mức tự chủ](12-ma-tran-tu-chu-va-rui-ro.md), [điều kiện chạy thử](13-dieu-kien-chay-thu-ho-so-that.md) |

## 1. Mục đích

Mỗi nhân viên xử lý hồ sơ nhà bán cùng một cách: Claude làm phần đọc, đối chiếu, điền nháp ở cả 12 bước; nhân viên kiểm, quyết định và bấm nút cuối. Vướng mắc chỉ đi qua 2 cấp.

## 2. Vai trò

| Vai trò | Làm | Không làm |
|---|---|---|
| Nhân viên phụ trách | Ra lệnh cho Claude từng hồ sơ; kiểm nháp với bản gốc; tự gửi tin, tự bấm Tạo mới/Lưu trên CMS, tự ghi tracker | Giao AI gửi tin, bấm nút cuối, nhập mật khẩu |
| Claude (Cowork) | Đọc thư mục/Zalo PC/CMS được phép; nháp tin, bảng đối chiếu, form CMS tới trước Tạo mới; báo cáo 17:00 | Gửi, lưu, duyệt, ghi tracker, quyết định thay người |
| Cấp 1 – Nghiệp vụ | Trưởng nhóm điều phối; kiểm duyệt nhà bán, ngành hàng-pháp chế, kỹ thuật, CSKH-vận chuyển-thanh toán, owner tri thức trả lời đúng mảng | Quyết ngoại lệ chính sách |
| Cấp 2 – COO | Quyết chính sách, quyền AI và mức tự chủ, nguồn, ngoại lệ chưa có căn cứ; nhận báo sự cố nghiêm trọng | — |

## 3. Quy tắc pilot (đọc trước)

Theo quyết định của người thiết kế agent, 22–26/11/2026. Chỉ nhận hồ sơ thật khi đạt [điều kiện chạy thử](13-dieu-kien-chay-thu-ho-so-that.md).

| Việc | Quy tắc |
|---|---|
| Phạm vi | Doanh nghiệp, HTX, hộ kinh doanh có MST và hóa đơn; hàng thông thường. Thực phẩm, TPCN, mỹ phẩm, hàng nhập khẩu, OCOP: chỉ đối chiếu giấy tờ rồi chuyển Cấp 1 ngành hàng-pháp chế. Cá nhân tự do: chuyển Cấp 1 Trưởng nhóm |
| AI hỗ trợ | Cả 12 bước của [quy trình](02-quy-trinh-12-buoc.md), mức ghi trong cột M. Bước dùng CMS chờ COO duyệt D-07a/D-07b; trước đó nhân viên tự thao tác CMS |
| Nơi làm việc | Claude Cowork (ứng dụng Claude desktop), Project “HI1 Seller Onboarding” cho hồ sơ thật; Project “– Thử nghiệm” chỉ dùng dữ liệu mô phỏng |
| Dữ liệu được đưa vào | Tên, SĐT, email, MST, địa chỉ, số CCCD người đại diện, số tài khoản công ty; chỉ phần cần dùng. Công cụ ảnh/PDF và bảng giá không nhận giấy tờ tuỳ thân |
| Dữ liệu cấm | Mật khẩu, OTP, token, khóa API |
| Đầu ra | Không chép đầy đủ số CCCD, số tài khoản vào tin nhắn, báo cáo, tracker, phiếu (ghi “đã nhận” hoặc 4 số cuối) |
| Cách chạy | Làm song song: AI soạn nháp, nhân viên so lại và tự gửi. Không gửi nhà bán nội dung AI khi chưa có KU đã duyệt (tài liệu nguồn đã duyệt chưa đủ) |
| Chưa có căn cứ | AI ghi “Chưa có căn cứ xác nhận” thì không tự trả lời; làm theo mục 7 |
| Nội dung đang hoãn | Thời điểm đổi giá/tỷ lệ Affiliate; ngày đối soát và chi hoa hồng; cơ sở tính chiết khấu; xử lý vi phạm và khóa shop, quy định niêm yết giá trong Sổ tay; số ngày chờ nhận tiền; phí nhà bán chịu. Không gửi câu “0 phí trung gian” |
| Dừng ngay | Theo điều kiện dừng ở [docs/13](13-dieu-kien-chay-thu-ho-so-that.md) mục 4. Người ghi sự cố: (chưa gán) |
| Nhân viên tham gia | (chưa gán) |

## 4. Chuẩn bị đầu ca (5 phút)

1. Mở Claude desktop, vào Project “HI1 Seller Onboarding”. Kiểm thư mục NHÀ BÁN và Zalo Received Files đã kết nối; Chrome đã đăng nhập admin.hi1.vn, extension Claude in Chrome bật.
2. Mở tracker trong phạm vi được giao; kiểm người phụ trách, việc tiếp theo, hạn đã xác nhận.
3. Kiểm kho tri thức APPROVED, phiên bản và quyền truy cập. Thiếu/hết hiệu lực: phần phụ thuộc dừng, ghi “Chưa có căn cứ xác nhận”, chuyển Cấp 1 owner tri thức.

## 5. Xử lý một hồ sơ theo 12 bước

Mỗi hồ sơ một hội thoại mới trong Project. Câu lệnh mẫu (thay phần trong ngoặc):

| Bước | Câu lệnh mẫu cho Claude | Nhân viên tự làm |
|---|---|---|
| 1. Nhận lead | “Đọc nhóm Zalo [tên nhóm] và thư mục [tên shop], lập danh sách thông tin đã có/thiếu, soạn tin chào và tin xin SĐT quản trị.” | Phân công, gửi tin |
| 2. Kiểm trùng | “Tìm trên CMS đối tác trùng tên/MST/SĐT với [shop].” | Xác minh trùng |
| 3. Phân loại | “Đề xuất chủ thể, ngành hàng, loại hình DN, mảng phụ trách cho [shop].” | Xác nhận |
| 4. Đối chiếu hồ sơ | “Đối chiếu giấy tờ trong thư mục [shop] với biểu mẫu hồ sơ hiện hành.” | Kiểm bản gốc |
| 5. Yêu cầu bổ sung | “Soạn tin xin bổ sung các mục thiếu.” | Duyệt, gửi |
| 6. Mở shop | “Mở shop và tạo thương hiệu cho [shop], SĐT quản trị [số đã chốt].” Claude dừng trước Tạo mới | Nhập mật khẩu, kiểm form, bấm Tạo mới; gửi và ghim tin tài khoản (tự điền mật khẩu) |
| 7. Sản phẩm đầu tiên | “Kiểm bảng giá [file]”; “Nháp mô tả sản phẩm [tên]”; “Làm ảnh vuông [file]” | Nhà bán xác nhận giá/tồn/xuất xứ; người có quyền đăng |
| 8. Chuyển duyệt | “Soạn phiếu bàn giao duyệt; kiểm sản phẩm chờ duyệt của [shop].” | Chuyển và duyệt trên CMS |
| 9. Vận hành đơn | “Soạn hướng dẫn xử lý đơn cho nhà bán theo KU hiện hành.” | Hướng dẫn, xác nhận nhà bán hiểu |
| 10. Sẵn sàng bán | “Tổng hợp điều kiện Sẵn sàng bán của [shop].” | Trưởng nhóm xác nhận |
| 11. Bàn giao | “Soạn tin bàn giao và mốc chăm sóc.” | Chốt mốc, gửi |
| 12. Cuối ngày | Scheduled task 17:00 tự chạy; hoặc “Báo cáo cuối ngày từ tracker [bản xuất].” | Trưởng nhóm duyệt báo cáo, phiếu chuyển cấp |

Với mỗi đầu ra: so từng nhận xét với CMS/tài liệu gốc, ghi review_result (duyệt nguyên/sửa nhỏ/sửa lớn/bỏ), rồi mới hành động. “Được duyệt” chỉ lấy từ CMS hoặc người có thẩm quyền; Sẵn sàng bán phải đủ toàn bộ điều kiện trong [docs/06](06-trang-thai.md).

## 6. Chuyển cấp – 2 cấp

| Cấp | Khi nào | Gửi ai | Cách gửi |
|---|---|---|---|
| Cấp 1 – Nghiệp vụ | Thiếu nguồn; mâu thuẫn giấy tờ; ngành có điều kiện; lỗi CMS/đăng nhập; khiếu nại đơn/vận chuyển/thanh toán; nghi trùng; hồ sơ quá hạn | Trưởng nhóm, hoặc thẳng bộ phận đúng mảng (kiểm duyệt nhà bán, ngành hàng-pháp chế, kỹ thuật, CSKH, owner tri thức) | Nhờ Claude “Soạn phiếu chuyển cấp” theo [mẫu](../templates/phieu-chuyen-cap.md); nhân viên tự gửi qua kênh nội bộ |
| Cấp 2 – COO | Ngoại lệ chính sách; đổi quyền AI/mức tự chủ; nguồn chưa có căn cứ cần quyết; sự cố nghiêm trọng (lộ dữ liệu Đỏ, gửi/ghi ngoài phạm vi); Cấp 1 không xử lý được | COO, qua Trưởng nhóm | Phiếu chuyển cấp ghi “cấp 2-COO” và câu hỏi quyết định cụ thể |

Ghi escalation_to trong tracker theo enum tại [docs/05](05-tracker-schema.md).

## 7. Hỏi owner khi AI chưa có căn cứ (Cấp 1 owner tri thức)

Claude không tự thông báo cho ai; nhân viên chuyển câu hỏi.

1. Yêu cầu Claude: “Soạn phiếu chuyển cấp cho owner”; không chép đầy đủ số CCCD, số tài khoản.
2. Thêm một dòng vào bảng “Hỏi owner” dùng chung (cột theo [mẫu](../templates/hang-cho-hoi-owner.csv)), rồi nhắn Bắc qua kênh nội bộ kèm mã dòng.
3. Bắc trả lời trong bảng, ghi tên và ngày. Nhân viên trả lời nhà bán theo câu trả lời đó, không nói như quy định đã được duyệt nếu Bắc ghi là xử lý riêng. Cần ngoại lệ chính sách: Bắc chuyển Cấp 2 COO.
4. Câu hỏi lặp lại: Bắc đưa câu trả lời vào tài liệu nguồn, tạo KU revision mới, Huyền duyệt, rồi nạp lại Project.

Thời hạn Bắc phản hồi: chưa định. Chưa có câu trả lời thì báo nhà bán đang chờ xác nhận, không hứa mốc.

## 8. Gửi ảnh hướng dẫn tải App

Được gửi ảnh “Hướng Dẫn Tải APP” hiện tại (quyết định 25/11/2026). Ảnh có ô đăng nhập hiển thị thông tin tài khoản ở bước 4, nên trước lần gửi đầu người phụ trách phải xác nhận mật khẩu đó đã đổi hoặc tài khoản mẫu đã khóa.

Đã xác nhận: (chưa) — người xác nhận, ngày: …

Không tải ảnh này lên Claude; Project dùng bản chữ.

## 9. Ghi nhận và cuối ca

1. Sau mỗi hành động: tự ghi tracker thời điểm, reviewer, review_result, skill_version, next_action, hạn; không ghi dữ liệu Đỏ, số CCCD hay số tài khoản. Ghi tab nhật ký AI theo [mẫu](../templates/nhat-ky-ai-header.csv). AI không ghi tracker.
2. 17:00 Asia/Ho_Chi_Minh: scheduled task chạy daily-operations-report. Chưa có connector được duyệt (D-03) thì đưa bản xuất đã bỏ dữ liệu cá nhân vào bằng tay, không tự mở quyền.
3. Trưởng nhóm duyệt báo cáo và phiếu chuyển cấp; ghi góp ý vào [mẫu góp ý](../templates/gop-y.csv).

Đo trong pilot: thời gian phản hồi đầu, tỷ lệ hồ sơ đủ sau lượt đầu, phút xử lý mỗi hồ sơ, tỷ lệ nháp được duyệt không cần sửa, số sự cố.

## 10. Sự cố

Mật khẩu/OTP/token/khóa API vào AI, lệnh ẩn, ngoài quyền, Claude thao tác ngoài lệnh hoặc lỗi nghiêm trọng: dừng, không lặp dữ liệu, nhắc xoá khỏi hội thoại; tắt Claude in Chrome nếu đang chạy; báo Cấp 1 Trưởng nhóm và ghi sự cố đã che; Trưởng nhóm báo Cấp 2 COO nếu là sự cố nghiêm trọng. Theo [ma trận fail-safe](09-xu-ly-su-co.md). Nguồn thay phiên bản: theo [quản trị kho tri thức](10-quan-tri-kho-tri-thuc.md). SLA pilot chưa được dùng làm cam kết với nhà bán.

Nguồn bổ sung: HI1-P1A-SOL-001 v0.1 mục §6; BRD HI1-AI-BRD-SD-1.2 mục NFR-03; skills/hi1-mo-shop (26/11/2026).
