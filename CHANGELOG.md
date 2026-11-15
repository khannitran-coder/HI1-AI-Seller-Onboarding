# Lịch sử thay đổi

## v0.1.0 — 2026-11-16

- Người thực hiện: Codex theo yêu cầu của Chi.
- Lý do: đóng gói Phương án A cho nhóm Phát triển & Hỗ trợ Nhà bán Hi1.
- Thay đổi: tài liệu vận hành, bốn Skill v0.1.0, mẫu tin, schema tracker, instructions và 14 ca giả lập.
- Trạng thái: pilot [CHỜ COO DUYỆT – D-01]; chưa có chính sách APPROVED được cung cấp; chưa vận hành thật.
- Kiểm tra tĩnh: xem kết quả xác thực trong PR; không thay thế kiểm thử hành vi trên Claude.
- Chạy lại 14 ca trên Claude: chưa chạy. Claude audit và người kiểm ghi kết quả thực tế; không suy kết quả từ kiểm tra tĩnh.

Khi đổi Skill: ghi ngày, người, tên Skill + version trước/sau, lý do và kết quả chạy lại 14 ca (hoặc ghi chưa chạy).

## Sửa theo audit PR #1 — 2026-11-16

- Người thực hiện: Codex theo kết quả audit Claude do Chi cung cấp; giữ phiên bản gói/nguồn v0.1.0 trong đợt sửa trước merge, chưa phát hành phiên bản mới.
- F1: đóng gói guardrails vào references của cả bốn Skill; thêm schema và phiếu chuyển cấp nội bộ cho daily-operations-report; bổ sung quy tắc đồng bộ.
- F2: description 300–600 ký tự, có cụm từ kích hoạt và trường hợp không dùng.
- F3: thêm created_at và first_contact_at sau source_channel, tổng 25 cột; cập nhật công thức tuổi hồ sơ/phản hồi đầu và TC-09.
- F4–F5: ánh xạ nhãn D-01…D-06 theo chủ đề, Phương án B là định hướng chưa quyết; xoá dòng trống thừa.
- Ghi nguyên kết quả Claude audit vào AUDIT.md; F7 do Chi chuyển repo sang private trước merge, chưa xác nhận hoàn tất.
- Kiểm tra tĩnh: frontmatter, độ dài description, đường dẫn và file trong từng zip Skill, header 25 cột, bản sao đồng bộ, quét dữ liệu nhạy cảm và diff whitespace (kết quả cụ thể trong PR).
- F6: 14 ca chưa chạy trên Claude; kết quả chạy sẽ ghi CHANGELOG ở tuần 1. Không suy kết quả hành vi từ kiểm tra tĩnh. Chưa merge, chờ Claude kiểm lại commit mới.

## v0.1.1 — 2026-11-16

- Người thực hiện: Codex theo kết quả QC/trích nguồn Claude do Chi cung cấp; chưa đọc trực tiếp toàn văn tài liệu nguồn.
- G1–G6: thêm ma trận 10 sự cố, vòng đời kho tri thức, phiếu bàn giao duyệt, skill_version (26 cột), SOP một hồ sơ 8 bước và truy vết 15 FR/12 BR.
- Bốn Skill v0.1.0 → v0.1.1; bổ sung Rủi ro trong Tình trạng nếu có, giữ contract COO; giữ phân loại dữ liệu theo v1.3 (L1/L2).
- Đồng bộ references fail-safe/schema và template đóng gói; không sửa AUDIT.md; không đổi phần KHỚP đã được Claude xác nhận.
- Kiểm tra tĩnh: zip độc lập, frontmatter/description, schema/CSV 26 cột, đủ 15 FR/12 BR, bản sao đồng bộ, quét PII và whitespace (kết quả trong PR).
- Chạy lại 14 ca trên Claude: chưa chạy, ghi kết quả ở tuần 1; bảng truy vết chỉ ra phạm vi chưa được ca hiện có kiểm trực tiếp.
- Chưa có trích WF-A01…A06 hoặc toàn văn PLAN-001/v0.2 trong lần QC này; không tự dựng nội dung hoặc thêm tài liệu quản trị. Giữ điều kiện Sẵn sàng bán tại docs/06.
