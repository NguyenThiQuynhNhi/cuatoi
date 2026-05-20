# post-comment-management.md

Tài liệu kỹ thuật cho module **Bài viết. Bình luận** — file `BEAUTY/post-comment-management.html`.

---

## Overview

- **Số trang:** 7
- **Title:** `Bài viết. Bình luận - BEAUTY Admin`
- **Nav-item active trong header:** `Bài viết. Bình luận`
- **Sidebar label:** `Bài viết. Bình luận`

### Sidebar items (7) — thứ tự từ trên xuống

| # | Label | Sidebar id | goSection key | Page id |
|---|---|---|---|---|
| 1 | Bài viết của thành viên thực | `sidebar-posts-real` | `posts-real` | `page-posts-real` *(active mặc định)* |
| 2 | Bài viết Best | `sidebar-posts-best` | `posts-best` | `page-posts-best` |
| 3 | Bài viết đã xóa | `sidebar-posts-deleted` | `posts-deleted` | `page-posts-deleted` |
| 4 | Bài viết đã ẩn | `sidebar-posts-hidden` | `posts-hidden` | `page-posts-hidden` |
| 5 | Bình luận | `sidebar-comments` | `comments` | `page-comments` |
| 6 | Bình luận đã xóa | `sidebar-comments-deleted` | `comments-deleted` | `page-comments-deleted` |
| 7 | Lý do xóa | `sidebar-delete-reason` | `delete-reason` | `page-delete-reason` |

`goSection(section)` toggle `.sidebar-item.active`, toggle `.main.page.active`, gọi `closeAllMenus()`.

### Rule chung toàn module

**Wording chuẩn:**
- `"nổi bật" / "Nổi bật"` → **`Best`** (viết hoa B). Áp dụng cho: tiêu đề trang, sidebar, count, button, menu-item.
- `"Gắn Nổi bật"` → **`Đánh dấu bài viết Best`**
- `"Gỡ nổi bật"` → **`Gỡ Best`**
- `"Tất cả thành viên ▼"` → **`Tất cả cấp bậc ▼`**
- `"Chọn danh mục ▼" + "Di chuyển"` (bulk) → gộp thành 1 button **`Thay đổi danh mục`** mở modal
- `"Nickname"` → **`Tên hiển thị`**
- `"Tựa đề"` → **`Tiêu đề`**
- `"Người đăng"` → **`Người viết`**

**Dropdown tìm kiếm — ID và Tên hiển thị là 2 option riêng (không gộp):**
- Trang 1–4 (posts): `ID | Tên hiển thị | Nội dung tiêu đề | Thẻ`
- Trang 5–6 (comments): `ID | Tên hiển thị | Nội dung bình luận | Tiêu đề bài viết`

**Column order rule:**
- Cột `Tên chuyên mục` **luôn đứng TRƯỚC** cột `Tên danh mục` ở mọi bảng.

**Dropdown đúng theo từng cột:**

| Cột | Trang active (real / best) | Trang deleted / hidden (post) | Trang comments / comments-deleted |
|---|---|---|---|
| Tên chuyên mục | Text thuần | Text thuần | Text thuần |
| Tên danh mục | cell-menu (1 item: "Thay đổi danh mục") | Text thuần | Text thuần |
| Tiêu đề / Nội dung | cell-menu (đa action) | cell-menu (post-hidden) / link (post-deleted) | cell-menu (Xem / Xóa hoặc Xem / Khôi phục) |
| Người viết | cell-menu (đầy đủ) | cell-menu | cell-menu |
| Lượt xem · Lượt thích · Bình luận | Text thuần | — | — |
| Địa chỉ IP | cell-menu (1 item: "Chặn IP") | cell-menu (1 item: "Chặn IP") | cell-menu (1 item: "Chặn IP") |

**Bộ lọc thời gian (dùng chung):** `[Label ngày:] [‹ date-range ›] [Ngày · Tuần (active) · Tháng · Năm · Tất cả]` — sát trái, cùng 1 search-row. KHÔNG dùng "Tự chọn" và KHÔNG có nút date-picker calendar.

**Bộ lọc hàng phải table-actions:** `Tất cả danh mục ▼` + `Tất cả cấp bậc ▼` + `Danh sách 30/50/100 ▼` (số/loại dropdown có thể thay đổi tùy trang).

### Action Modal Map — toàn bộ key (gộp 7 trang)

