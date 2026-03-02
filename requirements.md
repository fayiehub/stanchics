# Website Requirements Document
## Women in Tech Club — Kenya
**Version:** 1.0  
**Status:** Draft  
**Last Updated:** March 2026  

---

## 1. Project Overview

This document outlines the requirements for the official website of a nascent Women in Tech club based in Kenya. The club is in its early stages — it has held one introductory meeting and is still developing its formal mission, vision, and agenda. The website should reflect both the club's current state (community-first, people-forward) and its aspirational trajectory (talks, meetups, conferences, community outreach).

The site should feel **warm, welcoming, and human** — not corporate or overly polished. It should inspire women already working in tech to join, get involved, and feel seen.

---

## 2. Goals & Success Metrics

### Primary Goal
Convert site visitors into club members (newsletter signups / membership form submissions).

### Secondary Goals
- Communicate the club's purpose and values clearly, even while they are still evolving
- Build credibility and community trust from day one
- Provide a home for future events, resources, and stories

### Success Metrics
- Membership form/newsletter signups
- Event RSVPs
- Return visitor rate (community engagement)
- Time on page (especially About and Community pages)

---

## 3. Target Audience

**Primary:** Women already working in tech in Kenya — engineers, product managers, designers, data professionals, founders, and more.

**Secondary:** Women-led tech organisations, potential sponsors/partners, and community allies who may want to support the club.

> Note: The site is not targeting women trying to break into tech (that may evolve later). The tone should resonate with experienced professionals, not beginners.

---

## 4. Design Direction

| Attribute | Direction |
|---|---|
| Vibe | Warm, community-feel — not clinical or corporate |
| Tone | Conversational, empowering, inclusive |
| Visual style | Bright but grounded; human photography; generous whitespace |
| Typography | Friendly and readable; mix of a display font and a clean sans-serif |
| Colour palette | Warm tones (terracotta, warm gold, soft cream) with a grounding neutral — inspired by African warmth without being clichéd |
| Imagery | Real people, candid community photos, diverse representation |
| Avoid | Stock photo inauthenticity, heavy dark themes, overly techy/masculine aesthetics |

---

## 5. Site Architecture

The website consists of five core pages:

```
Home
├── About Us
├── Events
├── Community / Members
└── Contact Us
```

No authentication or login is required for v1. All pages are publicly accessible.

---

## 6. Page-by-Page Requirements

---

### 6.1 Home / Landing Page

**Purpose:** Make an immediate, emotional connection with visitors and drive them to sign up.

#### Sections

**Hero**
- Full-width section with a bold, short headline (e.g. *"Tech is better when we're all in the room."*)
- 1–2 sentence subheading describing the club
- Primary CTA button: **"Join the Community"** → links to membership form
- Background: warm lifestyle photo or illustrated pattern (not a generic stock image)

**What We're About (Mission Teaser)**
- 2–3 sentence informal description of the club's purpose
- Acknowledge that the club is early-stage and being shaped by its members — lean into this as a strength ("You get to help build this")
- Secondary CTA: **"Learn More"** → links to About page

**Pillars / What We Do**
- 3–4 icon + label cards representing the club's activities:
  - Talks & Panels
  - Meetups & Networking
  - Conferences
  - Community Outreach
- Each card has a 1-sentence description
- Note: these are aspirational for now; copy should use forward-looking language ("We're building toward…")

**Member Spotlight (Future-ready, initially placeholder)**
- A rotating or featured card highlighting one member
- Fields: photo, name, job title, company, one quote
- V1 can show 1–2 founding members or be hidden until populated

**Newsletter / Membership CTA Strip**
- Full-width warm-coloured band
- Headline: e.g. *"Be part of something being built."*
- Email input + **"Sign Me Up"** button
- Privacy note: "No spam. Just community."

**Footer Preview**
- Quick links to all pages
- Social media icons (placeholder for now)
- Location: Kenya 🇰🇪

---

### 6.2 About Us

**Purpose:** Tell the club's story authentically, even when that story is just beginning.

#### Sections

