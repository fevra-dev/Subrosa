# Cookie Consent Reference

Compliant cookie banner templates, category definitions, GPC signal handling, and jurisdiction-specific requirements.

> **Source of truth:** GPC legal-status and consent-standard anchors derive from `taxonomy/regulatory-taxonomy.md` records (`eu-gdpr-uk`, `us-ca-ccpa`); the ePrivacy Directive itself is a sectoral overlay — S-profile record `eu-eprivacy` (see master §Design Contract 4). Reconciled 2026-07-04; log: `.fable/reconciliation-log.md`. On conflict, the record wins (see `SKILL.md` §Regulatory Source of Truth).

---

## Legal Basis: ePrivacy Directive Art. 5(3) + GDPR

Cookie/tracking consent is governed by the ePrivacy Directive (2002/58/EC), not GDPR directly — though GDPR defines what "consent" means. The ePrivacy Directive requires:

1. **Clear and comprehensive information** about the purpose of storing/accessing information on terminal equipment
2. **User's consent** — a freely given, specific, informed, unambiguous indication of agreement (per GDPR Art. 4(11))
3. **Prior consent** — before the cookie/tracker fires, not after

**Exemption (Art. 5(3)):** Storage/access strictly necessary to provide an information society service explicitly requested by the subscriber. This covers: session cookies, authentication cookies, shopping cart cookies, security cookies, load balancing cookies, user consent preference cookies. Does NOT cover analytics, advertising, A/B testing, or social media plugins even if "first party."

---

## Cookie Categories

### Category 1 — Strictly Necessary

**No consent required.** Cannot be disabled without breaking core functionality.

**Definition:** Essential to provide a service the user has explicitly requested. The service cannot function without them.

**Examples:**
- Session authentication (keeps you logged in)
- CSRF tokens (security)
- Load balancer session stickiness
- Shopping cart contents
- Cookie consent preference storage (ironic but true — you need this to remember rejection)
- Language/currency preference if set as part of service request

**Banner copy:**
```
Essential cookies are required for this website to function. They cannot be
disabled. These cookies do not store personal information beyond what is
required for the service to work.
```

**Legitimate interest test:** Not applicable — strictly necessary cookies don't need a legal basis under ePrivacy Art. 5(3).

---

### Category 2 — Functional / Preference

**Consent required** (or legitimate interests in some member states — use consent for maximum compliance).

**Definition:** Enable enhanced functionality and personalization. Not strictly necessary but expected by users.

**Examples:**
- Remember language preference across sessions (if not set by user action)
- Remember theme (dark/light mode)
- Accessibility preferences
- Video player preferences (volume, quality)

**Banner copy:**
```
Functional cookies remember your preferences and customize your experience.
Disabling them means certain features may not work as expected.
```

---

### Category 3 — Analytics / Performance

**Consent required.** No analytics exception under GDPR/ePrivacy.

**The "anonymous analytics" trap:** Most analytics tools (Google Analytics, Mixpanel, Amplitude, Segment) are NOT anonymous — they process IP addresses, user agents, and often cross-site identifiers. If using these tools, you cannot claim anonymous analytics. Must obtain consent.

**True anonymous analytics** (no consent required if truly anonymous):
- Server-side aggregate counting with no user-level data
- Fathom Analytics (cookie-free, IP-not-stored mode)
- Plausible Analytics (cookieless, GDPR-exempt mode)
- Self-hosted Matomo with full anonymization settings

**Banner copy:**
```
Analytics cookies help us understand how visitors use our site. This
information is used to improve our service. [If using Google Analytics etc:]
Third parties may also process this data under their privacy policies.
```

**If Google Analytics (GA4):** Disclose GA4 specifically. Under CNIL (France), DSK (Germany), and Austrian DSB guidance, GA4 without additional safeguards (Consent Mode V2, server-side proxying, IP anonymization) is not GDPR compliant due to US data transfers. Document your transfer mechanism.

---

### Category 4 — Marketing / Advertising

**Explicit opt-in consent required.** Must be equal in prominence to refusal option.

**Definition:** Track user behavior across sites to build profiles for targeted advertising. Third parties typically involved.

**Examples:**
- Google Ads cookies (DoubleClick, _gcl_*, _gac_*)
- Meta Pixel
- LinkedIn Insight Tag
- Any retargeting or cross-site behavioral tracker

**Banner copy:**
```
Marketing cookies track your activity across websites to show you relevant
advertising. These cookies may be set by advertising partners who will use
them to build a profile of your interests. Declining will not reduce the
number of adverts you see, but they will be less targeted.
```

---

## Compliant Cookie Banner Templates

### Tier 1 — Minimal (Low non-essential use)

```
────────────────────────────────────────────────────────────
We use cookies to make our website work. We'd also like to use
analytics cookies to understand how you use our site.

  [Accept analytics]     [Reject non-essential]     [Learn more]
────────────────────────────────────────────────────────────
```

*Notes: No dark patterns. Both action buttons equal prominence. No pre-selection.*

### Tier 2 — Standard (Analytics + Marketing)

```
────────────────────────────────────────────────────────────
We use cookies

We use essential cookies to make our site work. With your consent,
we'd also like to set analytics and marketing cookies to help us
improve our site and show you relevant advertising.

  [Accept all]   [Manage preferences]   [Reject non-essential]
────────────────────────────────────────────────────────────
```

