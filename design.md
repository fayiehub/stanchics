# Design Specification
## Stanchics — Women in Tech Club, Kenya
**Version:** 1.0  
**Status:** Draft  
**Follows:** requirements.md v1.0  

---

## 1. Design Philosophy

Stanchics is a community built by women in tech, for women in tech. The design should feel like walking into a room full of brilliant, warm, accomplished people — not a corporate brochure or a generic "empowerment" campaign.

**Design Direction: Soft Editorial**  
Think a beautifully laid-out magazine for modern African professional women. Warm and approachable, but with structure and confidence. Nothing generic. Nothing purple-gradient-on-white. The site should feel like it was designed *specifically* for this community — Kenyan, tech-forward, and deeply human.

**The one thing visitors should remember:** *"This feels like my people."*

---

## 2. Brand Identity

### 2.1 Club Name & Wordmark

- **Name:** Stanchics *(placeholder)*
- **Wordmark treatment:** Lowercase or mixed-case logotype in the display font — approachable, not formal
- **Tagline (suggested):** *"Women in Tech. In Community."* or *"Connecting Kenya's Women in Tech."*

### 2.2 Colour Palette

The palette is anchored in soft, sophisticated blues — complementary to Stanbic's blue heritage but feminised, warmer, and community-oriented. Supported by warm neutrals and a single accent.

| Token | Name | Hex | Usage |
|---|---|---|---|
| `--color-primary` | Soft Cornflower | `#6B9FD4` | Primary buttons, links, active nav |
| `--color-primary-dark` | Deep Slate Blue | `#3D6E9E` | Hover states, headings |
| `--color-primary-light` | Mist Blue | `#C5DCF0` | Backgrounds, card tints, section fills |
| `--color-accent` | Warm Blush | `#E8A598` | Highlight accents, CTA strips, tags |
| `--color-accent-light` | Soft Peach | `#F5DDD8` | Subtle backgrounds, hover fills |
| `--color-neutral-900` | Ink | `#1E2A35` | Body text, headings |
| `--color-neutral-600` | Slate | `#5C6F7E` | Secondary text, captions |
| `--color-neutral-200` | Fog | `#EDF1F4` | Dividers, card backgrounds |
| `--color-neutral-50` | Cream White | `#FAFBFC` | Page background |
| `--color-white` | Pure White | `#FFFFFF` | Cards, overlays |

**Colour usage rules:**
- Primary blue is the dominant brand colour — used for all interactive elements
- Warm blush (`--color-accent`) is used sparingly as a contrast accent — it should feel special, not overwhelming
- Never use more than 2 colours in a single component
- Text on blue backgrounds: always white or `--color-neutral-50`
- Text on light backgrounds: always `--color-neutral-900` or `--color-neutral-600`

### 2.3 Typography

| Role | Font | Weight | Notes |
|---|---|---|---|
| Display / Hero | **Playfair Display** | 700 (Bold) | Headings, hero text, section titles |
| Body | **DM Sans** | 400, 500 | All body copy, nav, UI labels |
| Accent / Quote | **Playfair Display** | 400 Italic | Pull quotes, member testimonials |

**Type scale (desktop):**

| Label | Size | Weight | Line Height |
|---|---|---|---|
| Hero Heading | 56px | 700 | 1.15 |
| H1 | 40px | 700 | 1.2 |
| H2 | 32px | 700 | 1.25 |
| H3 | 22px | 500 | 1.3 |
| Body Large | 18px | 400 | 1.65 |
| Body | 16px | 400 | 1.7 |
| Small / Caption | 13px | 400 | 1.5 |
| Button | 15px | 500 | — |

**Type scale (mobile):** Scale down hero to 36px, H1 to 28px, H2 to 24px. All body sizes remain the same.

**Google Fonts import:**
```
https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@400;500&display=swap
```

### 2.4 Spacing System

Uses an 8px base grid. All spacing values are multiples of 8.

| Token | Value | Usage |
|---|---|---|
| `--space-2` | 8px | Tight internal padding |
| `--space-3` | 16px | Component internal spacing |
| `--space-4` | 24px | Card padding |
| `--space-5` | 32px | Between related elements |
| `--space-6` | 48px | Section sub-spacing |
| `--space-7` | 64px | Section padding (mobile) |
| `--space-8` | 96px | Section padding (desktop) |
| `--space-9` | 128px | Hero vertical padding |

### 2.5 Border Radius

