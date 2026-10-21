import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_ifx_css as build_cc_css, build_ifx_js as build_cc_js, build_ifx_data as build_cc_data
IMGS = json.load(open(os.path.join(HERE, 'imgs.json')))   # [DEMO]-record screenshots from the DXR guide
S = build_cc_data.STAGES
for _s in S: _s['what'] = _s['what'] + ' (In HubSpot: ' + _s['hs'] + '.)'

def path(*bits):
    out=[]
    for b in bits:
        if b == '>': out.append('<i>&rsaquo;</i>')
        elif b.startswith('!'): out.append(f'<span class="btn">{b[1:]}</span>')
        else: out.append(f'<span>{b}</span>')
    return '<div class="path">' + ''.join(out) + '</div>'

def fig(i, cap):
    return (f'<figure><img loading="lazy" alt="{cap}" src="{IMGS[i]}">'
            f'<figcaption>{cap}</figcaption></figure>')

def step(n, sid, title, sub, body):
    return (f'<li data-step="{sid}"><div class="head"><span class="num"><span>{n}</span></span>'
            f'<span class="ttl"><b>{title}</b><em>{sub}</em></span>'
            f'<span class="tick">Mark done</span>'
            f'<span class="chev" aria-hidden="true">&rsaquo;</span></div>'
            f'<div class="body">{body}</div></li>')