| Key | Title | Body | Done message |
|---|---|---|---|
| `delete-post` | Xóa bài viết | Bài viết sẽ được chuyển sang mục 'Bài viết đã xóa'. | Đã xóa bài viết. |
| `mark-best` | Đánh dấu bài viết Best | Bài viết sẽ được thêm vào danh sách Best. | Đã đánh dấu Best. |
| `remove-best` | Gỡ Best | Bài viết sẽ bị gỡ khỏi danh sách Best. | Đã gỡ Best. |
| `hide-post` | Tạm ẩn bài viết | Bài viết sẽ tạm ẩn khỏi feed người dùng. | Đã tạm ẩn bài viết. |
| `unfeature-post` | Gỡ khỏi trang chủ | Bài viết sẽ không còn xuất hiện trên trang chủ. | Đã gỡ khỏi trang chủ. |
| `restore-hidden` | Khôi phục bài viết | Bài viết sẽ được khôi phục về danh sách hoạt động. | Đã khôi phục bài viết. |
| `delete-comment` | Xóa bình luận | Bình luận sẽ được chuyển sang mục 'Bình luận đã xóa'. | Đã xóa bình luận. |
| `restore-comment` | Khôi phục bình luận | Bình luận sẽ được khôi phục về danh sách bình luận. | Đã khôi phục bình luận. |
| `block-ip` | Chặn địa chỉ IP | Mọi truy cập từ IP này sẽ bị chặn cho đến khi được mở lại. | Đã chặn IP. |
| `suspend-author` | Tạm khóa hoạt động | Tài khoản người viết sẽ bị tạm khóa cho đến khi được mở lại. | Đã tạm khóa người viết. |
| `force-leave-author` | Buộc rời bỏ hệ thống | Người viết sẽ bị buộc rời khỏi hệ thống ngay lập tức. | Đã buộc rời bỏ. |
| `cancel-upgrade` | Hủy nâng cấp tự động | Tài khoản sẽ ngừng được tự động nâng cấp cấp bậc. | Đã hủy nâng cấp tự động. |
| `notify-author` | Gửi thông báo đẩy | Gửi thông báo đẩy đến người viết bài. | Đã gửi thông báo đẩy. |
| `delete-reason` | Xóa lý do | Lý do này sẽ bị xóa khỏi hệ thống. Các bài viết/bình luận đã dùng lý do này sẽ giữ nguyên. | Đã xóa lý do. |
| `bulk-delete` | Xóa các bài viết đã chọn | Các bài viết sẽ được chuyển sang 'Bài viết đã xóa'. | Đã xóa các bài viết. |
| `bulk-remove-best` | Gỡ Best các bài đã chọn | Các bài viết sẽ bị gỡ khỏi danh sách Best. | Đã gỡ Best. |
| `bulk-restore` | Khôi phục các bài viết đã chọn | Các bài viết sẽ được khôi phục về danh sách hoạt động. | Đã khôi phục bài viết. |
| `bulk-restore-hidden` | Khôi phục các bài đã ẩn | Các bài viết sẽ được hiện lại trên feed và trang chủ. | Đã khôi phục bài viết. |
| `bulk-delete-comment` | Xóa các bình luận đã chọn | Các bình luận sẽ được chuyển sang 'Bình luận đã xóa'. | Đã xóa các bình luận. |
| `bulk-restore-comment` | Khôi phục các bình luận đã chọn | Các bình luận sẽ được khôi phục về danh sách bình luận. | Đã khôi phục bình luận. |

Hành vi chung: `openActionModal(type, id?)` set title/body từ map + lưu `pendingAction`; `closeActionModal()` reset; `confirmActionModal()` → khi `type === "delete-reason"` thì splice khỏi `deleteReasons`; mọi `type` còn lại chỉ `alert(cfg.done)`.

### Modal Thay đổi danh mục (`change-category-modal-backdrop`)

- Title dynamic:
  - Bulk → `Thay đổi danh mục (N bài)` (mở qua `openBulkChangeCategoryModal(target)`)
  - Single → `Thay đổi danh mục bài {id}` (mở qua `openSingleChangeCategoryModal(target, id)`)
- **Bước 1** — chọn danh mục chính: dropdown `#change-main-col` populate từ `Object.keys(postCategoryMap)`. Click option → `selectChangeMain(main)`: set `pendingMain`, reset `pendingSub`, render lại `#change-sub-menu` từ `postCategoryMap[main]`.
- **Bước 2** — chọn danh mục phụ: dropdown `#change-sub-col`. Click option → `selectChangeSub(sub)`: set `pendingSub`.
- `toggleChangeCat('main'|'sub', event)` → mở col, đóng col còn lại.
- **Validate** trong `confirmChangeCategory()`:
  - Nếu chưa chọn `pendingMain` → `alert("Vui lòng chọn danh mục chính.")` + return.
  - Nếu chưa chọn `pendingSub` → `alert("Vui lòng chọn danh mục phụ.")` + return.
  - Hợp lệ → cập nhật `p.mainCat`/`p.subCat` cho các post trong `pendingChangeCat.ids`, re-render bảng tương ứng, đóng modal, `alert("Đã thay đổi danh mục.")`.
