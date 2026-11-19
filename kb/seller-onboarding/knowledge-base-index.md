# Knowledge base index – Seller Onboarding

Tác giả: PM - TKC · Release đề xuất REL-SEL-20261120-01 · Chưa active.

## A. Giao thức truy xuất

Bảng định tuyến chỉ để tìm KU. Không dùng route_summary làm căn cứ trả lời. Mở toàn văn KU và KU quan hệ; kiểm audience, scope, ngày hiệu lực và nguồn trước khi trả lời. Chỉ dùng KU APPROVED **đã xác nhận hiệu lực**. Hiện nhiều ngày hiệu lực chưa xác nhận, vì vậy release này chưa được dùng tư vấn thật. CASE/LESSON chỉ tham khảo nội bộ; KU VERIFIED không dùng tư vấn. Thiếu căn cứ: “Chưa có căn cứ xác nhận” và chuyển owner. Trích ku_id khi nêu quy tắc. Căn cứ pháp lý chưa được pháp chế xác nhận không trích cho nhà bán.

## B. Domain và owner

| Domain | Owner đề xuất trong sổ KU | Phạm vi |
|---|---|---|
| SEL | Trưởng nhóm Phát triển nhà bán | Quy trình, trạng thái, điều kiện chủ thể, biểu mẫu chung |
| SEL | Kiểm duyệt ngành hàng/pháp chế | Chứng từ theo ngành; căn cứ pháp lý chờ kiểm |
| SEL | Phụ trách Affiliate | Phí sàn, chương trình Affiliate |

## C. Ý định → KU

| Ý định từ candidate | KU | Điều kiện dùng |
|---|---|---|
| Agent onboarding được làm những gì? | KU-000001 | Chỉ khi hiệu lực/scope đã xác nhận |
| Em đăng ký rồi nhưng chưa được duyệt | KU-000002 | Chỉ khi hiệu lực/scope đã xác nhận |
| Shop đã mở mà không thấy sản phẩm | KU-000002 | Chỉ khi hiệu lực/scope đã xác nhận |
| Hồ sơ của tôi đang ở trạng thái nào? | KU-000003 | Chỉ khi hiệu lực/scope đã xác nhận |
| Shop của tôi đã bán được chưa? | KU-000004 | Chỉ khi hiệu lực/scope đã xác nhận |
| Anh/chị muốn mở shop trên Hi1 | KU-000005 | Chỉ khi hiệu lực/scope đã xác nhận |
| Thiếu giấy tờ gì? | KU-000006 | Chỉ khi hiệu lực/scope đã xác nhận |
| Hướng dẫn em đưa sản phẩm OCOP lên sàn | KU-000007 | Chỉ khi hiệu lực/scope đã xác nhận |
| Hỗ trợ đăng 10 sản phẩm đầu tiên được không? | KU-000007 | Chỉ khi hiệu lực/scope đã xác nhận |
| Bao lâu thì có người liên hệ? | KU-000009 | Chỉ khi hiệu lực/scope đã xác nhận |
| Ai duyệt hồ sơ của tôi? | KU-000011 | Chỉ khi hiệu lực/scope đã xác nhận |
| Em không nhận được OTP | KU-000014 | Chỉ khi hiệu lực/scope đã xác nhận |
| Shop đã mở mà không thấy sản phẩm | KU-000015 | Chỉ khi hiệu lực/scope đã xác nhận |
| Bán trên Hi1 mất phí gì? | KU-000016 | Chỉ khi hiệu lực/scope đã xác nhận |
| Khi nào duyệt chắc? | KU-000016 | Chỉ khi hiệu lực/scope đã xác nhận |
| Bán trên Hi1 mất phí gì? | KU-000019 | Chỉ khi hiệu lực/scope đã xác nhận |
| Affiliate là gì, tôi phải trả bao nhiêu? | KU-000019 | Chỉ khi hiệu lực/scope đã xác nhận |
| Lên sàn cần cung cấp thông tin gì? | KU-000020 | Chỉ khi hiệu lực/scope đã xác nhận |
| Bán vật liệu xây dựng cần giấy tờ gì? | KU-000021 | Chỉ khi hiệu lực/scope đã xác nhận |
| Bán thực phẩm & đồ uống cần giấy tờ gì? | KU-000022 | Chỉ khi hiệu lực/scope đã xác nhận |
| Bán mỹ phẩm, dược phẩm cần giấy tờ gì? | KU-000023 | Chỉ khi hiệu lực/scope đã xác nhận |
| Bán điện – điện tử, điện gia dụng, cơ khí cần giấy tờ gì? | KU-000025 | Chỉ khi hiệu lực/scope đã xác nhận |
| Bán hàng tiêu dùng khác (dệt may, đồ gỗ, nhựa, …) cần giấy tờ gì? | KU-000026 | Chỉ khi hiệu lực/scope đã xác nhận |
| Cá nhân có mở shop được không? | KU-000028 | Chỉ khi hiệu lực/scope đã xác nhận |
| Hộ kinh doanh có lên sàn được không? | KU-000028 | Chỉ khi hiệu lực/scope đã xác nhận |
| Hộ kinh doanh dùng tài khoản ngân hàng nào? | KU-000029 | Chỉ khi hiệu lực/scope đã xác nhận |
| Doanh nghiệp dùng tài khoản ngân hàng nào? | KU-000029 | Chỉ khi hiệu lực/scope đã xác nhận |

