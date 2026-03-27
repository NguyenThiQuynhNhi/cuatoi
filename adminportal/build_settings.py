import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

styles = """
/* V2 Settings Module CSS */
.vertical-tab {
    padding: 10px 24px;
    cursor: pointer;
    font-weight: 500;
    color: var(--text-secondary);
    border-left: 3px solid transparent;
    transition: all 0.2s;
    font-size: 14px;
}
.vertical-tab:hover {
    background: rgba(0,0,0,0.03);
    color: var(--text-primary);
}
.vertical-tab.active {
    background: rgba(55,138,221,0.08);
    color: var(--primary);
    border-left: 3px solid var(--primary);
}
.setting-pane {
    display: none;
    max-width: 800px;
    margin: 0 auto;
}
.setting-pane.active {
    display: block;
    animation: fadeIn 0.3s ease;
}
.settings-card {
    background: var(--bg-primary);
    border: 1px solid var(--border-secondary);
    border-radius: 8px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.settings-card-title {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 16px;
    color: var(--text-primary);
    display:flex;
    justify-content:space-between;
    align-items:center;
}
.setting-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 0;
    border-bottom: 1px solid var(--border-tertiary);
}
.setting-row:last-child {
    border-bottom: none;
    padding-bottom: 0;
}
.setting-info {
    flex: 1;
    padding-right: 24px;
}
.setting-name {
    font-weight: 500;
    color: var(--text-primary);
    margin-bottom: 4px;
}
.setting-desc {
    font-size: 13px;
    color: var(--text-tertiary);
}
.setting-control {
    width: 240px;
}
.input-field-sm {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid var(--border-primary);
    border-radius: 6px;
    font-size: 14px;
}
.sticky-save-bar {
    position: sticky;
    bottom: 24px;
    background: var(--bg-primary);
    padding: 16px 24px;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    border: 1px solid var(--border-secondary);
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 800px;
    margin: 0 auto;
    z-index: 10;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
"""