| Token | Value | Usage |
|---|---|---|
| `--radius-sm` | 6px | Buttons, input fields |
| `--radius-md` | 12px | Cards |
| `--radius-lg` | 20px | Feature cards, modals |
| `--radius-full` | 9999px | Pills, avatar rings, tags |

### 2.6 Shadows

```css
--shadow-sm: 0 1px 3px rgba(61, 110, 158, 0.08);
--shadow-md: 0 4px 16px rgba(61, 110, 158, 0.10);
--shadow-lg: 0 12px 40px rgba(61, 110, 158, 0.14);
```

Use `--shadow-md` on cards. Use `--shadow-lg` for modals and featured elements.

---

## 3. Layout System

### 3.1 Grid

| Breakpoint | Columns | Gutter | Max Content Width |
|---|---|---|---|
| Mobile (`<768px`) | 4 | 16px | 100% |
| Tablet (`768–1024px`) | 8 | 24px | 100% |
| Desktop (`>1024px`) | 12 | 32px | 1200px |

Page wrapper: `max-width: 1200px; margin: 0 auto; padding: 0 24px;`

### 3.2 Section Anatomy

Every page section follows this structure:
- **Top padding:** `--space-8` (desktop) / `--space-7` (mobile)
- **Bottom padding:** `--space-8` (desktop) / `--space-7` (mobile)
- **Section label** (optional): small uppercase tag in `--color-primary` above the heading
- **Section heading:** H2 in Playfair Display
- **Section subheading** (optional): Body Large in `--color-neutral-600`
- **Content:** varies by section

---

## 4. Component Library

### 4.1 Buttons

**Primary Button** (used for main CTAs like "Join the Community")
```
Background: --color-primary
Text: white
Padding: 14px 28px
Border radius: --radius-sm
Font: DM Sans 500, 15px
Hover: background --color-primary-dark, translate Y -1px
Transition: all 200ms ease
```

**Secondary Button** (used for "Learn More", "View Event")
```
Background: transparent
Border: 1.5px solid --color-primary
Text: --color-primary
Padding: 13px 27px
Hover: background --color-primary-light
```

**Accent Button** (used in CTA strips)
```
Background: --color-accent
Text: white
Padding: 14px 28px
Hover: filter brightness(0.92)
```

**Ghost Button** (low-emphasis actions)
```
Background: transparent
Text: --color-neutral-600
Underline on hover
No border
```

### 4.2 Cards

**Member Spotlight Card**
```
Background: white
Border radius: --radius-md
Shadow: --shadow-md
Padding: --space-4
Layout:
  - Circular avatar (80px × 80px), ring in --color-primary-light
  - Name: DM Sans 500, 17px, --color-neutral-900
  - Title / Company: DM Sans 400, 14px, --color-neutral-600
  - Quote: Playfair Display italic, 15px, --color-neutral-600
Hover: shadow --shadow-lg, translate Y -2px
```

**Event Card**
```
Background: white
Border radius: --radius-md
Shadow: --shadow-sm
Padding: --space-4
Top accent bar: 4px, --color-primary (or --color-accent for featured)
Layout:
  - Event type tag (pill): background --color-primary-light, text --color-primary-dark
  - Event title: H3
  - Date + location: small, --color-neutral-600, with icons
  - Short description: body
  - CTA button: secondary style
Hover: shadow --shadow-md
```

**Pillar / Activity Card**
```
Background: --color-neutral-50
Border: 1px solid --color-neutral-200
Border radius: --radius-lg
Padding: --space-5
Layout:
  - Icon: 40px, in --color-primary
  - Title: DM Sans 500, 18px
  - Description: body, --color-neutral-600
Hover: background --color-primary-light, border-color --color-primary-light
```

### 4.3 Form Inputs

```
Height: 48px
Padding: 0 16px
Border: 1.5px solid --color-neutral-200
Border radius: --radius-sm
Font: DM Sans 400, 16px
Background: white
Focus: border-color --color-primary, box-shadow 0 0 0 3px rgba(107,159,212,0.15)
Placeholder: --color-neutral-600
```

**Textarea:** Same styles, min-height 120px, padding 12px 16px.

**Labels:** DM Sans 500, 14px, `--color-neutral-900`, margin-bottom 6px.

**Error state:** border-color `#D94F4F`, small error message below in 12px red.

### 4.4 Navigation Bar

