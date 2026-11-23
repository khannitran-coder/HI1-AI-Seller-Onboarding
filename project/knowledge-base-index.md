# Danh mục kho tri thức

v0.3.0 – pilot, chưa COO duyệt

**Hiện trạng: chưa có tài liệu hoặc KU nào APPROVED.** Danh mục này chỉ để TÌM đúng nhóm tài liệu; không phải căn cứ trả lời. Mọi dòng bên dưới đang ở DRAFT, không được nạp vào Project và không dùng tư vấn cho tới khi người duyệt chuyển sang APPROVED. Khi chưa có dòng APPROVED đúng nhóm, agent trả đúng câu “Chưa có căn cứ xác nhận”. Không upload bản pilot để thay nguồn duyệt.

Owner và người duyệt: theo quyết định của người thiết kế agent (2026-11-22), owner là Bắc (Phát triển nhà bán), người duyệt là Huyền. Người duyệt không tự duyệt KU do chính mình soạn; mỗi KU có hai người khác nhau soạn và duyệt.

## A. Giao thức truy xuất (bắt buộc)

1. Bảng B và C chỉ dùng để tìm. Tên nhóm, ý định hay tóm tắt không phải căn cứ trả lời.
2. Trước khi trả lời nghiệp vụ, mở tài liệu hoặc KU đầy đủ và các KU liên quan (ngoại lệ, phụ thuộc, bản thay thế). Thiếu một phần thì không kết luận.
3. Chỉ dùng dòng có Trạng thái APPROVED, còn hiệu lực và đúng phạm vi (loại nhà bán, ngành hàng, kênh). DRAFT và VERIFIED không dùng.
4. Case (L2) và bài học (L3) chỉ để tham khảo nội bộ, không nói với nhà bán như quy định.
5. Hai nguồn mâu thuẫn: không chọn hộ, ghi cả hai và chuyển owner.
6. Không có căn cứ: ghi “Chưa có căn cứ xác nhận” và chuyển owner của nhóm đó. Không hứa ngày duyệt, doanh thu, ưu đãi hay SLA chưa duyệt.
7. Mỗi câu trả lời nghiệp vụ ghi tên tài liệu hoặc mã KU và phiên bản (mục Nguồn trong output contract).

## B. Nhóm tài liệu, nguồn hiện có và trạng thái

Cột Version ghi theo tên file hoặc ngày sửa trên Drive, không phải số phiên bản đã duyệt. KU tạm là mã `batch:cXXXX` trong kb-workspace, với 001 là SIM-BATCH-001 và 002 là SIM-BATCH-002; chỉ để người duyệt đối chiếu. Người duyệt và ngày hiệu lực để trống tới khi duyệt.

