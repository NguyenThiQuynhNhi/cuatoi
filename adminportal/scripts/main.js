
      const PAGE_TITLES = {
        dashboard: "KPI Dashboard",
        dashboards: "Multi-area Dashboards",
        users: "User Management",
        "user-detail": "User Detail",
        agents: "Agent Approvals",
        "agent-list": "Agents Directory",
        "agent-detail": "Agent Detail",
        leads: "Lead Oversight",
        messages: "Messages & Emails",
        notifications: "Notifications",
        "edm-campaigns": "EDM Campaigns",
        "support-tickets": "Support Tickets",
        content: "CMS & Articles",
        "cms-pages": "CMS Pages",
        "seo-control": "SEO Control",
        properties: "Property Oversight",
        "property-moderation": "Property Moderation",
        ads: "Ad Management",
        payments: "Payment Reports",
        financials: "Financial Dashboard",
        analytics: "Market Analysis",
        activity: "Activity Monitoring",
        reports: "Underlying Reports",
        contacts: "Contacts & Organisations",
        projects: "Projects Oversight",
        offers: "Offers & Pricing",
        agreements: "Agreements & Templates",
        calendar: "Calendar Assignment",
        "feature-control": "Per-Account Feature Control",
        "staff-users": "Staff Users",
        "staff-roles": "Roles & Permissions",
        integrations: "External Integrations",
        "audit-logs": "Audit Logs",
        "admin-accounts": "Administrator Account Management",
        profile: "Admin Profile",
        settings: "System Settings",
      };

      function switchScreen(id, el) {
        // hide all screens
        document
          .querySelectorAll(".screen")
          .forEach((s) => s.classList.remove("active"));
        // deactivate all nav items
        document
          .querySelectorAll(".nav-item")
          .forEach((n) => n.classList.remove("active"));
        // activate target
        const screen = document.getElementById("screen-" + id);
        if (screen) screen.classList.add("active");
        if (el) el.classList.add("active");
        document.getElementById("page-title").textContent =
          PAGE_TITLES[id] || id;
      }

      function openScreen(id) {
        const navItem = Array.from(document.querySelectorAll(".nav-item")).find(
          (item) =>
            item.getAttribute("onclick") &&
            item.getAttribute("onclick").includes("'" + id + "'"),
        );
        switchScreen(id, navItem || null);
      }

      function switchTab(el, group) {
        const parent = el.closest(".tabs");
        if (!parent) return;
        parent
          .querySelectorAll(".tab")
          .forEach((t) => t.classList.remove("active"));
        el.classList.add("active");

        const card = el.closest(".card");
        const target = el.getAttribute("data-tab-target");
        if (!card || !target) return;

        const panels = card.querySelectorAll(".tab-panel");
        if (!panels.length) return;
        panels.forEach((panel) => panel.classList.remove("active"));
        const activePanel = card.querySelector(
          '.tab-panel[data-tab-panel="' + target + '"]',
        );
        if (activePanel) activePanel.classList.add("active");
      }

      function openProfile() {
        const profileNav = Array.from(
          document.querySelectorAll(".nav-item"),
        ).find(
          (item) =>
            item.getAttribute("onclick") &&
            item.getAttribute("onclick").includes("'profile'"),
        );
        if (profileNav) switchScreen("profile", profileNav);
      }

      function verifyWelcomeConfig() {
        const area = document.getElementById("welcome-area-unit").value;
        const currency = document.getElementById("welcome-currency").value;
        alert(
          "Welcome settings verified: area=" + area + ", currency=" + currency,
        );
        dismissWelcome();
      }

      function dismissWelcome() {
        const modal = document.getElementById("welcome-modal");
        if (modal) modal.classList.add("hidden");
      }

      // Highlight active nav item on click for child actions
      document.querySelectorAll(".nav-item").forEach((item) => {
        item.addEventListener("click", function () {
          document
            .querySelectorAll(".nav-item")
            .forEach((n) => n.classList.remove("active"));
          this.classList.add("active");
        });
      });
    