**Our Story**
- Narrative paragraph(s) about how and why the club started
- Honest about being early-stage — frame it as an exciting foundation moment
- Placeholder copy to be replaced once the club formalises its narrative

**Mission & Vision**
- Two clearly labelled blocks
- V1: Use placeholder/draft text with a note that these are being developed collaboratively
- Design should make it easy to update these later

**Our Values**
- 3–5 values, each with a title and 1–2 sentence description
- Suggested (to be confirmed by the club):
  - Community First
  - Authenticity
  - Lifting As We Climb
  - Curiosity & Growth
  - Inclusive Excellence

**The Team / Core Members**
- Grid of founding/core member cards
- Fields per card: photo, name, role in club (e.g. Organiser), day job title
- V1: Can start with 3–5 people

**Join the Conversation CTA**
- Inline CTA to join the club or attend the next event

---

### 6.3 Events

**Purpose:** Inform members about upcoming events and archive past ones.

#### Sections

**Upcoming Events**
- Card-based list of upcoming events
- Each card includes: event title, type (Talk / Meetup / Conference / Outreach), date, location (physical or virtual), short description, **"Register / RSVP"** button
- V1: If no events are scheduled yet, show a "Stay tuned — something's coming" placeholder with newsletter signup

**Past Events**
- Collapsible or separate tab for past events
- Lighter card style; replace CTA with "View Recap" (links to a blog post or photo album — future feature)
- V1: Can be hidden or show empty state gracefully

**Event Types Legend**
- Small visual key explaining the types of events the club runs
- Helps set expectations for what kind of community this is

**Host or Suggest an Event**
- Short CTA for members who want to propose a talk or sponsor a venue
- Links to Contact page or a simple suggestion form

---

### 6.4 Community / Members

**Purpose:** Celebrate the people in the club and make members feel seen and proud to belong.

#### Sections

**Community Intro**
- Short warm paragraph about what kind of community this is
- Emphasise: peer support, knowledge-sharing, real connections

**Member Spotlights**
- Grid or carousel of member feature cards
- Each card: photo, name, title/company, 1 line about what they work on or love about tech
- V1: Can start with 3–6 founding members; designed to scale

**By the Numbers (Future-ready)**
- Stats strip: e.g. Members, Events Held, Industries Represented
- V1: Can be hidden or show aspirational/placeholder numbers with a note

**Community Guidelines / Who We Are**
- Brief, warm description of the community's norms and who it's for
- Not a formal legal document — just a human statement of what behaviour the club values

**Join CTA**
- Prominent membership form or link
- Fields (V1): Full name, email, job title, company, LinkedIn (optional), "Why do you want to join?" (optional open text)
- On submit: confirmation message / email (email integration TBD)

---

### 6.5 Contact Us

**Purpose:** Give visitors a clear, low-friction way to get in touch.

#### Sections

**Contact Intro**
- Short friendly paragraph: who should reach out and why (e.g. partnerships, event proposals, press, general questions)

**Contact Form**
- Fields: Name, Email, Subject (dropdown: General Inquiry / Partnership / Event Proposal / Press / Other), Message
- Submit button: **"Send Message"**
- On submit: confirmation message

**Alternative Contact**
- Email address (to be added)
- Social media links (to be added)

**Location**
- "Based in Nairobi, Kenya 🇰🇪"
- Optional: Embedded map or city illustration (no specific office address needed for v1)

---

## 7. Global Components

### Navigation Bar
- Logo / Club name (left)
- Nav links: Home, About, Events, Community, Contact (centre or right)
- Primary CTA button: **"Join Us"** (always visible)
- Mobile: hamburger menu
- Sticky on scroll

### Footer
- Club name / logo
- Short tagline
- Quick links (all pages)
- Social icons (Instagram, LinkedIn, X/Twitter — placeholders for v1)
- "Based in Nairobi, Kenya 🇰🇪"
- Copyright line

### Membership / Sign-Up Form (Global Component)
- Can appear as a page section, modal, or standalone page
- Fields: Name, Email, Job Title, (optional) LinkedIn
- Simple, low-friction — not a lengthy application
- Should feel like joining a community, not applying for a job

