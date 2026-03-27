(function () {
  const ENTERPRISE_PAGE_TITLES = {
    "ad-campaign-detail": "Ad Campaign Detail",
    "ad-slot-inventory": "Ad Slot & Inventory Management",
    "ad-pricing-rules": "Ad Pricing Rules",
    "ad-policy-logs": "Ad Policy & Rejection Logs",
    "cms-version-history": "Content Version History",
    "editorial-workflow-settings": "Editorial Workflow Settings",
    "content-visibility-rules": "Content Visibility Rules",
    "taxonomy-tag-manager": "Taxonomy & Tag Manager",
    "taxonomy-manager": "Taxonomy Manager",
    "geo-hierarchy-manager": "Geo Hierarchy Manager",
    "transport-manager": "Transport Manager",
    "enum-config-editor": "Enumeration Config Editor",
    "data-access-policy": "Data Access Policy",
    "export-audit-log": "Export Audit Log",
    "pii-visibility-config": "PII Visibility Configuration",
    "staff-performance-dashboard": "Staff Performance Dashboard",
    "sla-escalation-rules": "SLA & Escalation Rules",
    "internal-notes-system": "Internal Notes",
    "api-key-token-management": "API Key / Token Management",
    "webhook-logs": "Webhook Logs",
    "integration-lifecycle-status": "Integration Lifecycle Status",
  };

  const ENTERPRISE_NAV_HTML = `
    <div class="nav-section" data-enterprise-nav="ads">
      <div class="nav-label">Ad Lifecycle</div>
      <div class="nav-item" onclick="switchScreen('ad-campaign-detail', this)" title="Ad Campaign Detail">
        <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M1 3h13v2H1zM2 6h11v6H2z"/></svg>
        <span>Ad Campaign Detail</span>
      </div>
      <div class="nav-item" onclick="switchScreen('ad-slot-inventory', this)" title="Ad Slot & Inventory Management">
        <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M1 2h6v5H1zM8 2h6v5H8zM1 8h6v5H1zM8 8h6v5H8z"/></svg>
        <span>Ad Slot & Inventory</span>
      </div>
      <div class="nav-item" onclick="switchScreen('ad-pricing-rules', this)" title="Ad Pricing Rules">
        <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M2 2h11v2H2zM2 6h8v2H2zM2 10h6v2H2z"/></svg>
        <span>Ad Pricing Rules</span>
      </div>
      <div class="nav-item" onclick="switchScreen('ad-policy-logs', this)" title="Ad Policy & Rejection Logs">
        <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M3 1h9v13H3z"/></svg>
        <span>Ad Policy Logs</span>
      </div>
    </div>

    <div class="nav-section" data-enterprise-nav="cms-advanced">
      <div class="nav-label">CMS Advanced</div>
      <div class="nav-item" onclick="switchScreen('cms-version-history', this)" title="Content Version History"><span>Version History</span></div>
      <div class="nav-item" onclick="switchScreen('editorial-workflow-settings', this)" title="Editorial Workflow Settings"><span>Workflow Settings</span></div>
      <div class="nav-item" onclick="switchScreen('content-visibility-rules', this)" title="Content Visibility Rules"><span>Visibility Rules</span></div>
      <div class="nav-item" onclick="switchScreen('taxonomy-tag-manager', this)" title="Taxonomy & Tag Manager"><span>Taxonomy & Tags</span></div>
    </div>

    <div class="nav-section" data-enterprise-nav="master-data">
      <div class="nav-label">Master Data</div>
      <div class="nav-item" onclick="switchScreen('taxonomy-manager', this)" title="Taxonomy Manager"><span>Taxonomy Manager</span></div>
      <div class="nav-item" onclick="switchScreen('geo-hierarchy-manager', this)" title="Geo Hierarchy Manager"><span>Geo Hierarchy</span></div>
      <div class="nav-item" onclick="switchScreen('transport-manager', this)" title="Transport Manager"><span>Transport Manager</span></div>
      <div class="nav-item" onclick="switchScreen('enum-config-editor', this)" title="Enumeration Config Editor"><span>Enum Config Editor</span></div>
    </div>

    <div class="nav-section" data-enterprise-nav="compliance">
      <div class="nav-label">Compliance</div>
      <div class="nav-item" onclick="switchScreen('data-access-policy', this)" title="Data Access Policy"><span>Data Access Policy</span></div>
      <div class="nav-item" onclick="switchScreen('export-audit-log', this)" title="Export Audit Log"><span>Export Audit Log</span></div>
      <div class="nav-item" onclick="switchScreen('pii-visibility-config', this)" title="PII Visibility Configuration"><span>PII Visibility</span></div>
    </div>

    <div class="nav-section" data-enterprise-nav="ops">
      <div class="nav-label">Ops Tooling</div>
      <div class="nav-item" onclick="switchScreen('staff-performance-dashboard', this)" title="Staff Performance Dashboard"><span>Staff Performance</span></div>
      <div class="nav-item" onclick="switchScreen('sla-escalation-rules', this)" title="SLA & Escalation Rules"><span>SLA & Escalation</span></div>
      <div class="nav-item" onclick="switchScreen('internal-notes-system', this)" title="Internal Notes"><span>Internal Notes</span></div>
    </div>

    <div class="nav-section" data-enterprise-nav="integration-advanced">
      <div class="nav-label">Integration Adv.</div>
      <div class="nav-item" onclick="switchScreen('api-key-token-management', this)" title="API Key / Token Management"><span>API Keys / Tokens</span></div>
      <div class="nav-item" onclick="switchScreen('webhook-logs', this)" title="Webhook Logs"><span>Webhook Logs</span></div>
      <div class="nav-item" onclick="switchScreen('integration-lifecycle-status', this)" title="Integration Lifecycle Status"><span>Lifecycle Status</span></div>
    </div>
  `;

  const ENTERPRISE_FALLBACK_SCREENS_HTML = `
    <div class="screen" id="screen-ad-campaign-detail"><div class="card"><div class="section-title">Ad Campaign Detail</div></div></div>
    <div class="screen" id="screen-ad-slot-inventory"><div class="card"><div class="section-title">Ad Slot & Inventory Management</div></div></div>
    <div class="screen" id="screen-ad-pricing-rules"><div class="card"><div class="section-title">Ad Pricing Rules</div></div></div>
    <div class="screen" id="screen-ad-policy-logs"><div class="card"><div class="section-title">Ad Policy & Rejection Logs</div></div></div>
    <div class="screen" id="screen-cms-version-history"><div class="card"><div class="section-title">Content Version History</div></div></div>
    <div class="screen" id="screen-editorial-workflow-settings"><div class="card"><div class="section-title">Editorial Workflow Settings</div></div></div>
    <div class="screen" id="screen-content-visibility-rules"><div class="card"><div class="section-title">Content Visibility Rules</div></div></div>
    <div class="screen" id="screen-taxonomy-tag-manager"><div class="card"><div class="section-title">Taxonomy & Tag Manager</div></div></div>
    <div class="screen" id="screen-taxonomy-manager"><div class="card"><div class="section-title">Taxonomy Manager</div></div></div>
    <div class="screen" id="screen-geo-hierarchy-manager"><div class="card"><div class="section-title">Geo Hierarchy Manager</div></div></div>
    <div class="screen" id="screen-transport-manager"><div class="card"><div class="section-title">Transport Manager</div></div></div>
    <div class="screen" id="screen-enum-config-editor"><div class="card"><div class="section-title">Enumeration Config Editor</div></div></div>
    <div class="screen" id="screen-data-access-policy"><div class="card"><div class="section-title">Data Access Policy</div></div></div>
    <div class="screen" id="screen-export-audit-log"><div class="card"><div class="section-title">Export Audit Log</div></div></div>
    <div class="screen" id="screen-pii-visibility-config"><div class="card"><div class="section-title">PII Visibility Configuration</div></div></div>
    <div class="screen" id="screen-staff-performance-dashboard"><div class="card"><div class="section-title">Staff Performance Dashboard</div></div></div>
    <div class="screen" id="screen-sla-escalation-rules"><div class="card"><div class="section-title">SLA & Escalation Rules</div></div></div>
    <div class="screen" id="screen-internal-notes-system"><div class="card"><div class="section-title">Internal Notes</div></div></div>
    <div class="screen" id="screen-api-key-token-management"><div class="card"><div class="section-title">API Key / Token Management</div></div></div>
    <div class="screen" id="screen-webhook-logs"><div class="card"><div class="section-title">Webhook Logs</div></div></div>
    <div class="screen" id="screen-integration-lifecycle-status"><div class="card"><div class="section-title">Integration Lifecycle Status</div></div></div>
  `;

  const adCreativeVersions = [
    {
      version: "v1.0",
      size: "1200x628",
      format: "PNG",
      by: "Admin Tanaka",
      at: "2026-03-20",
      status: "Approved",
    },
    {
      version: "v1.1",
      size: "1080x1080",
      format: "JPG",
      by: "Ops Sato",
      at: "2026-03-22",
      status: "Submitted",
    },
    {
      version: "v2.0",
      size: "300x250",
      format: "GIF",
      by: "Admin Tanaka",
      at: "2026-03-24",
      status: "Draft",
    },
  ];

  const adSlotInventory = [
    {
      slot: "Home",
      placement: "Top Hero",
      capacity: 4,
      booked: 4,
      conflict: "Conflict",
      next: "2026-03-31",
    },
    {
      slot: "Listing",
      placement: "Search Grid",
      capacity: 8,
      booked: 6,
      conflict: "Clear",
      next: "Now",
    },
    {
      slot: "Detail",
      placement: "Property Sidebar",
      capacity: 6,
      booked: 6,
      conflict: "Conflict",
      next: "2026-03-29",
    },
    {
      slot: "Article",
      placement: "In-article Banner",
      capacity: 5,
      booked: 2,
      conflict: "Clear",
      next: "Now",
    },
  ];

  const adPricingRules = [
    {
      id: "PR-100",
      model: "CPM",
      slot: "Home",
      seg: "All",
      base: 4200,
      status: "Active",
    },
    {
      id: "PR-120",
      model: "CPC",
      slot: "Listing",
      seg: "Premium",
      base: 180,
      status: "Active",
    },
    {
      id: "PR-140",
      model: "Flat",
      slot: "Article",
      seg: "All",
      base: 50000,
      status: "Draft",
    },
  ];

  const cmsVersions = [
    {
      v: "v1.0",
      st: "Published",
      a: "Author A",
      r: "Reviewer B",
      p: "Publisher C",
      t: "2026-03-01 10:30",
    },
    {
      v: "v1.1",
      st: "Approved",
      a: "Author A",
      r: "Reviewer D",
      p: "Publisher C",
      t: "2026-03-10 09:05",
    },
    {
      v: "v1.2",
      st: "Review",
      a: "Author E",
      r: "Reviewer D",
      p: "-",
      t: "2026-03-25 12:11",
    },
  ];

  const transportRows = [
    {
      line: "Yamanote Line",
      station: "Shinjuku",
      city: "Tokyo",
      status: "Active",
    },
    {
      line: "Midosuji Line",
      station: "Umeda",
      city: "Osaka",
      status: "Active",
    },
    { line: "Tozai Line", station: "Nijo", city: "Kyoto", status: "Review" },
  ];

  const exportAuditRows = [
    {
      when: "2026-03-24 10:21",
      actor: "Admin Tanaka",
      module: "Reports",
      scope: "Agent aggregate",
      reason: "Monthly board pack",
      result: "Approved",
    },
    {
      when: "2026-03-23 16:40",
      actor: "Ops Sato",
      module: "Leads",
      scope: "Assigned leads",
      reason: "Escalation follow-up",
      result: "Approved",
    },
    {
      when: "2026-03-22 09:15",
      actor: "Staff A",
      module: "Messages",
      scope: "Segment metrics",
      reason: "Campaign QA",
      result: "Approved",
    },
  ];

  const notesRows = [
    {
      when: "2026-03-25 11:20",
      entity: "Agent AG-1002",
      note: "Requested pricing override due to seasonal campaign.",
      author: "Ops Sato",
      visibility: "Internal only",
    },
  ];

  const apiTokenRows = [
    {
      agent: "Tokyo Sumai",
      id: "tok_01A9",
      scope: "listing.read,lead.write",
      limit: "300 req/min",
      status: "Enabled",
      last: "2026-03-25 15:42",
    },
    {
      agent: "Osaka Estate",
      id: "tok_77X2",
      scope: "listing.read",
      limit: "120 req/min",
      status: "Disabled",
      last: "2026-03-19 09:12",
    },
  ];

  const webhookRows = [
    {
      time: "2026-03-25 15:10",
      event: "lead.created",
      endpoint: "/hooks/crm",
      response: "201",
      latency: "120ms",
      retries: 0,
    },
    {
      time: "2026-03-25 15:06",
      event: "listing.updated",
      endpoint: "/hooks/search",
      response: "502",
      latency: "890ms",
      retries: 2,
    },
    {
      time: "2026-03-25 14:58",
      event: "ticket.escalated",
      endpoint: "/hooks/ops",
      response: "204",
      latency: "90ms",
      retries: 0,
    },
  ];

  function extendPageTitles() {
    if (typeof PAGE_TITLES !== "undefined") {
      Object.assign(PAGE_TITLES, ENTERPRISE_PAGE_TITLES);
    }
  }

  function injectEnterpriseNav() {
    const sidebar = document.querySelector(".sidebar");
    const footer = document.querySelector(".sidebar-footer");
    if (!sidebar || !footer) return;
    if (sidebar.querySelector('[data-enterprise-nav="ads"]')) return;

    const wrap = document.createElement("div");
    wrap.innerHTML = ENTERPRISE_NAV_HTML;
    Array.from(wrap.children).forEach((section) =>
      sidebar.insertBefore(section, footer),
    );

    sidebar.querySelectorAll(".nav-item").forEach((item) => {
      if (item.dataset.enterpriseBound === "1") return;
      item.dataset.enterpriseBound = "1";
      item.addEventListener("click", function () {
        document
          .querySelectorAll(".nav-item")
          .forEach((n) => n.classList.remove("active"));
        this.classList.add("active");
      });
    });
  }

  async function injectEnterpriseScreens() {
    const content = document.querySelector(".content");
    if (!content) return;
    if (document.getElementById("screen-ad-campaign-detail")) return;

    let html = "";
    try {
      const res = await fetch("./components/enterprise-modules.html", {
        cache: "no-store",
      });
      if (res.ok) {
        html = await res.text();
      }
    } catch (err) {
      html = "";
    }
    if (!html) {
      html = ENTERPRISE_FALLBACK_SCREENS_HTML;
    }

    const host = document.createElement("div");
    host.innerHTML = html;
    host
      .querySelectorAll(".screen")
      .forEach((screen) => content.appendChild(screen));
  }

  function rowBadge(status) {
    if (status === "Approved" || status === "Active" || status === "Enabled")
      return '<span class="badge badge-success">' + status + "</span>";
    if (status === "Draft" || status === "Review")
      return '<span class="badge badge-warning">' + status + "</span>";
    if (status === "Submitted")
      return '<span class="badge badge-info">' + status + "</span>";
    if (status === "Conflict" || status === "Disabled")
      return '<span class="badge badge-danger">' + status + "</span>";
    return '<span class="badge badge-gray">' + status + "</span>";
  }

  function renderCreativeVersions() {
    const body = document.getElementById("ad-creative-versions-body");
    if (!body) return;
    body.innerHTML = adCreativeVersions
      .map(
        (r) =>
          "<tr>" +
          "<td>" +
          r.version +
          "</td>" +
          "<td>" +
          r.size +
          "</td>" +
          "<td>" +
          r.format +
          "</td>" +
          "<td>" +
          r.by +
          "</td>" +
          "<td>" +
          r.at +
          "</td>" +
          "<td>" +
          rowBadge(r.status) +
          "</td>" +
          '<td><button class="btn-sm">View</button> <button class="btn-sm">Set active</button></td>' +
          "</tr>",
      )
      .join("");
  }

  window.renderAdInventoryTable = function () {
    const body = document.getElementById("ad-slot-inventory-body");
    if (!body) return;

    const slot = document.getElementById("ad-slot-filter");
    const conflict = document.getElementById("ad-conflict-filter");
    const slotValue = slot ? slot.value : "all";
    const conflictValue = conflict ? conflict.value : "all";

    const rows = adSlotInventory.filter((r) => {
      const slotOk = slotValue === "all" || r.slot === slotValue;
      const conflictOk =
        conflictValue === "all" || r.conflict === conflictValue;
      return slotOk && conflictOk;
    });

    body.innerHTML = rows
      .map(
        (r) =>
          "<tr>" +
          "<td>" +
          r.slot +
          "</td>" +
          "<td>" +
          r.placement +
          "</td>" +
          "<td>" +
          r.capacity +
          "</td>" +
          "<td>" +
          r.booked +
          "</td>" +
          "<td>" +
          rowBadge(r.conflict) +
          "</td>" +
          "<td>" +
          r.next +
          "</td>" +
          '<td><button class="btn-sm">Resolve</button></td>' +
          "</tr>",
      )
      .join("");
  };

  window.previewPricingModel = function () {
    const model = document.getElementById("pricing-model");
    const slot = document.getElementById("pricing-slot");
    const base = document.getElementById("pricing-base");
    const note = document.getElementById("pricing-preview-note");
    if (!model || !slot || !base || !note) return;

    note.textContent =
      "Preview: " +
      model.value +
      " applied on " +
      slot.value +
      " with base value ¥" +
      base.value +
      " and conflict-safe cap policy.";
  };

  function renderPricingRules() {
    const body = document.getElementById("ad-pricing-rules-body");
    if (!body) return;
    body.innerHTML = adPricingRules
      .map(
        (r) =>
          "<tr>" +
          "<td>" +
          r.id +
          "</td>" +
          "<td>" +
          r.model +
          "</td>" +
          "<td>" +
          r.slot +
          "</td>" +
          "<td>" +
          r.seg +
          "</td>" +
          "<td>" +
          r.base +
          "</td>" +
          "<td>" +
          rowBadge(r.status) +
          "</td>" +
          '<td><button class="btn-sm">Edit</button></td>' +
          "</tr>",
      )
      .join("");
  }

  function renderCmsVersions() {
    const body = document.getElementById("cms-version-history-body");
    if (!body) return;
    body.innerHTML = cmsVersions
      .map(
        (r, idx) =>
          "<tr>" +
          "<td>" +
          r.v +
          "</td>" +
          "<td>" +
          rowBadge(r.st) +
          "</td>" +
          "<td>" +
          r.a +
          "</td>" +
          "<td>" +
          r.r +
          "</td>" +
          "<td>" +
          r.p +
          "</td>" +
          "<td>" +
          r.t +
          "</td>" +
          '<td><button class="btn-sm" onclick="showCmsDiff(' +
          idx +
          ')">Diff</button></td>' +
          "</tr>",
      )
      .join("");
  }

  window.showCmsDiff = function (idx) {
    const panel = document.getElementById("cms-diff-view");
    if (!panel) return;
    const cur = cmsVersions[idx];
    const prev = cmsVersions[Math.max(0, idx - 1)];
    panel.innerHTML =
      "Comparing " +
      prev.v +
      " → " +
      cur.v +
      "<br/>" +
      "- Headline updated<br/>" +
      "- 2 paragraphs revised<br/>" +
      "- Metadata tags adjusted";
  };

  window.rollbackContentVersion = function () {
    const panel = document.getElementById("cms-diff-view");
    if (!panel) return;
    panel.textContent = "Rollback queued to latest approved version.";
  };

  function renderSystemTrees() {
    const tax = document.getElementById("sys-taxonomy-tree");
    if (tax) {
      tax.innerHTML =
        "Area Guide<br/>- Tokyo<br/>-- Shinjuku<br/>-- Minato<br/>- Osaka<br/>Insights<br/>- Rental\n";
    }
    const geo = document.getElementById("geo-hierarchy-tree");
    if (geo) {
      geo.innerHTML =
        "Tokyo<br/>- Shinjuku<br/>-- Nishi-Shinjuku<br/>Osaka<br/>- Kita<br/>-- Umeda";
    }
  }

  window.createTaxonomyNode = function () {
    const name = document.getElementById("taxonomy-node-name");
    const parent = document.getElementById("taxonomy-node-parent");
    const tax = document.getElementById("sys-taxonomy-tree");
    if (!name || !parent || !tax) return;
    tax.innerHTML += "<br/>" + parent.value + " / " + name.value;
  };

  window.deleteTaxonomyNode = function () {
    const tax = document.getElementById("sys-taxonomy-tree");
    if (!tax) return;
    tax.innerHTML += "<br/>[Last node marked for delete]";
  };

  function renderTransportTable() {
    const body = document.getElementById("transport-manager-body");
    if (!body) return;
    body.innerHTML = transportRows
      .map(
        (r) =>
          "<tr>" +
          "<td>" +
          r.line +
          "</td>" +
          "<td>" +
          r.station +
          "</td>" +
          "<td>" +
          r.city +
          "</td>" +
          "<td>" +
          rowBadge(r.status) +
          "</td>" +
          '<td><button class="btn-sm">Edit</button></td>' +
          "</tr>",
      )
      .join("");
  }

  window.filterExportAuditLog = function () {
    const body = document.getElementById("export-audit-log-body");
    const filter = document.getElementById("export-reason-filter");
    if (!body) return;
    const value = filter ? filter.value.toLowerCase() : "";
    const rows = exportAuditRows.filter((r) =>
      r.reason.toLowerCase().includes(value),
    );
    body.innerHTML = rows
      .map(
        (r) =>
          "<tr>" +
          "<td>" +
          r.when +
          "</td>" +
          "<td>" +
          r.actor +
          "</td>" +
          "<td>" +
          r.module +
          "</td>" +
          "<td>" +
          r.scope +
          "</td>" +
          "<td>" +
          r.reason +
          "</td>" +
          "<td>" +
          rowBadge(r.result) +
          "</td>" +
          "</tr>",
      )
      .join("");
  };

  window.togglePiiMask = function (field) {
    const map = {
      email: {
        id: "pii-email-view",
        masked: "a***@agency.jp",
        plain: "agent-owner@agency.jp",
      },
      phone: {
        id: "pii-phone-view",
        masked: "+81-***-**90",
        plain: "+81-90-1234-7890",
      },
      license: {
        id: "pii-license-view",
        masked: "JP-2025-****",
        plain: "JP-2025-1849",
      },
    };
    const cfg = map[field];
    if (!cfg) return;
    const el = document.getElementById(cfg.id);
    if (!el) return;
    const masked = el.classList.contains("masked");
    if (masked) {
      el.classList.remove("masked");
      el.textContent = cfg.plain;
    } else {
      el.classList.add("masked");
      el.textContent = cfg.masked;
    }
  };

  function renderStaffPerformanceBars() {
    const host = document.getElementById("staff-performance-bars");
    if (!host) return;
    const points = [44, 61, 58, 72, 69, 51, 37];
    const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
    host.innerHTML = points
      .map(
        (v, i) =>
          '<div class="bar-col"><div class="bar" style="height:' +
          v +
          'px; background: var(--bg-info)"></div><div class="bar-lbl">' +
          days[i] +
          "</div></div>",
      )
      .join("");
  }

  window.addInternalNote = function () {
    const type = document.getElementById("notes-entity-type");
    const id = document.getElementById("notes-entity-id");
    const content = document.getElementById("notes-content");
    if (!type || !id || !content || !content.value.trim()) return;

    notesRows.unshift({
      when: new Date().toISOString().slice(0, 16).replace("T", " "),
      entity: type.value + " " + id.value,
      note: content.value.trim(),
      author: "Admin Tanaka",
      visibility: "Internal only",
    });
    content.value = "";
    renderInternalNotes();
  };

  function renderInternalNotes() {
    const body = document.getElementById("internal-notes-body");
    if (!body) return;
    body.innerHTML = notesRows
      .map(
        (r) =>
          "<tr>" +
          "<td>" +
          r.when +
          "</td>" +
          "<td>" +
          r.entity +
          "</td>" +
          "<td>" +
          r.note +
          "</td>" +
          "<td>" +
          r.author +
          "</td>" +
          '<td><span class="badge badge-gray">' +
          r.visibility +
          "</span></td>" +
          "</tr>",
      )
      .join("");
  }

  function renderApiTokens() {
    const body = document.getElementById("api-token-body");
    if (!body) return;
    body.innerHTML = apiTokenRows
      .map(
        (r) =>
          "<tr>" +
          "<td>" +
          r.agent +
          "</td>" +
          "<td>" +
          r.id +
          "</td>" +
          "<td>" +
          r.scope +
          "</td>" +
          "<td>" +
          r.limit +
          "</td>" +
          "<td>" +
          rowBadge(r.status) +
          "</td>" +
          "<td>" +
          r.last +
          "</td>" +
          '<td><button class="btn-sm">Enable/Disable</button></td>' +
          "</tr>",
      )
      .join("");
  }

  window.renderWebhookLogs = function () {
    const body = document.getElementById("webhook-logs-body");
    const select = document.getElementById("webhook-status-filter");
    if (!body) return;
    const filter = select ? select.value : "all";
    const rows = webhookRows.filter((r) => {
      if (filter === "all") return true;
      return r.response.startsWith(filter[0]);
    });

    body.innerHTML = rows
      .map(
        (r) =>
          "<tr>" +
          "<td>" +
          r.time +
          "</td>" +
          "<td>" +
          r.event +
          "</td>" +
          "<td>" +
          r.endpoint +
          "</td>" +
          "<td>" +
          r.response +
          "</td>" +
          "<td>" +
          r.latency +
          "</td>" +
          "<td>" +
          r.retries +
          "</td>" +
          '<td><button class="btn-sm">View</button></td>' +
          "</tr>",
      )
      .join("");
  };

  window.setAdLifecycle = function (stage, el) {
    const label = document.getElementById("ad-lifecycle-stage");
    const note = document.getElementById("ad-lifecycle-note");
    const tabs = document.getElementById("ad-lifecycle-tabs");
    if (label) label.textContent = stage;
    if (note) note.textContent = stage + ": stage updated by admin action.";
    if (tabs && el) {
      tabs
        .querySelectorAll(".tab")
        .forEach((t) => t.classList.remove("active"));
      el.classList.add("active");
    }
  };

  window.saveFrequencyCapping = function () {
    const imp = document.getElementById("freq-impression");
    const clk = document.getElementById("freq-click");
    const win = document.getElementById("freq-window");
    if (!imp || !clk || !win) return;
    alert(
      "Frequency capping saved: impressions=" +
        imp.value +
        ", clicks=" +
        clk.value +
        ", window=" +
        win.value,
    );
  };

  function renderAllEnterpriseData() {
    renderCreativeVersions();
    window.renderAdInventoryTable();
    renderPricingRules();
    window.previewPricingModel();
    renderCmsVersions();
    renderSystemTrees();
    renderTransportTable();
    window.filterExportAuditLog();
    renderStaffPerformanceBars();
    renderInternalNotes();
    renderApiTokens();
    window.renderWebhookLogs();
  }

  async function initEnterpriseModules() {
    extendPageTitles();
    injectEnterpriseNav();
    await injectEnterpriseScreens();
    renderAllEnterpriseData();
  }

  initEnterpriseModules();
})();
