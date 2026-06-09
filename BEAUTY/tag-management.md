# Hashtag — Wireframe Specification

> File nguồn: `tag-management.html` — Module Hashtag của BEAUTY Admin.

---

## 1. Overview

### Số trang / section
Module có **2 trang chính**:

| # | Page ID | Sidebar item | Page title |
|---|---|---|---|
| 9.1 | `page-list` | `Danh sách Hashtag` | • Danh sách Hashtag |
| 9.2 | `page-best` | `Hashtag Phổ biến` | • Hashtag Phổ biến |

Cả 2 cùng dùng chung 1 modal xác nhận (`#action-modal-backdrop`) ở cuối body.

### Sidebar items và key điều hướng

| Sidebar element | id | onclick | Page mở |
|---|---|---|---|
| `Danh sách Hashtag` | `sidebar-list` | `goSection('list')` | `page-list` |
| `Hashtag Phổ biến` | `sidebar-best` | `goSection('best')` | `page-best` |

Sidebar label nhóm: `Hashtag` (tĩnh).

### Rule chung toàn module

| Rule | Mô tả |
|---|---|
| Wording — Action verbs | "Gắn phổ biến" thay cho "Gắn/Đánh Best"; "Gỡ phổ biến" thay cho "Gỡ Best". |
| Wording — Section noun | Tên category là `Hashtag Phổ biến` (không phải "Hashtag Best"). |
| Wording — Score column | Hiển thị là `Hashtag score` (key dữ liệu vẫn là `used`). |
| Wording — Bulk action label | Bên trái table actions luôn có dòng `Hashtag đã chọn:` trước các button. |
| Date format | `dd-MM-yyyy HH:mm` cho `created` / `lastUsed`. |
| Default sort | Cả 2 bảng load với `col: "used", dir: "desc"` (Hashtag score giảm dần). |
| Sort hint | Cột sortable mà chưa active vẫn hiện ký tự `⇅` để user biết là sortable. |
| Active sort icon | `▼` (desc) / `▲` (asc) — đổi màu sang `--primary` qua class `sorted-asc/sorted-desc`. |
| Internal data flag | `isBest: true/false` — vẫn dùng tên "Best" trong code nhưng không hiển thị UI. |
| Action key | `mark-best` / `unmark-best` / `bulk-mark-best` / `bulk-unmark-best` — internal, không hiển thị. |
| Bulk action — validate | Click bulk khi `selectedIds[target].size === 0` → alert `"Vui lòng chọn ít nhất 1 Hashtag."` và không mở modal. |
| Close menu | Click ngoài → `closeAllMenus()` đóng cả `.cell-menu` và `.criteria-wrap`. |
| Escape key | Đóng action modal. |

---

## 2. Trang 9.1 — Danh sách Hashtag (`page-list`)

### A. Bộ lọc & Tìm kiếm

**Hàng 1 — Bộ lọc thời gian:**

| Field | Giá trị / Option | Behavior |
|---|---|---|
| Date label | `Ngày sử dụng:` | tĩnh |
| Date range | `‹ 23-06-2025 ~ 30-06-2025 ›` (id=`list-date`) | click `‹` / `›` → `shiftDate('list', dir)` (chỉ alert placeholder) |
| Quick filter | `Ngày` / `Tuần` (active) / `Tháng` / `Năm` / `Tất cả` | UI tĩnh, không có handler |

**Hàng 2 — Tìm kiếm:**

| Field | Giá trị | Behavior |
|---|---|---|
| Search criteria dropdown | `ID` (mặc định) | click → `toggleCriteria('list', event)` mở menu |
| Search criteria options | `ID` / `Người tạo` / `Hashtag` | click → `selectCriteria('list', label)` đổi label |
| Input | placeholder = `Nhập từ khóa` | text input |
| Search button | `Tìm` | onclick → `alert('Chức năng đang phát triển.')` |

### B. Bulk action

**Bên trái (`table-actions-left`)** — label `Hashtag đã chọn:` rồi:

| # | Button | Class | onclick | Hành vi |
|---|---|---|---|---|
| 1 | `Xóa` | `btn-outline-danger` | `openActionModal('bulk-delete')` | Validate count > 0 → mở modal `bulk-delete` |
| 2 | `Gắn phổ biến` | `btn-outline-primary` | `openActionModal('bulk-mark-best')` | Validate count > 0 → mở modal `bulk-mark-best` |

**Bên phải (`table-actions-right`):**

| Dropdown | Options | Default | onchange |
|---|---|---|---|
| Số dòng/page | `Danh sách 30` / `Danh sách 50` / `Danh sách 100` | `Danh sách 30` | (không có handler) |