---

## 8. Content Requirements

| Page | Content Owner | V1 Status |
|---|---|---|
| Home hero copy | Club founders | Placeholder — needs real copy |
| Mission & Vision | Club collectively | TBD — being developed |
| Member bios & photos | Individual members | Collect from founding members |
| Events | Organising team | Empty state for v1 |
| Community guidelines | Core team | Draft suggested above |
| Contact details | Admin | To be confirmed |

---

## 9. Functional Requirements

| Feature | Priority | Notes |
|---|---|---|
| Membership / email signup form | Must Have | Minimal fields; confirmation on submit |
| Event listing | Must Have | Static cards for v1 |
| Responsive design (mobile-first) | Must Have | Primary audience likely on mobile |
| Contact form | Must Have | Basic form with email routing |
| Social media links | Should Have | Placeholder icons for v1 |
| Member spotlight section | Should Have | Manually curated for v1 |
| Event RSVP / registration | Should Have | Can link to external tool (e.g. Eventbrite) for v1 |
| Newsletter integration | Should Have | e.g. Mailchimp or ConvertKit |
| Blog / Resources section | Nice to Have | Not in v1; design should allow for future addition |
| Member login / portal | Not in scope | Future phase |
| Payments / dues | Not in scope | Future phase |

---

## 10. Technical Considerations

- **Hosting:** Azure App Service (Free tier, F1) for v1
- **Database:** Azure SQL Database or Azure Cosmos DB (Free tier) — a proper backend DB from day one so member and event data is ready for v2 without migration headaches. All form submissions (membership signups, contact, event RSVPs) write to this DB
- **CMS:** No dedicated CMS for v1. Since the site owner is technical and will handle updates directly, content (events, member spotlights) can be managed via the database or simple admin tooling. Revisit in v2 if a non-technical co-admin joins
- **Backend:** Lightweight REST API (e.g. Node.js/Express or Python/FastAPI) hosted on the same Azure App Service, handling form submissions and DB reads/writes
- **Email / Newsletter:** Recommend **Mailchimp** (free up to 500 contacts) — easy to manage, no coding required for campaigns, and integrates simply via API for signup forms. Alternative: **Brevo (formerly Sendinblue)** which has a more generous free tier
- **Analytics:** Add basic analytics from day one (e.g. Plausible or Google Analytics)
- **Performance:** Optimise images; target Lighthouse score >85
- **Accessibility:** WCAG 2.1 AA compliance minimum
- **Domain:** No custom domain for v1; will use the default Azure-assigned URL (e.g. `stanchics.azurewebsites.net`). A custom domain should be purchased before any public launch or promotion

---

## 11. Out of Scope (V1)

- Member login / dashboard
- Paid membership or dues collection
- Blog / resource library
- Job board
- Forum or community chat
- Multi-language support
- Event livestreaming

---

## 12. Resolved Decisions (from Open Questions)

| # | Question | Decision |
|---|---|---|
| 1 | Club name | **Stanchics** (placeholder — to be confirmed) |
| 2 | Primary contact email | Site owner's personal email (to be configured in backend env variables) |
| 3 | Social media platforms | On hold — social icons omitted from v1 |
| 4 | Domain name | No custom domain for v1; Azure default URL. Purchase before public launch |
| 5 | Newsletter platform | **Mailchimp** recommended (free up to 500 contacts, easy to manage) |
| 6 | Site updates owner | Site owner will manage all content updates post-launch |
| 7 | Brand colours | Soft, approachable blues as primary — complementary to Stanbic's blue palette but feminised and warmer. Full palette defined in design.md |

---

## 13. Next Steps

1. ✅ Finalise requirements (this document)
2. ⬜ Answer open questions (Section 12)
3. ⬜ Create design file (wireframes → high-fidelity mockups)
4. ⬜ Review and approve design
5. ⬜ Develop site
6. ⬜ Content population (copy, photos, member bios)
7. ⬜ QA & testing
8. ⬜ Launch 🚀

---

*This document is a living draft. It should be updated as the club's mission, vision, and structure are formalised.*
