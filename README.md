# IntaForensics Salesforce Guide

Enablement for the IntaForensics sales team moving from HubSpot to the Xypher Salesforce org (go-live 8 Oct 2026).
Fork of `../cybercrowd-starter-guide`. Edit the `build_ifx_*.py` files, never `index.html`; rebuild with
`python3 build_ifx_page.py`. Copy: `deliverables/IntaForensics_Salesforce_Guide.html`.
Live at **https://saascend-org.github.io/xypher-intaforensics-starter-guide/** (public repo saascend-org/xypher-intaforensics-starter-guide, Pages from main). After a rebuild: commit and push index.html.

IFX differences: password + MFA login (no SSO); proposals via Create IntaForensics Proposal; Closed Won has no
work-package form (xyOpportunityPath only routes DXR/CyberCrowd/blank to it) - fill VR5 fields in Details, then
Closed > Closed Won; F13 award email by service line; deals keep their own names; gates on from day one.
