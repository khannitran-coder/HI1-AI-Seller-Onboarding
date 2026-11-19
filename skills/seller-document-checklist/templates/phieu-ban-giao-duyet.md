# Nháp phiếu bàn giao duyệt

v0.2.0 – đối chiếu hồ sơ theo QĐ-01/QĐ-02; phiếu vẫn là nháp.

Chuẩn hồ sơ là biểu mẫu 13 mục tại KU-000020 (QĐ-01); mục ngân hàng theo KU-000029 (QĐ-02). Chỉ lập phiếu khi nguồn KU APPROVED, đúng phạm vi/hiệu lực và release KB active. [CHỜ COO DUYỆT – D-05] chuyển đúng người duyệt. Đây là nháp, không phải quyết định duyệt.

| Trường | Nội dung |
|---|---|
| merchant_id | SIM-xxx |
| loại hình/ngành hàng | [loại hình/ngành hàng đã xác nhận] |
| checklist_version | [KU-000020 v1 + mã release KB active; ghi KU-000029 v1 nếu có mục ngân hàng] |
| kết quả đối chiếu (đủ/thiếu/cần xác minh) | [kết quả từng mục] |
| căn cứ | [tài liệu + phiên bản; thiếu ghi Chưa có căn cứ xác nhận] |
| điểm rủi ro | [mô tả rủi ro đã che; không tự đặt thang điểm] |
| mục chờ PM xác nhận | [nếu phát sinh: lưu riêng, không chấm Đủ/Thiếu hoặc dùng làm điều kiện duyệt] |
| nội dung cần người có thẩm quyền quyết định | [câu hỏi cụ thể] |
| người chuyển | [vai trò/mã người được phép] |
| thời điểm | [ISO 8601 có múi giờ] |
| kết quả duyệt/trả về | [điền sau; ghi nguyên văn lý do trong phạm vi dữ liệu được phép] |

Không chép PII/dữ liệu Đỏ từ lý do gốc sang AI/repo; nếu lý do chứa dữ liệu nhạy cảm, dừng và người có quyền xử lý tại hệ thống chính thức. AI không tự điền quyết định. Người kiểm tra và tự chuyển qua kênh chính thức.

Cần người duyệt trước khi gửi/lưu: Có

Nguồn: bảng hỏi COO mục Q10 (phiên bản chưa được cung cấp); BRD HI1-AI-BRD-SD-1.2 mục PDHB-FR-08.
