# Claude's Guide: Figma to Elementor - Real Estate Website Builder

## Project Overview

This project converts natural language descriptions and design inspirations into professional Elementor Pro templates for WordPress. It was developed to create AX Capital-style luxury real estate websites.

---

## Architecture

```
figma-to-elementor/
├── app.py                      # Flask server (main entry point)
├── analyzers/
│   └── site_analyzer.py        # Analyzes inspiration websites
├── parsers/
│   ├── description_parser.py   # Parses natural language to design spec
│   └── figma_parser.py         # Legacy Figma JSON parser
├── generators/
│   ├── elementor_generator.py      # Basic Elementor generator
│   └── elementor_pro_generator.py  # Pro features generator
├── connectors/
│   └── wordpress_connector.py  # WordPress REST API integration
├── templates/
│   └── index.html              # Web UI
├── static/
│   └── css/style.css           # UI styles
└── WordPress Update Scripts/
    ├── update_services.py      # Services section updater
    ├── update_services_v2.py   # Improved version
    ├── complete_fix.py         # Services + Footer fix
    └── fullwidth_fix.py        # Full-width sections (BEST VERSION)
```

---

## Key Learnings: WordPress + Elementor Integration

### 1. WordPress REST API Authentication

```python
# Use Application Passwords (NOT regular passwords)
WP_URL = "https://your-site.com"
USERNAME = "email@example.com"
APP_PASSWORD = "xxxx xxxx xxxx xxxx xxxx xxxx"  # With spaces!

# Basic auth with requests
response = requests.get(
    f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
    auth=(USERNAME, APP_PASSWORD),
    params={"context": "edit"}  # Required to get meta data
)
```

### 2. Getting Elementor Data

```python
# Elementor data is stored in page meta
data = response.json()
meta = data.get("meta", {})
elementor_data_str = meta.get("_elementor_data", "[]")
elements = json.loads(elementor_data_str)
```

### 3. Updating Elementor Pages

```python
payload = {
    "meta": {
        "_elementor_data": json.dumps(new_elements),
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "wp-page"
    }
}

response = requests.post(
    f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
    auth=(USERNAME, APP_PASSWORD),
    json=payload
)
```

**IMPORTANT**: After API update, user must open Elementor editor and click "UPDATE" to regenerate CSS!

---

## Elementor Structure: Full-Width Sections

### The Key to Full-Width: `stretch_section`

For sections to span the full viewport (1920px+), use **SECTION elements** with `stretch_section`:

```python
{
    "id": "unique_id",
    "elType": "section",  # NOT container!
    "settings": {
        "stretch_section": "section-stretched",  # THIS IS THE KEY!
        "layout": "full_width",
        "content_width": {"size": 1400, "unit": "px"},
        "padding": {"top": "100", "right": "0", "bottom": "100", "left": "0", "unit": "px"},
        "background_background": "classic",
        "background_color": "#0a0a0f"
    },
    "elements": [
        {
            "id": "column_id",
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [
                # Your content containers go here
            ]
        }
    ]
}
```

### Container vs Section

- **Section** (`elType: "section"`): Use for full-width backgrounds with `stretch_section`
- **Container** (`elType: "container"`): Use for content layout within sections

---

## Design System: AX Capital Style

### Colors

```python
colors = {
    "dark": "#0a0a0f",           # Main background
    "gold": "#c9a962",           # Accent/highlights
    "white": "#FFFFFF",          # Headings
    "text_muted": "rgba(255,255,255,0.6)",  # Body text
    "text_subtle": "rgba(255,255,255,0.5)", # Subtle text
    "border": "rgba(255,255,255,0.15)"      # Borders
}
```

### Typography

```python
typography = {
    "heading_large": {
        "family": "Montserrat",
        "size": 48,
        "weight": "300",  # Light weight for elegance
        "letter_spacing": 1
    },
    "heading_accent": {
        "family": "Montserrat",
        "size": 13,
        "weight": "500",
        "letter_spacing": 3,
        "transform": "uppercase"
    },
    "body": {
        "family": "Montserrat",
        "size": 14,
        "weight": "400",
        "line_height": 1.6
    }
}
```

---

## Service Cards with Image Backgrounds