```
Background: white
Border-bottom: 1px solid --color-neutral-200
Height: 72px
Layout: logo left | nav links centre | "Join Us" button right
Position: sticky top:0, z-index 100
Backdrop filter: blur(8px) (subtle glass effect on scroll)

Nav links:
  Font: DM Sans 500, 15px
  Color: --color-neutral-600
  Active / Hover: --color-primary
  Active underline: 2px solid --color-primary, bottom

Mobile (< 768px):
  Hamburger icon (right side)
  Full-screen slide-in drawer from right
  Links stacked vertically, large touch targets
  "Join Us" button at bottom of drawer
```

### 4.5 Footer

```
Background: --color-neutral-900 (Ink)
Text: --color-neutral-200
Padding: --space-8 0 --space-5

Layout (3 columns on desktop, stacked on mobile):
  Col 1: Logo + tagline + location badge ("Nairobi, Kenya 🇰🇪")
  Col 2: Quick links (Home, About, Events, Community, Contact)
  Col 3: Newsletter signup (email input + button)

Bottom bar:
  Border-top: 1px solid rgba(255,255,255,0.1)
  Copyright text (left) | "Made with ❤️ in Nairobi" (right)
  Font size: 13px, --color-neutral-600
```

### 4.6 Section CTA Strip

Used on Home page between sections to drive signups.

```
Background: --color-primary (or gradient: --color-primary → --color-primary-dark)
Text: white
Padding: --space-7 --space-4
Layout: centred
  - Heading: Playfair Display 700, 32px, white
  - Subheading: DM Sans 400, 17px, rgba(255,255,255,0.85)
  - Input + button inline (desktop) / stacked (mobile)
  - Privacy note: 12px, rgba(255,255,255,0.65)
```

### 4.7 Tags / Pills

```
Display: inline-flex
Padding: 4px 12px
Border radius: --radius-full
Font: DM Sans 500, 12px
Uppercase, letter-spacing: 0.05em

Variants:
  Blue:  background --color-primary-light, text --color-primary-dark
  Blush: background --color-accent-light, text #B05C50
  Neutral: background --color-neutral-200, text --color-neutral-600
```

### 4.8 Avatar

```
Circular: border-radius 50%
Ring: 2px solid --color-primary-light, offset 2px
Sizes: 40px (small), 64px (medium), 96px (large)
Fallback: initials on --color-primary-light background, text --color-primary-dark
```

---

## 5. Page-by-Page Design Specs

---

### 5.1 Home Page

**Section 1: Hero**
```
Background: --color-neutral-50 with a soft radial gradient (--color-primary-light at 10% opacity) top-right
Min-height: 85vh
Layout: Two column (desktop) — text left (6 cols), image right (6 cols)
          Single column stacked (mobile) — image above fold, text below

Left column:
  - Small tag: "Women in Tech · Kenya" (blue pill)
  - H1 Headline: Playfair Display 700, 56px
    Suggested: "Tech is better when we're all in the room."
  - Body Large subheading: 18px, --color-neutral-600, max-width 480px
  - CTA row: [Primary Button "Join the Community"] [Secondary Button "Learn More"]
  - Social proof micro-line: "Join [X] women already in the community" (placeholder)

Right column:
  - Warm lifestyle/community photo (real people preferred)
  - Photo treatment: border-radius --radius-lg, slight warm overlay
  - Optional: floating stat card overlaid bottom-left of photo
    (e.g. "1st Meetup · Feb 2026", small card in white with shadow)
```

**Section 2: What We're About**
```
Background: white
Layout: centred, max-width 720px
  - Section label: "Our Story"
  - H2: "A community still being written — by us."
  - 2–3 paragraphs of warm, honest copy about the club's early stage
  - No CTA (let it breathe)
```

**Section 3: What We Do (Pillars)**
```
Background: --color-neutral-50
Layout: 2×2 grid (desktop), stacked (mobile)
4 Pillar cards: Talks & Panels | Meetups | Conferences | Outreach
Card icons: simple line icons in --color-primary
```

**Section 4: Member Spotlight**
```
Background: white
Layout: section label + H2 centred, then horizontal scroll row of cards (desktop: 3 visible)
3 member spotlight cards
CTA below: "See the Community →" → links to Community page
```

**Section 5: Newsletter / Join CTA Strip**
```
Background: gradient --color-primary → --color-primary-dark
Full width
Email signup inline form
```

---

### 5.2 About Page

**Section 1: Page Hero (sub-hero)**
```
Background: --color-primary-light (soft blue wash)
Height: 320px
Layout: centred
  - Section label: "About Us"
  - H1: "We're building something real."
  - Subheading body text
```

