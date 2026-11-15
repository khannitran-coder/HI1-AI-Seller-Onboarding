# Lịch sử thay đổi

## v0.1.0 — 2026-11-16

- Người thực hiện: PM - TKC.
- Lý do: đóng gói Phương án A cho nhóm Phát triển & Hỗ trợ Nhà bán Hi1.
- Thay đổi: tài liệu vận hành, bốn Skill v0.1.0, mẫu tin, schema tracker, instructions và 14 ca giả lập.
- Trạng thái: pilot [CHỜ COO DUYỆT – D-01]; chưa có chính sách APPROVED được cung cấp; chưa vận hành thật.
- Kiểm tra tĩnh: xem kết quả xác thực trong PR; không thay thế kiểm thử hành vi trên Claude Project.
- Chạy lại 14 ca trên Claude Project: chưa chạy. Người kiểm định kiểm tra và người kiểm ghi kết quả thực tế; không suy kết quả từ kiểm tra tĩnh.

Khi đổi Skill: ghi ngày, người, tên Skill + version trước/sau, lý do và kết quả chạy lại 14 ca (hoặc ghi chưa chạy).

## Sửa theo audit PR #1 — 2026-11-16

- Người thực hiện: PM - TKC.
- F1: đóng gói guardrails vào references của cả bốn Skill; thêm schema và phiếu chuyển cấp nội bộ cho daily-operations-report; bổ sung quy tắc đồng bộ.
- F2: description 300–600 ký tự, có cụm từ kích hoạt và trường hợp không dùng.
- F3: thêm created_at và first_contact_at sau source_channel, tổng 25 cột; cập nhật công thức tuổi hồ sơ/phản hồi đầu và TC-09.
- F4–F5: ánh xạ nhãn D-01…D-06 theo chủ đề, Phương án B là định hướng chưa quyết; xoá dòng trống thừa.
- Ghi nguyên kết quả kiểm định vào AUDIT.md; F7 do PM chuyển repo sang private trước merge, chưa xác nhận hoàn tất.
- Kiểm tra tĩnh: frontmatter, độ dài description, đường dẫn và file trong từng zip Skill, header 25 cột, bản sao đồng bộ, quét dữ liệu nhạy cảm và diff whitespace (kết quả cụ thể trong PR).
- F6: 14 ca chưa chạy trên Claude Project; kết quả chạy sẽ ghi CHANGELOG ở tuần 1. Không suy kết quả hành vi từ kiểm tra tĩnh. Chưa merge, chờ người kiểm định kiểm tra lại commit mới.

## v0.1.1 — 2026-11-16

- Người thực hiện: PM - TKC.
- G1–G6: thêm ma trận 10 sự cố, vòng đời kho tri thức, phiếu bàn giao duyệt, skill_version (26 cột), SOP một hồ sơ 8 bước và truy vết 15 FR/12 BR.
- Bốn Skill v0.1.0 → v0.1.1; bổ sung Rủi ro trong Tình trạng nếu có, giữ contract COO; giữ phân loại dữ liệu theo v1.3 (L1/L2).
- Đồng bộ references fail-safe/schema và template đóng gói; không sửa AUDIT.md; không đổi phần KHỚP đã được xác nhận qua kiểm định.
- Kiểm tra tĩnh: zip độc lập, frontmatter/description, schema/CSV 26 cột, đủ 15 FR/12 BR, bản sao đồng bộ, quét PII và whitespace (kết quả trong PR).
- Chạy lại 14 ca trên Claude Project: chưa chạy, ghi kết quả ở tuần 1; bảng truy vết chỉ ra phạm vi chưa được ca hiện có kiểm trực tiếp.
- Chưa có trích WF-A01…A06 hoặc toàn văn PLAN-001/v0.2 trong lần QC này; không tự dựng nội dung hoặc thêm tài liệu quản trị. Giữ điều kiện Sẵn sàng bán tại docs/06.

## v0.1.2 — 2026-11-16

