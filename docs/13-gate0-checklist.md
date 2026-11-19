# Checklist Gate 0 trước khi đưa nguồn vào T1-ready

Tác giả: PM - TKC · Áp dụng cho nguồn tri thức nhà bán và các phòng ban khác.

| Bước | Người làm | Bằng chứng cần ghi |
|---|---|---|
| 1. Đăng ký nguồn | Người nạp | source_id, tên, phiên bản, nơi lưu gốc, quyền truy cập. |
| 2. Phân lớp trước xử lý | Người nạp | Xanh/Vàng/Đỏ; kiểm cả ảnh nhúng, bảng, phụ lục, video và liên kết. Nghi Đỏ thì dừng nguồn. |
| 3. Tạo bản che | Người nạp | Chỉ trên bản sao trong vùng hạn chế; che giá trị Đỏ, thay dữ liệu Vàng theo quyết định quyền hiện hành. Không dùng tác nhân xử lý bản Đỏ để tự che. |
| 4. Kiểm độc lập | Người kiểm thứ hai | Xem toàn bộ bản che, kể cả trang/ô/ảnh nhúng; ghi đạt hoặc BLOCKED, người kiểm và thời điểm. |
| 5. Tính hash | Người được phân công | Hash SHA-256 của **bản đã che**; ghi vào sổ nguồn cùng phiên bản. Sửa bản che thì tính lại và kiểm lại. |
| 6. Chuyển T1-ready | Người kiểm thứ hai | Chỉ bản đạt vào thư mục T1-ready có quyền hạn chế; cấp gate0_id gắn source_id@version + hash. |
| 7. Bàn giao batch | PM | Đối chiếu gate0_id và hash với sổ nguồn trước khi mở nội dung; thiếu hoặc lệch thì chặn. |

Nguồn bị BLOCKED chỉ lưu con trỏ trong vùng hạn chế. Không lưu bản gốc, giá trị Đỏ hoặc bảng đối chiếu danh tính trong repo. Việc đánh dấu APPROVED cho tri thức là bước duyệt riêng sau Gate 0.