- `closeChangeCategoryModal()` đóng backdrop, đóng cả 2 col, reset `pendingChangeCat`.

### Modal View Post / View Comment (`view-modal-backdrop`)

- `viewPost(id)` — tìm post trong `postsReal/postsBest/postsDeleted` qua `findPostById(id)`. Hiển thị: ID, Người viết + cấp bậc (từ `memberGrades`), Chuyên mục, Danh mục, Ngày đăng, IP; content: tiêu đề + nội dung.
- `viewComment(id)` — tìm comment trong `commentsList/commentsDeleted`. Hiển thị: ID, Người viết + cấp bậc, Chuyên mục, Danh mục, Ngày viết, IP; content: "Trên bài viết: ..." + nội dung.
- `closeViewModal()` đóng backdrop.

### Global handlers

- `document.click` → `closeAllMenus()` + đóng tất cả `.change-cat-col.open`.
- `document.keydown` "Escape" → `closeActionModal()` + `closeChangeCategoryModal()` + `closeViewModal()`.
- `toggleMenu(event, menuEl)` toggle `.open` trên cell-menu (cho phép **mở nhiều cell-menu đồng thời**, không tự đóng anh em).

---

## 1. Bài viết của thành viên thực
`id="page-posts-real"` *(active mặc định)*

Page title: `• Bài viết của thành viên thực`

### Bộ lọc thời gian
- Date label: `"Ngày đăng bài viết:"`
- `[‹ date-range ›]` (id `real-date-display`, default `23-06-2025 ~ 30-06-2025`), nav button gọi `shiftDateRange('real', -1|1)`.
- Quick-filter: `Ngày | Tuần (active) | Tháng | Năm | Tất cả` — `setQuickFilter('real', key, this)`.

### Tìm kiếm
- Dropdown options: `ID | Tên hiển thị | Nội dung tiêu đề | Thẻ` — render qua `renderCriteriaMenu('real')`, click option → `selectCriteria('real', label)`.
- Input id: `search-input-real`, placeholder: `"Nhập thông tin"`.
- Button: `"Tìm"` — `alert('Chức năng đang phát triển.')`.

### Bulk action — table-actions
**Trái** (label `"Mục đã chọn:"`):
1. `Thay đổi danh mục` — `btn-outline-primary btn-sm` → `openBulkChangeCategoryModal('real')`
2. `Xóa` — `btn-outline-danger btn-sm` → `bulkAction('real', 'delete')` → modal `bulk-delete`

**Phải:**
1. `Tất cả danh mục ▼` — id `filter-cat-real`, options từ `postCategoryMap`
2. `Tất cả cấp bậc ▼` — id `filter-grade-real`, values: `lv1 | lv2 | lv3 | kol | expert | doctor`
3. `Danh sách 30/50/100 ▼`

Count: `count-real` mặc định `2,345 bài`.

### Bảng danh sách
**Thead (đúng thứ tự):**

`[checkbox] | Tên chuyên mục | Tên danh mục | Tiêu đề | Người viết | Lượt xem | Lượt thích | Bình luận | Địa chỉ IP`

**Từng cột:**

| Cột | Loại | Nội dung / Action |
|---|---|---|
| checkbox | Input checkbox | `toggleRow(this, 'real', id)` / `toggleAll(this, 'tbody-real')` |
| Tên chuyên mục | Text thuần | `post.topic` |
| Tên danh mục | cell-menu | trigger = `mainCat - subCat`, menu 1 item |
| Tiêu đề | cell-menu | trigger = `post.title`, menu 5 item (`renderTitleMenu(p,'real')`) |
| Người viết | cell-menu | trigger = `post.author`, menu 7 item (`renderAuthorMenu`) |
| Lượt xem | Text thuần | `fmtNum(post.views)` |
| Lượt thích | Text thuần | `fmtNum(post.likes)` |
| Bình luận | Text thuần | `fmtNum(post.comments)` |
| Địa chỉ IP | cell-menu | trigger = `post.ip` (font monospace), menu 1 item (`renderIpCell`) |

**cell-menu Tên danh mục — menu-list:**
1. `Thay đổi danh mục` → `openSingleChangeCategoryModal('real', post.id)`

**cell-menu Tiêu đề — menu-list:**
1. `Xem bài viết` → `viewPost(post.id)`
2. `Đánh dấu bài viết Best` → `openActionModal('mark-best', post.id)`
3. `Tạm ẩn bài viết` → `openActionModal('hide-post', post.id)`
4. `Gỡ khỏi trang chủ` → `openActionModal('unfeature-post', post.id)`
5. `<hr class="menu-divider"/>`
6. `Xóa` → `openActionModal('delete-post', post.id)`