- Người thực hiện: PM - TKC.
- seller-document-checklist, seller-communication, first-product-assistant: v0.1.1 → v0.1.2. Checklist 9 mục và điều kiện chủ thể; mẫu E–I, không chứa thông tin đăng nhập; khung SEO và chuẩn bị ảnh/khối lượng.
- Thêm 2 sự cố trong docs/09 và đồng bộ 4 bản references/guardrails.md; ghi backlog v0.2 trong docs/11.
- daily-operations-report giữ version 0.1.1 vì quy trình không đổi; reference an toàn được đồng bộ theo F1.
- README giữ nguyên phần giới thiệu PM và hướng dẫn cũ; chèn nguyên văn kiến trúc v0.1.2 (chỉ chuẩn hoá Markdown).
- Kiểm tra tĩnh: zip Skill tự chứa, YAML/description, schema 26 cột, quét chuỗi cấm/PII và whitespace; xem kết quả trong PR.
- Chạy lại 14 ca trên Claude Project: chưa chạy, chờ người kiểm định thực hiện; không tuyên bố đạt kiểm thử hành vi.
- Chưa COO duyệt D-04/D-07/D-08; không triển khai quyền ghi CMS hoặc gửi tin bằng AI. Không merge, chờ người kiểm định kiểm tra.

### Sửa F8 theo kiểm định — 2026-11-16

- Người thực hiện: PM - TKC.
- Tách phần “Tin gửi nhà bán” và “Ghi chú cho nhân viên (không gửi)” ở đủ chín mẫu A–I; metadata, nhãn duyệt và ghi chú nội bộ nằm sau phân cách.
- Kiểm tra tĩnh và quét chuỗi bí mật lại trước merge; 14 ca hành vi trên Claude Project vẫn chưa chạy. Giữ phiên bản đợt sửa trước merge v0.1.2.

## v0.1.3 — 2026-11-16

- Người thực hiện: PM - TKC.
- Thêm ma trận tự chủ M0–M5, A01–A08, điều kiện nâng/hạ, nút dừng, nhật ký và rủi ro R01–R09: ĐỀ XUẤT, chưa có hiệu lực.
- README làm rõ giới hạn theo thiết kế, mức theo hành động và lộ trình D-07a/D-07b; docs/03 trỏ đề xuất; docs/11 truy vết hành động/quyết định.
- Không đổi hành vi hoặc version bốn Skill; không bật connector/quyền, không đổi schema tracker 26 cột. Không triển khai cơ chế nhật ký hoặc hậu kiểm trong lần này.
- Kiểm tra tĩnh: mã hành động/quyết định, liên kết, quét chuỗi bí mật và diff whitespace; không cần chạy lại 14 ca hành vi vì chỉ sửa tài liệu, không sửa Skill.
- Chưa merge; chờ người kiểm định kiểm tra. Lộ trình từ M0 được làm rõ trong cập nhật dưới đây; đánh giá rủi ro và người theo dõi là đề xuất.

### Chuẩn hoá tài liệu và lộ trình — 2026-11-16

- Người thực hiện: PM - TKC.
- Cho phép công khai ma trận; R09 chỉ mô tả tổng quát quy trình cấp/bàn giao thông tin đăng nhập theo D-08.
- M0 chỉ vào M3 sau COO duyệt; ≥30 lượt tại M3 trước nâng lên M3+/M4; giữ trần A04/A05 và cấm A07/A08.
- Thêm mẫu nhật ký AI 9 cột ở tab riêng, bắt buộc trước M3+/M4; tracker chính vẫn 26 cột. Chưa bật quyền hoặc connector.
- Chuẩn hoá tác giả và vai trò PM trong nội dung tệp, đồng bộ references; không đổi hành vi hoặc version bốn Skill, không sửa lịch sử commit.
- Kiểm tra: quét dấu vết tác giả/công cụ soạn và chuỗi bí mật; kiểm gói Skill, schema và liên kết. 14 ca hành vi chưa chạy.
