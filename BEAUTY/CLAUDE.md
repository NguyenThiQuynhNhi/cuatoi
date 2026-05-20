# CLAUDE.md — BEAUTY Admin Mockup

Quy tắc chung cho toàn bộ mockup HTML/CSS/JS trong thư mục `BEAUTY/`. Áp dụng khi tạo trang mới hoặc chỉnh sửa các trang hiện có (`doctor-management.html`, `hospital-management.html`, `partner-management.html`, `product-management.html`, `virtual-member-management.html`, ...).

Mục tiêu: tất cả các trang trong `BEAUTY/` phải đồng nhất về **layout, màu sắc, typography, component, hành vi**. Khi thêm tính năng mới → kế thừa pattern có sẵn, không tự ý đặt class/style mới.

---

## 1. Cấu trúc file

- Mỗi trang là 1 file `.html` đơn (single-file) tự chứa CSS + JS inline trong `<style>` và `<script>`.
- `<head>`:
  - `lang="vi"`, `meta charset="UTF-8"`, viewport responsive.
  - Font: **Be Vietnam Pro** (Google Fonts, weight `300;400;500;600;700`).
  - `<title>` theo format: `{Tên trang} - BEAUTY Admin`.
- Thứ tự body: `header` → `sidebar` (nếu có) → nhiều `<main class="main page" id="page-...">` (mỗi page 1 màn).
- Các modal/backdrop đặt cuối `<body>`, ngoài `<main>`.
- KHÔNG dùng framework (không Bootstrap/Tailwind), chỉ CSS thuần + JS thuần.

---

## 2. Design tokens (`:root` CSS variables)

Bắt buộc khai báo và dùng đúng các biến sau (không hardcode màu/khoảng cách):

```
--primary: #6c3fc5;       --primary-light: #ede9f8;   --primary-mid: #c4b0ec;
--accent:  #e8436a;       --accent-light:  #fde8ed;
--gray-50..900: thang xám chuẩn (#f8f7fc → #1e1a35)
--white: #ffffff;
--shadow-sm / --shadow-md: shadow tím nhạt theo primary
--radius: 10px;  --radius-sm: 6px;
--sidebar-w: 210px;  --header-h: 52px;
```

- Màu chủ đạo = **primary tím**. Màu nguy hiểm/nhấn = **accent đỏ-hồng**.
- Văn bản: `gray-900` (tiêu đề), `gray-700` (body), `gray-500` (meta/hint), `gray-400` (disabled).
- Background nền: `gray-50`. Card: `white`. Hover row/menu: `gray-100`.

---

## 3. Typography

- `font-family: "Be Vietnam Pro", sans-serif;`
- Body: **13px**.
- Page title: 15px / 700.
- Card header / detail title: 16–18px / 600–700.
- Table th: 11.5px / 600 / `gray-500` / `text-align: center`.
- Table td: 12px / `gray-700` / `text-align: center` (dùng class `td-left` để căn trái).
- Form label: 12px / 600 / `gray-700`. Input: 12px.
- Button: 12px / 600. `.btn-sm`: 11px.
- Tooltip: 11px white trên `gray-900`.
- Bắt buộc tiếng Việt cho mọi label/text mặc định.

---

## 4. Layout xương sống

```
<body>
  <header class="header"> ... </header>          (fixed top, gradient tím, height 52)
  <aside class="sidebar"> ... </aside>            (fixed left, width 210, optional)
  <main class="main page active" id="page-list"> ... </main>
  <main class="main page"        id="page-detail">...</main>
  <main class="main page"        id="page-form">...</main>
  <!-- modals/backdrops cuối body -->
</body>
```

- `.page { display: none }` + `.page.active { display: block }` — chuyển trang bằng JS thêm/bỏ `active`, KHÔNG reload.
- `.main` margin-left = `--sidebar-w` (nếu có sidebar), padding 20px.
- Header gradient: `linear-gradient(135deg, #4a2096, #6c3fc5, #8b5cf6)`.
- Mỗi page bắt đầu bằng `breadcrumb` (nếu là chi tiết/form) rồi tới `.card`.

---

## 5. Component chuẩn — bắt buộc tái sử dụng