### C. Bảng danh sách (`#tbody-list`)

**Thead — thứ tự cột:**

| # | Header | Loại | Sortable |
|---|---|---|---|
| 1 | checkbox `toggleAll(this, 'tbody-list')` | checkbox toàn cột | — |
| 2 | `Tên Hashtag` | text + cell-menu | — |
| 3 | `Hashtag score` ▼ (init) | text sortable | có (`toggleSort('list', 'used')`) |
| 4 | `Người tạo` | text | — |
| 5 | `Cấp bậc` | text | — |
| 6 | `Ngày tạo` | text | — |
| 7 | `Lần cuối sử dụng` ⇅ (init) | text sortable | có (`toggleSort('list', 'used-date')`) |

**Từng cột — chi tiết render:**

| Cột | Loại | Nội dung hiển thị | Action |
|---|---|---|---|
| Checkbox | `<input type="checkbox" data-id="{t.id}">` | — | `toggleRow(this, 'list', t.id)` cập nhật `selectedIds.list` |
| Tên Hashtag | cell-menu trigger là `<span class="tag-chip">{t.name}</span>` (thêm class `best is-best-mark` nếu `t.isBest`) | tên hashtag có dấu `#` | click → toggle menu |
| Hashtag score | text plain | `fmtNum(t.used)` (format vi-VN) | — |
| Người tạo | text plain | `escText(t.creator)` | — |
| Cấp bậc | text plain | `escText(t.grade)` | — |
| Ngày tạo | text plain | `escText(t.created)` | — |
| Lần cuối sử dụng | text plain | `escText(t.lastUsed)` | — |

**Cell-menu cột Tên Hashtag — menu items theo thứ tự:**

1. `Tìm bài viết chứa Hashtag này` → `alert('Tìm bài viết chứa Hashtag {t.name} (đang phát triển).')`
2. **Nếu `t.isBest === true`** → `Gỡ phổ biến` → `openTagAction('unmark-best', t.id)`
   **Nếu `t.isBest === false`** → `Gắn phổ biến` → `openTagAction('mark-best', t.id)`
3. `Xóa Hashtag` → `openTagAction('delete-tag', t.id)`

Không có `<hr>` phân cách giữa các menu-item.

**Footer:**
- Pagination: `‹ 1 (active) 2 3 4 ›` (UI tĩnh, không có handler)
- Right spacer: `width: 120px`

### D. Action Modal Map

Các key liên quan trang này (subset of full map — xem mục 4):
- `bulk-delete`, `bulk-mark-best`, `mark-best`, `unmark-best`, `delete-tag`

### E. Các modal khác
Không có modal nào riêng cho trang này — dùng chung action modal ở mục 4.

### F. Business Rules (riêng trang 9.1)

| Rule | Mô tả |
|---|---|
| Cell-menu thứ 2 — biến thể | Hashtag đang Phổ biến (`isBest=true`) → hiện `Gỡ phổ biến`; còn lại hiện `Gắn phổ biến`. |
| Bulk `Xóa` | Xóa toàn bộ hashtag có `id ∈ selectedIds.list` khỏi `tags`, sau đó `selectedIds.list.clear()`. |
| Bulk `Gắn phổ biến` | Set `isBest=true` cho mỗi hashtag có `id ∈ selectedIds.list`, sau đó `selectedIds.list.clear()`. |
| Count display | `{N} Hashtag` — id `list-count`, cập nhật sau mỗi `renderListTable()`. |
| Toggle sort | Click cùng cột → đảo `asc/desc`. Click cột khác → set `col` mới + `dir="desc"`. |

### G. JS Functions quan trọng (sử dụng cho trang này)

