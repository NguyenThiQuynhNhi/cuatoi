import re
import os

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

new_sidebar_html = """<!-- ── SIDEBAR ─────────────────────────────────────── -->
      <!-- include: ./components/sidebar.html -->
      <aside class="sidebar">
        <div class="sidebar-header">
          <div class="logo-mark">
            <svg viewBox="0 0 14 14">
              <path d="M7 1L13 4V10L7 13L1 10V4Z" />
            </svg>
          </div>
          <span class="logo-text">PropAdmin<span class="logo-badge">ADMIN</span></span>
        </div>

        <div class="nav-section">
          <div class="nav-label">Overview</div>
          <div class="nav-item active" onclick="switchScreen('dashboard', this)" title="KPI Dashboard">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><rect x="1" y="1" width="5" height="5" rx="1" /><rect x="9" y="1" width="5" height="5" rx="1" /><rect x="1" y="9" width="5" height="5" rx="1" /><rect x="9" y="9" width="5" height="5" rx="1" /></svg>
            <span>KPI Dashboard</span>
          </div>
          <div class="nav-item" onclick="switchScreen('dashboards', this)" title="Multi-area Dashboards">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M2 12h11M3 10V5M7 10V2M11 10V7" stroke-linecap="round" /></svg>
            <span>Dashboards</span>
          </div>
          <div class="nav-item" onclick="switchScreen('agent-analytics', this)" title="Agent Analytics">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M1 13L5 8l3 3 3-4 3-3" /></svg>
            <span>Agent Analytics</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Users & Agents</div>
          <div class="nav-item" onclick="switchScreen('users', this)" title="User Management">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="7.5" cy="4.5" r="2.5" /><path d="M2 13c0-3.04 2.46-5.5 5.5-5.5S13 9.96 13 13" /></svg>
            <span>User Management</span>
          </div>
          <div class="nav-item" onclick="switchScreen('agent-list', this)" title="Agent Directory">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M2 4h11M2 7.5h11M2 11h11" stroke-linecap="round" /></svg>
            <span>Agents Directory</span>
          </div>
          <div class="nav-item" onclick="switchScreen('agents', this)" title="Agent Approvals">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M5 1h5l1 3H4L5 1zm-3 3h11l-1 9H3L2 4z" /></svg>
            <span>Agent Approvals</span>
            <span class="nav-badge">4</span>
          </div>
          <div class="nav-item" onclick="switchScreen('leads', this)" title="Lead Oversight">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M2 2h11v2H2zM2 6h11v2H2zM2 10h7v2H2z" /></svg>
            <span>Lead Oversight</span>
          </div>
          <div class="nav-item" onclick="switchScreen('staff-users', this)" title="Staff Users">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="5" cy="5" r="2"/><circle cx="10.5" cy="5" r="1.5"/><path d="M1.5 12c0-2 1.5-3.5 3.5-3.5s3.5 1.5 3.5 3.5"/><path d="M8.7 12c0-1.7 1.1-2.9 2.7-2.9"/></svg>
            <span>Staff Users</span>
          </div>
          <div class="nav-item" onclick="switchScreen('admin-accounts', this)" title="Admin Accounts">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="7.5" cy="4.5" r="2.5"/><path d="M2 13c0-3.04 2.46-5.5 5.5-5.5S13 9.96 13 13"/><path d="M12 2v2M11 3h2" stroke-linecap="round"/></svg>
            <span>Admin Accounts</span>
          </div>
          <div class="nav-item" onclick="switchScreen('staff-roles', this)" title="Roles & Permissions">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M7.5 1l5.5 2.5v4C13 11 10.6 13 7.5 14 4.4 13 2 11 2 7.5v-4z"/></svg>
            <span>Roles & Permissions</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Properties</div>
          <div class="nav-item" onclick="switchScreen('properties', this)" title="Property Oversight">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M1 14V7.5L7.5 1 14 7.5V14H9.5v-4h-4v4H1z" /></svg>
            <span>Property Oversight</span>
          </div>
          <div class="nav-item" onclick="switchScreen('property-moderation', this)" title="Property Moderation">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M2 2h11v7H2z" /><path d="M5 13h5" stroke-linecap="round" /></svg>
            <span>Property Moderation</span>
          </div>
          <div class="nav-item" onclick="switchScreen('projects', this)" title="Projects">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><rect x="1" y="2" width="13" height="11" rx="1"/><rect x="3" y="4" width="4" height="3" rx=".5" fill="var(--bg-primary)"/></svg>
            <span>Projects</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Content (CMS & Layout)</div>
          <div class="nav-item" onclick="switchScreen('global-cms', this)" title="CMS Advanced">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><rect x="2" y="2" width="11" height="11" rx="1" /><rect x="4" y="5" width="7" height="1.5" fill="var(--bg-primary)" /><rect x="4" y="8" width="5" height="1.5" fill="var(--bg-primary)" /></svg>
            <span style="font-weight: 600; color: var(--primary);">CMS Advanced</span>
          </div>
          <div class="nav-item" onclick="switchScreen('content', this)" title="CMS & Articles">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><rect x="1" y="1" width="13" height="2" rx="1" /><rect x="1" y="5" width="9" height="2" rx="1" /><rect x="1" y="9" width="11" height="2" rx="1" /><rect x="1" y="13" width="7" height="2" rx="1" /></svg>
            <span>CMS & Articles</span>
          </div>
          <div class="nav-item" onclick="switchScreen('cms-pages', this)" title="CMS Pages">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><rect x="2" y="2" width="11" height="11" rx="1" /><rect x="4" y="5" width="7" height="1.5" fill="var(--bg-primary)" /><rect x="4" y="8" width="5" height="1.5" fill="var(--bg-primary)" /></svg>
            <span>CMS Pages</span>
          </div>
          <div class="nav-item" onclick="switchScreen('taxonomy', this)" title="Taxonomy & Categories">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M2 3h11M4 7h9M6 11h7" /></svg>
            <span>Taxonomy</span>
          </div>
          <div class="nav-item" onclick="switchScreen('seo-control', this)" title="SEO Control">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="6.5" cy="6.5" r="3.5"/><path d="M9.5 9.5L13 13" stroke-linecap="round"/></svg>
            <span>SEO Control</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Monetisation & Ads</div>
          <div class="nav-item" onclick="switchScreen('ad-inventory', this)" title="Ad Inventory Selection">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="1" y="2" width="13" height="11" rx="1" /><path d="M4 5h7M4 8h5" /></svg>
            <span style="font-weight: 600; color: var(--primary);">Ad Inventory Mgmt</span>
            <span class="nav-badge" style="background:var(--primary); color:#000;">PRO</span>
          </div>
          <div class="nav-item" onclick="switchScreen('ads', this)" title="Ad Management">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="1" y="3" width="13" height="9" rx="1" /><path d="M4 9V6l2 3 2-3v3M11 9V6" stroke-linecap="round" stroke-linejoin="round" /></svg>
            <span>Ad Management</span><span class="nav-badge">2</span>
          </div>
          <div class="nav-item" onclick="switchScreen('offers', this)" title="Offers & Pricing">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M2 3h11v2H2zM2 6h11v6H2z" /></svg>
            <span>Offers & Pricing</span>
          </div>
          <div class="nav-item" onclick="switchScreen('payments', this)" title="Payment Reports">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="1" y="3" width="13" height="9" rx="1"/><rect x="1" y="6" width="13" height="2" fill="currentColor" stroke="none"/></svg>
            <span>Payment Reports</span>
          </div>
          <div class="nav-item" onclick="switchScreen('financials', this)" title="Financial Dashboard">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M2 12h11v1H2zM3 11V7h2v4H3zm3 0V4h2v7H6zm3 0V6h2v5H9z" /></svg>
            <span>Financials</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Comms, Support & Compliance</div>
          <div class="nav-item" onclick="switchScreen('compliance', this)" title="Compliance">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M7.5 1l5.5 2.5v4C13 11 10.6 13 7.5 14 4.4 13 2 11 2 7.5v-4z"/></svg>
            <span style="font-weight: 600; color: var(--primary);">Compliance</span>
          </div>
          <div class="nav-item" onclick="switchScreen('messages', this)" title="Messages & Emails">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="1.5" y="2.5" width="12" height="9" rx="1"/><path d="M2.5 4l5 3.5L12.5 4"/></svg>
            <span>Messages & Emails</span>
          </div>
          <div class="nav-item" onclick="switchScreen('notifications', this)" title="Notifications">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M7.5 1.5A4 4 0 0 1 11.5 5v3l1 1V10h-10V9l1-1V5a4 4 0 0 1 4-3.5z" /></svg>
            <span>Notifications</span>
          </div>
          <div class="nav-item" onclick="switchScreen('edm-campaigns', this)" title="EDM Campaigns">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="1.5" y="2.5" width="12" height="10" rx="1" /><path d="M3 5h9M3 8h6" stroke-linecap="round" /></svg>
            <span>EDM Campaigns</span>
          </div>
          <div class="nav-item" onclick="switchScreen('support-tickets', this)" title="Support Tickets">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M2 2h11v9H6l-3 2v-2H2z" /></svg>
            <span>Support & Tickets</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Operations & Analytics</div>
          <div class="nav-item" onclick="switchScreen('ops-tooling', this)" title="Ops Tooling">
             <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="7.5" cy="7.5" r="3.5"/><path d="M7.5 1v3M7.5 11v3M1 7.5h3M11 7.5h3"/></svg>
            <span style="font-weight: 600; color: var(--primary);">Ops Tooling</span>
          </div>
          <div class="nav-item" onclick="switchScreen('analytics', this)" title="Market Analysis">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M1 13L5 8l3 3 3-4 3-3"/></svg>
            <span>Market Analysis</span>
          </div>
          <div class="nav-item" onclick="switchScreen('activity', this)" title="Activity">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M1.5 8h2.5l1.5-3 2.2 6 1.8-4h3" stroke-linecap="round" stroke-linejoin="round" /></svg>
            <span>Activity</span>
          </div>
          <div class="nav-item" onclick="switchScreen('reports', this)" title="Reports">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M3 1h7l2 2v11H3z"/><path d="M5 6h5M5 8h5M5 10h4" stroke="var(--bg-primary)" stroke-width="1"/></svg>
            <span>Reports</span>
          </div>
          <div class="nav-item" onclick="switchScreen('contacts', this)" title="Contacts">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="5" cy="5" r="2"/><path d="M1.5 10.5c0-2 1.5-3.5 3.5-3.5s3.5 1.5 3.5 3.5"/><circle cx="11" cy="5" r="1.5"/><path d="M8.8 10.5c.2-1.5 1.2-2.6 2.7-2.6 1.6 0 2.8 1.2 2.8 2.8"/></svg>
            <span>Contacts</span>
          </div>
          <div class="nav-item" onclick="switchScreen('agreements', this)" title="Agreements">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M3 1h9v13H3z"/><path d="M5 4h5M5 7h5M5 10h4" stroke="var(--bg-primary)" stroke-width="1"/></svg>
            <span>Agreements</span><span class="nav-badge">P2</span>
          </div>
          <div class="nav-item" onclick="switchScreen('calendar', this)" title="Calendar Assignment">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><rect x="1" y="2" width="13" height="12" rx="1" /><rect x="1" y="5" width="13" height="2" fill="var(--bg-primary)" /></svg>
            <span>Calendar Assignment</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Settings, Data & Integrations</div>
          <div class="nav-item" onclick="switchScreen('master-data', this)" title="Master Data">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M7.5 1v13M1 7.5h13M3 3h2M10 12h2" /></svg>
            <span style="font-weight: 600; color: var(--primary);">Master Data</span>
          </div>
          <div class="nav-item" onclick="switchScreen('integration-adv', this)" title="Integration Adv.">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M4 1L7.5 4L11 1" stroke-linecap="round"/><path d="M7.5 14V4" stroke-linecap="round"/><rect x="2" y="11" width="11" height="3" rx="0.5"/></svg>
            <span style="font-weight: 600; color: var(--primary);">Integration Adv.</span>
          </div>
          <div class="nav-item" onclick="switchScreen('settings', this)" title="System Settings">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"><circle cx="7.5" cy="7.5" r="2" /><path d="M7.5 1v2M7.5 12v2M1 7.5h2M12 7.5h2M3.2 3.2l1.4 1.4M10.4 10.4l1.4 1.4M3.2 11.8l1.4-1.4M10.4 4.6l1.4-1.4" /></svg>
            <span>System Settings</span>
          </div>
          <div class="nav-item" onclick="switchScreen('feature-control', this)" title="Feature Control">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M7.5 1l2 2.4h3.1v3.1l2.4 2-2.4 2v3.1H9.5l-2 2.4-2-2.4H2.4V10.5L0 8.5l2.4-2V3.4h3.1z"/></svg>
            <span>Feature Control</span>
          </div>
          <div class="nav-item" onclick="switchScreen('integrations', this)" title="Integrations (Basic)">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="1.5" y="2" width="4" height="4"/><rect x="9.5" y="2" width="4" height="4"/><rect x="5.5" y="9" width="4" height="4"/><path d="M5.5 4h4M7.5 6.2V9"/></svg>
            <span>Integrations (Basic)</span>
          </div>
          <div class="nav-item" onclick="switchScreen('audit-logs', this)" title="Audit Logs">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor"><path d="M3 1h9v13H3z"/><path d="M5 4h5M5 7h5M5 10h4" stroke="var(--bg-primary)" stroke-width="1"/></svg>
            <span>Audit Logs</span>
          </div>
          <div class="nav-item" onclick="switchScreen('profile', this)" title="My Profile">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="7.5" cy="4.5" r="2.5"/><path d="M2 13c0-3.04 2.46-5.5 5.5-5.5S13 9.96 13 13"/></svg>
            <span>My Profile</span>
          </div>
        </div>

        <div class="sidebar-footer">
          <div class="avatar">AT</div>
          <div class="avatar-info">
            <div class="avatar-name">Admin Tanaka</div>
            <div class="avatar-role">Platform Architect</div>
          </div>
        </div>
      </aside>

      <!-- ── MAIN ────────────────────────────────────────── -->"""

