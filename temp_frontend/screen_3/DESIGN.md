---
name: Mission Command Glass
colors:
  surface: '#0d131f'
  surface-dim: '#0d131f'
  surface-bright: '#333947'
  surface-container-lowest: '#080e1a'
  surface-container-low: '#161c28'
  surface-container: '#1a202c'
  surface-container-high: '#242a37'
  surface-container-highest: '#2f3542'
  on-surface: '#dde2f4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dde2f4'
  inverse-on-surface: '#2a303e'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e0fdff'
  on-primary: '#00373a'
  primary-container: '#00f2fe'
  on-primary-container: '#006a70'
  inverse-primary: '#00696f'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#fff5ee'
  on-tertiary: '#472a00'
  tertiary-container: '#ffd3a1'
  on-tertiary-container: '#875400'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#ffb95f'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#653e00'
  background: '#0d131f'
  on-background: '#dde2f4'
  surface-variant: '#2f3542'
typography:
  display-hero:
    fontFamily: Space Grotesk
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.03em
  display-hero-mobile:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  title-sm:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  telemetry-value-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  telemetry-value-md:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  label-code:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  space-2xs: 0.125rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-base: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
  gutter-mobile: 0.75rem
  gutter-desktop: 1.25rem
  margin-mobile: 1rem
  margin-desktop: 2rem
---

## Brand & Style

The design system projects mission-critical authority, predictive vigilance, and split-second operational clarity. Built for hydrologists, disaster response coordinators, and automated flood defense operators, it transforms massive geospatial telemetry into decisive real-time control.

The aesthetic fuses **Tactical Command-Center / Mission Control** with **Engineered Glassmorphism**:
- Ultra-dark, layered cockpit ergonomics designed for 24/7 low-light monitoring.
- High-contrast tactical signifiers: crisp structural outlines, cold optical backdrops, and concentrated neon status accents.
- Precision instrumentation: tight tabular data alignment, active sensor telemetry markers, and ambient alert halos that draw the operator's eye directly to escalating hydraulic threats.

## Colors

The palette establishes an optical hierarchy modeled on avionics and radar systems. High-luminance accents exist purely as functional signals against light-absorbing void surfaces.

### Surface Tiers
- **Void (Root Canvas):** `#060B13` - Total floor isolation for low-light control rooms.
- **Base Canvas:** `#0B1220` - Structural shell and fixed viewport grids.
- **Surface Layer 1 (Cards):** `#0F172A` with `rgba(255, 255, 255, 0.03)` fill.
- **Surface Layer 2 (Elevated Panels):** `#1E293B` at `70%` alpha with `backdrop-filter: blur(16px)`.

### Operational Status Tokens
- **System Tech / Calibration:** Electric Cyan (`#00F2FE` / `#38BDF8`) - Nominal agent loops, telemetry lines, radar sweeps.
- **Normal / Nominal:** Emerald Neon (`#10B981`) - Sensor stabilized, safe water discharge thresholds.
- **Advisory / Warning:** Amber Spark (`#F59E0B` / `#FB923C`) - Upstream surge, rainfall velocity warning.
- **Critical / Threat:** Crimson Pulse (`#EF4444` / `#F43F5E`) - Breach imminent, automated barrier engagement required.

### Typography & Border Contrasts
- **Primary Text:** Stark White (`#F8FAFC`) - Maximum optical legibility for urgent data.
- **Secondary Text:** Slate Neutral (`#94A3B8`) - Structural metadata and unit indicators.
- **Tertiary / Sub-Data:** Darkened Slate (`#64748B`) - Timestamps and static axis rules.
- **Glass Inset Borders:** `rgba(255, 255, 255, 0.08)` baseline, switching to `rgba(0, 242, 254, 0.25)` when active.

## Typography

The typography architecture reinforces tactical separation of concerns:

1. **Strategic Titles & Directives (Space Grotesk):** Engineered geometric grotesque headers with tight tracking deliver assertive, high-tech momentum for mission commands and station identifiers.
2. **Operational Text & Reports (Inter):** Neutral, maximum-legibility sans-serif calibrated for crisp reading across dense incident logs and agent decision histories.
3. **Telemetry & Dynamic Values (JetBrains Mono):** Tabular numeric metrics, sensor readouts, timestamps, and coordinates use fixed-width mono styling to ensure fluctuating real-time figures never introduce horizontal layout jitter. All system status tags must be displayed in uppercase using `label-caps`.

## Layout & Spacing

The layout is an adaptive, density-controlled command grid. It treats visual real estate as a zero-waste telemetry plane.

- **Desktop Operations (Command View):** 12-column modular fluid grid anchored by persistent left/right tactical rails (280px to 380px fixed width) for threat escalation filters and agent action logs, flanking an auto-scaling central geospatial situational map. Gutters are locked to `1.25rem` (`20px`).
- **Data Density:** High-density default. Component paddings maintain a strict compact cadence (e.g., `space-sm` vertical, `space-md` horizontal) to maximize immediate situational visibility above the fold.
- **Breakpoints:**
  - `Desktop Tactical (>= 1440px)`: Full 3-pane command view (Agents | GIS Map & River Profiles | Incident Pipeline).
  - `Field Tablet (768px - 1439px)`: 2-pane collapsible layout. The central map remains full-canvas, with slide-over drawers for hydraulic calculations.
  - `First Responder Mobile (< 768px)`: Single-column priority stack. Telemetry values compress from horizontal arrays into card-based vertical stacks with sticky threat status headers.