| Function | Mục đích | Tham số | Hành vi chính |
|---|---|---|---|
| `goSection(section)` | Đổi sang section khác | `'list'` / `'best'` | Set sidebar/page active class, `closeAllMenus()` |
| `shiftDate(target, dir)` | Đổi date range | `target='list'`, `dir=±1` | **Chưa implement** — chỉ alert |
| `toggleCriteria(target, e)` | Mở/đóng dropdown tiêu chí | | Đóng dropdown khác, toggle wrap |
| `selectCriteria(target, label)` | Chọn 1 tiêu chí | | Set text label, đóng dropdown |
| `toggleSort(target, col)` | Click header sortable | | Đảo dir nếu cùng col, đổi col + desc nếu khác. Gọi `renderArrows` + render bảng tương ứng |
| `renderArrows(target)` | Vẽ icon trên header | | Active: `▲`/`▼`; inactive: `⇅`. Toggle class `sorted-asc/sorted-desc` |
| `sortTags(arr, target)` | Trả về array đã sort | | Sort theo `col` của `sortColumn[target]`; `used` so sánh số, `created`/`used-date` parse `dd-mm-yyyy` rồi so sánh Date. **Note:** `parseDate` chỉ match pattern `^dd-MM-yyyy$` — chuỗi có giờ phút như `"23-06-2025 09:34"` sẽ KHÔNG match và trả về `new Date(0)`. |
| `toggleRow(chk, target, id)` | Tick 1 dòng | | Add/remove `id` khỏi `selectedIds[target]` |
| `toggleAll(chk, tbodyId)` | Tick header | | Set tất cả checkbox theo `chk.checked`, sync `selectedIds[target]` (chỉ box có `data-id`) |
| `renderListTable()` | Render lại bảng | — | Gọi `sortTags(tags, 'list')`, set count, đổ HTML vào `tbody-list` |
| `openTagAction(type, id)` | Cell-menu single action | | Set `pendingAction = {type, id}`, mở modal core, `closeAllMenus()` |
| `openActionModal(type)` | Bulk action | | Tính `target` từ `type` (xem mục 4), nếu count=0 thì alert; còn lại set `pendingAction = {type, id: null}` và mở modal |

### H. Data fields — array `tags`

12 record mẫu. Mỗi object có 8 field:

| Field | Kiểu | Ví dụ |
|---|---|---|
| `id` | string | `"T001"` |
| `name` | string | `"#giảm cân"` |
| `used` | number | `788` |
| `creator` | string | `"tuongvy"` |
| `grade` | string | `"Lv.1"` / `"Lv.2"` / `"Lv.3"` / `"KOL"` / `"Chuyên gia"` / `"Bác sĩ"` |
| `created` | string | `"10-06-2025 16:53"` (dd-MM-yyyy HH:mm) |
| `lastUsed` | string | `"23-06-2025 09:34"` |
| `isBest` | boolean | `true` / `false` |

Phân bố `isBest`: 4 record `true` (T001, T002, T003, T007), 8 record `false`.

---

## 3. Trang 9.2 — Hashtag Phổ biến (`page-best`)

### A. Bộ lọc & Tìm kiếm

Giống trang `page-list` về cấu trúc, khác về id/target:

| Field | Giá trị | Khác biệt vs trang 9.1 |
|---|---|---|
| Date label | `Ngày sử dụng:` | giống |
| Date range id | `best-date`, gọi `shiftDate('best', dir)` | target khác |
| Criteria wrap id | `criteria-best` | target khác |
| Search input | placeholder `Nhập từ khóa` | giống |
| Search criteria options | `ID` / `Người tạo` / `Hashtag` | giống |

### B. Bulk action

**Bên trái** — label `Hashtag đã chọn:` rồi:

| # | Button | Class | onclick |
|---|---|---|---|
| 1 | `Gỡ phổ biến` | `btn-outline-danger` | `openActionModal('bulk-unmark-best')` |

(Không có nút `Xóa` hay `Gắn phổ biến` ở trang này.)

**Bên phải:**

| Dropdown | Options | Default | onchange |
|---|---|---|---|
| Số dòng/page | `Danh sách 30` / `Danh sách 50` / `Danh sách 100` | `Danh sách 30` | (không có handler) |

### C. Bảng danh sách (`#tbody-best`)

**Thead — y hệt trang 9.1** (xem bảng cột ở mục 2.C), chỉ khác `id` của span sort:
- Hashtag score → `sa-best-used` (init `▼`)
- Lần cuối sử dụng → `sa-best-used-date` (init `⇅`)

Hai cột này gọi `toggleSort('best', ...)` thay vì `'list'`.

**Render từng dòng:**

| Cột | Khác biệt vs trang 9.1 |
|---|---|
| Checkbox | `onchange="toggleRow(this, 'best', t.id)"` |
| Tên Hashtag | Tag-chip **luôn** có class `best is-best-mark` (vì page này chỉ hiển thị isBest=true) |
| Các cột còn lại | Giống y hệt |

**Cell-menu — 3 item:**

1. `Tìm bài viết chứa Hashtag này` → `alert(...)` (giống trang 9.1)
2. `Gỡ phổ biến` → `openTagAction('unmark-best', t.id)`
3. `Xóa Hashtag` → `openTagAction('delete-tag', t.id)`

Không có `<hr>` phân cách.