| Nhóm tài liệu cần tìm | Tài liệu hiện có (chưa duyệt) | Owner → duyệt | Version | Ngày hiệu lực | Trạng thái | Người duyệt | Ngày rà soát tiếp | KU tạm | Nạp Project |
|---|---|---|---|---|---|---|---|---|---|
| Checklist hồ sơ theo loại hình/ngành hàng | Thông tin và giấy tờ mở shop (văn bản mở shop, tờ rơi, Sổ tay nhà bán); giấy tờ riêng cho thực phẩm, TPCN, mỹ phẩm, hàng nhập khẩu. Chưa có checklist theo loại hình DN/HKD/HTX và chưa có OCOP | Bắc → Huyền | Sổ tay không rõ ngày; văn bản mở shop sửa 21/11/2026 | | DRAFT | | | 001:c0001; 002:c0002, c0004 | Không |
| Chính sách nhà bán và điều kiện phê duyệt | Mô hình F2C và đối tượng hợp tác (nhà sản xuất, nhập khẩu, đại lý ủy quyền); quy định cơ bản (giá niêm yết, phí ship, nguồn gốc hàng). Chưa có điều kiện duyệt, từ chối, tiêu chí | Bắc → Huyền | Sổ tay không rõ ngày | | DRAFT | | | 002:c0001, c0010 | Không |
| Chính sách nội dung, ngành hàng cấm/có điều kiện | Chỉ có quy định chung “không bán hàng giả, nhái, cấm”. Chưa có danh mục cấm hoặc có điều kiện | Bắc → Huyền | | | DRAFT (một phần) | | | 002:c0010 | Không |
| Hướng dẫn App Nhà Bán Hi1 hiện hành | Hướng dẫn tải và dùng app; CMS (đăng nhập, thông tin shop, thương hiệu, sản phẩm, đơn hàng); app Hi1 Seller. Menu chưa được xác minh bằng ảnh chụp hiện hành | Bắc → Huyền | Sổ tay không rõ ngày; ảnh hướng dẫn sửa 02/10/2026 | | DRAFT | | | 001:c0019; 002:c0005–c0008 | Không |
| Hướng dẫn vận chuyển/thanh toán/xử lý đơn | Trạng thái đơn hàng, quy trình đơn, thanh toán COD/online, đối soát, đổi trả; hợp đồng mẫu Điều 4 và 6. Biểu phí thanh toán và biểu cước vận chuyển chưa có nội dung | Bắc → Huyền | 11.11.2026; Sổ tay | | DRAFT | | | 001:c0006–c0008; 002:c0007, c0009, c0011, c0012 | Không |
| Mẫu tin và kênh liên hệ chính thức | Mẫu tin A–I trong skills/seller-communication/templates; mẫu A–D đề xuất trong bảng trả lời của COO. Cấu hình Skill, không tạo KU | Bắc → Huyền | v0.1.2 | | DRAFT | | | | Không |
| SLA, lịch làm việc và chuyển cấp | SLA đề xuất thí điểm và ba cấp chuyển cấp trong bảng trả lời của COO (tài liệu nêu rõ chưa phải quy định hiện hành) | Bắc → Huyền | | | DRAFT | | | | Không |
| Ánh xạ trạng thái CMS và bằng chứng sẵn sàng bán | Tám nhãn hồ sơ trong docs/06 (khớp bảng trả lời COO), mã CMS thật [CHỜ XÁC MINH]. Sổ tay chỉ có trạng thái đơn hàng và sản phẩm | Bắc → Huyền | v0.1.0 | | DRAFT | | | 002:c0009 (đơn hàng) | Không |
| Hợp đồng hợp tác và phụ lục (phí, đối soát, chấm dứt) | Hợp đồng hợp tác mẫu; quy trình ký hợp đồng và phụ lục. Khối thông tin các bên cần bản che | Bắc → Huyền | 11.11.2026 | | DRAFT | | | 001:c0002–c0011; 002:c0003 | Không |
| Chiết khấu Affiliate (phụ lục, cơ sở tính, đối soát, chi hộ) | Phụ lục Affiliate; bảng nhập giá; thư thông báo triển khai (dự kiến 1/7/2026). Có mâu thuẫn CF-01…CF-03 chưa quyết | Bắc → Huyền | 11.11.2026; thư sửa 25/06/2026 | | DRAFT | | | 001:c0012–c0018; 002:c0013 | Không |
| SOP 12 bước, bàn giao, xử lý sự cố | docs/02, docs/07, docs/09 của repo | Bắc → Huyền | v0.1.0 | | DRAFT | | | | Không |

Ngoài phạm vi nhà bán (không đưa vào agent này): ưu đãi “Chủ tịch tặng” dành cho khách hàng (001:c0020), thuộc Marketing.

Mâu thuẫn đang chờ owner: CF-01 (hiệu lực đổi giá/tỷ lệ), CF-02 (mốc đối soát và chi trả Affiliate), CF-03 (cơ sở tính Affiliate), CF-04 (quy trình gỡ/khóa khi vi phạm), CF-05 (số ngày thanh toán sau khi khách nhận hàng). Chi tiết trong kb-workspace.

## C. Ý định thường gặp → nhóm cần mở

Ý định lấy từ bảng trả lời đào tạo của COO. Cột KU tạm chỉ để người duyệt biết nguồn nào sẽ phục vụ; chưa dùng làm căn cứ.