### 5.1 Button — `.btn` + biến thể
```html
<button class="btn btn-primary">...</button>
```
Biến thể: `btn-primary`, `btn-outline-primary`, `btn-danger`, `btn-outline-danger`, `btn-secondary`, `btn-ghost`. Modifier kích thước: `btn-sm`.

Quy tắc icon trong button: SVG inline (`width=10–12`, `stroke="currentColor"`, `stroke-width="2–2.5"`, `fill="none"`) đặt trước text, gap 5px.

Hành động ngữ nghĩa:
- **Primary action** (Lưu, Đăng, Xác nhận positive) → `btn-primary`.
- **Destructive** (Xóa, Buộc rời bỏ) → `btn-danger`.
- **Outline destructive** (Hủy form, Xóa hàng loạt) → `btn-outline-danger`.
- **Outline primary** (Khôi phục, Gửi thông báo, Thay đổi cấp bậc, +Thêm) → `btn-outline-primary`.
- **Ghost** (Quay lại, đóng nhẹ) → `btn-ghost`.

### 5.2 Card
```html
<div class="card"><div class="card-body"> ... </div></div>
```
Mọi nội dung chính bọc trong `.card`. Khoảng cách giữa các card: `margin-bottom: 14px`.

### 5.3 Breadcrumb
```html
<div class="breadcrumb">
  <span class="bc-link" onclick="goPage('list')">Danh sách ...</span>
  <span class="bc-sep">/</span>
  <span class="bc-current">Chi tiết ...</span>
</div>
```

### 5.4 Tabs
```html
<div class="tabs">
  <div class="tab active" id="tab-info" onclick="switchTab('info')">...</div>
  <div class="tab"        id="tab-deleted" onclick="switchTab('deleted')">...</div>
</div>
<div id="panel-info"> ... </div>
<div id="panel-deleted" style="display:none"> ... </div>
```
Tab active dùng `color: var(--primary)` + `border-bottom: 2px solid var(--primary)`.

### 5.5 Bảng (table)
Cấu trúc bắt buộc:
```html
<div class="table-actions">
  <div class="table-actions-left">
    <span>Mục đã chọn:</span>
    <button class="btn btn-outline-danger btn-sm">Xóa</button>
    <!-- bulk action khác... -->
  </div>
  <div class="table-actions-right">
    <div class="select-dropdown"><select><option>Danh sách 30</option>...</select></div>
  </div>
</div>
<div class="table-wrap">
  <table id="table-info">
    <thead><tr><th><input type="checkbox" id="chk-all-info" onchange="toggleAllInTable(this,'table-info')"/></th>...</tr></thead>
    <tbody id="tbody-info"></tbody>
  </table>
</div>
<div class="table-footer">
  <div><button class="btn btn-danger">Thêm (+)</button></div>
  <div class="pagination">
    <button class="pg-btn">‹</button>
    <button class="pg-btn active">1</button>
    <button class="pg-btn">›</button>
  </div>
</div>
```
- `table` có `min-width: 1200px` + bọc trong `.table-wrap` (cuộn ngang).
- Cột đầu = checkbox dòng, hàm `toggleRow(this,'tr-id')`.
- Cột tên / nhận diện chính dùng `.cell-menu` (xem 5.6).

### 5.6 Cell menu (dropdown trong dòng bảng)
```html
<td class="td-left">
  <div class="cell-menu">
    <button class="menu-trigger" onclick="toggleMenu(event, this.parentElement)">{Tên}</button>
    <div class="menu-list">
      <button class="menu-item" onclick="...">Thông tin chi tiết</button>
      <button class="menu-item" onclick="...">Lịch sử hoạt động</button>
      <button class="menu-item" onclick="...">Chỉnh sửa</button>
      <button class="menu-item" onclick="openActionModal('soft-delete')">Xóa</button>
      <button class="menu-item" onclick="openActionModal('notify')">Gửi thông báo</button>
    </div>
  </div>
</td>
```
- `menu-trigger` = text gạch chân màu primary.
- Click ngoài menu → `closeAllMenus()` (đã wire trong global click listener).