**Footer:**
- Pagination: `‹ 1 (active) 2 ›` (UI tĩnh, ít hơn trang 9.1)
- Right spacer: `width: 120px`

### D. Action Modal Map
Liên quan: `bulk-unmark-best`, `unmark-best`, `delete-tag`.

### E. Các modal khác
Không có.

### F. Business Rules (riêng trang 9.2)

| Rule | Mô tả |
|---|---|
| Data source | `renderBestTable` filter `tags.filter(t => t.isBest)` rồi mới sort. |
| Cell-menu | Luôn 2 item — chỉ hiện hành động Gỡ phổ biến, không có nhánh "Gắn phổ biến". |
| Bulk `Gỡ phổ biến` | Set `isBest=false` cho mỗi hashtag có `id ∈ selectedIds.best`, sau đó `selectedIds.best.clear()`. |
| Count display | `{N} Hashtag` — id `best-count`. |

### G. JS Functions quan trọng (riêng trang này)

| Function | Mục đích | Hành vi chính |
|---|---|---|
| `renderBestTable()` | Render bảng `tbody-best` | Lọc `isBest=true`, sort theo `sortColumn.best`, đổ HTML |

### H. Data fields
Dùng chung array `tags` — xem mục 2.H. Trang này chỉ hiển thị các record có `isBest === true`.

---

## 4. Action Modal Map (dùng chung 2 trang)

| Key | Title | Body | Done message | `primary`? |
|---|---|---|---|---|
| `mark-best` | `Gắn phổ biến Hashtag` | `Hashtag sẽ được thêm vào mục Hashtag Phổ biến.` | `Đã gắn phổ biến.` | `true` |
| `unmark-best` | `Gỡ phổ biến` | `Hashtag sẽ bị gỡ khỏi Hashtag Phổ biến, trở về Hashtag thường.` | `Đã gỡ phổ biến.` | — |
| `delete-tag` | `Xóa Hashtag` | `Hashtag sẽ bị xóa khỏi hệ thống và không còn dùng được trong bài viết.` | `Đã xóa Hashtag.` | — |
| `bulk-mark-best` | `Gắn phổ biến các Hashtag đã chọn` | `Các Hashtag sẽ được thêm vào mục Hashtag Phổ biến.` | `Đã gắn phổ biến.` | `true` |
| `bulk-delete` | `Xóa các Hashtag đã chọn` | `Các Hashtag sẽ bị xóa khỏi hệ thống.` | `Đã xóa các Hashtag.` | — |
| `bulk-unmark-best` | `Gỡ phổ biến các Hashtag đã chọn` | `Các Hashtag sẽ trở về Hashtag thường.` | `Đã gỡ phổ biến.` | — |

**Cấu trúc modal (`#action-modal-backdrop`):**

| Element | id | Nội dung |
|---|---|---|
| Title | `action-modal-title` | Mặc định `Xác nhận`, set theo `cfg.title` khi mở |
| Body | `action-modal-body` | Mặc định `Bạn có chắc chắn?`, set theo `cfg.body` |
| Cancel button | — | `Hủy` → `closeActionModal()` |
| Confirm button | — | `Xác nhận` → `confirmActionModal()`. Toggle class `is-primary` theo `cfg.primary` |

**Logic `openActionModal(type)` chọn target:**

```
target =
  (type chứa "best" AND không chứa "unmark")   → "list"
  type === "bulk-unmark-best"                   → "best"
  còn lại                                       → "list"
```

`bulk-delete` không match điều kiện đầu → fallback "list" — đúng (Xóa chỉ ở trang Danh sách).

---

## 5. JS Functions tổng hợp (toàn module)

### Helpers
| Function | Mục đích |
|---|---|
| `escText(s)` | Escape `<`, `>`, `&`, `"`, `'` cho HTML |
| `fmtNum(n)` | `Number(n).toLocaleString('vi-VN')` |
| `parseDate(s)` | Parse `dd-MM-yyyy` thành `Date`. **Note:** chỉ match strict pattern không có time component. Chuỗi có HH:mm sẽ fail và trả về `new Date(0)`. |

### Navigation & UI
| Function | Mục đích |
|---|---|
| `goSection(section)` | Đổi page, set active class |
| `shiftDate(target, dir)` | **Chưa implement** — chỉ alert |
| `toggleCriteria(target, e)` / `selectCriteria(target, label)` | Dropdown tiêu chí tìm kiếm |
| `renderCriteriaMenu(target)` | Đổ option vào `.criteria-menu` từ `SEARCH_CRITERIA` |
| `toggleMenu(event, menuEl)` | Toggle class `open` cho `.cell-menu` |
| `closeAllMenus()` | Đóng mọi `.cell-menu.open` và `.criteria-wrap.open` |

