# Schema tracker

v0.1.0 – pilot, chưa COO duyệt. [CHỜ COO DUYỆT – D-04]

Schema dưới đây là đề xuất pilot [CHỜ COO DUYỆT – D-04]. Enum ngoài yêu cầu gốc cần Claude/COO kiểm tra; chưa ánh xạ CMS thật [CHỜ XÁC MINH]. Không tự thêm cột để hợp thức hoá dữ liệu thiếu. Ô trống nghĩa chưa biết/chưa áp dụng, không đồng nghĩa đạt; giữ merchant_id bắt buộc.

| Cột (đúng thứ tự) | Kiểu | Giá trị cho phép / quy tắc |
|---|---|---|
| merchant_id | chuỗi | Mã hồ sơ không PII; ví dụ SIM-001; bắt buộc |
| source_channel | chuỗi | Tên kênh trong danh mục đã duyệt; chưa có danh mục thì để trống |
| seller_type | enum | doanh nghiệp / hộ kinh doanh / HTX; cá nhân tự do chờ QĐ-07, không tự nhận |
| product_category | chuỗi | Danh mục ngành hàng APPROVED; chưa có thì chờ xác minh |
| owner_role | chuỗi | Vai trò/mã nội bộ được phân công, không tên người/SĐT |
| status | enum | Đúng 8 nhãn trong 06-trang-thai.md |
| status_updated_at | thời gian | ISO 8601 có múi giờ; người ghi khi đổi trạng thái |
| shop_status | enum | chưa xác minh / đã gửi đăng ký / được kích hoạt / tạm dừng |
| product_status | enum | chưa xác minh / chưa có / chờ duyệt / hiển thị / không hiển thị |
| ready_status | enum | chưa xác minh / chưa sẵn sàng / chờ Trưởng nhóm xác nhận / sẵn sàng bán |
| missing_items | danh sách chuỗi | Tên mục thiếu, không nội dung giấy tờ; phân cách bằng dấu chấm phẩy |
| checklist_version | chuỗi | Phiên bản chính xác của checklist được dùng; không có thì để trống, chờ nguồn |
| contact_status | enum | chưa liên hệ / đã liên hệ / chờ phản hồi / cần nhắc |
| last_action | chuỗi | Hành động gần nhất + thời điểm có múi giờ; không PII |
| next_action | chuỗi | Hành động tiếp theo, không PII |
| next_due_at | thời gian | ISO 8601 có múi giờ; chỉ hạn đã xác nhận, thiếu thì để trống |
| approval_evidence | chuỗi | Tham chiếu CMS/bằng chứng từ người có quyền, thời điểm; không chép nội dung nhạy cảm |
| risk_flags | danh sách chuỗi | nghi trùng / mâu thuẫn / thiếu nguồn / lỗi hệ thống / chờ kiểm tra ngành hàng / sự cố dữ liệu / khác đã che |
| escalation_to | enum | cấp 1 / cấp 2-kiểm duyệt nhà bán / cấp 2-ngành hàng-pháp chế / cấp 2-kỹ thuật / cấp 2-CSKH-vận chuyển-thanh toán / cấp 3-COO |
| ai_used | boolean | true / false |
| reviewer | chuỗi | Vai trò/mã người duyệt được phép, không PII |
| review_result | enum | duyệt nguyên / sửa nhỏ / sửa lớn / bỏ; trống nếu chưa duyệt |
| handling_minutes | số | Số phút xử lý thực tế ≥0; không cộng thời gian chờ; trống nếu chưa đo |

Mọi cột cấm dữ liệu Đỏ. Trường tự do phải che PII, không ghi tên người/SĐT hoặc URL có token. AI chỉ đọc; nhân viên chịu trách nhiệm ghi sau duyệt. Đồng bộ Sheet–CMS chưa được thiết lập trong repo.

Schema hiện chưa có created_at, lịch sử phân công/liên hệ và lịch làm việc: không đủ để tự tính tuổi hồ sơ hoặc SLA theo giờ làm việc. Không lấy status_updated_at thay thời điểm tạo; không suy tuổi từ merchant_id. Báo cáo phải ghi “Chưa có căn cứ xác nhận” nếu không có nhật ký được cấp quyền. handling_minutes do người ghi nhận thời gian thao tác, không lấy chênh lệch thời điểm bao gồm chờ.