**cell-menu Người viết — menu-list:**
1. `Thông tin chi tiết` → `alert('Chức năng đang phát triển.')`
2. `Lịch sử hoạt động` → `alert('Chức năng đang phát triển.')`
3. `Chỉnh sửa thông tin` → `alert('Chức năng đang phát triển.')`
4. `<hr class="menu-divider"/>`
5. `Tạm khóa hoạt động` → `openActionModal('suspend-author', post.id)`
6. `Buộc rời bỏ` → `openActionModal('force-leave-author', post.id)`
7. `Hủy nâng cấp tự động` → `openActionModal('cancel-upgrade', post.id)`
8. `Gửi thông báo đẩy` → `openActionModal('notify-author', post.id)`

**cell-menu Địa chỉ IP — menu-list:**
1. `Chặn IP` → `openActionModal('block-ip', post.id)`

### Action Modal keys dùng trên trang
`mark-best`, `hide-post`, `unfeature-post`, `delete-post`, `suspend-author`, `force-leave-author`, `cancel-upgrade`, `notify-author`, `block-ip`, `bulk-delete`.

### Data fields — `postsReal[]`
`id, topic, mainCat, subCat, title, content, author, views, likes, comments, ip, postedAt`.

---

## 2. Bài viết Best
`id="page-posts-best"`

Page title: `• Bài viết Best`

### Bộ lọc thời gian
- Date label: `"Ngày đăng bài viết:"`
- `[‹ date-range ›]` (id `best-date-display`) — `shiftDateRange('best', ±1)`.
- Quick-filter giống Trang 1 — `setQuickFilter('best', key, this)`.

### Tìm kiếm
- Dropdown options: `ID | Tên hiển thị | Nội dung tiêu đề | Thẻ`.
- Input id: `search-input-best`, placeholder `"Nhập thông tin"`.
- Button `"Tìm"` → alert phát triển.

### Bulk action — table-actions
**Trái:**
1. `Gỡ Best` — `btn-outline-danger btn-sm` → `bulkAction('best', 'remove-best')` → modal `bulk-remove-best`

**Phải:** `Tất cả danh mục ▼` (`filter-cat-best`) + `Tất cả cấp bậc ▼` (`filter-grade-best`) + `Danh sách 30/50/100 ▼`.

Count: `count-best` mặc định `345 bài`.

### Bảng danh sách
**Thead (thứ tự cột KHÁC Trang 1):**

`[checkbox] | Tên chuyên mục | Tên danh mục | Lượt thích | Tiêu đề | Bình luận | Người viết | Địa chỉ IP | Lượt xem`

**Từng cột:**

| Cột | Loại | Nội dung / Action |
|---|---|---|
| checkbox | Input | `toggleRow(this, 'best', id)` |
| Tên chuyên mục | Text thuần | `post.topic` |
| Tên danh mục | cell-menu | giống Trang 1 — `openSingleChangeCategoryModal('best', id)` |
| Lượt thích | Text thuần | `fmtNum(post.likes)` |
| Tiêu đề | cell-menu | trigger = `post.title`, menu **khác Trang 1** (`renderTitleMenu(p,'best')`) |
| Bình luận | Text thuần | `fmtNum(post.comments)` |
| Người viết | cell-menu | Giống Trang 1 (`renderAuthorMenu`) |
| Địa chỉ IP | cell-menu | Giống Trang 1 |
| Lượt xem | Text thuần | `fmtNum(post.views)` |

**cell-menu Tiêu đề — menu-list:**
1. `Xem bài viết` → `viewPost(post.id)`
2. `Gỡ Best` → `openActionModal('remove-best', post.id)`
3. `Tạm ẩn bài viết` → `openActionModal('hide-post', post.id)`
4. `Gỡ khỏi trang chủ` → `openActionModal('unfeature-post', post.id)`
5. `<hr class="menu-divider"/>`
6. `Xóa` → `openActionModal('delete-post', post.id)`

**cell-menu Người viết — menu-list:** Giống Trang 1.

**cell-menu Tên danh mục / Địa chỉ IP — menu-list:** Giống Trang 1.

### Action Modal keys dùng trên trang
`remove-best`, `hide-post`, `unfeature-post`, `delete-post`, `suspend-author`, `force-leave-author`, `cancel-upgrade`, `notify-author`, `block-ip`, `bulk-remove-best`.

### Data fields — `postsBest[]`
Giống `postsReal[]`.

---

## 3. Bài viết đã xóa
`id="page-posts-deleted"`

