# Minimalist Design System

This design system serves as the single source of truth for the project's aesthetics. It is based on a structured, high-contrast, industrial, and minimalist design language. 

**Whenever implementing new UI components, features, or writing CSS, strictly adhere to the guidelines below.**

## Color Palette

The color scheme relies on subtle shades of white/gray for depth and a stark contrast with near-black elements to draw focus.

| Use Case | Hex Code | Description |
| :--- | :--- | :--- |
| **Primary Background** | `#F9F9F9` | Soft off-white. The base layer of the website, providing subtle depth. |
| **Surface/Header** | `#FFFFFF` | Pure white. Used for elevated containers, navigation bars, and content cards resting on the base background. |
| **Primary Text** | `#111111` | Near-black. High contrast text used for main headers, navigation links, and crucial information. |
| **Secondary Text** | `#666666` | Medium gray. Used for descriptive text, subtitles, meta-information, and placeholder text. |
| **Accent & Primary Action** | `#1A1A1A` | Dark charcoal. Used for primary call-to-action buttons (like "Shop Now") and solid focal blocks. |
| **Borders & Dividers** | `#EAEAEA` | Subtle gray. Used for separation lines, subtle borders, and structure definitions. |


## Typography

* **Font Family:** A modern, clean, Neo-grotesque Sans-Serif font such as `Inter`, `Helvetica Neue`, or `Roboto`.
* **Hierarchy:**
  * **Headers:** Sharp, occasionally heavier weights (DemiBold or Bold), but very clean without excessive kerning.
  * **Body Text:** Light or Regular weights. Clean spacing. Do not make body text too bold.
  * **Interactive/Labels:** ALL-CAPS styling for tiny tags or structural labels (e.g., `NEW`, `TECHNICAL SPECIFICATIONS`) with increased letter spacing.

## Layout & Composition Rules

1. **Abundant Whitespace:** Elements should have plenty of "breathing room." Do not crowd content. Wide padding is necessary. 
2. **Sharp Geometry:** Elements should feel precise and engineered.
   * **Border Radius:** `0px` to `4px` absolute maximum. Buttons and containers should primarily be sharp rectangles.
3. **Subtle Elevation:** Do not rely on heavy drop-shadows. Use background color differences (`#F9F9F9` vs `#FFFFFF`) and very, very subtle 1px borders (`#EAEAEA`) to distinguish surfaces.
4. **Dividers:** Use thin vertical or horizontal strokes (1px solid `#EAEAEA`) to establish structural boundaries between content blocks instead of heavy colored blocks.

## Interaction & Animation Rules

* Use highly responsive but subtle interactions.
* **Hover States:** Instead of completely changing primary button colors, consider subtle opacity shifts, slight scale-ups (e.g., `transform: scale(1.02)`), or thin sharp borders appearing. 
* Animations should feel snapping and precise, not slow and bouncy.