## D. Danh mục KU APPROVED

est_tokens là ước lượng ký tự/3 của thân KU, chỉ để tính dung lượng, không dùng làm hạn mức chính xác.

| ku_id | Title | route_summary | Authority | Audience | Hiệu lực | est_tokens |
|---|---|---|---|---|---|---:|
| KU-000001 | Phạm vi nghiệp vụ onboarding nhà bán và giới hạn của tài liệu đào tạo | Phạm vi onboarding nhà bán; SLA/menu/chứng từ trong tài liệu đào tạo chỉ là đề xuất. | RULE | staff | Chưa xác nhận | 230 |
| KU-000002 | Phân biệt Đã gửi đăng ký – Gian hàng được kích hoạt – Sẵn sàng bán | Ba mốc khác nhau: đã gửi đăng ký ≠ được kích hoạt ≠ sẵn sàng bán. | RULE | staff, seller | Chưa xác nhận | 82 |
| KU-000003 | 8 trạng thái công việc hồ sơ nhà bán và điều kiện vào | Tám nhãn trạng thái hồ sơ nhà bán, điều kiện vào và việc tiếp theo. | RULE | staff, seller | Chưa xác nhận | 306 |
| KU-000004 | Điều kiện để đánh dấu SẴN SÀNG BÁN | Checklist điều kiện sẵn sàng bán; thiếu một điểm là chưa đạt. | RULE | staff, seller | Chưa xác nhận | 176 |
| KU-000005 | Quy trình bước 1–3: nhận lead, kiểm trùng, phân loại nhà bán | Tiếp nhận lead, kiểm trùng, phân loại loại hình và ngành hàng. | RULE | staff | Chưa xác nhận | 192 |
| KU-000006 | Quy trình bước 4–5: đối chiếu checklist hồ sơ và yêu cầu bổ sung | Đối chiếu checklist hồ sơ, soạn yêu cầu bổ sung để nhân viên duyệt gửi. | RULE | staff | Chưa xác nhận | 159 |
| KU-000007 | Quy trình bước 6–7: hướng dẫn gian hàng trên App Nhà Bán Hi1 và chuẩn hóa sản phẩm đầu tiên | Hướng dẫn gian hàng trên app và chuẩn hóa sản phẩm đầu tiên; không nhận OTP. | RULE | staff | Chưa xác nhận | 161 |
| KU-000008 | Quy trình bước 8–11: chuyển duyệt, vận hành đơn, kiểm tra sẵn sàng bán, bàn giao | Chuyển duyệt, hướng dẫn vận hành đơn, kiểm sẵn sàng bán, bàn giao. | RULE | staff | Chưa xác nhận | 205 |
| KU-000009 | SLA thí điểm (đề xuất, chưa áp dụng) | SLA thí điểm đề xuất 2h/4h/1 ngày/2 ngày – chưa xác nhận. | RULE | staff | Chưa xác nhận | 110 |
| KU-000010 | Ba cấp chuyển cấp khi vướng hoặc quá hạn và phiếu chuyển cấp tối thiểu | Ba cấp chuyển cấp và phiếu chuyển cấp tối thiểu. | RULE | staff | Chưa xác nhận | 175 |
| KU-000011 | Thẩm quyền duyệt: hồ sơ nhà bán, nội dung sản phẩm, checklist và ngoại lệ | Ai duyệt hồ sơ, sản phẩm, checklist và ngoại lệ. | RULE | staff | Chưa xác nhận | 138 |
| KU-000013 | Xử lý hồ sơ thiếu hoặc giấy tờ không khớp | Giấy tờ thiếu/không khớp: lập sai khác, yêu cầu làm rõ, không kết luận giả. | RULE | staff | Chưa xác nhận | 85 |
| KU-000014 | Nhà bán chưa biết dùng app; trùng tài khoản hoặc không nhận OTP | Hướng dẫn app theo ảnh đã xác thực; trùng tài khoản/OTP chuyển kỹ thuật. | RULE | staff | Chưa xác nhận | 114 |
| KU-000015 | Shop đã duyệt nhưng sản phẩm chưa hiển thị | Shop duyệt mà sản phẩm chưa hiển thị: kiểm từng lớp, lập phiếu. | RULE | staff | Chưa xác nhận | 68 |
| KU-000016 | Nhà bán hỏi phí, doanh thu, bảo đảm bán được hàng | Hỏi phí/doanh thu/cam kết: chỉ trích chính sách hiệu lực, không hứa. | RULE | staff, seller | Chưa xác nhận | 60 |
| KU-000017 | Nhà bán yêu cầu đăng hàng có điều kiện/khó xác minh | Hàng có điều kiện: gắn chờ kiểm tra ngành hàng, chuyển pháp chế. | RULE | staff | Chưa xác nhận | 52 |
| KU-000018 | Dữ liệu nhạy cảm trong onboarding và quy tắc tối thiểu hóa | Dữ liệu nhạy cảm và quy tắc tối thiểu hóa trong onboarding. | RULE | staff, agent_config | Chưa xác nhận | 206 |
| KU-000019 | Chính sách phí sàn và chương trình Affiliate cho nhà bán | Không thu phí nhà bán; Affiliate: nhà bán tự đặt % chiết khấu, chỉ trả khi có đơn đủ điều kiện. | RULE | staff, seller | Chưa xác nhận | 218 |
| KU-000020 | Biểu mẫu thông tin đối tác cần cung cấp khi lên sàn (13 mục) | Biểu mẫu 13 mục thông tin đối tác gửi khi lên sàn. | RULE | staff, seller | Chưa xác nhận | 306 |
| KU-000021 | Chứng nhận/hồ sơ sản phẩm bắt buộc – ngành Vật liệu xây dựng | Danh sách chứng từ ngành hàng; căn cứ pháp lý chờ pháp chế xác nhận. | RULE | staff, seller | Chưa xác nhận | 184 |
| KU-000022 | Chứng nhận/hồ sơ sản phẩm bắt buộc – ngành Thực phẩm & đồ uống | Bộ chứng từ thực phẩm; sản phẩm OCOP cần thêm chứng nhận OCOP. | RULE | staff, seller | Chưa xác nhận | 198 |
| KU-000023 | Chứng nhận/hồ sơ sản phẩm bắt buộc – ngành Mỹ phẩm, dược phẩm | Danh sách chứng từ ngành hàng; căn cứ pháp lý chờ pháp chế xác nhận. | RULE | staff, seller | Chưa xác nhận | 164 |
| KU-000025 | Chứng nhận/hồ sơ sản phẩm bắt buộc – ngành Điện – điện tử, điện gia dụng, cơ khí | Danh sách chứng từ ngành hàng; căn cứ pháp lý chờ pháp chế xác nhận. | RULE | staff, seller | Chưa xác nhận | 134 |
| KU-000026 | Chứng nhận/hồ sơ sản phẩm bắt buộc – ngành Hàng tiêu dùng khác (dệt may, đồ gỗ, nhựa, …) | Danh sách chứng từ ngành hàng; căn cứ pháp lý chờ pháp chế xác nhận. | RULE | staff, seller | Chưa xác nhận | 132 |
| KU-000027 | Biểu mẫu danh mục sản phẩm đối tác cung cấp | Các trường danh mục sản phẩm đối tác gửi: mã, ảnh 500x500, giá+VAT, % chiết khấu, HDSD. | RULE | staff, seller | Chưa xác nhận | 92 |
| KU-000028 | Điều kiện chủ thể được nhận hồ sơ nhà bán | Chủ thể được nhận: DN/HTX/HKD có MST, xuất được hóa đơn; cá nhân tự do chuyển Trưởng nhóm. | RULE | staff, seller | Chưa xác nhận | 53 |
| KU-000029 | Tài khoản ngân hàng theo loại chủ thể | DN/HTX dùng tài khoản pháp nhân; HKD dùng tài khoản chủ hộ trên ĐKKD; chỉ kiểm có/không. | RULE | staff, seller | Chưa xác nhận | 102 |

## KU VERIFIED – chưa dùng tư vấn

- KU-000024: Chứng nhận/hồ sơ sản phẩm bắt buộc – ngành Hóa chất & nguyên liệu công nghiệp — căn cứ hóa chất cũ, chờ pháp chế.

## Audience agent_config – đưa vào Project instructions sau khi rà soát

- KU-000012: Những việc AI không được tự làm trong onboarding nhà bán (audience: agent_config).
- KU-000018: Dữ liệu nhạy cảm trong onboarding và quy tắc tối thiểu hóa (audience: staff, agent_config).

Checklist 9 mục c0028 đã REJECTED theo QĐ-01; không định tuyến tới nguồn cũ.