**Section 2: Our Story**
```
Background: white
Two-column layout: text left (7 cols), accent visual right (5 cols)
Accent visual: soft illustrated abstract shape or collage placeholder
```

**Section 3: Mission & Vision**
```
Background: --color-neutral-50
Two cards side by side (desktop), stacked (mobile)
  Mission card: --color-primary top border (4px), white background
  Vision card: --color-accent top border (4px), white background
Each: icon, title, paragraph text
```

**Section 4: Our Values**
```
Background: white
Horizontal list of 4–5 value items
Each: number (01, 02…) in large faded blue text behind the title (decorative), title, description
Desktop: 2-column staggered layout
```

**Section 5: The Team**
```
Background: --color-neutral-50
3–5 member cards in a row (desktop), 2 column (tablet), 1 column (mobile)
Card: photo, name, club role, job title
```

---

### 5.3 Events Page

**Section 1: Page Hero**
```
Background: --color-neutral-900 (dark, moody contrast from other pages)
Text: white
Height: 280px
Centred layout
H1: "Events & Gatherings"
Subheading: "Where the community comes alive."
```

**Section 2: Upcoming Events**
```
Background: --color-neutral-50
Event cards in a vertical list (desktop: 2 column grid, mobile: 1 column)
Empty state (if no events):
  Illustration placeholder + "Something's coming soon." heading
  Newsletter signup inline
```

**Section 3: Past Events**
```
Background: white
Lighter card treatment (greyed out CTA replaced by "View Recap")
Collapsible section — hidden by default, "Show Past Events" toggle
```

**Section 4: Host or Suggest an Event**
```
Background: --color-accent-light (warm peach)
Centred, max-width 640px
H2 + body copy + Secondary button "Get in Touch →"
```

---

### 5.4 Community / Members Page

**Section 1: Page Hero**
```
Background: gradient from --color-primary-light (top) to white (bottom)
Height: 340px
Centred
H1: "The Women of Stanchics"
Subheading: warm description of the community
```

**Section 2: Member Spotlights Grid**
```
Background: white
3-column grid (desktop), 2-column (tablet), 1-column (mobile)
Member spotlight cards
```

**Section 3: Community Guidelines**
```
Background: --color-neutral-50
Single column, max-width 720px, centred
H2 + paragraph text
Styled as a warm "welcome letter", not a terms list
```

**Section 4: Join / Membership Form**
```
Background: white
Two-column layout: left — warm copy about joining; right — the form
Form fields:
  - Full Name (text)
  - Email (email)
  - Job Title (text)
  - Company (text)
  - LinkedIn URL (text, optional)
  - What draws you to Stanchics? (textarea, optional)
Submit: Primary button "Join the Community"
Post-submit: Inline success message (no page reload)
  "🎉 Welcome! We'll be in touch soon."
```

---

### 5.5 Contact Page

**Section 1: Page Hero**
```
Background: white
Height: auto (minimal)
H1: "Say Hello"
Subheading: 1 sentence
```

**Section 2: Contact Split Layout**
```
Background: white
Two column (desktop): left — contact info + warm copy; right — contact form
Left:
  - "Who should reach out": General Inquiry, Partnerships, Event Proposals, Press
  - Email address (styled with icon)
  - Location: "Nairobi, Kenya 🇰🇪"
Right — Contact Form:
  - Name, Email
  - Subject (dropdown: General / Partnership / Event Proposal / Press / Other)
  - Message (textarea)
  - Submit: Primary button "Send Message"
  - Post-submit inline confirmation
```

---

## 6. Motion & Interaction

### Page Load
- Nav fades in: `opacity 0 → 1`, `200ms`
- Hero headline: slides up from `translateY(20px)`, `400ms ease-out`, `100ms delay`
- Hero subheading: same, `200ms delay`
- Hero CTA buttons: same, `300ms delay`
- Hero image: fades in, `500ms`, `150ms delay`

### Scroll Animations
- Section headings: `fadeInUp` on first viewport entry (Intersection Observer)
- Cards: staggered `fadeInUp` with `100ms` between each card

### Hover States
- All buttons: `transform: translateY(-1px)` + shadow deepening, `150ms`
- Cards: `transform: translateY(-2px)` + shadow upgrade, `200ms`
- Nav links: colour transition `200ms`

### Form
- Input focus: border colour + glow ring, `150ms`
- Submit button: loading spinner while submitting
- Success message: slides down from above with `fadeInDown`, `300ms`