### Card Structure (3 per row on desktop)

```python
def create_service_card(title, desc, image_url):
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 32, "unit": "%"},  # 3 cards = ~96% + gaps
            "width_tablet": {"size": 48, "unit": "%"},  # 2 per row
            "width_mobile": {"size": 100, "unit": "%"}, # 1 per row
            "min_height": {"size": 280, "unit": "px"},
            "flex_direction": "column",
            "flex_justify_content": "flex-end",  # Content at bottom
            "border_radius": {"top": "8", "right": "8", "bottom": "8", "left": "8", "unit": "px"},
            "overflow": "hidden",
            "background_background": "classic",
            "background_image": {"url": image_url, "id": ""},
            "background_position": "center center",
            "background_size": "cover",
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {
                "horizontal": 0, "vertical": 10, "blur": 30, "spread": 0,
                "color": "rgba(0,0,0,0.3)"
            }
        },
        "elements": [{
            # Gradient overlay container
            "id": gen_id(),
            "elType": "container",
            "settings": {
                "content_width": "full",
                "padding": {"top": "100", "right": "24", "bottom": "24", "left": "24"},
                "background_background": "gradient",
                "background_color": "transparent",
                "background_color_b": "rgba(10,10,15,0.9)",
                "background_gradient_type": "linear",
                "background_gradient_angle": {"size": 180, "unit": "deg"}
            },
            "elements": [
                # Title and description widgets
            ]
        }]
    }
```

### High-Quality Real Estate Images (Unsplash)

```python
IMAGES = {
    "luxury_villa": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80",
    "dubai_skyline": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80",
    "modern_interior": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80",
    "investment": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80",
    "penthouse": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80",
    "waterfront": "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=800&q=80",
}
```

---

## Footer Structure (AX Capital Style)

```
┌────────────────────────────────────────────────────────────────────┐
│  BRAND          Nav Col 1    Nav Col 2    Nav Col 3    CONTACTS   │
│  (gold logo)    Apartments   Off-Plan     Rent         Dubai, UAE │
│                 Penthouses   Catalogs     Developers   Address    │
│                 Villas       Area Guides  Corporate    [icons]    │
│                 Townhouses   Sell         Reviews      [CALL US]  │
├────────────────────────────────────────────────────────────────────┤
│  🔍 Properties or locations                                        │
└────────────────────────────────────────────────────────────────────┘
```

---

## Running the App

### Start Server

```bash
cd /Users/antoniasepulvedagrasins/figma-to-elementor
PORT=8080 python3 app.py
```

### Update WordPress Page

```bash
python3 fullwidth_fix.py  # Best version - full-width sections
```

---

## WordPress Credentials (TEST SITE)

```
Site: https://wordpress-1097675-6048787.cloudwaysapps.com
User: grasinsantonia@gmail.com
App Password: 7Fbg xKjQ fdKi JCNk JQIv ESxr
Page ID: 110
Page URL: /test5-2/
```

---

## Common Issues & Solutions

### 1. Sections Not Full Width
**Problem**: Background doesn't span full screen
**Solution**: Use `elType: "section"` with `stretch_section: "section-stretched"`

### 2. Changes Don't Appear
**Problem**: API updates but page looks the same
**Solution**: Open Elementor editor → Click UPDATE to regenerate CSS

### 3. Cards Not 3 Per Row
**Problem**: Cards stack vertically or wrong layout
**Solution**: Use percentage widths (32%) with `flex_wrap: "wrap"` and `flex_justify_content: "space-between"`

### 4. API Auth Fails
**Problem**: 401 or connection errors
**Solution**: Use Application Password (with spaces), not regular password

---

## Version History

- **v1.0**: Initial WebBuilder AI app with basic Elementor generation
- **v1.1**: Added WordPress REST API integration
- **v1.2**: Services section with image cards
- **v1.3**: Full-width sections + AX Capital footer (CURRENT)

---

## Next Steps / TODO

- [ ] Fix services section card alignment for exact 1920px
- [ ] Add more sections (About, Testimonials, Contact form)
- [ ] Implement hover effects on cards
- [ ] Add responsive breakpoint adjustments
- [ ] Create template library system