Page title: `• Bài viết đã xóa`

### Bộ lọc thời gian
- Date label: `"Ngày xóa:"`
- `[‹ date-range ›]` (id `deleted-date-display`) — `shiftDateRange('deleted', ±1)`.
- Quick-filter giống Trang 1 — `setQuickFilter('deleted', key, this)`.

### Tìm kiếm
- Dropdown options: `ID | Tên hiển thị | Nội dung tiêu đề | Thẻ`.
- Input id: `search-input-deleted`, placeholder `"Nhập thông tin"`.
- Button `"Tìm"` → alert phát triển.

### Bulk action — table-actions
**Trái:**
1. `Khôi phục` — `btn-outline-primary btn-sm` → `bulkAction('deleted', 'restore')` → modal `bulk-restore`

**Phải:** `Tất cả danh mục ▼` (`filter-cat-deleted`) + `Tất cả cấp bậc ▼` (`filter-grade-deleted`) + `Danh sách 30/50/100 ▼`.

Count: `count-deleted` mặc định `567 bài`.

### Bảng danh sách
**Thead:**

`[checkbox] | Tên chuyên mục | Tên danh mục | Người viết | Tiêu đề | Địa chỉ IP | Người xử lý | Lý do xóa | Ngày viết | Ngày xóa`

**Từng cột:**

| Cột | Loại | Nội dung / Action |
|---|---|---|
| checkbox | Input | `toggleRow(this, 'deleted', id)` |
| Tên chuyên mục | Text thuần | `post.topic` |
| Tên danh mục | **Text thuần** (KHÔNG cell-menu, bài đã xóa không cho đổi danh mục) | `mainCat - subCat` |
| Người viết | cell-menu | Giống Trang 1 (`renderAuthorMenu`) |
| Tiêu đề | **Link click** (không cell-menu) | `<span class="post-title-link" onclick="viewPost(id)">title</span>` |
| Địa chỉ IP | cell-menu | Giống Trang 1 — menu 1 item `Chặn IP` |
| Người xử lý | Text thuần | `post.handler` |
| Lý do xóa | Text thuần | `post.reason` |
| Ngày viết | Text thuần | `post.postedAt` |
| Ngày xóa | Text thuần | `post.deletedAt` |

### Action Modal keys dùng trên trang
`suspend-author`, `force-leave-author`, `cancel-upgrade`, `notify-author`, `block-ip`, `bulk-restore`.

### Data fields — `postsDeleted[]`
`id, topic, mainCat, subCat, title, content, author, ip, handler, reason, postedAt, deletedAt`.

---

## 4. Bài viết đã ẩn
`id="page-posts-hidden"`

Page title: `• Bài viết đã ẩn`

Trang có **2 sub-tab** dùng `.tabs / .tab` (underline tab, đồng nhất với pattern toàn hệ thống), toggle bằng `switchHiddenSub(sub, btn)`.

### Sub-tabs
1. `Bài viết tạm ẩn` *(active mặc định)* — id `tab-hidden-suspended`, key `suspended`
2. `Gỡ khỏi trang chủ` — id `tab-hidden-unfeatured`, key `unfeatured`

Tabs đặt **bên trong card chứa bảng**, ngay dưới `table-title` và trên `table-actions`. Filter & search nằm trong **card riêng** ở trên (dùng chung cho cả 2 sub-tab).

### Bộ lọc thời gian
- Date label động — id `hidden-date-label`:
  - Sub `suspended` → `"Ngày tạm ẩn:"`
  - Sub `unfeatured` → `"Ngày gỡ bài viết:"`
- `[‹ date-range ›]` (id `hidden-date-display`) — `shiftDateRange('hidden', ±1)`.
- Quick-filter giống Trang 1 — `setQuickFilter('hidden', key, this)`.

### Tìm kiếm
- Dropdown options: `ID | Tên hiển thị | Nội dung tiêu đề | Thẻ`.
- Input id: `search-input-hidden`, placeholder `"Nhập thông tin"`.
- Button `"Tìm"` → alert phát triển.

### Bulk action — table-actions
**Trái:**
1. `Khôi phục` — `btn-outline-primary btn-sm` → `bulkAction('hidden', 'restore')` → modal `bulk-restore-hidden` *(map trong `bulkAction` chuyển `restore` → `bulk-restore-hidden` khi `target === "hidden"`)*

**Phải:** `Tất cả danh mục ▼` (`filter-cat-hidden`) + `Tất cả cấp bậc ▼` (`filter-grade-hidden`) + `Danh sách 30/50/100 ▼`.

Count: `count-hidden` đổi theo sub-tab — `567 bài` / `234 bài`.
Title text: `hidden-title-text` đổi theo sub-tab — `• Bài viết đã ẩn` / `• Bài viết đã gỡ`.

