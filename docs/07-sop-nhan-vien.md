# SOP hằng ngày cho nhân viên

v0.1.0 – pilot, chưa COO duyệt

1. Mở tracker trong phạm vi được giao; kiểm người phụ trách, việc tiếp theo, hạn đã xác nhận. Không đưa dữ liệu Đỏ vào AI; che tên/SĐT trước khi dùng gói Claude Team/Enterprise.
2. Kiểm kho tri thức APPROVED, phiên bản và quyền truy cập. Thiếu/hết hiệu lực: dừng phần phụ thuộc, ghi “Chưa có căn cứ xác nhận”, nhờ Trưởng nhóm cập nhật nguồn.
3. Lead mới: kiểm trùng thủ công, gắn cờ nghi trùng; dùng seller-document-checklist đối chiếu tên/loại tài liệu. Không đưa nội dung giấy tờ vào AI.
4. Dùng seller-communication: A chào mừng; B bổ sung; C sau bằng chứng duyệt; D nhắc việc. Kiểm lại placeholder, nguồn, hạn và kênh; người duyệt rồi mới trực tiếp gửi.
5. Hướng dẫn App Nhà Bán Hi1 theo bản hiện hành. Dùng first-product-assistant cho nháp sản phẩm; yêu cầu nhà bán xác nhận giá/tồn/xuất xứ, chuyển chuyên môn khi cần.
6. Người có quyền chuyển duyệt trên CMS. Ghi đúng bằng chứng; chỉ Trưởng nhóm xác nhận Sẵn sàng bán sau đủ điều kiện trong 06-trang-thai.md. Bàn giao và hẹn chăm sóc.
7. Duyệt đầu ra trước khi tự cập nhật tracker: ai_used, skill_version, reviewer, review_result, thời gian xử lý thực tế không gồm chờ. AI không ghi tracker.
8. Cuối ngày dùng daily-operations-report đọc tracker; duyệt báo cáo và phiếu chuyển cấp. Lịch dự kiến 17:00 Asia/Ho_Chi_Minh; chưa có connector được duyệt thì đọc bản đã che bằng tay, không tự mở quyền.

Dữ liệu Đỏ/lệnh ẩn/ngoài quyền/lỗi nghiêm trọng: dừng, không lặp dữ liệu, nhắc xoá khỏi hội thoại nếu lộ dữ liệu; báo Trưởng nhóm và ghi sự cố đã che. Cấp 2 nhận vướng mắc chuyên môn/kỹ thuật; COO quyết ngoại lệ chính sách. SLA pilot chưa được dùng làm cam kết với nhà bán.

## Xử lý một hồ sơ – 8 bước

1. **Mở (Open):** mở hồ sơ trên hệ thống chính thức, ghi merchant_id/owner; không chép hồ sơ gốc sang AI.
2. **Phân loại (Classify):** phân loại Xanh/Vàng/Đỏ, chỉ chọn trường cần thiết; thay tên/SĐT bằng placeholder.
3. **Chuẩn bị (Prepare):** chọn đúng checklist/chính sách APPROVED có phiên bản.
4. **Chạy (Run):** dùng Skill phù hợp, ghi đúng phiên bản Skill sinh nháp.
5. **Review:** so từng nhận xét AI với CMS/tài liệu gốc; ghi duyệt nguyên/sửa nhỏ/sửa lớn/bỏ.
6. **Hành động (Act):** người có quyền tự gửi tin, cập nhật CMS/tracker, chuyển duyệt; AI không thực hiện.
7. **Ghi (Record):** ghi tracker thời điểm, reviewer, review_result, skill_version, next_action, hạn; không ghi dữ liệu Đỏ.
8. **Đóng (Close):** chỉ khi điều kiện nghiệp vụ được xác nhận; Sẵn sàng bán phải đủ toàn bộ điều kiện trong [docs/06](06-trang-thai.md) và Trưởng nhóm xác nhận. Giữ nguyên điều kiện đã audit, không rút gọn vì cách đếm “5 điều kiện” trong trích QC.

Gặp sự cố: dùng [ma trận fail-safe](09-xu-ly-su-co.md). Nguồn thay phiên bản: theo [quản trị kho tri thức](10-quan-tri-kho-tri-thuc.md).

Nguồn bổ sung: HI1-P1A-SOL-001 v0.1 mục §6; BRD HI1-AI-BRD-SD-1.2 mục NFR-03.