### 5.7 Note ellipsis + Tooltip
```html
<div class="tooltip-wrap">
  <span class="note-ellipsis">{text rút gọn}</span>
  <div class="tooltip">{full text}</div>
</div>
```
- Ghi chú trong bảng: rút gọn ~50 ký tự, hover ra tooltip đen.

### 5.8 Form
```html
<div class="form-grid">
  <div class="form-group">
    <label class="form-label">Tên <span class="req">*</span></label>
    <input class="form-input" placeholder="..." />
    <div class="error-text"></div>
  </div>
  ...
  <div class="form-row-full"> ... </div>  <!-- chiếm full width -->
</div>
<div class="form-actions">
  <button class="btn btn-outline-danger" onclick="handleFormCancel()">Hủy</button>
  <button class="btn btn-primary" onclick="handleFormSubmit()">Lưu</button>
</div>
```
- Trường bắt buộc đánh dấu bằng `<span class="req">*</span>` (màu accent).
- Lỗi: thêm class `invalid` lên input + nội dung trong `.error-text`.
- Form luôn 2 cột (`form-grid`); group cần full width dùng `form-row-full`.

### 5.9 Detail page header
```html
<div class="detail-header">
  <div class="detail-header-title">
    <div class="doctor-avatar">XX</div>
    <div>
      <div class="detail-title">Tên</div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:6px">
        <span class="meta-badge">ID: ...</span>
        <span class="meta-badge">...</span>
      </div>
    </div>
  </div>
  <div style="display:flex;gap:12px;flex-wrap:wrap">
    <!-- action buttons: Chỉnh sửa, Tạm khóa, Buộc rời bỏ, Gửi thông báo đẩy... -->
  </div>
</div>
<div class="stats-grid">
  <div class="stat-box"><div class="stat-label">...</div><div class="stat-value">0</div></div>
  ...
</div>
```
- `.stats-grid` mặc định 4 cột.

### 5.10 Action modal (xác nhận)
**1 modal duy nhất** dùng chung cho mọi confirm action (xóa, khôi phục, tạm khóa, gửi thông báo, ...). Cấu trúc cố định:
```html
<div class="action-modal-backdrop" id="action-modal-backdrop" onclick="closeActionModal()">
  <div class="action-modal" role="dialog" aria-modal="true" onclick="event.stopPropagation()">
    <h3 class="action-modal-title" id="action-modal-title">...</h3>
    <p  class="action-modal-body"  id="action-modal-body">...</p>
    <div class="action-modal-actions">
      <button class="action-modal-btn action-modal-btn-cancel"  onclick="closeActionModal()">Hủy</button>
      <button class="action-modal-btn action-modal-btn-confirm" onclick="confirmActionModal()">Xác nhận</button>
    </div>
  </div>
</div>
```
JS dùng map cấu hình:
```js
const actionModalMap = {
  "soft-delete":  { title: "Xóa ...",          body: "..." },
  "hard-delete":  { title: "Xóa vĩnh viễn",    body: "..." },
  "restore":      { title: "Khôi phục ...",    body: "..." },
  "suspend":      { title: "Tạm khóa ...",     body: "..." },
  "force-leave":  { title: "Buộc rời bỏ",      body: "..." },
  "notify":       { title: "Gửi thông báo",    body: "Gửi thông báo đẩy đến ...." },
};
function openActionModal(type) { /* set title/body, add .open */ }
function closeActionModal()    { /* remove .open */ }
```
- Click backdrop hoặc nút Hủy → đóng. Phím `Escape` → đóng.
- Mỗi page có riêng `actionModalMap` với wording phù hợp domain (bác sĩ / TVA / đối tác / sản phẩm).

### 5.11 Modal lớn (write-post, change-level, ...)
- Dùng cùng pattern `*-backdrop` + `role="dialog"` + `event.stopPropagation()`.
- Z-index: backdrop chuẩn = 260; modal chồng (write-post) = 270.
- Đóng bằng nút `×` góc phải, click backdrop, hoặc Escape.

