# HI1 KU Contract 1.1 — hợp đồng giữa skill `hi1-knowledge-curator` và backend

Tác giả: PM - TKC · Áp dụng cho kiến trúc Data Pipeline Tri thức v1.0.

Hợp đồng này dùng chung cho cả hai cách chạy:
- **no-code**: Claude xuất Markdown/YAML để người duyệt, ID chính thức do sổ KU (Google Sheet) cấp.
- **backend**: Claude xuất `batch-manifest.json` + `candidates.jsonl`; backend kiểm tra, cấp ID, lưu trạng thái.

Sửa hợp đồng → tăng `contract_version`, cập nhật skill cùng lúc.

## Thay đổi 1.0 → 1.1 (sau pilot B-TEST-20261120-01)
- `source_ref` → `source_refs[]` (≥1, phần tử đầu là nguồn chính); mỗi ref có `doc_version` và `approval_state` (APPROVED / PENDING / UNKNOWN) lấy từ sổ nguồn hoặc nhãn trong tài liệu. `authority_type` giữ nghĩa *loại tri thức*; RULE từ nguồn chưa APPROVED hợp lệ ở candidate nhưng **không được duyệt APPROVED** trước khi nguồn APPROVED.
- Thêm `audience_proposed` (staff / seller / agent_config). agent_config = guardrail/cấu hình agent, không xuất vào kho tư vấn.
- `body.evidence_docs` → `body.required_docs` (chứng từ nhà bán phải nộp).
- Flags thêm `gate0_unverified`, `scope_unconfirmed`.
- Facet khi nguồn im lặng = `null` + `scope_unconfirmed`; `"ALL"` chỉ khi nguồn nói rõ áp dụng chung.
- `owner_proposed` chỉ khi nguồn/sổ RACI nêu owner tri thức; người thực hiện một bước không phải owner.
- Locator: .md `L20-L30 §tiêu đề`; Excel `Sheet!A1:D9`; docx/pdf `Mục/Câu + tiêu đề + đoạn`.

## 1. Ai được điền gì

| Nhóm trường | LLM (candidate) | Backend / người duyệt (canonical) |
|---|---|---|
| batch_id, revision | Nhận từ sổ/backend, không tự tạo | Cấp |
| client_record_id | Tạo (c0001…) | — |
| ku_id (`KU-000123`, không mã hóa domain/authority) | **Không** | Cấp khi chấp nhận candidate |
| ku_version | **Không** | Tăng khi người duyệt giữ ID qua revision |
| title, body, layer, scope, route_summary, keywords, intents | Đề xuất | Xác nhận/sửa |
| authority_type, effective_window, supersedes, owner, sensitivity | Chỉ dạng `*_proposed` | Xác nhận |
| status (DRAFT/VERIFIED/APPROVED) | **Không** | Quản lý |
| verified_by, approved_by, approved_at | **Không** | Ghi |
| source_hash, gate0_id | **Không** (lấy từ sổ nguồn) | Lấy từ sổ nguồn |
| release, active/recalled | **Không** | Sổ phát hành / manifest phát hành |

## 2. `batch-manifest.json`

```json
{
  "contract_version": "hi1-ku-contract/1.1",
  "profile": "backend",
  "mode": "A",
  "batch_id": "B-2026-11-021",
  "revision": 1,
  "agent": "seller-onboarding",
  "inputs": [
    { "source_id": "SRC-012", "version": "v3", "gate0_id": "G0-0144", "redacted_file_hash": "sha256:…" }
  ],
  "checkpoint": {
    "phase_done": "P2",
    "processed": ["SRC-012"],
    "blocked": [{ "source_id": "SRC-015", "reason": "RED_SUSPECTED", "locator": "tr.2" }],
    "pending_human": ["owner cho c0007"]
  }
}
```
Gate 0 (`gate0_id`, hash) do backend/người điền và đối chiếu; LLM chỉ chép lại giá trị được cung cấp, không tự xác nhận.

## 3. `candidates.jsonl`
Mỗi dòng một object theo `candidate.schema.json`. Ví dụ (xuống dòng cho dễ đọc):

```json
{"contract_version":"hi1-ku-contract/1.1","batch_id":"B-2026-11-021","revision":1,"client_record_id":"c0003",
 "source_refs":[{"source_id":"SRC-012","version":"v3","doc_version":"3.0","locator":"tr.4 §2.3","approval_state":"PENDING"}],
 "title":"Giấy tờ bắt buộc với hộ kinh doanh ngành thực phẩm",
 "body":{"conditions":"Nhà bán là HKD, đăng ký ngành thực phẩm","content":"Nộp ĐKKD và giấy chứng nhận ATTP còn hạn.","exceptions":"…","required_docs":["ĐKKD","Giấy ATTP"]},
 "audience_proposed":["staff","seller"],
 "layer":"L1","authority_type_proposed":"RULE",
 "scope":{"domain":"SEL","department":"Phát triển & hỗ trợ nhà bán","facets":{"seller_type":["HKD"],"category":["thực phẩm"],"channel":null}},
 "effective_window_proposed":{"from":"2026-05-01","to":null},
 "sensitivity_proposed":"GREEN","owner_proposed":"Kiểm duyệt nhà bán",
 "route_summary":"HKD bán thực phẩm cần ĐKKD và giấy ATTP còn hạn.","flags":["scope_unconfirmed"],"inferred_fields":[]}
```

## 4. Phản hồi validation (backend → skill)

```json
{"batch_id":"B-2026-11-021","revision":1,"results":[
  {"client_record_id":"c0003","result":"accepted","assigned_ku_id":"KU-000123"},
  {"client_record_id":"c0004","result":"rejected","errors":[
    {"code":"LOCATOR_NOT_FOUND","field":"source_refs[0].locator","reason":"Không có §2.9 trong SRC-012@v3","fixable":true}]}
]}
```
Sửa record bị reject → nộp **revision mới cùng batch_id**, chỉ gồm record sửa.

## 5. Quy tắc idempotency
- Nộp lại **nguyên vẹn** cùng batch_id + revision → backend trả lại kết quả/ID cũ.
- Cùng batch_id + revision nhưng nội dung khác → từ chối; phải nộp revision mới.
- Revision mới: backend hiển thị cặp cũ–mới theo vùng nguồn chồng lấn; **người duyệt** quyết định giữ ID (tăng ku_version), tách ID hay gộp. Không tự giữ ID chỉ vì cùng locator/hash body. KU APPROVED không bị ghi đè.
- Ứng viên trùng nguồn/vị trí giữa các batch → gắn cờ cho người duyệt, không tự gộp.

## 6. LLM tuyệt đối không làm (profile backend)
Đọc bản gốc chứa Đỏ · tự xác nhận Gate 0 · cấp ku_id · đặt status/duyệt · ghi trực tiếp vào kho · bật/thu hồi release · sửa CMS.

## 7. Gate 0
- no-code: chỉ có bằng chứng thủ tục (dòng Gate 0 trong sổ nguồn: gate0_id, người che, người kiểm 2, hash bản che; chỉ nạp từ thư mục T1-ready). Xác nhận phải diễn ra **trước khi tải/mở file**.
- backend: scanner tự động chạy trước lời gọi model, lưu log + hash; kết quả nghi ngờ → chặn và chuyển người kiểm. "Scanner không báo" không có nghĩa là chắc chắn hết dữ liệu Đỏ.
