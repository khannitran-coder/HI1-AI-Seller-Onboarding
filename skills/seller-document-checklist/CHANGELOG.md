# Changelog – seller-document-checklist

Tác giả: PM - TKC

## 0.2.0 – 2026-11-20

- Thay checklist 9 mục bằng biểu mẫu 13 mục KU-000020 theo QĐ-01; tách email liên hệ và email đối soát theo QĐ-04.
- Áp quy tắc tài khoản ngân hàng theo chủ thể tại KU-000029 (QĐ-02), chỉ kiểm cờ có/không; dẫn KU-000021…KU-000026 cho ngành hàng và KU-000028 cho điều kiện chủ thể.
- Chặn tư vấn hóa chất từ KU-000024 `VERIFIED`; ưu tiên KU `APPROVED` toàn văn trong Project knowledge thuộc release active hơn bản tóm tắt trong Skill.
- Giữ hai mục chỉ có ở checklist cũ ở trạng thái **Chờ PM xác nhận**, không đưa vào chấm Đủ/Thiếu. Cập nhật guardrails dữ liệu theo QĐ-05 và mẫu nháp bàn giao.
- Thêm ba ca hành vi SDC-01…SDC-03 trong `tests/test-cases.md`.

Kiểm kỹ thuật: `python tools/build_skills.py --check` đạt (6 Skill); bốn phép so fixture của CI `price-old`, `price-real`, `tracker-errors`, `tracker-clean` đạt expected JSON. Chưa chạy 14 ca hành vi nền và 3 ca SDC trên Project thử nghiệm; không coi các kiểm kỹ thuật là bằng chứng đạt cổng eval.