### 5.12 Search/filter row (đầu trang list)
- Bọc trong `.card` đầu tiên.
- Có thể chứa: `.date-range` (chọn ngày + nav), `.tf-btn` (quick filter active = primary), `.criteria-wrap` (dropdown tiêu chí), `.search-input-lg`, nút `btn-primary` "Tìm kiếm".
- Reset filter: nút `btn-outline-primary` "Khởi tạo lại" (nếu có).

### 5.13 Pagination
```html
<div class="pagination">
  <button class="pg-btn">‹</button>
  <button class="pg-btn active">1</button>
  <button class="pg-btn">2</button>
  <button class="pg-btn">›</button>
</div>
```
- Đặt giữa `.table-footer`, kèm dropdown size bên trái (`Danh sách 30/50/100`).

### 5.14 Category builder (chọn danh mục chính + phụ)
- 1 dropdown chính + 1 dropdown phụ multi-select (max 3 sub) + nút "+ Thêm".
- Tối đa 3 main, mỗi main tối đa 3 sub.
- Hiển thị đã chọn dạng card mỗi nhóm: chip main (nền primary, chữ trắng) + danh sách chip sub (nền primary-light) + counter `n/3 danh mục phụ`.
- Lỗi: `"Chỉ được tối đa 3 danh mục chính."` / `"Mỗi danh mục chính chỉ chọn tối đa 3 danh mục phụ."`.

---

## 6. Quy tắc JavaScript

- **Không** dùng framework. Chỉ JS thuần ES6+.
- Tổ chức: data array (`activeMembers`, `deletedMembers`, ...) + render functions (`renderMemberTable`, `renderCounters`, `renderMemberCategorySelections`, ...) + handlers (`openActionModal`, `handleMemberAction`, `goPage`, ...).
- **State** lưu trong biến module-level (`let selectedMemberId`, `let memberCategorySelections = []`, ...).
- Render bảng: build innerHTML cho `tbody-{tab}` (template string), KHÔNG mutate DOM rời rạc.
- Event delegation cho click toàn cục để đóng menu/dropdown:
  ```js
  document.addEventListener("click", (e) => {
    closeAllMenus(); closeDatePicker(); closeCriteriaDropdown(); ...
  });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeActionModal(); ... });
  ```
- Đặt tên hàm action theo verb: `openXxxModal`, `closeXxxModal`, `confirmActionModal`, `goPage(page)`, `goAdd`, `goEdit`, `goDetail`, `switchTab(name)`, `handleMemberAction(action, id)`.
- Truyền tham số chứa text user-input vào `onclick="..."` phải `replace(/'/g, "&#39;")` để tránh vỡ HTML.
- Không gọi API thật — mọi action mock bằng `alert("Đã ...")` hoặc cập nhật state local rồi re-render.

---

## 7. Alert & feedback

- **Confirm hành động** (cần xác nhận trước khi chạy): luôn dùng `action-modal` (mục 5.10), KHÔNG dùng `confirm()`/`alert()`.
- **Validate form / dropdown** (lỗi đầu vào): dùng `alert("...")` tiếng Việt, ngắn, có dấu chấm cuối.
  - Format chuẩn: `"Vui lòng chọn {trường}."` / `"Chỉ được tối đa N {đối tượng}."` / `"{Trường} không được để trống."`.
- **Thông báo đã thực hiện** (sau khi mock xong): `alert("Đã {hành động}.")`.
- **Tooltip** chỉ dùng cho note dài / icon meta, KHÔNG dùng làm thông báo.
- Không dùng `console.log` còn sót, không dùng `prompt()` trừ trường hợp chỉnh ghi chú nhanh inline.

---

## 8. Icon

- Sử dụng SVG inline, KHÔNG icon font.
- Kích thước: 10–12px trong button nhỏ, 14–16px trong button thường, 20–24px trong header/avatar.
- Thuộc tính chuẩn:
  ```html
  <svg width="12" height="12" viewBox="0 0 24 24" fill="none"
       stroke="currentColor" stroke-width="2">...</svg>
  ```
- Bộ icon tham chiếu (đã có trong các file): bell (chuông – Gửi thông báo), trash (xóa), pencil/edit, eye (xem), check, push (Gửi thông báo đẩy), arrow-left, calendar.

---