def table(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="tblwrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

LOGIN = [
 step(1,'l1','Open the Salesforce email','Subject: your Salesforce password',
   '<p>Salesforce emailed you a link on Wednesday evening. Click it to <strong>set your password</strong>. '
   'It works once &mdash; if it has expired or you cannot find it (check junk), ask Leah and we will send a new one.</p>'),
 step(2,'l2','Set up the authenticator','A code on your phone at each login',
   '<p>Salesforce asks you to connect an authenticator app. <strong>Salesforce Authenticator</strong> is simplest; '
   'the Microsoft or Google authenticator you already use also works.</p>'),
 step(3,'l3','Bookmark the login page','xypher.my.salesforce.com',
   '<p>From now on, go to <strong>https://xypher.my.salesforce.com</strong>. Your username is your '
   '<strong>IntaForensics email address</strong> (Lisa: your xypher.co.uk address).</p>'
   '<div class="note warn"><span class="tag">Do not press the Microsoft sign-in button</span>'
   '<p>Single sign-on is not connected to IntaForensics accounts yet, and using it can create a second, '
   'empty user for you. Username and password until we say otherwise.</p></div>'),
 step(4,'l4','Open the Sales app','Top left, the nine dots',
   '<p>Click the nine-dot <strong>App Launcher</strong> and choose <strong>Sales</strong>. That is '
   'where the tabs below live &mdash; and the only app that shows the proposal button.</p>' + path('!App Launcher','>','!Sales')),
]

ORDER = [
 step(1,'o1','Make sure the deal has products','The costs table is built from them',
   '<p>The proposal prices whatever is on the deal&rsquo;s <strong>Products</strong> panel. '
   '128 of your 166 open deals already have products from your HubSpot line items. On the rest, add them first '
   '(Products panel &rsaquo; Add Products).</p>'),
 step(2,'o2','Click Create IntaForensics Proposal','The actions menu at the top of the deal',
   '<p>On an open IntaForensics deal, open the <strong>&#9662;</strong> menu at the top right of the deal and choose '
   '<strong>Create IntaForensics Proposal</strong>.</p>' + path('Opportunity','>','!&#9662;','>','!Create IntaForensics Proposal')),
 step(3,'o3','Check the template, write the scope','Template follows the Service Line',
   '<p>The template is chosen from the deal&rsquo;s Service Line (Digital Forensics, Digital Investigation, Cell Site '
   'Analysis, eDiscovery or LIMA) and the client and primary contact are filled in. Write the '
   '<strong>Scope of Requirements and Strategy</strong> &mdash; one paragraph per line. It is saved to the deal, so '
   'the next version starts from it. Check the costs; VAT at 20% is on by default.</p>'),
 step(4,'o4','Create it, then send it yourself','It is saved to Files',
   '<p>The branded PDF lands in the deal&rsquo;s <strong>Files</strong> with its reference '
   '(<code>IF-20261008-0930-v1</code>, then <code>-v2</code>&hellip;). <strong>Salesforce does not email it</strong> '
   '&mdash; download it and send it to the client as you do today. Leah still reviews proposals before they go '
   '(Lisa for LIMA and eDiscovery; Toni when Leah is away).</p>'),
]

CLOSE = [
 step(1,'c1','Choose Closed, then Closed Won','The stage path opens the case form',
   '<p>On the stage path at the top of the case choose <strong>Closed</strong>, then <strong>Select Closed Stage</strong> '
   '&rsaquo; <strong>Closed Won</strong> &rsaquo; <strong>Next</strong>. The <strong>Close Won - Case Details</strong> form opens. '
   'It has five short steps and <strong>nothing is saved until you click Finish</strong> on the last one. '
   'Have the signed estimate to hand - you upload it at the end.</p>'
   + path('Case','>','!Closed','>','Select Closed Stage','>','!Closed Won','>','Next')),
 step(2,'c2','Step 1 - Award','External reference, dates, win reason',
   '<p><strong>External reference</strong> is the client&rsquo;s case reference (e.g. FA-2026-20705). Check the '
   '<strong>Signed date</strong> and <strong>Contract start date</strong> (both default to today) and pick a '
   '<strong>Win reason</strong>. <strong>One-off case</strong> is ticked - untick it only for an ongoing contract, then give '
   'the end date. If the case is at <strong>Negotiation</strong>, four sign-off fields appear here too: verbal commit date '
   'and evidence (the signed estimate counts), paper process and legal review.</p>'),
 step(3,'c3','Step 2 - Case details','Case type, offence, funding',
   '<p><strong>Case type</strong> (Digital Forensics, Video Forensics, Cell Site Analysis or Digital Investigation) and '
   '<strong>Funding</strong> are filled in from the products on the case - change them if they are wrong. Pick the '
   '<strong>Offence type</strong> (the LIMA list), CPS permissions if known, and the operation name and crime number if '
   'there are any. The <strong>Case contact</strong> is the solicitor or client on the case - the primary contact is '
   'already chosen.</p>'),
 step(4,'c4','Step 3 - Instruction','Background, instructions, suspects, deadlines, OIC',
   '<p><strong>Background to instruction</strong> starts from the scope you wrote on the proposal. Add the '
   '<strong>Objective / instructions for the expert</strong>, the <strong>Work deadline</strong> and the trial date if set. '
   'Write each suspect on its own line as <strong>SURNAME, First name</strong> - the form refuses a name without the comma. '
   'Add the officer in the case (OIC) if there is one.</p>'),
 step(5,'c5','Step 4 - Devices','And Cell Site parameters on Cell Site cases',
   '<p>Give the <strong>Number of devices</strong> (0 for a data-only case), then the make and model of each, one per line, '
   'and where the devices are now. Choosing <strong>On-site examination</strong> asks for the address. On a '
   '<strong>Cell Site</strong> case, also fill the locations of interest, the numbers and networks (one per line: '
   'number - network), the date and time period, and whether the call data records are in.</p>'),
 step(6,'c6','Step 5 - Quote and documents, then Finish','Hours, rate, travel and TRT are required',
   '<p><strong>Quoted hours</strong>, <strong>hourly rate</strong> and <strong>travel costs</strong> are filled in from the '
   'products - check them. Pick the <strong>Quoted TRT</strong> (5, 10, 25 or 30 working days, or Other and give the number). '
   'Check the <strong>Credit terms</strong>, then <strong>upload the signed estimate</strong> and any case bundle. '
   'The case cannot close until at least one document is on it. Click <strong>Finish</strong>.</p>'),
 step(7,'c7','Salesforce tells Submissions','No email from you, no invoice',
   '<p>The case moves to Closed Won and Salesforce emails <strong>submissions@</strong> and the department head for the '
   'case type - Digital Forensics, Video Forensics and Digital Investigation &rsaquo; Jake Blythe; Cell Site &rsaquo; '
   'Steve Hatton; eDiscovery &rsaquo; Lisa Washer and ediscovery@; LIMA &rsaquo; Kyle Horner - with a copy to you. '
   'It lists everything from the form, with links to the documents, so the case can be opened on LIMA straight away. '
   'Suspect names, crime number, OIC and Cell Site numbers are <strong>wiped from Salesforce 28 days later</strong>; LIMA '
   'is the record after that. If the last screen says the email could not be sent, forward the details to Submissions '
   'yourself and tell your Salesforce admin.</p>'),
]

TIDY = [
 step(1,'t1','Open My Opportunities','Every open IntaForensics deal you own',
   '<p>Click <strong>Opportunities</strong>, then switch the list to <strong>My Opportunities</strong>. '
   'Click the <strong>Close Date</strong> column to sort oldest first.</p>'
   + path('Sales app','>','!Opportunities','>','list: My Opportunities','>','sort by Close Date')
   + fig(0,'The Opportunities list view (demo records). The dropdown by the title switches lists.')),
 step(2,'t2','Close what is dead','Old HubSpot deals nobody is working',
   '<p>Your HubSpot pipeline came across as it was &mdash; including cases that stopped moving weeks '
   'or months ago. <strong>100 of your 166 open deals have a close date that has already passed.</strong> If it is dead, '
   'move it to <strong>Closed Lost</strong> with a Loss Reason and a line of Loss Detail. '
   'Losing a deal needs no MEDDPICC evidence.</p>'),
 step(3,'t3','Fix the close date on what is alive','Your honest date',
   '<p>If the deal is real, give it the date you actually expect a decision. A past date on an open '
   'deal shows as overdue on your manager&rsquo;s report.</p>'),
 step(4,'t4','Check Service Line, set Funding Route','Two fields HubSpot never had',
   '<p>You cannot leave Qualify without either. HubSpot had no reliable service line, so we worked it out '
   'from the deal name, notes and emails &mdash; check it is right; it picks your proposal template and who hears '
   'when you win. Funding Route is new and blank on every deal. Open the deal, go to <strong>Details</strong>, '
   'click the pencil, save.</p>'
   '<p>Your deal names are your own &mdash; Salesforce does not rename IntaForensics deals.</p>'),
 step(5,'t5','Give it a Next Step with a future date','The rule every stage move checks',
   '<p>Write the next action in <strong>Next Step</strong> and a date of today or later in '
   '<strong>Next Step Date</strong>. Without it, no stage will move.</p>'),
 step(6,'t6','Move the stage when you can evidence it','Read "To Advance, Still Needed"',
   '<p>The field <strong>To Advance, Still Needed</strong> on every deal lists exactly what is missing '
   'for the next stage. Fill those, then move the stage on the path at the top.</p>'
   + fig(1,'The Sales Path with the guidance for the current stage (demo record).')),
]

DICT = table(['In HubSpot', 'In Salesforce', 'Notes'], [
 ['Company', '<strong>Account</strong>', 'Some of your companies already existed in Salesforce &mdash; for DXR, CyberCrowd or as a Business Central customer (Forensic Access, for example). They were joined, not duplicated &mdash; you are on the <strong>Account Team</strong>.'],
 ['Contact (customer / opportunity lifecycle)', '<strong>Contact</strong>', 'People at companies you are already working with. Private individuals sit on the <strong>PRIVATE CLIENT</strong> account.'],
 ['Contact (owned lead)', '<strong>Lead</strong>', 'HubSpot has no Lead object; the lifecycle stage decided. Convert a Lead when it becomes a deal.'],
 ['Deal', '<strong>Opportunity</strong>', 'Same owner, amount, close date, stage (mapped below) and <strong>name</strong> &mdash; case references such as <code>FA-2026-20873</code> are kept.'],
 ['Deal line items', '<strong>Products</strong> on the deal', 'Your HubSpot quote lines, matched to the IntaForensics price list. They feed the proposal form.'],
 ['Emails, tasks, meetings, notes', '<strong>Activity</strong> timeline', 'On the record they belonged to in HubSpot.'],
 ['Original owner, created date, stage, case fields', '<strong>Legacy</strong> fields', 'Legacy Owner, Legacy Stage, and Legacy Details (analysis type, collar number, credit terms&hellip;) &mdash; kept for reference, never edited.'],
 ['The HubSpot record itself', '<strong>Legacy Record Link</strong>', '&ldquo;Open original record&rdquo; opens it in HubSpot while HubSpot is still available.'],
])

STAGEMAP = table(['HubSpot deal stage', 'Salesforce stage', 'Forecast', 'Deals'], [
 ['Enquiry (and Forecast)', 'Qualify (10%)', 'Pipeline', '30'],
 ['Proposal Requested', 'Solution Validation (30%)', 'Pipeline', '24'],
 ['Quote sent to Enquirer', 'Proposal / Bid Submitted (70%)', 'Best Case', '112'],
 ['&mdash; (no HubSpot stage)', 'Negotiation / Commercial Agreement (90%)', 'Commit', '0'],
 ['Proposal Awarded', 'Closed Won', 'Closed', '403'],
 ['Proposal Not Awarded', 'Closed Lost', 'Omitted', '563'],
])

LEADMAP = table(['HubSpot lead status', 'Salesforce Lead Status'], [
 ['New &middot; Open &middot; In progress &middot; Attempted to contact', 'Working'],
 ['Connected &middot; Open deal', 'Engaged'],
 ['Bad timing', 'Nurturing'],
 ['Unqualified', 'Disqualified (needs a Disqualify Reason)'],
])

ERRS = ''.join(f'<div class="err"><div class="msg">{m}</div><p>{w}</p></div>'
               for m,w in build_cc_data.ERRORS)
PICK = ''.join(f'<button data-stage="{s["id"]}" aria-pressed="false">{s["pos"]}. {s["name"]}</button>' for s in S)

EXTRA_CSS = '''
.tblwrap{overflow-x:auto;margin:14px 0 6px;border:1px solid var(--line);border-radius:12px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:.93rem}
th{font-family:var(--f-disp);font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;text-align:left;
   color:var(--ink-soft);background:var(--tint);padding:10px 14px}
td{padding:10px 14px;border-top:1px solid var(--line);vertical-align:top;color:var(--ink)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:16px 0}
.stat{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.stat b{display:block;font-family:var(--f-disp);font-size:1.5rem;color:var(--accent-ink)}
.stat span{font-size:.85rem;color:var(--muted)}
.brand{display:flex;align-items:center;gap:10px;margin-bottom:14px}
.brand img{height:34px;width:auto}
'''

LOGO = ''
lp = os.path.expanduser('~/Work/SaaScend/Xypher/enablement-slides/assets/logo_white.png')
if os.path.exists(lp):
    import base64
    LOGO = 'data:image/png;base64,' + base64.b64encode(open(lp,'rb').read()).decode()

HTML = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<!-- Internal enablement for the IntaForensics sales team (Xypher group). Field names, dropdown
     options and pass/fail marks re-checked against the Xypher production org on 7-8 Oct 2026. -->
<meta name="robots" content="noindex, nofollow, noarchive">
<title>IntaForensics Salesforce Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<style>{build_cc_css.CSS}{EXTRA_CSS}</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    {'<div class="brand"><img alt="SaaScend" src="'+LOGO+'"></div>' if LOGO else ''}
    <p class="eyebrow">SaaScend &times; Xypher &middot; IntaForensics sales team</p>
    <h1>Your HubSpot pipeline is now in Salesforce</h1>
    <p class="stand">Your companies, contacts, deals and history came across from HubSpot. This guide gets you logged in, shows you where everything went, and walks you
      through tidying your deals so they move.</p>
    <div class="prog">
      <div class="top">
        <span class="lbl">Deals tidied</span>
        <span class="count" id="count">0</span>
      </div>
      <div class="bar"><i id="bar"></i></div>
      <p class="row" id="progsub">List the deals you want to tidy below and tick them off as you go.</p>
      <div class="row">
        <span>How many open deals are you tidying?</span>
        <input type="number" id="target" min="0" max="999" placeholder="—" aria-label="Number of deals to tidy">
        <button class="ghost" id="resetall" type="button">Start over</button>
      </div>
    </div>
  </div>
</header>

<nav class="jump">
  <div class="wrap">
    <a href="#login">Logging in</a>
    <a href="#orderform">Proposals</a>
    <a href="#closing">Closing a deal</a>
    <a href="#moved">What came across</a>
    <a href="#basics">Finding your way</a>
    <a href="#tidy">Tidy your deals</a>
    <a href="#stages">What each stage needs</a>
    <a href="#tracker">Your list</a>
    <a href="#errors">When it will not save</a>
    <a href="#help">Help</a>
  </div>
</nav>

<div class="wrap">
<main>

<section id="login">
  <h2>Logging in</h2>
  <p class="dek">One email, one password, one authenticator app.</p>
  <ul class="steps">{''.join(LOGIN)}</ul>
</section>

<section id="moved">
  <h2>What came across from HubSpot</h2>
  <p class="dek">Everything you were working is here, under the same owner. Counts are from the
    Xypher production org on 7 October.</p>
  <div class="stats">
    <div class="stat"><b>3,059</b><span>companies &rarr; Accounts</span></div>
    <div class="stat"><b>1,245</b><span>Contacts</span></div>
    <div class="stat"><b>6,215</b><span>Leads</span></div>
    <div class="stat"><b>1,132</b><span>deals &rarr; Opportunities</span></div>
    <div class="stat"><b>166</b><span>of them still open</span></div>
  </div>
  <h3>Where each thing went</h3>
  {DICT}
  <h3>Your deal stages</h3>
  <p>Stages map one-to-one. The percentage is what the forecast assumes, and it follows the stage
    automatically. <strong>Negotiation is new to you</strong>: use it when the client has said yes in principle
    and you are agreeing paperwork &mdash; it is the only stage that counts as Commit.</p>
  {STAGEMAP}
  <h3>Your lead statuses</h3>
  {LEADMAP}
  <div class="note"><span class="tag">What did not come across, on purpose</span>
    <p><strong>Call recordings</strong> stayed in HubSpot. About <strong>5,800 contacts nobody ever owned</strong>
    (the purchased list) go to marketing, not to Sales. People who <strong>already existed in Salesforce</strong> for
    another Xypher business kept that one record &mdash; you may find a lead owned by a DXR colleague; that is the
    same person, not a missing one.</p></div>
</section>

<section id="basics">
  <h2>Finding your way around</h2>
  <p class="dek">Four things to recognise. Once these make sense the rest is just typing.</p>
  <ul class="steps">
    <li data-step="b1"><div class="head"><span class="num"><span>A</span></span>
      <span class="ttl"><b>Tabs across the top</b><em>Home, Leads, Accounts, Contacts, Opportunities&hellip;</em></span>
      <span class="tick">Mark done</span><span class="chev" aria-hidden="true">&rsaquo;</span></div>
      <div class="body"><p>Each tab is a type of record: <strong>Accounts</strong> are companies,
      <strong>Contacts</strong> are people, <strong>Opportunities</strong> are deals,
      <strong>Leads</strong> are people you have not qualified yet. Click a tab for a list; click a row
      to open the record.</p></div></li>
    <li data-step="b2"><div class="head"><span class="num"><span>B</span></span>
      <span class="ttl"><b>List views</b><em>Your filtered tables</em></span>
      <span class="tick">Mark done</span><span class="chev" aria-hidden="true">&rsaquo;</span></div>
      <div class="body"><p>The dropdown next to a list&rsquo;s name switches between saved filters
      &mdash; <strong>My Opportunities</strong>, <strong>Closing This Month</strong>,
      <strong>Recently Viewed</strong>. Changing the view never changes data.</p></div></li>
    <li data-step="b3"><div class="head"><span class="num"><span>C</span></span>
      <span class="ttl"><b>Shared accounts</b><em>Some of your customers are also DXR or CyberCrowd customers</em></span>
      <span class="tick">Mark done</span><span class="chev" aria-hidden="true">&rsaquo;</span></div>
      <div class="body"><p>Where a company already existed in Salesforce, your record was joined to it.
      The account owner may be a colleague from another business (Forensic Access is owned by CyberCrowd); you are on the <strong>Account Team</strong> panel and
      your deals, contacts and history are all there. This is the group seeing one customer once.</p></div></li>
    <li data-step="b4"><div class="head"><span class="num"><span>D</span></span>
      <span class="ttl"><b>Saving is not the same as advancing</b><em>The single most useful thing to know</em></span>
      <span class="tick">Mark done</span><span class="chev" aria-hidden="true">&rsaquo;</span></div>
      <div class="body"><p>Editing a field and saving is always fine. <strong>Changing the Stage</strong>
      is what triggers the checks. Your migrated deals sit at the stage they had in HubSpot; the checks
      only apply the first time you move one forward.</p></div></li>
  </ul>
</section>

<section id="orderform">
  <h2>Creating a proposal</h2>
  <p class="dek">Your five HubSpot proposal templates, now built from the deal in one click.</p>
  <ul class="steps">{''.join(ORDER)}</ul>
</section>

<section id="closing">
  <h2>When a case is awarded</h2>
  <p class="dek">Close it from the path and fill the five-step case form. Salesforce sends Submissions everything they need to open the case on LIMA.</p>
  <ul class="steps">{''.join(CLOSE)}</ul>
</section>

<section id="tidy">
  <h2>Tidy your deals</h2>
  <p class="dek">Your first week. Six steps, per deal; ticks are remembered on this browser.</p>
  <ul class="steps">{''.join(TIDY)}</ul>
</section>

<section id="stages">
  <h2>What each stage actually needs</h2>
  <p class="dek">Pick a stage for the fields it demands and, for every dropdown, which options let you
    move on. Read straight from the production rules, so it matches what Salesforce will tell you.</p>
  <div class="stagepick" id="stagepick">{PICK}</div>
  <div class="stagebox" id="stagebox"></div>
  <div class="note" style="margin-top:16px"><span class="tag">The light path</span>
    <p>Any deal over &pound;0 and under &pound;5k, and renewals (LIMA licences, for example), skip the
    MEDDPICC grades. They still need Service Line, Funding Route, a Next Step and the closing fields.</p></div>
</section>

<section id="tracker">
  <h2>Your list</h2>
  <p class="dek">Jot the deals you are tidying and tick each off. Kept on this browser only &mdash;
    nobody else sees it.</p>
  <div class="deals" id="deals"></div>
  <div class="addrow">
    <input type="text" id="dealname" placeholder="Deal name, as you would recognise it" aria-label="Deal name to add">
    <button type="button" id="dealadd">Add</button>
  </div>
</section>

<section id="errors">
  <h2>When it will not save</h2>
  <p class="dek">The messages you are most likely to hit, and what each means.</p>
  <div class="errs">{ERRS}</div>
  <div class="note"><span class="tag">A general rule</span>
    <p>The message appears in a red box at the <em>top</em> of the form, often scrolled out of
    sight. If a save seems to do nothing, scroll up. It is a checklist, not a telling-off.</p></div>
</section>

<section id="help">
  <h2>Help</h2>
  <p>Ask <strong>Leah</strong> first &mdash; if one person is stuck, usually several are.</p>
  <p>If something looks wrong rather than confusing &mdash; a deal under the wrong owner, a company
    that looks duplicated, history that is missing &mdash; screenshot it and send it to SaaScend.
    Migration fixes are quickest in the first two weeks.</p>
</section>

</main>
</div>

<footer>
  <div class="wrap">
    Prepared by SaaScend for the IntaForensics sales team, 8 October 2026. Every field name, dropdown
    option and pass/fail mark is read from the Salesforce production org; if the guide and the system
    disagree, the guide is wrong &mdash; tell us. Your ticks and list are stored in this browser only.
  </div>
</footer>

<script>window.__IFX_STAGES__ = {json.dumps(S, separators=(",",":"))};</script>
<script>{build_cc_js.JS}</script>
</body>
</html>
'''
out = os.path.join(HERE, 'index.html')
open(out,'w',encoding='utf-8').write(HTML)
print(f"  IntaForensics index.html written: {len(HTML)/1024:.0f} KB · stages {len(S)} · errors {len(build_cc_data.ERRORS)}")