### Sort & Selection
| Function | Mục đích |
|---|---|
| `sortTags(arr, target)` | Trả về copy đã sort theo `sortColumn[target]` |
| `toggleSort(target, col)` | Click header — đảo dir hoặc đổi col |
| `renderArrows(target)` | Cập nhật icon trên 2 cột sortable |
| `toggleRow(chk, target, id)` | Tick/untick 1 dòng |
| `toggleAll(chk, tbodyId)` | Tick/untick toàn bảng (chỉ box có `data-id`) |

### Render
| Function | Mục đích |
|---|---|
| `renderListTable()` | Render `tbody-list` + update `list-count` |
| `renderBestTable()` | Render `tbody-best` + update `best-count` (chỉ `isBest=true`) |

### Action Modal
| Function | Mục đích |
|---|---|
| `openTagAction(type, id)` | Cell-menu single action — set `pendingAction`, mở modal |
| `openActionModal(type)` | Bulk action — validate count > 0, set `pendingAction`, mở modal |
| `openActionModalCore(cfg)` | Set title/body, toggle is-primary, hiện backdrop |
| `closeActionModal()` | Đóng backdrop, reset `pendingAction = null` |
| `confirmActionModal()` | Apply action theo `pendingAction.type`, render lại 2 bảng, alert `cfg.done`, đóng modal |

### Init (chạy 1 lần ở cuối script)
1. `['list', 'best'].forEach(renderCriteriaMenu)` — đổ option dropdown tiêu chí
2. `renderArrows('list')` + `renderArrows('best')` — vẽ icon sort
3. `renderListTable()` + `renderBestTable()` — render data

### Global listeners
- `document.addEventListener('click', () => closeAllMenus())`
- `document.addEventListener('keydown', e => { if (e.key === 'Escape') closeActionModal() })`

---

## 6. Global state

| Biến | Kiểu | Giá trị mặc định | Mục đích |
|---|---|---|---|
| `tags` | Array<object> | 12 sample (mục 2.H) | Data nguồn duy nhất |
| `SEARCH_CRITERIA` | `["ID", "Người tạo", "Hashtag"]` | const | Dropdown tìm kiếm |
| `currentSection` | string | `"list"` | Section đang active |
| `sortBy` | `{list, best}` | `{list: "usedDesc", best: "usedDesc"}` | **Không sử dụng nữa** (legacy — sau khi bỏ dropdown sort) |
| `sortColumn` | `{list: {col, dir}, best: {col, dir}}` | `{list: {col:"used", dir:"desc"}, best: {col:"used", dir:"desc"}}` | Trạng thái sort hiện tại |
| `selectedIds` | `{list: Set, best: Set}` | `{Set(), Set()}` | ID đang check |
| `pendingAction` | `{type, id} \| null` | `null` | Action đang chờ confirm |

---

## 7. Các điểm chưa implement / placeholder

| Element | Vấn đề |
|---|---|
| `shiftDate(target, dir)` | Chỉ `alert("Chuyển khoảng thời gian: ...")`, không thực sự đổi `#list-date` / `#best-date`. |
| Quick filter buttons (`Ngày` / `Tuần` / ...) | Không có onclick handler, không filter. |
| Search button `Tìm` | `alert('Chức năng đang phát triển.')` — không filter `tags`. |
| Search input | Không có oninput / onkeydown — không filter live. |
| Search criteria | Đổi được label nhưng không tham gia filter logic. |
| Dropdown `Danh sách 30/50/100` | Không có handler — không thay đổi pagination. |
| Pagination buttons (`‹ 1 2 3 ... ›`) | UI tĩnh, không có handler. |
| Menu item `Tìm bài viết chứa Hashtag này` | Chỉ `alert(...)`. |
| `parseDate` | Pattern `^(\d{2})-(\d{2})-(\d{4})$` không match chuỗi có giờ phút như `"10-06-2025 16:53"`. Sort theo `created` / `used-date` thực tế đang dùng `new Date(0)` cho **mọi** record (toàn bộ value `lastUsed`/`created` có `HH:mm`). → Sort theo `used-date` thực ra sẽ trả thứ tự gốc (vì so sánh `0 - 0 === 0`). **Sort theo `used` (Hashtag score) hoạt động đúng vì so sánh number.** |
| State `sortBy` | Khai báo nhưng không còn function nào đọc/ghi sau khi dropdown sort bị bỏ. |