*Notes: All three options must be equally prominent. "Reject" must be as easy as "Accept." Pre-expanded preference panel acceptable but not required.*

### Tier 3 — Granular preference panel

```
COOKIE PREFERENCES
──────────────────────────────────────────────────────────────
☑ Strictly necessary    [Always on — cannot disable]
  Required for the site to function.

☐ Analytics             [Toggle: OFF] ← default for non-consent
  Help us understand usage patterns to improve the site.
  Provider: [Plausible / Google Analytics / other]

☐ Marketing             [Toggle: OFF] ← default
  Personalized advertising based on your browsing.
  Providers: [list]

                          [Save preferences]
──────────────────────────────────────────────────────────────
```

---

## Non-Compliant Patterns — Refuse to Generate

| Pattern | Why non-compliant | Regulator enforcement |
|---|---|---|
| "By continuing to use this site, you accept cookies" | Not unambiguous affirmative action | CNIL, ICO, Irish DPC all reject this |
| Pre-ticked checkboxes for analytics/marketing | Planet49 CJEU C-673/17 (2019) — pre-ticked boxes invalid | Binding EU case law |
| Cookie wall (accept cookies or leave) | Coercion undermines "freely given" | EDPB Opinion 05/2019; national DPA enforcement |
| "Accept" prominent, "Reject" hidden/grey/small | Undermines freely given consent | CNIL, Spanish AEPD enforcement actions |
| No "Reject all" equivalent to "Accept all" | Must be as easy to reject as to accept | CNIL 2022 guidelines |
| Consent buried in privacy policy | Not "clear and comprehensive" | Standard enforcement position |
| Cookies firing before consent | Violates "prior consent" requirement | ICO, German DSK enforcement |
| Consent for analytics described as "anonymous" when using GA | Misleading — GA is not anonymous | Multiple DPA enforcement actions 2022-2023 |

---

## Global Privacy Control (GPC)

**Specification:** W3C Community Group. HTTP header `Sec-GPC: 1` and JavaScript `navigator.globalPrivacyControl = true`.

**Legal status by jurisdiction:**

| Jurisdiction | Legal effect | Basis |
|---|---|---|
| California | Valid CCPA opt-out of sale/sharing | Cal. Code Regs. tit. 11, § 7026 (CPPA rules) |
| Colorado | Valid universal opt-out signal | CO AG rules under CPA |
| Connecticut | Recognized opt-out signal | CTDPA regulations |
| EU/EEA | EDPB Opinion 8/2024: valid for consent withdrawal; NOT valid as initial consent | EDPB Opinion 8/2024 |
| UK | ICO guidance: legitimate user signal; honor for opt-out processing | ICO draft guidance 2023 |

**Implementation requirement:** If your product targets California, Colorado, or Connecticut users and uses third-party cookies for advertising/analytics, you must honor GPC signals:

```javascript
// Check GPC signal on page load
if (navigator.globalPrivacyControl === true || 
    document.cookie.includes('Sec-GPC=1')) {
  // User has indicated universal opt-out
  // Must not set non-essential cookies
  // Must not share data with third parties for advertising
  disableNonEssentialCookies();
  notifyThirdPartyOptOut();
}
```

---

## Consent Management Platform (CMP) Requirements

If using a CMP (OneTrust, Cookiebot, Didomi, Osano):

1. **IAB TCF v2.2 compliance** required for advertising — CMP must be registered with IAB Europe
2. **Consent records:** Store timestamp, user choice, CMP version, and purpose/vendor consent for each user. Retain for 3 years (GDPR limitation period)
3. **Vendor list:** Disclose all third-party vendors receiving consent. Update vendor list when adding new vendors
4. **Granular consent:** TCF v2.2 requires purpose-level consent, not just vendor-level

**Recommended CMPs by use case:**
- Consumer product, privacy-focused: Osano, Didomi
- Enterprise/AdTech: OneTrust, TrustArc
- Developer-friendly: Cookiebot, CookieYes
- Privacy-first (minimal UI): Panelbear, Fathom built-in

---

## Jurisdiction-Specific Cookie Requirements

**France (CNIL):** Strictest in EU. "Reject all" must be as prominent as "Accept all." Analytics exemption does NOT apply to Google Analytics without additional safeguards. 13-month consent validity maximum. Consent must be renewed after 13 months.

**Germany (DSK):** Bundesgerichtshof ruling (Cookie II, 2020): affirmative action required. Bundled consent (ticking "I agree to terms") insufficient for cookie consent. Dark patterns specifically prohibited in Telecommunications Act (TKG) 2021.

**Spain (AEPD):** "Continue browsing" does not constitute consent. Scroll/swipe does not constitute consent.

**Italy (Garante):** Issued specific cookie guidelines 2021. "Cookie walls" permitted only in limited circumstances with a paid alternative offered.

**UK (ICO):** Post-Brexit applying UK GDPR + PECR (Privacy and Electronic Communications Regulations 2003). Consulting on updated guidance — ICO 2023 draft broadly aligns with EDPB.

**United States:** No federal cookie law. California CCPA applies to opt-out signals. Utah, Virginia, Colorado, Connecticut, Texas, Montana, Oregon, Delaware have state privacy laws — some with cookie/tracking opt-out requirements. Check state-by-state for current requirements.
