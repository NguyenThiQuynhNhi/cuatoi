# Admin Portal Mockup - Full Function and Component Reference

Tài liệu này mô tả chi tiết toàn bộ chức năng và thành phần đang có trong website mockup admin portal.

Nguon giao dien: admin_portal_mockup.html

## 1) Tong quan he thong

- Loai: Single-page mockup, khong dung framework.
- Nen tang: HTML + CSS + JavaScript thuan.
- Co che chinh:
  - Dieu huong theo screen bang class active.
  - Dieu huong tab trong tung card bang data-tab-target va data-tab-panel.
  - Layout co sidebar trai, topbar tren, noi dung o giua.

## 2) Cau truc tong the cua trang

- Portal shell:
  - Sidebar: menu module chinh.
  - Main:
    - Topbar: title, top search, quick actions.
    - Content: danh sach man hinh screen.
- Welcome modal:
  - Hien popup cau hinh area unit va currency.

## 3) Danh sach man hinh hien co

Tat ca man hinh duoc dieu khien bang id dang screen-tenmanhinh:

1. screen-dashboard
2. screen-users
3. screen-agents
4. screen-content
5. screen-properties
6. screen-ads
7. screen-payments
8. screen-analytics
9. screen-leads
10. screen-messages
11. screen-contacts
12. screen-projects
13. screen-offers
14. screen-agreements
15. screen-calendar
16. screen-feature-control
17. screen-admin-accounts
18. screen-profile
19. screen-settings

## 4) Chi tiet chuc nang theo man hinh

### 4.1 Dashboard

- KPI grid:
  - Total end users
  - Registered agents
  - Active listings
  - MRR
  - DAU, WAU, MAU
  - Avg session time
- Chart mini:
  - DAU 7 ngay
  - Phan bo plan agent
- Bang xep hang agent:
  - Ranking, listing, sales, ad spend, rating, status
  - Action: View, Edit, Suspend

### 4.2 Users

- Filter:
  - Type, location, status
- KPI:
  - Buyers/Renters, Sellers, Support accounts
- Bang Registered users:
  - User info, type, location, registered, activity, inquiries, saved, status
  - Action: View, Edit, Suspend, Restore

### 4.3 Agents

- Muc duyet agent:
  - Pending, Approved, Rejected tabs
- Bang approvals:
  - Company, contact da mask, location, submit date, masked license, coverage, access scope
  - Action: Approve, Reject
- Rule quyen rieng tu:
  - Aggregate only voi du lieu nhay cam

### 4.4 Content

- Module CMS va bai viet:
  - Tabs: All content, Pending, Flagged, Static pages, Homepage CMS
- Bang content:
  - Category, author, publish date, views, status
- Static pages and legal docs:
  - Privacy Policy, Terms, Specified Commercial Transaction Law

### 4.5 Property Oversight

- Filter:
  - Type, prefecture, status
- KPI:
  - Total listings, flagged, avg listing age
- Bang property:
  - Property, agent, type, price, listed date, views, saves, status
  - Action: View, Suspend, Review, Delete, Archive

### 4.6 Ad Management

- Tabs:
  - Sponsored properties, Banner ads, Sponsored articles
- Pending approval list
- Live ad performance:
  - IMP, CL, CTR, CV, CVR, spend, status

### 4.7 Payment Reports

- KPI doanh thu:
  - Subscription, ad revenue, paid features, total
- Revenue breakdown by type
- Monthly trend chart
- Billing management:
  - Contract, monthly billing, payment method, next invoice, status

### 4.8 Analytics

- Funnel:
  - Impressions den contact
- User demographics:
  - Nationality split
- Top areas by property views:
  - Area performance, trend

### 4.9 Lead Oversight

- Rule governance:
  - Chi xem metadata/status/audit, khong xem noi dung chat private
- Filter:
  - Inquiry type, status, potential
- Bang lead:
  - Assigned agent, next follow-up, violations
  - Action: Audit log, Warn, Lock

### 4.10 Messages and Emails

- Tabs:
  - Client notifications
  - Agent/support notifications
  - Template library
  - Live chat
- Client notifications:
  - Segment, channel, schedule, open/click rate
- Agent notifications:
  - Flow SLA, delivered, errors
- Template library:
  - Theo account type va compliance
- Live chat support console:
  - Danh sach hoi thoai trai
  - Khung chat phai voi lich su tin nhan
  - O nhap va nut Send
  - Chi support channels, khong mo private agent-client chat

### 4.11 Contacts

- Filter:
  - Country, nationality, city, assigned
- Bang contacts oversight:
  - Ref, initials, organisation, assigned, activities read-only

### 4.12 Projects

- Danh sach du an phat trien moi
- Trang thai project
- So property linked
- Action detail

### 4.13 Offers

- Quan ly offer lien ket lead va property
- Stage workflow va ngay cap nhat

### 4.14 Agreements

- Danh dau Phase 2 or TBD
- Mo ta huong xu ly sat nhap hoac tach module

### 4.15 Calendar and Activity

- Read-only oversight
- Tabs: Viewing, Task, Call, Email, SMS, Comments
- SLA va audit log

### 4.16 Feature Control

- Feature matrix theo plan:
  - Basic, Standard, Premium
  - Per-account override
- Policy side panel:
  - Auto renew reminders, cancellation priority, usage counters

### 4.17 Admin Accounts

- KPI admin staff
- Bang staff account:
  - Role, 2FA, last login, session policy, status