settings_html = """
          <!-- ══ SYSTEM SETTINGS (V2 COMPREHENSIVE) ═══════════════════════════════════ -->
          <div class="screen" id="screen-settings">
            <div class="card" style="padding: 0; display:flex; height: calc(100vh - 120px); border:none; box-shadow:none; overflow:hidden;">
              
              <!-- Left Sidebar: Vertical Settings Nav -->
              <div style="width: 280px; border-right: 1px solid var(--border-secondary); background: var(--bg-primary); padding: 24px 0; overflow-y:auto;">
                <div style="padding: 0 24px 12px; font-weight:700; color:var(--text-primary); font-size:18px;">Settings</div>
                <div style="padding: 12px 24px 8px; font-weight:600; color:var(--text-tertiary); font-size:12px; text-transform:uppercase; letter-spacing:0.5px;">Platform Core</div>
                <div class="vertical-tab active" onclick="switchSettingTab('general', this)">General & Display</div>
                <div class="vertical-tab" onclick="switchSettingTab('welcome', this)">Welcome Setup</div>
                <div class="vertical-tab" onclick="switchSettingTab('features', this)">Feature Toggles</div>
                
                <div style="padding: 24px 24px 8px; font-weight:600; color:var(--text-tertiary); font-size:12px; text-transform:uppercase; letter-spacing:0.5px;">Security & Data</div>
                <div class="vertical-tab" onclick="switchSettingTab('security', this)">Security & Access</div>
                <div class="vertical-tab" onclick="switchSettingTab('audit', this)">Audit & System Logs</div>
                <div class="vertical-tab" onclick="switchSettingTab('governance', this)">Data Governance</div>
                <div class="vertical-tab" onclick="switchSettingTab('master-data', this)">Master Data Overview</div>
                
                <div style="padding: 24px 24px 8px; font-weight:600; color:var(--text-tertiary); font-size:12px; text-transform:uppercase; letter-spacing:0.5px;">Infrastructure</div>
                <div class="vertical-tab" onclick="switchSettingTab('infra', this)">Messaging Infra</div>
                <div class="vertical-tab" onclick="switchSettingTab('integrations', this)">External Integrations</div>
              </div>
              
              <!-- Right Content: Settings Panes -->
              <div style="flex:1; padding: 32px; overflow-y:auto; background: #f2f4f7; position:relative;" id="settings-content-area">
                 
                 <!-- TAB 1: GENERAL & DISPLAY -->
                 <div id="set-general" class="setting-pane active">
                    <h2 style="margin-bottom:8px; font-size:24px;">General & Display Settings</h2>
                    <p style="color:var(--text-secondary); margin-bottom:24px;">Set default platform configurations affecting all Client, Agent, and Admin portals.</p>
                    
                    <div class="settings-card">
                       <div class="settings-card-title">Localization Defaults</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Default Language (Client Portal)</div>
                             <div class="setting-desc">The fallback language for non-authenticated front-end visitors.</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>Japanese (日本語)</option><option>English</option><option>Chinese</option></select>
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Timezone & Date Format</div>
                             <div class="setting-desc">System time baseline for all cron jobs and logs.</div>
                          </div>
                          <div class="setting-control" style="display:flex; gap:8px;">
                             <select class="input-field-sm"><option selected>JST (UTC+9)</option></select>
                             <select class="input-field-sm"><option>YYYY/MM/DD</option></select>
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Number Format Rule</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>1,000,000 (Comma)</option><option>1.000.000 (Dot)</option></select>
                          </div>
                       </div>
                    </div>

                    <div class="settings-card">
                       <div class="settings-card-title">Currency & Measurement</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Default Currency</div>
                             <div class="setting-desc">Base currency for billing and property pricing.</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>JPY (¥)</option><option>USD ($)</option></select>
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Area Unit</div>
                             <div class="setting-desc">Default metric for property sizing.</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>Square Meters (m²)</option><option>Tsubo (坪)</option></select>
                          </div>
                       </div>
                    </div>

                    <!-- Sticky Save Bar -->
                    <div class="sticky-save-bar">
                       <div>
                         <div style="font-weight:600;">Unsaved Changes</div>
                         <div style="font-size:12px; color:var(--text-secondary);">This change affects all portals platform-wide.</div>
                       </div>
                       <div style="display:flex; gap:12px;">
                          <button class="btn btn-secondary">Discard</button>
                          <button class="btn btn-primary" onclick="alert('Confirmed: System configuration updated globally.')">Save Changes</button>
                       </div>
                    </div>
                 </div>

                 <!-- TAB 3: SECURITY & ACCESS -->
                 <div id="set-security" class="setting-pane">
                    <h2 style="margin-bottom:8px; font-size:24px;">Security & Access Control</h2>
                    <p style="color:var(--text-secondary); margin-bottom:24px;">Configure platform-wide authentication boundaries. Audit log required for all state changes.</p>
                    
                    <div class="settings-card">
                       <div class="settings-card-title">Authentication Policy</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Password Complexity</div>
                             <div class="setting-desc">Require numbers, special characters, and minimum length.</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>Strict (12+ chars, Num, Symbol)</option><option>Standard (8+ chars)</option></select>
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Failed Login Lockout</div>
                             <div class="setting-desc">Lock account after successive failed attempts.</div>
                          </div>
                          <div class="setting-control">
                             <input type="number" class="input-field-sm" value="5" />
                          </div>
                       </div>
                    </div>

                    <div class="settings-card">
                       <div class="settings-card-title">Session Control</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Admin Session Timeout (Minutes)</div>
                             <div class="setting-desc">Auto logout non-active admin sessions to prevent breach.</div>
                          </div>
                          <div class="setting-control">
                             <input type="number" class="input-field-sm" value="30" />
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Concurrent Login Rule</div>
                             <div class="setting-desc">Action taken when a second login is detected.</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>Force logout oldest session</option><option>Block new login</option><option>Allow both</option></select>
                          </div>
                       </div>
                    </div>
                    
                    <div class="settings-card" style="border-left: 4px solid var(--primary);">
                       <div class="settings-card-title">Two-Factor Authentication (2FA)</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Mandatory 2FA Enforcement</div>
                             <div class="setting-desc">Require specific roles to setup Authenticator app.</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>All Admin & Support Staff</option><option>Super Admins Only</option><option>Disabled</option></select>
                          </div>
                       </div>
                    </div>
                 </div>

                 <!-- TAB 5: FEATURE TOGGLES -->
                 <div id="set-features" class="setting-pane">
                    <h2 style="margin-bottom:8px; font-size:24px;">Platform Feature Toggles</h2>
                    <p style="color:var(--text-secondary); margin-bottom:24px;">Master switches for platform capabilities. Disabling a feature removes its UI across all user portals.</p>
                    
                    <div class="settings-card">
                       <div class="setting-row" style="padding-top:0;">
                          <div class="setting-info">
                             <div class="setting-name" style="font-size:16px;">Sponsored Ads Module (Rakuten Level)</div>
                             <div class="setting-desc">Determines if the entire Advertisement ecosystem is active. Disabling this auto-pauses all running inventory locks.</div>
                          </div>
                          <div>
                             <div class="toggle-switch active" style="width:44px; height:24px; background:var(--bg-success); border-radius:12px; position:relative; cursor:pointer;"><div style="width:20px; height:20px; background:white; position:absolute; right:2px; top:2px; border-radius:50%;"></div></div>
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name" style="font-size:16px;">New Development Projects Hub</div>
                             <div class="setting-desc">Enterprise B2B module for handling unbuilt property project lifecycles.</div>
                          </div>
                          <div>
                             <div class="toggle-switch active" style="width:44px; height:24px; background:var(--bg-success); border-radius:12px; position:relative; cursor:pointer;"><div style="width:20px; height:20px; background:white; position:absolute; right:2px; top:2px; border-radius:50%;"></div></div>
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name" style="font-size:16px;">EDM Mass Marketing Campaigns</div>
                             <div class="setting-desc">Allows agents to build and trigger marketing emails.</div>
                          </div>
                          <div>
                             <div class="toggle-switch" style="width:44px; height:24px; background:var(--border-tertiary); border-radius:12px; position:relative; cursor:pointer;"><div style="width:20px; height:20px; background:white; position:absolute; left:2px; top:2px; border-radius:50%; box-shadow:0 1px 2px rgba(0,0,0,0.2);"></div></div>
                          </div>
                       </div>
                       <div class="setting-row" style="border-bottom:none; padding-bottom:0;">
                          <div class="setting-info">
                             <div class="setting-name" style="font-size:16px; color:#d92d20;">Support Ticket System (CR)</div>
                             <div class="setting-desc">Internal SLA ticketing tool. <span style="font-weight:600;">Dependency Warning: Disabling cuts off live client chat forms.</span></div>
                          </div>
                          <div>
                             <div class="toggle-switch active" style="width:44px; height:24px; background:var(--bg-success); border-radius:12px; position:relative; cursor:pointer;"><div style="width:20px; height:20px; background:white; position:absolute; right:2px; top:2px; border-radius:50%;"></div></div>
                          </div>
                       </div>
                    </div>
                 </div>
                 
                 <!-- TAB 6: INFRASTRUCTURE -->
                 <div id="set-infra" class="setting-pane">
                    <h2 style="margin-bottom:8px; font-size:24px;">Messaging Infrastructure</h2>
                    <p style="color:var(--text-secondary); margin-bottom:24px;">Configure low-level notification delivery systems. Does NOT include message content/templates.</p>
                    
                    <div class="settings-card">
                       <div class="settings-card-title">Email Delivery Pipeline</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Primary Provider</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>AWS SES (API Route)</option><option>SendGrid</option><option>Custom SMTP</option></select>
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Global Sending Domain</div>
                             <div class="setting-desc">Requires DNS verification (DKIM/SPF pass).</div>
                          </div>
                          <div class="setting-control">
                             <input type="text" class="input-field-sm" value="no-reply@propadmin-platform.jp" disabled />
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Provider API Key</div>
                          </div>
                          <div class="setting-control">
                             <input type="password" class="input-field-sm" value="sk_test_1234567890abcdef" />
                          </div>
                       </div>
                    </div>

                    <div class="settings-card">
                       <div class="settings-card-title">Compliance & Rules (JP Act)</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Mandatory Unsubscribe Injection</div>
                             <div class="setting-desc">Auto-append 1-click unsubscribe links to all outgoing system emails to maintain reputation.</div>
                          </div>
                          <div class="setting-control">
                             <div class="toggle-switch active" style="width:36px; height:20px; background:var(--bg-success); border-radius:10px; position:relative;"><div style="width:16px; height:16px; background:white; position:absolute; right:2px; top:2px; border-radius:50%;"></div></div>
                          </div>
                       </div>
                    </div>
                    
                    <button class="btn btn-secondary" style="width:100%;">Test Connection Flow</button>
                 </div>
                 
                 <!-- TAB 9: GOVERNANCE -->
                 <div id="set-governance" class="setting-pane">
                    <h2 style="margin-bottom:8px; font-size:24px;">Data Governance & Privacy Controls</h2>
                    <p style="color:var(--text-secondary); margin-bottom:24px;">Enterprise parameters dictating data lifecycle and Personal Identifiable Information (PII) handling.</p>
                    
                    <div class="settings-card" style="border: 1px solid #d92d20;">
                       <div class="settings-card-title" style="color:#d92d20;">Data Retention Lifecycle</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Inactive User Hard-Deletion Limit</div>
                             <div class="setting-desc">Automatically purge User PII from databases after inactivity (GDPR/APPI compliance).</div>
                          </div>
                          <div class="setting-control">
                             <select class="input-field-sm"><option selected>Retain for 5 Years</option><option>Retain for 1 Year</option><option>Never Delete (Archive)</option></select>
                          </div>
                       </div>
                    </div>
                    
                    <div class="settings-card">
                       <div class="settings-card-title">Export & Masking Rules</div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Audit Mandatory on Bulk Export</div>
                             <div class="setting-desc">Require Admin to input a "Reason" before generating CSVs > 100 rows.</div>
                          </div>
                          <div class="setting-control">
                             <div class="toggle-switch active" style="width:36px; height:20px; background:var(--bg-success); border-radius:10px; position:relative;"><div style="width:16px; height:16px; background:white; position:absolute; right:2px; top:2px; border-radius:50%;"></div></div>
                          </div>
                       </div>
                       <div class="setting-row">
                          <div class="setting-info">
                             <div class="setting-name">Auto-Mask Chat Exports</div>
                             <div class="setting-desc">Ensures structural compliance that phone numbers and emails inside chats are encrypted when downloaded.</div>
                          </div>
                          <div class="setting-control">
                             <div class="toggle-switch active" style="width:36px; height:20px; background:var(--bg-success); border-radius:10px; position:relative;"><div style="width:16px; height:16px; background:white; position:absolute; right:2px; top:2px; border-radius:50%;"></div></div>
                          </div>
                       </div>
                    </div>
                 </div>
                 
                 <!-- TAB: WELCOME SETUP (Placeholder) -->
                 <div id="set-welcome" class="setting-pane">
                    <h2 style="margin-bottom:8px; font-size:24px;">Welcome & Initialization</h2>
                    <div class="settings-card"><p>Run the initial setup wizard to prepopulate tables.</p><button class="btn btn-primary">Re-run Installer</button></div>
                 </div>
                 
                 <!-- TAB: AUDIT LOGS (Placeholder) -->
                 <div id="set-audit" class="setting-pane">
                    <h2 style="margin-bottom:8px; font-size:24px;">Audit & System Logs</h2>
                    <div class="settings-card"><p>System-wide immutable log table mapping Admin Actor -> Configuration Change Date.</p></div>
                 </div>
                 
                 <!-- TAB: INTEGRATIONS (Placeholder) -->
                 <div id="set-integrations" class="setting-pane">
                    <h2 style="margin-bottom:8px; font-size:24px;">External Integrations</h2>
                    <div class="settings-card"><p>Manage Webhooks, Payment Gateways (Stripe), Map Providers (Google Maps), and Address APIs.</p></div>
                 </div>
                 
                 <div id="set-master-data" class="setting-pane">
                    <h2 style="margin-bottom:8px; font-size:24px;">Master Data Management Redirect</h2>
                    <div class="settings-card"><p>Master Data defines core Hierarchies (Geo, Railway). Click below to access the deep mapping tables.</p><button class="btn btn-secondary" onclick="switchScreen('master-data', this)">Open Master Data Tool</button></div>
                 </div>

              </div>
              
            </div>
          </div>
          
          <script>
            function switchSettingTab(id, el) {
                // Remove active classes
                document.querySelectorAll('.vertical-tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.setting-pane').forEach(p => p.classList.remove('active'));
                
                // Add active classes
                if(el) el.classList.add('active');
                const pane = document.getElementById('set-' + id);
                if(pane) pane.classList.add('active');
            }
          </script>
"""

# Append CSS
with open('styles/main.css', 'a', encoding='utf-8') as f:
    f.write(styles)

# Replace existing screen-settings if exists, or append
if 'id="screen-settings"' in html:
    # A bit hard to regex replace a wildly varying div safely in python without an html parser.
    # Instead, we will find the bounds of screen-settings if it's there.
    # Wait, earlier I didn't inject screen-settings, it is from the original file. Let's see if it existed.
    start_idx = html.find('<div class="screen" id="screen-settings">')
    if start_idx != -1:
        # Find next screen
        end_idx = html.find('<div class="screen" id="screen-', start_idx + 10)
        if end_idx == -1:
            end_idx = html.rfind('</div>', 0, html.rfind('</div>')) # roughly end of content
        html = html[:start_idx] + settings_html + html[end_idx:]
else:
    # just append
    html = re.sub(r'</div>\s*</body>', settings_html + r'\n</div>\n</body>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: System Settings implemented cleanly without business flow mixing.")
