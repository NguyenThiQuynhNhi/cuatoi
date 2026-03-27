import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sidebar_pattern = re.compile(r'<!-- ── SIDEBAR ─────────────────────────────────────── -->.*?<!-- ── MAIN ────────────────────────────────────────── -->', re.DOTALL)

new_sidebar = """<!-- ── SIDEBAR ─────────────────────────────────────── -->
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
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <rect x="1" y="1" width="5" height="5" rx="1" />
              <rect x="9" y="1" width="5" height="5" rx="1" />
              <rect x="1" y="9" width="5" height="5" rx="1" />
              <rect x="9" y="9" width="5" height="5" rx="1" />
            </svg>
            <span>KPI Dashboard</span>
          </div>
          <div class="nav-item" onclick="switchScreen('agent-analytics', this)" title="Agent Analytics">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.3">
              <path d="M2 12h11M3 10V5M7 10V2M11 10V7" stroke-linecap="round" />
            </svg>
            <span>Agent Analytics</span>
          </div>
          <div class="nav-item" onclick="switchScreen('financials', this)" title="Financial Dashboard (CR)">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <path d="M2 12h11v1H2zM3 11V7h2v4H3zm3 0V4h2v7H6zm3 0V6h2v5H9z" />
            </svg>
            <span>Financials (CR)</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Users & Agents</div>
          <div class="nav-item" onclick="switchScreen('users', this)" title="Unified User Directory">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2">
              <circle cx="7.5" cy="4.5" r="2.5" />
              <path d="M2 13c0-3.04 2.46-5.5 5.5-5.5S13 9.96 13 13" />
            </svg>
            <span>User Directory</span>
          </div>
          <div class="nav-item" onclick="switchScreen('agents', this)" title="Agent Approvals">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <path d="M5 1h5l1 3H4L5 1zm-3 3h11l-1 9H3L2 4z" />
            </svg>
            <span>Agent Approvals</span>
            <span class="nav-badge">4</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Properties</div>
          <div class="nav-item" onclick="switchScreen('properties', this)" title="Property Oversight">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <path d="M1 14V7.5L7.5 1 14 7.5V14H9.5v-4h-4v4H1z" />
            </svg>
            <span>Property Oversight</span>
          </div>
          <div class="nav-item" onclick="switchScreen('property-moderation', this)" title="Property Moderation">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2">
              <path d="M2 2h11v7H2z" />
              <path d="M5 13h5" stroke-linecap="round" />
            </svg>
            <span>Moderation & Complaints</span>
            <span class="nav-badge" style="background:var(--badge-danger);">12</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Content (CMS - Global)</div>
          <div class="nav-item" onclick="switchScreen('global-cms', this)" title="Global CMS Configuration">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <rect x="2" y="2" width="11" height="11" rx="1" />
              <rect x="4" y="5" width="7" height="1.5" fill="var(--bg-primary)" />
              <rect x="4" y="8" width="5" height="1.5" fill="var(--bg-primary)" />
            </svg>
            <span style="font-weight: 500; color: var(--primary);">Global CMS Config</span>
          </div>
          <div class="nav-item" onclick="switchScreen('content', this)" title="Articles & Pages">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <rect x="1" y="1" width="13" height="2" rx="1" />
              <rect x="1" y="5" width="9" height="2" rx="1" />
              <rect x="1" y="9" width="11" height="2" rx="1" />
              <rect x="1" y="13" width="7" height="2" rx="1" />
            </svg>
            <span>Articles & Pages</span>
          </div>
          <div class="nav-item" onclick="switchScreen('taxonomy', this)" title="Taxonomy & Categories">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2">
              <path d="M2 3h11M4 7h9M6 11h7" />
            </svg>
            <span>Taxonomy</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Monetisation & Ads</div>
          <div class="nav-item" onclick="switchScreen('ad-inventory', this)" title="Ad Inventory Management">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2">
              <rect x="1" y="2" width="13" height="11" rx="1" />
              <path d="M4 5h7M4 8h5" />
            </svg>
            <span style="font-weight: 500; color: var(--primary);">Ad Inventory Mgmt</span>
            <span class="nav-badge" style="background:var(--primary); color:#000;">PRO</span>
          </div>
          <div class="nav-item" onclick="switchScreen('ads', this)" title="Sponsored Property Ads">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2">
              <rect x="1" y="3" width="13" height="9" rx="1" />
              <path d="M4 9V6l2 3 2-3v3M11 9V6" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <span>Sponsored Ads</span>
          </div>
          <div class="nav-item" onclick="switchScreen('offers', this)" title="Offers & Pricing">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <path d="M2 3h11v2H2zM2 6h11v6H2z" />
            </svg>
            <span>Offers & Pricing</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Comms & Support</div>
          <div class="nav-item" onclick="switchScreen('notifications', this)" title="System Notifications">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <path d="M7.5 1.5A4 4 0 0 1 11.5 5v3l1 1V10h-10V9l1-1V5a4 4 0 0 1 4-3.5z" />
            </svg>
            <span>Notifications</span>
          </div>
          <div class="nav-item" onclick="switchScreen('edm-campaigns', this)" title="EDM Campaigns">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2">
              <rect x="1.5" y="2.5" width="12" height="10" rx="1" />
              <path d="M3 5h9M3 8h6" stroke-linecap="round" />
            </svg>
            <span>EDM Campaigns</span>
          </div>
          <div class="nav-item" onclick="switchScreen('support-tickets', this)" title="Support Tickets">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <path d="M2 2h11v9H6l-3 2v-2H2z" />
            </svg>
            <span>Support Tickets</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Operations</div>
          <div class="nav-item" onclick="switchScreen('activity', this)" title="Activity">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.3">
              <path d="M1.5 8h2.5l1.5-3 2.2 6 1.8-4h3" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <span>Activity</span>
          </div>
          <div class="nav-item" onclick="switchScreen('calendar', this)" title="Calendar Assignment">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="currentColor">
              <rect x="1" y="2" width="13" height="12" rx="1" />
              <rect x="1" y="5" width="13" height="2" fill="var(--bg-primary)" />
            </svg>
            <span>Task Calendar</span>
          </div>
        </div>

        <div class="nav-section">
          <div class="nav-label">Settings & System (Merged)</div>
          <div class="nav-item" onclick="switchScreen('master-data', this)" title="Master Data (Geo/Rail)">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2">
              <path d="M7.5 1v13M1 7.5h13M3 3h2M10 12h2" />
            </svg>
            <span style="font-weight: 500; color: var(--primary);">Master Data (Geo/Rail)</span>
          </div>
          <div class="nav-item" onclick="switchScreen('settings', this)" title="System Settings">
            <svg class="nav-icon" viewBox="0 0 15 15" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round">
              <circle cx="7.5" cy="7.5" r="2" />
              <path d="M7.5 1v2M7.5 12v2M1 7.5h2M12 7.5h2M3.2 3.2l1.4 1.4M10.4 10.4l1.4 1.4M3.2 11.8l1.4-1.4M10.4 4.6l1.4-1.4" />
            </svg>
            <span>System Settings</span>
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

html = sidebar_pattern.sub(new_sidebar, html)

screens_to_append = """
          <!-- ══ GLOBAL CMS CONFIGURATION (V2) ═══════════════════════════════════ -->
          <div class="screen" id="screen-global-cms">
            <div class="card" style="padding: 0; display:flex; height: calc(100vh - 120px); border:none; box-shadow:none;">
              <!-- Left Sidebar: Block Manager -->
              <div style="width: 320px; border-right: 1px solid var(--border-secondary); display: flex; flex-direction: column; background: var(--bg-secondary); border-radius: 8px 0 0 8px;">
                <div style="padding: 16px; border-bottom: 1px solid var(--border-secondary);">
                  <div style="font-weight: 600; margin-bottom: 12px; color:var(--text-primary);">Central Block Manager</div>
                  <div style="display:flex; gap: 8px;">
                    <button class="btn btn-primary" style="flex:1;">Client Portal</button>
                    <button class="btn btn-secondary" style="flex:1;">Agent Portal</button>
                  </div>
                  <select class="input-field" style="margin-top: 12px;">
                    <option>Homepage Layout</option>
                    <option>City/Area Page Layout</option>
                    <option>Buyer Guide Series</option>
                  </select>
                </div>
                
                <div style="padding: 16px; flex:1; overflow-y: auto;">
                  <div style="font-size: 13px; font-weight: 600; color: var(--text-tertiary); margin-bottom: 8px;">ACTIVE BLOCKS (DRAG TO REORDER)</div>
                  
                  <!-- Blocks -->
                  <div class="drag-block" style="background:var(--bg-primary); border:1px solid var(--border-tertiary); padding: 12px; border-radius: 6px; margin-bottom: 8px; cursor: grab; display:flex; align-items:center;">
                    <span style="color:var(--text-tertiary); margin-right:8px;">≡</span>
                    <div style="flex:1; font-weight:500;">Hero Banner Slider</div>
                    <div class="toggle-switch active" style="width:36px; height:20px; background:var(--bg-success); border-radius:10px; position:relative;"><div style="width:16px; height:16px; background:white; position:absolute; right:2px; top:2px; border-radius:50%;"></div></div>
                  </div>
                  
                  <div class="drag-block active" style="background:var(--bg-surface); border:1px solid var(--primary); padding: 12px; border-radius: 6px; margin-bottom: 8px; cursor: grab; display:flex; align-items:center;">
                    <span style="color:var(--text-tertiary); margin-right:8px;">≡</span>
                    <div style="flex:1; font-weight:500; color:var(--primary);">Sponsored Search Slot</div>
                    <div class="toggle-switch active" style="width:36px; height:20px; background:var(--bg-success); border-radius:10px; position:relative;"><div style="width:16px; height:16px; background:white; position:absolute; right:2px; top:2px; border-radius:50%;"></div></div>
                  </div>
                  
                  <!-- Block config panel snippet -->
                  <div style="background:var(--bg-surface); padding: 12px; margin-top:-4px; margin-bottom: 8px; border: 1px solid var(--primary); border-top:none; border-radius: 0 0 6px 6px;">
                    <div style="font-size:12px; color:var(--text-secondary); margin-bottom:4px;">Content Source Type</div>
                    <select class="input-field"><option>Algorithmic (Paid Ranking)</option><option>Manual Property ID</option></select>
                  </div>
                  
                  <div class="drag-block" style="background:var(--bg-primary); border:1px solid var(--border-tertiary); padding: 12px; border-radius: 6px; margin-bottom: 8px; cursor: grab; display:flex; align-items:center; opacity:0.6;">
                    <span style="color:var(--text-tertiary); margin-right:8px;">≡</span>
                    <div style="flex:1; font-weight:500;">New Developments Grid</div>
                    <div class="toggle-switch" style="width:36px; height:20px; background:#e4e7ec; border-radius:10px; position:relative;"><div style="width:16px; height:16px; background:white; position:absolute; left:2px; top:2px; border-radius:50%;"></div></div>
                  </div>
                  
                  <div class="drag-block" style="background:var(--bg-primary); border:1px dashed var(--border-tertiary); padding: 12px; border-radius: 6px; margin-bottom: 8px; cursor: pointer; display:flex; align-items:center; justify-content:center; color: var(--primary);">
                    + Add Block
                  </div>
                </div>
              </div>
              
              <!-- Right Preview Canvas -->
              <div style="flex: 1; display:flex; flex-direction:column; background: #eaecf0; border-radius: 0 8px 8px 0; overflow:hidden;">
                <div style="padding: 12px 24px; background:var(--bg-primary); border-bottom:1px solid var(--border-secondary); display:flex; justify-content:space-between; align-items:center;">
                  <div style="font-size:14px; font-weight:500;">Live Preview: Homepage Layout</div>
                  <div>
                    <button class="btn btn-secondary">Preview Desktop</button>
                    <button class="btn btn-primary">Save Layout</button>
                  </div>
                </div>
                <!-- Iframe mock -->
                <div style="flex:1; padding: 24px; overflow-y: auto; display:flex; justify-content:center;">
                  <div style="width: 100%; max-width: 900px; background:white; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); min-height:800px; border: 1px solid var(--border-tertiary);">
                    <!-- skeleton of a homepage -->
                    <div style="height: 300px; background: #f2f4f7; border-radius: 8px 8px 0 0; display:flex; align-items:center; justify-content:center; font-size:24px; color:#98a2b3; font-weight:bold;">HERO BANNER</div>
                    <div style="padding: 24px;">
                       <div style="height: 40px; width: 300px; background:#e4e7ec; border-radius:20px; margin-bottom:16px;"></div>
                       <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px;">
                          <div style="height: 200px; background: rgba(55,138,221,0.1); border: 2px dashed var(--primary); border-radius: 8px; display:flex; align-items:center; justify-content:center; color:var(--primary); font-weight:600;">Sponsored Slot Active</div>
                          <div style="height: 200px; background: #f2f4f7; border-radius: 8px;"></div>
                          <div style="height: 200px; background: #f2f4f7; border-radius: 8px;"></div>
                       </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ══ AD INVENTORY MANAGEMENT (V2) ═══════════════════════════════════ -->
          <div class="screen" id="screen-ad-inventory">
            <div class="table-toolbar">
              <div class="table-tabs">
                <div class="tab active">Gantt Availability (Bookings)</div>
                <div class="tab">Placement Definitions & Pricing</div>
                <div class="tab">Rejection Policies</div>
              </div>
              <div class="toolbar-actions">
                <button class="btn btn-secondary">Export Schedule</button>
                <button class="btn btn-primary">+ New Booking / Blockout</button>
              </div>
            </div>
            
            <div class="card" style="padding:0; overflow:hidden;">
              <!-- Gantt Chart Mock -->
              <div style="display:flex; border-bottom:1px solid var(--border-secondary); background:var(--bg-secondary);">
                <div style="width:250px; padding: 12px 16px; font-weight:600; border-right:1px solid var(--border-secondary);">Ad Placement Zone</div>
                <div style="flex:1; display:flex; overflow-x:auto;">
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px;">Apr 1</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px;">Apr 2</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px;">Apr 3</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px;">Apr 4</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px; background:rgba(0,0,0,0.03);">Apr 5</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px; background:rgba(0,0,0,0.03);">Apr 6</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px;">Apr 7</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px;">Apr 8</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px;">Apr 9</div>
                  <div style="min-width: 60px; padding: 12px; text-align:center; border-right:1px solid var(--border-tertiary); font-size:12px;">Apr 10</div>
                </div>
              </div>
              
              <div style="display:flex; border-bottom:1px solid var(--border-secondary);">
                <div style="width:250px; padding: 16px; border-right:1px solid var(--border-secondary);">
                  <div style="font-weight:500;">Homepage Hero Leaderboard</div>
                  <div style="font-size:12px; color:var(--text-tertiary);">Client Portal • Fixed Rate</div>
                </div>
                <div style="flex:1; display:flex; position:relative; background-image: linear-gradient(to right, var(--border-tertiary) 1px, transparent 1px); background-size: 60px 100%;">
                  <div style="position:absolute; left: 0px; top: 12px; width: 178px; height: 32px; background: var(--bg-info); border: 1px solid var(--primary); border-radius: 4px; padding: 6px; font-size:12px; font-weight:600; color:var(--primary); overflow:hidden; white-space:nowrap;">
                    Campaign: Mitsui Premium
                  </div>
                  <div style="position:absolute; left: 180px; top: 12px; width: 238px; height: 32px; background: #fef3f2; border: 1px solid #d92d20; border-radius: 4px; padding: 6px; font-size:12px; font-weight:600; color:#d92d20; overflow:hidden; white-space:nowrap;">
                    [CONFLICT] 2 campaigns assigned
                  </div>
                </div>
              </div>
              
              <div style="display:flex; border-bottom:1px solid var(--border-secondary);">
                <div style="width:250px; padding: 16px; border-right:1px solid var(--border-secondary);">
                  <div style="font-weight:500;">Search Result Top Banner</div>
                  <div style="font-size:12px; color:var(--text-tertiary);">CPM Basis • Freq Capped: 3</div>
                </div>
                <div style="flex:1; display:flex; position:relative; background-image: linear-gradient(to right, var(--border-tertiary) 1px, transparent 1px); background-size: 60px 100%;">
                  <div style="position:absolute; left: 120px; top: 12px; width: 418px; height: 32px; background: var(--bg-surface); border: 1px solid var(--border-primary); border-radius: 4px; padding: 6px; font-size:12px; font-weight:500; color:var(--text-secondary); overflow:hidden; white-space:nowrap;">
                    Open Inventory (Bidding active)
                  </div>
                </div>
              </div>
            </div>
            <div style="padding:16px; font-size:13px; color:var(--text-secondary);">Enterprise Ad Logic Active: Bidding engines will resolve open CPB slots. Drag bookings to reschedule.</div>
          </div>

          <!-- ══ MASTER DATA MANAGEMENT (V2) ═══════════════════════════════════ -->
          <div class="screen" id="screen-master-data">
             <div class="table-toolbar">
              <div class="table-tabs">
                <div class="tab">Geo Hierarchy</div>
                <div class="tab active">Railway & Station Network</div>
                <div class="tab">Property Types</div>
                <div class="tab">System Enums</div>
              </div>
              <div class="toolbar-actions">
                <button class="btn btn-secondary">Export CSV</button>
                <button class="btn btn-primary">Bulk Import Stations</button>
              </div>
            </div>
            
            <div class="grid-2-col" style="display:grid; grid-template-columns: 1fr 2fr; gap:24px;">
              <div class="card" style="padding:0; overflow:hidden; height: calc(100vh - 220px);">
                 <div style="padding: 16px; border-bottom: 1px solid var(--border-secondary); font-weight:600;">Railway Operators & Lines</div>
                 <div style="padding: 16px; overflow-y:auto; height:100%;">
                   <div style="margin-bottom:8px;">
                     <div style="display:flex; align-items:center; cursor:pointer; font-weight:600;">
                       <span style="display:inline-block; width:16px;">▾</span> JR East
                     </div>
                     <div style="padding-left: 20px; border-left: 1px solid var(--border-tertiary); margin-left: 6px; margin-top: 4px;">
                        <div style="padding: 4px 0; display:flex; align-items:center; color: var(--primary); font-weight:500; cursor:pointer;"><span style="display:inline-block; width:16px;">▾</span> Yamanote Line</div>
                        <div style="padding-left: 20px; border-left: 1px solid var(--border-tertiary); margin-left: 6px; margin-top: 4px;">
                           <div style="padding: 4px 0; display:flex; justify-content:space-between; align-items:center; font-size:13px;">Tokyo <span class="nav-badge" style="background:#f2f4f7; color:#344054;">Hub</span></div>
                           <div style="padding: 4px 0; display:flex; justify-content:space-between; align-items:center; font-size:13px;">Yurakucho</div>
                           <div style="padding: 4px 0; display:flex; justify-content:space-between; align-items:center; font-size:13px; background:var(--bg-surface); font-weight:500; border-radius:4px; margin-left:-4px; padding-left:4px;">Shimbashi <span class="nav-badge" style="background:#f2f4f7; color:#344054;">Hub</span></div>
                           <div style="padding: 4px 0; display:flex; justify-content:space-between; align-items:center; font-size:13px;">Hamamatsucho</div>
                        </div>
                        <div style="padding: 4px 0; display:flex; align-items:center; color: var(--text-secondary); cursor:pointer;"><span style="display:inline-block; width:16px;">▸</span> Chuo Line (Rapid)</div>
                        <div style="padding: 4px 0; display:flex; align-items:center; color: var(--text-secondary); cursor:pointer;"><span style="display:inline-block; width:16px;">▸</span> Keihin-Tohoku Line</div>
                     </div>
                   </div>
                   <div style="margin-bottom:8px;">
                     <div style="display:flex; align-items:center; cursor:pointer; font-weight:600;">
                       <span style="display:inline-block; width:16px;">▸</span> Tokyo Metro (Subway)
                     </div>
                   </div>
                 </div>
              </div>
              
              <div class="card" style="padding: 24px;">
                 <div style="font-size:20px; font-weight:600; margin-bottom: 24px;">Shimbashi Station Intersections</div>
                 <p style="color:var(--text-secondary); margin-bottom: 24px;">Map physical intersections. Warning: Do not delete stations with active properties assigned.</p>
                 
                 <div class="table-wrap">
                   <table class="data-table">
                     <thead>
                       <tr>
                         <th>Intersecting Line</th>
                         <th>Operator</th>
                         <th>Distance / Transfer</th>
                         <th></th>
                       </tr>
                     </thead>
                     <tbody>
                       <tr>
                         <td>Keihin-Tohoku Line</td>
                         <td>JR East</td>
                         <td>0 min (Same platform structure)</td>
                         <td style="text-align:right"><button class="btn btn-secondary">Unlink</button></td>
                       </tr>
                       <tr>
                         <td>Ginza Line</td>
                         <td>Tokyo Metro</td>
                         <td>3 min walk</td>
                         <td style="text-align:right"><button class="btn btn-secondary">Unlink</button></td>
                       </tr>
                       <tr>
                         <td>Asakusa Line</td>
                         <td>Toei Subway</td>
                         <td>5 min walk</td>
                         <td style="text-align:right"><button class="btn btn-secondary">Unlink</button></td>
                       </tr>
                       <tr>
                         <td>Yurikamome Line</td>
                         <td>Yurikamome</td>
                         <td>Direct connection</td>
                         <td style="text-align:right"><button class="btn btn-secondary">Unlink</button></td>
                       </tr>
                     </tbody>
                   </table>
                 </div>
                 <div style="margin-top:24px;">
                    <button class="btn btn-secondary">+ Add Intersection</button>
                 </div>
              </div>
            </div>
          </div>
"""

# Insert string into end of class="content"
content_idx = html.rfind('</div>')  # We just assume standard structure, but better use a simple split
if '<!-- Scripts -->' in html:
    html = html.replace('<!-- Scripts -->', screens_to_append + '\n<!-- Scripts -->')
else:
    # Just insert it before </body> using regex
    html = re.sub(r'</div>\s*</body>', screens_to_append + '\n</div>\n</body>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html updated")