## Elevation & Depth

Visual hierarchy is achieved through glassmorphism, luminescence, and precision edge-lighting rather than drop shadows.

- **Ground Plane (Z0):** Deep void (`#060B13`). Unblurred, absorbs eye strain during extended night watches.
- **Sub-Panels (Z1):** Background `#0F172A` at `75%` opacity with `backdrop-filter: blur(12px)`. Border is a crisp `1px solid rgba(255, 255, 255, 0.07)`. No outer shadow.
- **Active Interactive Cards (Z2):** Background `#1E293B` at `65%` opacity with `backdrop-filter: blur(20px)`. Border is `1px solid rgba(56, 189, 248, 0.20)`. Subtle inner glow applied via `box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.1)`.
- **Targeted / Critical Alerts (Z3):** Floating alert dialogs and agent action banners. Outer perimeter illuminated with a radial status halo:
  - Critical: `box-shadow: 0 0 24px -4px rgba(239, 68, 68, 0.35), inset 0 0 12px rgba(239, 68, 68, 0.15)`.
  - Advisory: `box-shadow: 0 0 24px -4px rgba(245, 158, 11, 0.28), inset 0 0 12px rgba(245, 158, 11, 0.12)`.
  - Tech/Calibrated: `box-shadow: 0 0 20px -4px rgba(0, 242, 254, 0.25)`.

## Shapes

The geometric architecture balances modern ergonomics with high-precision engineering:

- Standard cards, module containers, and dialog panels use **12px to 16px** radii (`rounded-lg` to `rounded-xl`).
- Micro-telemetry chips, status badges, and sensor pill tags use rounded containment (`9999px`) to immediately separate data pills from angular structural panels.
- Action triggers and command buttons use a disciplined **8px** radius (`rounded-md`), communicating immediate mechanical certainty.

## Components

### 1. Command Buttons
- **Primary / Authorize Intervention:** High-intensity electric cyan background (`#00F2FE`), text `#060B13` (bold, weight 700). Hover produces a luminous cyan flare (`box-shadow: 0 0 16px rgba(0, 242, 254, 0.6)`).
- **Secondary / Cancel / Inspect:** Translucent dark slate (`rgba(30, 41, 59, 0.7)`), text `#F8FAFC`, border `1px solid rgba(255, 255, 255, 0.12)`.
- **Emergency Override:** Crimson fill (`#EF4444`), text `#FFFFFF`, animated pulsing perimeter shadow for irreversible barriers and sirens.

### 2. Telemetry Chips & Status Badges
- Constructed with `label-caps` typography, `4px 10px` interior padding, and pill borders.
- Include a leading 6px pulsing dot indicator (`box-shadow: 0 0 8px currentColor`).
- **Normal:** Background `rgba(16, 185, 129, 0.12)`, text `#34D399`, border `1px solid rgba(16, 185, 129, 0.25)`.
- **Critical:** Background `rgba(239, 68, 68, 0.16)`, text `#F87171`, border `1px solid rgba(239, 68, 68, 0.40)`.

### 3. Glassmorphic Data Cards
- Padding: `space-base` to `space-lg`.
- Top header carries an uppercase monospace sensor/agent identifier (`label-caps`) paired with an icon glyph.
- Dynamic readouts place numerical values in `telemetry-value-lg` with the physical unit (e.g., `m³/s`, `cm/h`) set in `label-code` muted slate beside it.

### 4. Input Fields & Parameter Controls
- Background: `rgba(15, 23, 42, 0.8)`. Border: `1px solid rgba(255, 255, 255, 0.1)`.
- Focus State: Border transitions to `#00F2FE` with `box-shadow: 0 0 12px rgba(0, 242, 254, 0.25)`.
- Typography: `Inter 14px`, text `#F8FAFC`. Placeholder `#64748B`.

### 5. Checkboxes & Radio Toggles
- Square / circular controls with a recessed dark ground (`#060B13`) and `1px solid #64748B`.
- Checked state: `#00F2FE` fill with a stark black checkmark, accompanied by an ambient micro-glow.

### 6. Specialized Domain Components
- **Agent Prediction Feed:** Real-time log displaying autonomous model reasoning, confidence scores (e.g., `98.4% CONF`), and recommended valve closures with split-second countdown timers.
- **Hydraulic Sensor Sparklines:** Micro-charts embedded directly in list rows featuring glowing vector paths and gradient fills tracing baseline vs. crest levels.
- **River Gauge Threshold Bar:** Segmented horizontal progress track color-coded across Safe, Moderate, and Overflow zones with dynamic neon crest needles.