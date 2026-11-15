# Audit của Claude – PR #1 (v0.1.0)

Ngày audit: 16/11/2026 · Người audit: Claude (theo yêu cầu của Chi) · Đối tượng: nhánh feat/seller-onboarding-package, commit 0b3352e

## Phạm vi
4 Skill, project instructions, docs 01–08, templates, tracker schema, 14 ca test. Audit tĩnh (đọc nội dung, kiểm cấu trúc, frontmatter, dữ liệu nhạy cảm). Chưa chạy Skill trên Claude.

## Phát hiện
| Mã | Mức | Nội dung | Xử lý |
|---|---|---|---|
| F1 | Chặn merge | Skill tham chiếu file ngoài folder, gãy khi upload zip | Đóng gói references/templates vào từng Skill |
| F2 | Chặn merge | description quá ngắn, khó kích hoạt đúng Skill | Viết lại 300–600 ký tự kèm cụm từ người dùng |
| F3 | Chặn merge | Thiếu created_at, first_contact_at để đo KPI và tuổi hồ sơ | Thêm 2 cột, tổng 25 cột |
| F4 | Nên sửa | Mọi nhãn chờ duyệt đều là D-04 | Ánh xạ D-01…D-06 đúng chủ đề |
| F5 | Nhỏ | Dòng trống thừa | Xoá |
| F6 | Ghi nhận | 14 ca chưa chạy; nội dung an toàn lặp ở 4 Skill | Chạy ở tuần 1; giữ đồng bộ qua quy tắc thay đổi |
| F7 | Chặn vận hành | Repo đang public; chứa quy tắc vận hành và cơ chế chống prompt injection nội bộ | Chi chuyển repo sang private trước khi merge |

Điểm tốt: không có dữ liệu thật/PII; guardrails đầy đủ và đúng BRD; xử lý dữ liệu Đỏ, prompt injection, ngoài quyền nhất quán; Skill 04 không bịa tuổi hồ sơ/SLA; test case có tiêu chí đạt rõ.

## Câu hỏi
- Ai là owner duy trì bản references trong Skill khi docs thay đổi? (đề xuất: Chi)
- Tracker dùng Google Sheet nào, ai có quyền ghi? (chờ D-06)

## Kết luận
Chưa merge. Merge sau khi F1–F3 đã sửa, F7 đã xử lý và Claude kiểm lại commit mới.