### Bảng danh sách (chung 2 sub-tab, đổi data theo `currentHiddenSub`)

**Thead (cột 8 và 10 đổi label động):**

`[checkbox] | Tên chuyên mục | Tên danh mục | Người viết | Tiêu đề | Địa chỉ IP | Người xử lý | {Lý do ẩn|Lý do gỡ} | Ngày viết | {Ngày ẩn|Ngày gỡ}`

- TH id `hidden-th-reason`: `Lý do ẩn` (suspended) / `Lý do gỡ` (unfeatured)
- TH id `hidden-th-date`: `Ngày ẩn` (suspended) / `Ngày gỡ` (unfeatured)

**Từng cột:**

| Cột | Loại | Nội dung / Action |
|---|---|---|
| checkbox | Input | `toggleRow(this, 'hidden', id)` |
| Tên chuyên mục | Text thuần | `post.topic` |
| Tên danh mục | **Text thuần** (bài đã ẩn — không cho đổi danh mục) | `mainCat - subCat` |
| Người viết | cell-menu | `renderAuthorMenuHidden(p)` — menu 6 item (không có "Chỉnh sửa thông tin" và không có `<hr>`) |
| Tiêu đề | cell-menu | `renderTitleMenuHidden(p)` — menu 2 item |
| Địa chỉ IP | cell-menu | Giống Trang 1 — menu 1 item `Chặn IP` |
| Người xử lý | Text thuần | `post.handler` |
| Lý do ẩn / Lý do gỡ | Text thuần | `post.reason` |
| Ngày viết | Text thuần | `post.datePosted` |
| Ngày ẩn / Ngày gỡ | Text thuần | `post.dateHidden` (suspended) hoặc `post.dateUnfeatured` (unfeatured) — render qua `dateKey` |

**cell-menu Tiêu đề (`renderTitleMenuHidden`) — menu-list:**
1. `Xem bài viết` → `viewPost(post.id)`
2. `Khôi phục` → `openActionModal('restore-hidden', post.id)`

**cell-menu Người viết (`renderAuthorMenuHidden`) — menu-list:**
1. `Thông tin chi tiết` → `alert('Chức năng đang phát triển.')`
2. `Lịch sử hoạt động` → `alert('Chức năng đang phát triển.')`
3. `Tạm khóa hoạt động` → `openActionModal('suspend-author', post.id)`
4. `Buộc rời bỏ` → `openActionModal('force-leave-author', post.id)`
5. `Hủy nâng cấp tự động` → `openActionModal('cancel-upgrade', post.id)`
6. `Gửi thông báo đẩy` → `openActionModal('notify-author', post.id)`

### Action Modal keys dùng trên trang
`restore-hidden`, `suspend-author`, `force-leave-author`, `cancel-upgrade`, `notify-author`, `block-ip`, `bulk-restore-hidden`.

### Data fields
- `postsHiddenSuspended[]`: `id, topic, mainCat, subCat, title, content, author, ip, handler, reason, datePosted, dateHidden`
- `postsHiddenUnfeatured[]`: `id, topic, mainCat, subCat, title, content, author, ip, handler, reason, datePosted, dateUnfeatured`

### Đặc biệt — `switchHiddenSub(sub, btn)`

- Set `currentHiddenSub = sub`.
- Bỏ `.active` mọi `#page-posts-hidden .tab`, thêm `.active` vào `btn` được click.
- `selectedIds.hidden.clear()`.
- Update `hidden-date-label` / `hidden-th-reason` / `hidden-th-date` / `hidden-title-text` / `count-hidden` theo `isSuspended`.
- Gọi `renderTableHidden()` — render từ data tương ứng (`postsHiddenSuspended` hoặc `postsHiddenUnfeatured`), với `dateKey = "dateHidden" | "dateUnfeatured"`.

---

## 5. Bình luận
`id="page-comments"`

Page title: `• Bình luận`

### Bộ lọc thời gian
- Date label: `"Ngày viết bình luận:"`
- `[‹ date-range ›]` (id `comments-date-display`) — `shiftDateRange('comments', ±1)`.
- Quick-filter giống Trang 1 — `setQuickFilter('comments', key, this)`.

### Tìm kiếm
- Dropdown options: `ID | Tên hiển thị | Nội dung bình luận | Tiêu đề bài viết`.
- Input id: `search-input-comments`, placeholder `"Nhập thông tin"`.
- Button `"Tìm"` → alert phát triển.

### Bulk action — table-actions
**Trái:**
1. `Xóa` — `btn-outline-danger btn-sm` → `bulkAction('comments', 'delete-comment')` → modal `bulk-delete-comment`