| Ý định | Nhóm cần mở | KU tạm | Khi chưa APPROVED |
|---|---|---|---|
| “Anh/chị muốn mở shop trên Hi1” | Checklist; Mẫu tin | 001:c0001; 002:c0004 | Soạn nháp, ghi “Chưa có căn cứ xác nhận” cho mục cần nguồn |
| “Thiếu giấy tờ gì?”, “Kiểm tra hồ sơ doanh nghiệp/HTX” | Checklist | 001:c0001; 002:c0002 | Chỉ liệt kê theo checklist dự thảo, ghi rõ chưa duyệt; không kết luận đủ/thiếu |
| “Hướng dẫn đưa sản phẩm OCOP lên sàn” | Checklist theo ngành; Ngành hàng cấm/có điều kiện; App | 002:c0002, c0006 | Chưa có nguồn OCOP; chuyển kiểm duyệt ngành hàng |
| Hàng thực phẩm, TPCN, mỹ phẩm, hàng nhập khẩu cần giấy tờ gì | Checklist | 002:c0002 | Nêu danh sách dự thảo, chưa duyệt; chuyển kiểm duyệt ngành hàng |
| Hi1 hợp tác với đối tượng nào (nhà sản xuất, đại lý…) | Chính sách nhà bán | 002:c0001 | Chuyển Trưởng nhóm; không kết luận từ chối nhà bán |
| “Em đăng ký rồi nhưng chưa được duyệt” | Trạng thái CMS; SLA | | Không hứa ngày duyệt; chuyển Trưởng nhóm |
| “Shop đã mở mà không thấy sản phẩm” | Trạng thái CMS; App | 001:c0019; 002:c0006, c0008 | Không đánh dấu sẵn sàng bán; tạo phiếu cho nhân viên đối chiếu |
| “Hỗ trợ đăng 10 sản phẩm đầu tiên” | App; Chính sách nội dung | 002:c0006, c0010 | Hướng dẫn theo bản đã xác minh; claim chỉ khi có chứng cứ |
| Xử lý đơn hàng, trạng thái đơn, đổi trả | Hướng dẫn xử lý đơn | 002:c0007, c0009, c0012 | Hướng dẫn theo nguồn đã duyệt; không hứa hoàn tiền |
| Hỏi về phí, doanh thu, bảo đảm có đơn | Hợp đồng; Affiliate | 001:c0006, c0007; 002:c0001 | Không cam kết doanh thu hay ưu đãi chưa duyệt |
| Cách tính chiết khấu Affiliate | Affiliate | 001:c0012, c0018 | Không kết luận: CF-03 chưa quyết |
| Lịch đối soát, thời gian nhận tiền hàng | Hợp đồng; Hướng dẫn thanh toán | 001:c0007; 002:c0011 | Không kết luận số ngày: CF-05 chưa quyết |
| Đổi giá hoặc tỷ lệ Affiliate có hiệu lực khi nào | Hợp đồng; Affiliate | 001:c0002, c0017 | Không kết luận: CF-01 chưa quyết |
| Bị gỡ sản phẩm hoặc khóa shop | Chính sách nhà bán; Hợp đồng | 002:c0010; 001:c0004 | Không kết luận quy trình: CF-04 chưa quyết; chuyển Trưởng nhóm |
| Chấm dứt hợp tác, tranh chấp | Hợp đồng | 001:c0010, c0011 | Chuyển pháp chế |

## D. Điều kiện để một dòng được nạp Project

Một dòng chỉ chuyển sang APPROVED và được nạp khi đủ: Bắc xác nhận nội dung (owner); Huyền duyệt và ghi phiên bản, ngày hiệu lực; mâu thuẫn liên quan đã được owner quyết; chạy lại các ca đánh giá gắn nhóm đó và đạt cổng cứng. Tài liệu nạp kho dùng chung phải che số CCCD, số tài khoản và chữ ký (Gate 0, xem [phân loại dữ liệu](../docs/04-phan-loai-du-lieu.md)). Điều kiện chạy thử hồ sơ thật: [docs/13](../docs/13-dieu-kien-chay-thu-ho-so-that.md). Vòng đời và trường metadata: [quản trị kho tri thức](../docs/10-quan-tri-kho-tri-thuc.md).

Khi đổi phiên bản nguồn: dừng hướng dẫn cũ, owner kiểm tra hiệu lực trước khi thay. Không nạp mật khẩu, OTP, token hay dữ liệu cá nhân của nhà bán vào kho tri thức dùng chung.
