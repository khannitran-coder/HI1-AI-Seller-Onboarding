# Chính sách nhà bán: mô hình F2C, quy định cơ bản, thông điệp phí

> **Chỉ gồm KU đã APPROVED theo file phê duyệt.** Còn hiệu lực và đúng phạm vi mới được dùng; xem giao thức truy xuất trong knowledge-base-index. KU chưa ghi ngày hiệu lực được dùng từ ngày duyệt (quy tắc pilot). KU có nhãn MÂU THUẪN CHƯA QUYẾT: không kết luận phần đang mâu thuẫn.

### 001:c0021 — Thông điệp phí trên tờ rơi mở shop: 0 phí sàn, 0 phí nền tảng, 0 phí trung gian
- Trạng thái: APPROVED (còn mâu thuẫn chưa quyết); người duyệt người thiết kế agent (duyệt cho pilot, chưa đối chiếu từng KU với nguồn); ngày duyệt 2026-11-25; hiệu lực từ chưa ghi
- **MÂU THUẪN CHƯA QUYẾT CF-06: các loại phí nhà bán chịu; không gửi nhà bán câu “0 phí trung gian”.** Với đúng nội dung này: không kết luận, không gửi nhà bán; nêu các nguồn đang khác nhau (KU liên quan: 001:c0006), ghi “Chưa có căn cứ xác nhận” và chuyển Bắc. Phần khác của KU được dùng.
- Phiên bản candidate: r2
- Loại: L1/RULE; đối tượng: staff; phạm vi: {"seller_type": ["DN", "HKD", "HTX"]}
- Nguồn: SIM-SRC-002 (61e9c3c2dec45e9a07d5.jpg, Dải chữ đỏ dưới tiêu đề)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: conflict, gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0006

**Điều kiện**
Tờ rơi mời mở shop dành cho doanh nghiệp, HTX, hộ kinh doanh có mã số thuế và hóa đơn hàng hóa.

**Nội dung**
Tờ rơi ghi: “0 phí sàn – 0 phí nền tảng – 0 phí trung gian”.

**Ngoại lệ**
Tờ rơi không nêu ngoại lệ. CẢNH BÁO mâu thuẫn CF-06 với hợp đồng mẫu Điều 4 (001:c0006, nhà bán chịu phí cổng thanh toán, phí vận chuyển nếu có): không khẳng định với nhà bán rằng không có phí nào cho tới khi owner quyết.

**Chứng từ**
Không nêu.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Lần xử lý r1 đọc thiếu dải chữ này do chữ OCR bị đứt, nên đã đánh giá nhầm là khớp hợp đồng. r2 đọc trực tiếp từ ảnh.


### 002:c0001 — Mô hình F2C của Hi1 và đối tượng nhà bán được hợp tác
- Trạng thái: APPROVED; người duyệt người thiết kế agent (duyệt cho pilot, chưa đối chiếu từng KU với nguồn); ngày duyệt 2026-11-25; hiệu lực từ chưa ghi
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 01 Giới thiệu mô hình sàn F2C; mục 02 Ghi chú dưới phần Cung cấp thông tin)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0006

**Điều kiện**
Nhà bán muốn hợp tác với sàn Hi1 theo mô hình F2C (Factory to Consumer: bán từ nhà máy đến người tiêu dùng, bỏ qua trung gian).

**Nội dung**
Sàn TMĐT F2C Hi1 chỉ hợp tác với nhà sản xuất, nhà nhập khẩu hoặc đại lý ủy quyền; không hợp tác với trung gian kinh doanh.
Theo mô hình F2C trên Hi1: nhà sản xuất/nhà bán chủ động đăng sản phẩm và tự vận hành gian hàng; sàn kết nối công nghệ, không thu phí sàn, hỗ trợ marketing, CSKH, vận hành, livestream trên app và tích hợp AI; người tiêu dùng mua hàng chính hãng trực tiếp từ nhà sản xuất.

**Ngoại lệ**
Nguồn không nêu ngoại lệ. “Không thu phí sàn” không đồng nghĩa không có phí nào: phí cổng thanh toán và phí vận chuyển (nếu có) vẫn do nhà bán chịu theo hợp đồng.

**Chứng từ**
Không nêu ở mục này.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Phạm vi 'nhà sản xuất, nhà nhập khẩu, đại lý ủy quyền' là trục khác với loại hình DN/HKD/HTX nên facet seller_type để null. Không dùng 'chính hãng' để hứa với khách hay nhà bán khi chưa có chứng cứ.


### 002:c0010 — Quy định cơ bản cho nhà bán: giá niêm yết, phí ship, nguồn gốc hàng hóa
- Trạng thái: APPROVED (còn mâu thuẫn chưa quyết); người duyệt người thiết kế agent (duyệt cho pilot, chưa đối chiếu từng KU với nguồn); ngày duyệt 2026-11-25; hiệu lực từ chưa ghi
- **MÂU THUẪN CHƯA QUYẾT CF-04: xử lý khi nhà bán vi phạm, gỡ sản phẩm, khóa gian hàng.** Với đúng nội dung này: không kết luận, không gửi nhà bán; nêu các nguồn đang khác nhau (KU liên quan: 001:c0004), ghi “Chưa có căn cứ xác nhận” và chuyển Bắc. Phần khác của KU được dùng.
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 05 — khung 'Quy định cơ bản cho nhà bán' A–C)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: conflict, gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0004

**Điều kiện**
Nhà bán đăng bán sản phẩm trên Hi1.

**Nội dung**
A. Giá niêm yết công khai: mỗi sản phẩm phải có giá rõ ràng, gồm giá thị trường và giá cho hội viên Hi1. Không ghi “inbox giá”, không đăng giá ảo. Thay đổi giá thì cập nhật trực tiếp trên CMS.
B. Phí ship: trường hợp 1, người bán chịu toàn bộ phí; trường hợp 2, khách tự trả 100%. Tùy chỉnh tại mục “Cài đặt miễn phí vận chuyển” trên app Hi1.
C. Hàng hóa phải có nguồn gốc rõ ràng: không bán hàng giả, hàng nhái, hàng cấm. Sản phẩm cần có nhãn mác, mô tả đúng, thông tin xuất xứ rõ ràng. Vi phạm thì bị gỡ sản phẩm, cảnh báo hoặc khóa gian hàng.

**Ngoại lệ**
Nguồn không nêu ngoại lệ, không có danh mục hàng cấm cụ thể và không nêu quy trình thông báo hay thời hạn khắc phục trước khi gỡ hoặc khóa.

**Chứng từ**
Nhãn mác, mô tả, thông tin xuất xứ của sản phẩm.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Mâu thuẫn nghi ngờ CF-04 với SIM-BATCH-001:c0004: hợp đồng yêu cầu thông báo và cho 03 ngày làm việc khắc phục trước khi tạm ẩn/gỡ; sổ tay ghi bị gỡ, cảnh báo hoặc khóa gian hàng, không nêu bước thông báo.

