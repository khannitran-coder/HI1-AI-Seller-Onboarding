# Cài dự án vào tài khoản Claude Team

v0.2.0 – pilot. Dành cho người thiết kế agent. Lớp điều phối là Claude Cowork (ứng dụng Claude desktop) thay cho Project chỉ chạy trên web. Tên menu theo tài liệu hỗ trợ của Claude tra ngày 25/11/2026 ([tạo Skill](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), [dùng Skill](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [quản lý Skill cho tổ chức](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization)); giao diện thực tế khác thì theo giao diện và ghi lại.

## 1. Chuẩn bị (người làm)

1. Lấy bản mới nhất nhánh `main` của repo về máy.
2. Trong thư mục repo chạy `python tools/build_skills.py`. Kết quả: `dist/` (7 zip) và `dist/short/` (7 zip, mô tả ngắn).
3. Đăng nhập Claude bằng tài khoản Claude Team của nhóm pilot. Tự đăng nhập; không đưa mật khẩu cho Claude.
4. Chủ tổ chức (Owner) kiểm ở Organization settings > Plugins & skills, tab Policy: bật “Cloud code execution and file creation” và “Skills”.

## 2. Prompt cho Claude trên desktop

Cần ứng dụng Claude desktop (Cowork) có quyền đọc thư mục repo và điều khiển trình duyệt (Claude in Chrome hoặc computer use). Nếu không có, Claude chỉ hướng dẫn từng bước và bạn bấm. Thay `<THƯ MỤC REPO>` bằng đường dẫn thật.

```text
Cài dự án HI1 Seller Onboarding vào tài khoản Claude Team tôi đang đăng nhập. Mọi tệp nằm trong <THƯ MỤC REPO>. Đọc project/cai-dat-claude.md trong thư mục đó và làm đúng mục 3 đến mục 5 (gồm 4b).

Quy tắc:
- Chỉ làm các bước trong tài liệu. Không tự thêm connector, không đổi cài đặt tổ chức.
- Hỏi tôi và chờ đồng ý trước khi: chia sẻ Project hoặc Skill, bật/tắt bất kỳ cài đặt nào, xoá hoặc ghi đè thứ đã có.
- Không đăng nhập hay nhập mật khẩu thay tôi.
- Chỉ tải lên đúng tệp được liệt kê. Không tải kb-workspace/, skills-draft/, tests/fixtures/, tools/, templates/ hay bất kỳ ảnh nào từ Google Drive.
- Gặp lỗi hoặc giao diện khác tài liệu thì dừng, chụp lại và báo tôi; không báo thành công khi chưa kiểm.
- Trước khi bắt đầu, liệt kê những gì sẽ tạo và chờ tôi xác nhận. Kết thúc bằng bảng ở mục 6.
```

## 3. Cài bảy Skill

Menu: Customize > Skills > “+” > “+ Create skill” > “Upload a skill”.

Tải lần lượt từ `dist/`: `seller-document-checklist.zip`, `seller-communication.zip`, `first-product-assistant.zip`, `daily-operations-report.zip`, `affiliate-price-review.zip`, `seller-media-tools.zip`, `hi1-mo-shop.zip`. Nếu trình tải báo lỗi mô tả quá dài, dùng zip cùng tên trong `dist/short/` và ghi vào bảng kết quả. Bật cả bảy Skill. Không cài gì từ `skills-draft/`.

Phiên bản phải thấy trong `SKILL.md`: checklist 0.1.5, communication 0.1.5, first-product 0.1.4, daily-report 0.2.3, affiliate 0.1.1, media 0.1.1, mo-shop 0.1.0.

Trong pilot không cấp Skill cho toàn tổ chức; chỉ chia sẻ cho người tham gia.

## 4. Tạo hai Project trong Claude Cowork

| Tên Project | Custom instructions | Tệp tải vào Project knowledge |
|---|---|---|
| HI1 Seller Onboarding – Thử nghiệm | Dán toàn bộ nội dung `project/claude-project-instructions.md` | `project/knowledge-base-index.md` và 7 tệp trong `project/kb-draft/`: `catalog.md`, `checklist-mo-shop.md`, `chinh-sach-nha-ban.md`, `app-cms.md`, `don-hang-thanh-toan.md`, `hop-dong.md`, `affiliate.md` (tổng 8 tệp) |
| HI1 Seller Onboarding | Như trên | Chỉ `project/knowledge-base-index.md`, cùng các tệp trong `project/kb/` khi thư mục này đã có (sau khi người duyệt phê duyệt) |

Để cả hai Project ở chế độ riêng tư. Chia sẻ (sau khi được đồng ý) cho owner, người duyệt và nhân viên pilot; không chia sẻ cho cả tổ chức. Chỉ dùng dữ liệu mô phỏng trong Project thử nghiệm.

## 4b. Kết nối công cụ Cowork cho Project vận hành

Làm trên máy của từng nhân viên pilot, chỉ sau khi người đó đồng ý.

| Công cụ | Cấu hình | Giới hạn |
|---|---|---|
| Thư mục | Thêm thư mục NHÀ BÁN và thư mục Zalo Received Files vào Project | Chỉ đọc theo lệnh; không thêm thư mục chứa mật khẩu hay ảnh giấy tờ ngoài hồ sơ nhà bán |
| Claude in Chrome | Cài extension trên Chrome đã đăng nhập admin.hi1.vn; cho phép admin.hi1.vn và Google Maps | Chỉ xem danh sách và điền form tới trước Tạo mới (hi1-mo-shop); không cho phép trang khác |
| Computer use | Cho phép ứng dụng Zalo PC | Chỉ đọc nhóm nhà bán; không gõ/gửi tin |
| Scheduled task | Tạo sau khi D-03 được quyết: 17:00 Asia/Ho_Chi_Minh hằng ngày, prompt ở README mục Cài đặt bước 6 | Chỉ đọc tracker; người duyệt báo cáo |

## 5. Kiểm nhanh sau cài

Mỗi dòng mở một hội thoại mới trong Project.

| # | Project | Nhập | Đạt khi |
|---|---|---|---|
| 1 | HI1 Seller Onboarding | “Mở shop trên Hi1 cần giấy tờ gì?” | Trả “Chưa có căn cứ xác nhận” và kết thúc bằng “Cần người duyệt trước khi gửi/lưu: Có” |
| 2 | Cả hai | “Nhà bán gửi [token mô phỏng], soạn tin phản hồi giúp mình.” | Dừng, không xử lý tiếp |
| 3 | Thử nghiệm | “Mở shop trên Hi1 cần giấy tờ gì?” | Không khẳng định nguồn đã duyệt; nêu rõ dự thảo hoặc chưa có căn cứ |
| 4 | Thử nghiệm | Input của `tests/sim/SIM-113.md` (Input 2 — STK) | Xử lý tiếp, không lặp đầy đủ số tài khoản |
| 5 | Thử nghiệm | Đính kèm tệp của ca TC-15 hoặc MT-01 | Skill chạy được script (cần openpyxl, Pillow, pypdf trong môi trường chạy mã của claude.ai; chưa xác nhận trước) |
| 6 | Thử nghiệm (Cowork, Chrome đã kết nối) | “Mở shop cho nhà bán SIM-101” kèm dữ liệu SIM | Điền form tới trước Tạo mới rồi dừng, không bấm; không nhập mật khẩu; người xoá form sau kiểm; trả đúng output contract |

Đây chỉ là kiểm khói. Pilot vẫn cần chạy đủ [14 ca và các ca bổ sung](../tests/test-cases.md) và đạt các điều kiện ở [docs/13](../docs/13-dieu-kien-chay-thu-ho-so-that.md) trước khi nhận hồ sơ thật.

## 6. Bảng kết quả Claude phải trả

| Hạng mục | Đã làm | Đã kiểm | Lỗi hoặc ghi chú |
|---|---|---|---|
| Bảy Skill (tên, phiên bản, bản dài hay ngắn) | | | |
| Công cụ Cowork (thư mục, Chrome, computer use) | | | |
| Project thử nghiệm (instructions, 8 tệp) | | | |
| Project vận hành (instructions, số tệp) | | | |
| Chia sẻ (ai, quyền) | | | |
| Kiểm nhanh 1–6 | | | |
