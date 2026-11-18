# Góp ý từ phiếu chốt input kiến trúc và cài đặt

Tác giả: PM - TKC  
Trạng thái: **bản tổng hợp để review, chưa phải quyết định đã duyệt**  
Nguồn: Google Doc “Phiếu chốt input kiến trúc và cài đặt”, đọc ngày 18/11/2026. Các ô “Trả lời” ở Phần A và “Đúng thực tế?” ở Phần C vẫn là `[Trả lời]`; phần xác nhận cuối phiếu chưa điền.

## Ý kiến đã ghi trong phiếu, cần người có quyền chốt

| Mã | Ý kiến trong phiếu | Ảnh hưởng và việc cần xác nhận |
|---|---|---|
| D-02 | Đề nghị bỏ giới hạn dữ liệu Đỏ vì dùng Claude doanh nghiệp và có cam kết bảo mật. | COO và người phụ trách dữ liệu phải xác nhận phạm vi, điều khoản xử lý và loại dữ liệu cụ thể. **Chưa đổi** quy tắc Đỏ tại docs/04, Project instructions hoặc các Skill. Hợp đồng bảo mật chưa tự chứng minh được quyền đưa CCCD, số tài khoản, OTP hay mật khẩu vào AI. |
| D-04, D-08 | Đề nghị sau khi mở shop gửi link tài khoản cùng tên đăng nhập và mật khẩu. | Mâu thuẫn với đề xuất D-08 và guardrail hiện hành. Cần COO/Trưởng nhóm chốt kênh bàn giao an toàn; chưa đưa mật khẩu vào mẫu G, AI hoặc repo. |
| D-08b | Phụ lục giá bán của hợp đồng giấy cần tự điều chỉnh bố cục khi in khổ A4. | Cần mẫu B11 đã duyệt, xác nhận sheet/vùng in và tiêu chí trang in với pháp chế. Chưa bật bản nháp `seller-contract-draft` hoặc sửa workbook thật. |
| B1 / bảng giá | Cần kiểm giá trên các sàn khác. | Cần xác định sàn, sản phẩm tương đương, nguồn giá, thời điểm lấy, cách xử lý khuyến mại và người duyệt quy tắc. Chưa coi giá sàn khác là ngưỡng tự động; B1 vẫn “Chưa gửi”. |
| B3 / ngoại lệ sản phẩm | Nêu dược phẩm, mỹ phẩm và các giấy tờ về chất lượng, tự công bố/công bố, lưu hành, nhà máy sản xuất khi áp dụng. | Cần danh mục ngành–loại giấy tờ–điều kiện áp dụng và nguồn chính sách APPROVED. B3 ghi “Chưa gửi (chưa có)”; chưa bổ sung điều kiện pháp lý vào checklist/Skill. |
| C3 | Địa chỉ lấy hàng cần xác nhận lại vị trí GPS, số lượng kho và số điện thoại tương ứng từng kho với nhà bán. | Đưa thành điểm cần xác minh của người phụ trách trước khi Trưởng nhóm xác nhận Sẵn sàng bán. Số điện thoại dùng placeholder trong AI; chưa thêm cột tracker hay coi GPS đã được kiểm chứng tự động. |

## Thông tin cài đặt và tài liệu được điền thêm

| Mã | Nội dung đã ghi | Trạng thái áp dụng |
|---|---|---|
| B4 | Có link ảnh giao diện App Nhà Bán/admin trong phiếu; trạng thái vẫn “Chưa gửi”. | Cần người phụ trách xác minh quyền truy cập, phiên bản và việc che dữ liệu trước khi dùng làm hướng dẫn. |
| B9 | Người cung cấp ghi “Hạnh”; câu hỏi đáp vẫn “Chưa gửi”. | Chưa nạp vào kho tri thức. |
| B10 | Ghi “N/A” cho số liệu nền. | Chưa có số liệu để so sánh trước/sau pilot; không suy kết quả KPI. |
| B11 | Có link thư mục mẫu hợp đồng/phụ lục; trạng thái vẫn “Chưa gửi”. | Cần xác minh bản APPROVED và quyền sử dụng trước D-08b. |
| E6 | Người nhận báo cáo 17:00 ghi “Chi, Huyền, Bắc”; COO nhận tổng hợp tuần. | Chưa tạo tác vụ/gửi báo cáo; cần xác nhận danh tính, kênh và D-03 trước cấu hình. |
| E8 | Lịch đào tạo ghi 21–24/11, 60 phút, toàn nhóm. | Ghi như giá trị trong phiếu; chưa đặt lịch hoặc xác nhận giờ/người tham dự. |

Các mục D-01, D-03, D-05, D-06, D-07a, D-07b, D-09 và C1–C9 chưa có lựa chọn “Đồng ý/Sửa/Chưa chốt” hoàn tất. Không coi các đề xuất soạn sẵn trong phiếu là quyết định chốt. Việc mở quyền AI, thay đổi phân lớp dữ liệu, SLA, chính sách hợp đồng và lịch báo cáo vẫn theo các gate hiện có trong repo.