## 9. Naming convention

- **ID/class HTML**: kebab-case (`vf-main-category-picker`, `tbody-info`, `tab-deleted`).
- **JS function/var**: camelCase (`renderMemberTable`, `selectedMemberId`).
- **Page id**: `page-{slug}` (`page-list`, `page-detail`, `page-form`).
- **Tab id**: `tab-{key}`, panel id: `panel-{key}`.
- **Form input id**: prefix viết tắt theo trang (`vf-` cho virtual member form, `df-` cho doctor form, ...).
- **Action key trong modal map**: kebab-case (`soft-delete`, `hard-delete`, `force-leave`).

---

## 10. Quy tắc khi thêm tính năng mới

1. **Kiểm tra trang mẫu** (`doctor-management.html` / `virtual-member-management.html`) trước — nếu đã có pattern, copy y nguyên class/structure.
2. Chỉ thêm CSS biến thể khi component thực sự khác về ngữ nghĩa; còn lại tái sử dụng class có sẵn.
3. Mọi action confirm đi qua `action-modal` + `actionModalMap` — KHÔNG tự build modal riêng cho từng nút.
4. Mọi nút "Gửi thông báo" / "Gửi thông báo đẩy" dùng đúng SVG bell (toolbar/menu) hoặc SVG push (detail page) — không tự thiết kế icon.
5. Mọi bảng data động render qua JS từ array, KHÔNG hardcode `<tr>` tĩnh trong HTML (trừ trang chưa migrate).
6. Tiếng Việt có dấu, đúng chính tả; thuật ngữ thống nhất:
   - "Thành viên ảo" / "TVA" (virtual member)
   - "Xóa" (soft) / "Xóa vĩnh viễn" (hard) / "Khôi phục"
   - "Tạm khóa" / "Buộc rời bỏ"
   - "Gửi thông báo" (text/menu) / "Gửi thông báo đẩy" (button detail page)
   - "Danh mục chính" / "Danh mục phụ"
7. Khi sửa file: ưu tiên `Edit` (diff nhỏ); không reformat hàng loạt; không tự ý đổi tokens, font, hoặc đảo cấu trúc layout.
8. Sau khi thêm/sửa: kiểm tra (a) tab switch còn hoạt động, (b) modal mở/đóng, (c) bảng render đủ dòng, (d) responsive cuộn ngang, (e) không có ID trùng.

---

## 11. Anti-patterns — KHÔNG làm

- ❌ Thêm framework (Bootstrap, Tailwind, jQuery, React).
- ❌ Inline style dài dòng thay vì class (chỉ inline khi 1-off và ngắn, ví dụ `style="display:flex;gap:8px"`).
- ❌ Hardcode màu hex (`#6c3fc5` ...), phải dùng `var(--primary)`.
- ❌ Dùng `confirm()` / `prompt()` cho action chính (trừ chỉnh ghi chú inline).
- ❌ Tự build modal xác nhận riêng — luôn tái sử dụng `action-modal`.
- ❌ Bỏ `role="dialog"` + `aria-modal="true"` khỏi modal.
- ❌ Đặt text tiếng Anh cho UI hiển thị cho user.
- ❌ Tạo file `.css` / `.js` riêng — toàn bộ inline trong `.html`.
- ❌ Thêm comment dài dòng giải thích code đã rõ; chỉ ghi chú section bằng `/* ====== TÊN ====== */`.

---

## 12. Checklist trước khi commit

- [ ] Dùng đúng tokens trong `:root`, không có hex rời.
- [ ] Mọi button có class `btn` + biến thể; có icon SVG khi cần.
- [ ] Action confirm đi qua `action-modal` + map.
- [ ] Bảng có `table-actions` + `table-wrap` + `table-footer` + pagination.
- [ ] Form có `form-grid` + `form-actions` + nút Hủy/Lưu chuẩn.
- [ ] Page chuyển bằng `goPage()` (toggle `.active`), không reload.
- [ ] Tiếng Việt có dấu, thuật ngữ đồng nhất.
- [ ] Không có ID trùng, không có console.log còn sót.
- [ ] Click ngoài / Escape đóng được mọi popup.