- Action:
  - Operation log, create admin

### 4.18 Profile

- Profile and security:
  - Display name, email, language, timezone, 2FA
- Authentication policy:
  - Username/password, forgot password OTP, auto logout old session, password policy

### 4.19 Settings

Settings su dung tab panel thuc su:

- Basic:
  - Currency, language, timezone, area unit, saved limits
- Security:
  - Password min length, complexity, 2FA required, session timeout, second login behavior
- Integrations:
  - Payment gateway, maps, CRM sync, message relay
- Region and Taxonomy:
  - Prefecture/city, railway/station, article/video categories
- Admin accounts:
  - Available roles, create account, permission model, log retention

## 5) Component catalog chi tiet

### 5.1 Layout and navigation components

- portal: container tong
- sidebar: menu trai
- sidebar-header, logo-mark, logo-text, logo-badge
- nav-section, nav-label, nav-item, nav-icon, nav-badge
- sidebar-footer, avatar, avatar-name, avatar-role
- main, topbar, page-title
- search-box, search-shortcuts, saved-pill
- topbar-actions, icon-btn, notif-dot
- content, screen

### 5.2 Data display components

- kpi-grid, kpi-card, kpi-label, kpi-value, kpi-change
- charts-row
- card, card-title, card-sub
- mini-chart, bar-col, bar, bar-lbl
- donut-wrap, donut-legend, legend-row, legend-dot, legend-val
- table-wrap, table, th, td
- badge system:
  - badge-success, badge-warning, badge-danger, badge-info, badge-gray

### 5.3 Interaction and form components

- section-header, section-title
- tabs, tab, tab-panel
- filter-bar, filter-select
- row-actions
- btn-sm, btn-primary, btn-danger
- field-row, field-label, field-value
- progress-bar, progress-fill
- breadcrumb
- detail-grid, split-grid, stack
- hint, oos-note, masked

### 5.4 Timeline and utility components

- timeline, timeline-item
- t-dot, t-content, t-title, t-time

### 5.5 Chat components

- chat-layout
- chat-list, chat-item, chat-title, chat-meta
- chat-window, chat-header, chat-body
- bubble left, bubble right
- chat-compose

### 5.6 Welcome modal components

- welcome-modal
- welcome-card
- welcome-title
- welcome-desc

## 6) JavaScript function reference

1. switchScreen(id, el)

- Muc dich: chuyen man hinh trong SPA.
- Xu ly:
  - remove active tat ca screen
  - remove active tat ca nav-item
  - add active cho screen dich va menu duoc click
  - cap nhat page title theo PAGE_TITLES

2. switchTab(el, group)

- Muc dich: chuyen tab trong card.
- Xu ly:
  - remove active tat ca tab trong cung tabs container
  - add active cho tab click
  - lay data-tab-target
  - tim tab-panel tuong ung bang data-tab-panel
  - hien panel dung, an panel khac

3. openProfile()

- Muc dich: mo nhanh man Profile tu icon topbar.
- Xu ly: tim nav item profile va goi switchScreen.

4. verifyWelcomeConfig()

- Muc dich: xac nhan area unit va currency o welcome modal.
- Xu ly: doc gia tri select, alert ket qua, dong modal.

5. dismissWelcome()

- Muc dich: dong welcome modal.
- Xu ly: add class hidden cho welcome-modal.

6. Nav active click listener

- Muc dich: dam bao item dang click duoc danh dau active.
- Xu ly: event listener tren tat ca nav-item.

## 7) Bang map PAGE_TITLES

- dashboard: KPI Dashboard
- users: User Management
- agents: Agent Approvals
- leads: Lead Oversight
- messages: Messages and Emails
- content: CMS and Articles
- properties: Property Oversight
- ads: Ad Management
- payments: Payment Reports
- analytics: Market Analysis
- contacts: Contacts and Organisations
- projects: Projects Oversight
- offers: Offers Oversight
- agreements: Agreements Oversight
- calendar: Calendar and Activities (Read-only)
- feature-control: Per-Account Feature Control
- admin-accounts: Administrator Account Management
- profile: Admin Profile
- settings: System Settings

## 8) Quyen va privacy rules da the hien trong UI

- Admin chi xem aggregate voi mot so du lieu agent nhay cam (masked contact, masked license).
- Lead module va Contacts module dat note privacy ro rang.
- Messaging module:
  - Co support chat console cho admin-agent/client
  - Khong mo private chat giua agent-client

## 9) Responsive behavior

- Breakpoint 900px:
  - Sidebar thu gon thanh icon
  - Grid chuyen 1 cot cho nhieu khu vuc
  - Chat layout chuyen 1 cot
- Breakpoint 600px:
  - KPI va stat grid toi uu cho mobile

## 10) Cach mo rong tiep theo de san sang production

1. Tach du lieu mau thanh JSON hoac API layer.
2. Them state manager cho screen va tab, bo inline onclick.
3. Bo sung i18n va format date/currency theo locale.
4. Them validation, debounce search, pagination cho bang lon.
5. Them RBAC that su theo role (Super Admin, Ops, Finance, Viewer).
6. Doi chat mock thanh websocket hoac realtime provider.
7. Them test UI (visual regression) va test interaction.

## 11) Ghi chu files lien quan trong workspace

- admin_portal_mockup.html: file mockup chinh admin portal
- Scope.html: tai lieu scope tham khao trong workspace
- UI Implementation Confirmation.csv: doi soat implementation

End of document.