**CSS animation base:**
```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

---

## 7. Iconography

- **Icon library:** [Lucide Icons](https://lucide.dev/) — clean, consistent line icons
- **Size:** 20px default, 24px for feature icons, 40px for pillar cards
- **Colour:** Always matches surrounding text or uses `--color-primary`
- **Icons to use:**
  - Events: `calendar`, `map-pin`, `clock`
  - Community: `users`, `heart`, `star`
  - Contact: `mail`, `send`
  - Pillars: `mic`, `coffee`, `presentation`, `globe`
  - Nav: `menu`, `x` (close), `arrow-right`

---

## 8. Imagery Guidelines

- **Style:** Candid, warm, authentic — real people in real moments
- **Subject:** Women working, collaborating, networking, presenting
- **Representation:** Diverse — varied ages, roles, backgrounds; Kenyan/African context preferred
- **Treatment:** 
  - No heavy filters
  - Slight warmth (+5 temperature in editing)
  - Photos on `--color-primary-light` or `--color-neutral-50` backgrounds look best
- **Aspect ratios:**
  - Hero: 3:2 or 4:3 landscape
  - Member avatars: 1:1 (square, displayed as circle)
  - Event cards: 16:9
- **Placeholder:** Use [UI Avatars](https://ui-avatars.com/) for member photo placeholders in development

---

## 9. Responsive Behaviour Summary

| Element | Desktop | Tablet | Mobile |
|---|---|---|---|
| Nav | Horizontal links | Horizontal (compact) | Hamburger drawer |
| Hero | 2-column | 2-column | 1-column (stacked) |
| Pillar cards | 2×2 grid | 2×2 grid | 1 column |
| Member cards | 3-column | 2-column | 1-column |
| Event cards | 2-column | 2-column | 1-column |
| Contact / Form split | 2-column | 1-column (stacked) | 1-column |
| Footer | 3-column | 2-column | 1-column |
| CTA strip form | Inline (input + button) | Inline | Stacked |

---

## 10. Accessibility

- All colour pairings meet **WCAG AA** contrast (4.5:1 for text, 3:1 for large text and UI)
- All interactive elements have visible `:focus` states (blue glow ring)
- All images have descriptive `alt` text
- Form fields have associated `<label>` elements
- Navigation is keyboard-navigable with logical tab order
- Animations respect `prefers-reduced-motion` — disable all transitions/animations when set

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 11. Tech Stack for Implementation

| Layer | Technology | Notes |
|---|---|---|
| Frontend | HTML5 + CSS3 + Vanilla JS *or* React | Decision TBD at coding stage |
| Fonts | Google Fonts (Playfair Display + DM Sans) | Self-host for performance in v2 |
| Icons | Lucide Icons (CDN) | `https://unpkg.com/lucide@latest` |
| Backend | Node.js/Express or Python/FastAPI | Hosted on Azure App Service (Free) |
| Database | Azure SQL Database (Free tier) | Stores: members, contact submissions |
| Email/Newsletter | Mailchimp API | Free up to 500 contacts |
| Deployment | Azure App Service (Free F1 tier) | `stanchics.azurewebsites.net` |

---

## 12. CSS Variables — Master Reference

```css
:root {
  /* Colours */
  --color-primary:        #6B9FD4;
  --color-primary-dark:   #3D6E9E;
  --color-primary-light:  #C5DCF0;
  --color-accent:         #E8A598;
  --color-accent-light:   #F5DDD8;
  --color-neutral-900:    #1E2A35;
  --color-neutral-600:    #5C6F7E;
  --color-neutral-200:    #EDF1F4;
  --color-neutral-50:     #FAFBFC;
  --color-white:          #FFFFFF;

  /* Typography */
  --font-display:  'Playfair Display', Georgia, serif;
  --font-body:     'DM Sans', system-ui, sans-serif;

  /* Spacing */
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 24px;
  --space-5: 32px;
  --space-6: 48px;
  --space-7: 64px;
  --space-8: 96px;
  --space-9: 128px;

  /* Radius */
  --radius-sm:   6px;
  --radius-md:   12px;
  --radius-lg:   20px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(61, 110, 158, 0.08);
  --shadow-md: 0 4px 16px rgba(61, 110, 158, 0.10);
  --shadow-lg: 0 12px 40px rgba(61, 110, 158, 0.14);

  /* Transitions */
  --transition-fast:   150ms ease;
  --transition-normal: 200ms ease;
  --transition-slow:   300ms ease;
}
```

---

*This design specification is the source of truth for implementation. Any deviations during the coding stage should be documented and fed back into this document.*