**Phải:** `Tất cả danh mục ▼` (`filter-cat-comments`) + `Tất cả cấp bậc ▼` (`filter-grade-comments`) + `Danh sách 30/50/100 ▼`.

Count: `count-comments` mặc định `6,456 bình luận`.

### Bảng danh sách
**Thead:**

`[checkbox] | Tên chuyên mục | Tên danh mục | Người viết | Nội dung | Ngày viết | Địa chỉ IP`

**Từng cột:**

| Cột | Loại | Nội dung / Action |
|---|---|---|
| checkbox | Input | `toggleRow(this, 'comments', id)` |
| Tên chuyên mục | Text thuần | `c.topic` |
| Tên danh mục | **Text thuần** (bình luận — không cho đổi danh mục) | `mainCat - subCat` |
| Người viết | cell-menu | `renderAuthorMenuComment(c)` — menu 6 item (không có "Chỉnh sửa thông tin", không có `<hr>`) |
| Nội dung | cell-menu | `renderContentMenuComment(c, "active")` — trigger là `content` truncate 50 ký tự (class `content-ellipsis`, có `title` tooltip full) |
| Ngày viết | Text thuần | `c.date` |
| Địa chỉ IP | cell-menu | Giống Trang 1 — menu 1 item `Chặn IP` |

**cell-menu Người viết — menu-list:**
1. `Thông tin chi tiết` → `alert('Chức năng đang phát triển.')`
2. `Lịch sử hoạt động` → `alert('Chức năng đang phát triển.')`
3. `Tạm khóa hoạt động` → `openActionModal('suspend-author', c.id)`
4. `Buộc rời bỏ` → `openActionModal('force-leave-author', c.id)`
5. `Hủy nâng cấp tự động` → `openActionModal('cancel-upgrade', c.id)`
6. `Gửi thông báo đẩy` → `openActionModal('notify-author', c.id)`

**cell-menu Nội dung (mode `"active"`) — menu-list:**
1. `Xem bình luận` → `viewComment(c.id)`
2. `Xóa` → `openActionModal('delete-comment', c.id)`

### Action Modal keys dùng trên trang
`delete-comment`, `suspend-author`, `force-leave-author`, `cancel-upgrade`, `notify-author`, `block-ip`, `bulk-delete-comment`.

### Data fields — `commentsList[]`
`id, topic, mainCat, subCat, postTitle, content, author, ip, date`.

---

## 6. Bình luận đã xóa
`id="page-comments-deleted"`

Page title: `• Bình luận đã xóa`

### Bộ lọc thời gian
- Date label: `"Ngày xóa:"`
- `[‹ date-range ›]` (id `cdeleted-date-display`) — `shiftDateRange('cdeleted', ±1)`.
- Quick-filter giống Trang 1 — `setQuickFilter('cdeleted', key, this)`.

### Tìm kiếm
- Dropdown options: `ID | Tên hiển thị | Nội dung bình luận | Tiêu đề bài viết`.
- Input id: `search-input-cdeleted`, placeholder `"Nhập thông tin"`.
- Button `"Tìm"` → alert phát triển.

### Bulk action — table-actions
**Trái:**
1. `Khôi phục` — `btn-outline-primary btn-sm` → `bulkAction('cdeleted', 'restore-comment')` → modal `bulk-restore-comment`

**Phải:** **KHÔNG có** `Tất cả danh mục ▼` (khác các trang khác). Chỉ có `Tất cả cấp bậc ▼` (`filter-grade-cdeleted`) + `Danh sách 30/50/100 ▼`.

Count: `count-cdeleted` mặc định `3,234 bình luận`.

### Bảng danh sách
**Thead:**

`[checkbox] | Tên chuyên mục | Tên danh mục | Nội dung bình luận | Người viết | Địa chỉ IP | Người xử lý | Lý do xóa | Ngày xóa`

**Từng cột:**

| Cột | Loại | Nội dung / Action |
|---|---|---|
| checkbox | Input | `toggleRow(this, 'cdeleted', id)` |
| Tên chuyên mục | Text thuần | `c.topic` |
| Tên danh mục | Text thuần | `mainCat - subCat` |
| Nội dung bình luận | cell-menu | `renderContentMenuComment(c, "deleted")` — trigger truncate 50 ký tự + tooltip full |
| Người viết | cell-menu | `renderAuthorMenuCommentDeleted(c)` — menu **5 item** (bỏ "Hủy nâng cấp tự động" so với Trang 5) |
| Địa chỉ IP | cell-menu | Giống Trang 1 — menu 1 item `Chặn IP` |
| Người xử lý | Text thuần | `c.handler` |
| Lý do xóa | Text thuần | `c.reason` |
| Ngày xóa | Text thuần | `c.dateDeleted` |