sidebar_pattern = re.compile(r'<!-- ── SIDEBAR ─────────────────────────────────────── -->.*?<!-- ── MAIN ────────────────────────────────────────── -->', re.DOTALL)
html = sidebar_pattern.sub(new_sidebar_html, html)

# We should also inject simple plaeholder screens for the 3 missing ones so that clicking them works
screens_to_add = """
          <!-- ══ COMPLIANCE (NEW) ═══════════════════════════════════ -->
          <div class="screen" id="screen-compliance">
            <div class="card">
              <h2>Compliance Center</h2>
              <p>Work In Progress: Centralize moderation and legal frameworks.</p>
            </div>
          </div>
          
          <!-- ══ OPS TOOLING (NEW) ═══════════════════════════════════ -->
          <div class="screen" id="screen-ops-tooling">
            <div class="card">
              <h2>Ops Tooling</h2>
              <p>Work In Progress: Powerful tools for the operation floor.</p>
            </div>
          </div>
          
          <!-- ══ INTEGRATION ADV (NEW) ═══════════════════════════════════ -->
          <div class="screen" id="screen-integration-adv">
            <div class="card">
              <h2>Integration Adv.</h2>
              <p>Work In Progress: Heavy third-party API configurations.</p>
            </div>
          </div>
"""

# append to index html after screen-master-data or inside content
if 'id="screen-master-data"' in html:
    idx = html.rfind('</div>\n          </div>\n', 0, html.find('id="screen-master-data"') + 5000) # approximate
    # let's just use re.sub before </body>
    content_closer = r'</div>\s*</body>'
    html = re.sub(content_closer, screens_to_add + r'\n</div>\n</body>', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS")