**cell-menu Nội dung bình luận (mode `"deleted"`) — menu-list:**
1. `Xem bình luận` → `viewComment(c.id)`
2. `Khôi phục` → `openActionModal('restore-comment', c.id)`

**cell-menu Người viết — menu-list:**
1. `Thông tin chi tiết` → `alert('Chức năng đang phát triển.')`
2. `Lịch sử hoạt động` → `alert('Chức năng đang phát triển.')`
3. `Tạm khóa hoạt động` → `openActionModal('suspend-author', c.id)`
4. `Buộc rời bỏ` → `openActionModal('force-leave-author', c.id)`
5. `Gửi thông báo đẩy` → `openActionModal('notify-author', c.id)`

### Action Modal keys dùng trên trang
`restore-comment`, `suspend-author`, `force-leave-author`, `notify-author`, `block-ip`, `bulk-restore-comment`.

### Data fields — `commentsDeleted[]`
`id, topic, mainCat, subCat, postTitle, content, author, ip, handler, reason, dateDeleted`.

---

## 7. Lý do xoá
`id="page-delete-reason"`

Page title: `• Lý do xoá`

**KHÔNG có** date filter, **KHÔNG có** quick-filter, **KHÔNG có** search row.

### Khu vực thêm/sửa (`.reason-input-row`)
- Input id `reason-input`, class `reason-input` (nền `--success-light`, viền `--success`), placeholder `"Nhập lý do xoá"`. Sự kiện:
  - `oninput="handleReasonInputChange()"`: nếu đang edit (`editingReasonId` ≠ null) và input rỗng → `resetReasonEditor()`.
  - `onkeydown="handleReasonKey(event)"`: Escape → `resetReasonEditor()`; Enter → `submitReason()`.
- Button id `reason-submit-btn`, class `btn btn-primary`. Text:
  - Mode thêm mới → `"Thêm"`
  - Mode đang sửa → `"Cập nhật"`
  - Click → `submitReason()`.

### Bảng danh sách lý do
**Thead (3 cột — không có checkbox, không có bulk):**

`Lý do xóa | Quản lý | Người tạo`

**Từng cột:**

| Cột | Loại | Nội dung / Action |
|---|---|---|
| Lý do xóa | Chip clickable | `<button class="reason-chip">reason</button>` (highlight `.editing` khi đang sửa). Click → `editReason(r.id)`. |
| Quản lý | Button | `Xóa` — `btn-outline-danger btn-sm` → `openActionModal('delete-reason', r.id)` |
| Người tạo | Text thuần | `r.creator` |

Count: `count-reason` cập nhật động `${deleteReasons.length} lý do`.

### Action Modal keys dùng trên trang
- `delete-reason` — khi confirm sẽ xoá item khỏi `deleteReasons`, nếu đang edit chính item đó thì `resetReasonEditor()`, còn không thì `renderReasonTable()`.

### Data fields — `deleteReasons[]`
`id, reason, creator`.

Data seed:
```
R001 | Vi phạm điều lệ cộng đồng | Admin
R002 | Spam quảng cáo            | maimai
R003 | Nội dung không phù hợp    | Admin
R004 | Dẫn link bên ngoài        | chikihong
```

### Đặc biệt — Logic chip editor

**`editReason(id)`** (click chip):
1. Tìm reason theo id; nếu không có → return.
2. Set `editingReasonId = id`.
3. `reason-input.value = r.reason` + `.classList.add("editing")` + focus.
4. Đổi text `reason-submit-btn` thành `"Cập nhật"`.
5. Re-render bảng (chip đang edit có class `.editing`).

**`submitReason()`** (click nút hoặc nhấn Enter):
- Trim input. Rỗng → `alert("Vui lòng nhập lý do.")` + return.
- Nếu `editingReasonId` ≠ null → update `r.reason`, `alert("Đã cập nhật lý do.")`, gọi `resetReasonEditor()`.
- Nếu thêm mới → tạo `nextId = "R" + (max-id-number + 1).padStart(3,"0")`, `unshift({id, reason: text, creator: "Admin"})`, clear input, `alert("Đã thêm lý do.")`, re-render.

**`resetReasonEditor()`**:
- `editingReasonId = null`.
- Clear `reason-input.value`, bỏ class `editing`.
- Đổi text nút về `"Thêm"`.
- Re-render bảng.

**`handleReasonInputChange()`**:
- Nếu đang edit + input rỗng → `resetReasonEditor()` (tự thoát mode sửa).

**`handleReasonKey(event)`**:
- `Escape` → `resetReasonEditor()`.
- `Enter` → `submitReason()`.
