#!/usr/bin/env python3
"""
ULTIMATE V1 TEMPLATE - Desktop-Optimized Elementor Generator
============================================================
This is the LOCKED, PERFECTED template based on the final desktop version.
All future pages should match this quality and structure.

Key Features:
- Full-width sections (1920px stretch via elType: "section" + stretch_section)
- Service cards: 6 cards, 3 per row (32% width with responsive breakpoints)
- Gradient overlays on image cards for text readability
- AX Capital-style footer with 5 columns
- Montserrat typography system
- Color system: Dark (#0a0a0f), Gold (#c9a962)
- High-quality Unsplash images

Version: 1.0 ULTIMATE
Date: December 2024
"""

import json
import random
import string

# =============================================================================
# DESIGN SYSTEM CONSTANTS - DO NOT MODIFY
# =============================================================================

COLORS = {
    'dark': '#0a0a0f',
    'dark_alt': '#0d0d12',
    'gold': '#c9a962',
    'white': '#FFFFFF',
    'text_muted': 'rgba(255,255,255,0.7)',
    'text_subtle': 'rgba(255,255,255,0.5)',
    'text_faint': 'rgba(255,255,255,0.4)',
    'border_subtle': 'rgba(255,255,255,0.1)',
    'border_faint': 'rgba(255,255,255,0.08)',
    'card_bg': 'rgba(255,255,255,0.03)',
    'gold_bg': 'rgba(201,168,124,0.15)',
}

TYPOGRAPHY = {
    'font_family': 'Montserrat',
    'h1_size': 56,
    'h2_size': 48,
    'h3_size': 36,
    'h4_size': 20,
    'body_size': 16,
    'small_size': 14,
    'label_size': 13,
    'micro_size': 12,
}

SPACING = {
    'section_padding': 100,
    'container_padding': 40,
    'card_gap': 24,
    'element_gap': 20,
}

# High-quality Unsplash images for real estate
IMAGES = {
    'hero': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=1920&q=80',
    'services': [
        'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80',
        'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80',
        'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80',
        'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80',
        'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80',
        'https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=800&q=80',
    ]
}


def gen_id():
    """Generate unique Elementor element ID"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))


# =============================================================================
# ULTIMATE SERVICE CARD - 3 PER ROW WITH IMAGE + GRADIENT
# =============================================================================

def create_service_card(title, description, image_url):
    """
    Service card optimized for 3-per-row layout
    - 32% width on desktop
    - 48% width on tablet
    - 100% width on mobile
    - Background image with gradient overlay
    """
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 32, "unit": "%"},
            "width_tablet": {"size": 48, "unit": "%"},
            "width_mobile": {"size": 100, "unit": "%"},
            "min_height": {"size": 280, "unit": "px"},
            "flex_direction": "column",
            "flex_justify_content": "flex-end",
            "padding": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": True},
            "border_radius": {"top": "8", "right": "8", "bottom": "8", "left": "8", "unit": "px", "isLinked": True},
            "overflow": "hidden",
            "background_background": "classic",
            "background_image": {"url": image_url, "id": ""},
            "background_position": "center center",
            "background_size": "cover",
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {
                "horizontal": 0,
                "vertical": 10,
                "blur": 30,
                "spread": 0,
                "color": "rgba(0,0,0,0.3)"
            }
        },
        "elements": [{
            "id": gen_id(),
            "elType": "container",
            "settings": {
                "content_width": "full",
                "padding": {"top": "100", "right": "24", "bottom": "24", "left": "24", "unit": "px", "isLinked": False},
                "background_background": "gradient",
                "background_color": "transparent",
                "background_color_b": "rgba(10,10,15,0.9)",
                "background_gradient_type": "linear",
                "background_gradient_angle": {"size": 180, "unit": "deg"}
            },
            "elements": [
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": title,
                        "header_size": "h4",
                        "title_color": COLORS['white'],
                        "typography_typography": "custom",
                        "typography_font_family": TYPOGRAPHY['font_family'],
                        "typography_font_size": {"size": TYPOGRAPHY['h4_size'], "unit": "px"},
                        "typography_font_weight": "600"
                    }
                },
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": f'<p style="color: {COLORS["text_muted"]}; font-size: {TYPOGRAPHY["small_size"]}px; line-height: 1.6; margin-top: 8px;">{description}</p>'
                    }
                }
            ]
        }]
    }


# =============================================================================
# ULTIMATE SERVICES SECTION - FULL-WIDTH WITH 6 CARDS
# =============================================================================

def create_services_section(services=None):
    """
    Full-width services section using Elementor SECTION with stretch
    - Uses elType: "section" (NOT container) for true full-width
    - stretch_section: "section-stretched" for 1920px coverage
    - 6 service cards in 2 rows (3 per row)
    """
    if services is None:
        services = [
            ("Property Search", "Access exclusive listings across Dubai's premium neighborhoods", IMAGES['services'][0]),
            ("Investment Advisory", "Expert guidance on high-yield real estate opportunities", IMAGES['services'][1]),
            ("Property Management", "Full-service management for your real estate portfolio", IMAGES['services'][2]),
            ("Legal Services", "Comprehensive due diligence and transaction support", IMAGES['services'][3]),
            ("Luxury Rentals", "Premium furnished apartments and villas for rent", IMAGES['services'][4]),
            ("Off-Plan Projects", "Early access to Dubai's most anticipated developments", IMAGES['services'][5]),
        ]

    cards = [create_service_card(t, d, i) for t, d, i in services]

    return {
        "id": gen_id(),
        "elType": "section",  # CRITICAL: Must be "section" not "container"
        "settings": {
            "stretch_section": "section-stretched",  # CRITICAL: Enables full-width
            "layout": "full_width",
            "content_width": {"size": 1400, "unit": "px"},
            "gap": "no",
            "padding": {"top": "100", "right": "0", "bottom": "100", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": COLORS['dark']
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    # Section Header
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "boxed",
                            "boxed_width": {"size": 1400, "unit": "px"},
                            "flex_direction": "column",
                            "flex_align_items": "center",
                            "padding": {"top": "0", "right": "40", "bottom": "60", "left": "40", "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "WHY CHOOSE US",
                                    "align": "center",
                                    "title_color": COLORS['gold'],
                                    "typography_typography": "custom",
                                    "typography_font_family": TYPOGRAPHY['font_family'],
                                    "typography_font_size": {"size": TYPOGRAPHY['label_size'], "unit": "px"},
                                    "typography_font_weight": "500",
                                    "typography_letter_spacing": {"size": 4, "unit": "px"}
                                }
                            },
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "Our Services",
                                    "header_size": "h2",
                                    "align": "center",
                                    "title_color": COLORS['white'],
                                    "typography_typography": "custom",
                                    "typography_font_family": TYPOGRAPHY['font_family'],
                                    "typography_font_size": {"size": TYPOGRAPHY['h2_size'], "unit": "px"},
                                    "typography_font_weight": "300",
                                    "typography_letter_spacing": {"size": 1, "unit": "px"},
                                    "_margin": {"top": "16", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {COLORS["text_subtle"]}; font-size: {TYPOGRAPHY["body_size"]}px; max-width: 600px; line-height: 1.7;">Comprehensive real estate solutions tailored to your investment goals in Dubai\'s dynamic property market.</p>',
                                    "_margin": {"top": "20", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            }
                        ]
                    },
                    # Cards Grid - 3 per row using percentage widths
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "boxed",
                            "boxed_width": {"size": 1400, "unit": "px"},
                            "flex_direction": "row",
                            "flex_wrap": "wrap",
                            "flex_justify_content": "space-between",
                            "flex_gap": {"size": SPACING['card_gap'], "unit": "px", "column": "24", "row": "24"},
                            "padding": {"top": "0", "right": "40", "bottom": "0", "left": "40", "unit": "px", "isLinked": False}
                        },
                        "elements": cards
                    }
                ]
            }
        ]
    }


# =============================================================================
# ULTIMATE FOOTER - AX CAPITAL STYLE
# =============================================================================

def create_footer(brand_name="BRAND"):
    """
    Full-width footer with AX Capital styling
    - Logo + 4 nav columns + contact section
    - Full-width via elType: "section" + stretch_section
    """
    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "content_width": {"size": 1400, "unit": "px"},
            "gap": "no",
            "padding": {"top": "80", "right": "0", "bottom": "50", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": COLORS['dark'],
            "border_border": "solid",
            "border_width": {"top": "1", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False},
            "border_color": COLORS['border_subtle']
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    # Main footer content row
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "boxed",
                            "boxed_width": {"size": 1400, "unit": "px"},
                            "flex_direction": "row",
                            "flex_justify_content": "space-between",
                            "flex_align_items": "flex-start",
                            "flex_wrap": "wrap",
                            "padding": {"top": "0", "right": "40", "bottom": "0", "left": "40", "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            # Logo column
                            _create_footer_logo(brand_name),
                            # Nav columns container
                            _create_footer_nav_columns(),
                            # Contact section
                            _create_footer_contact()
                        ]
                    },
                    # Search bar
                    _create_footer_search()
                ]
            }
        ]
    }


def _create_footer_logo(brand_name):
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 180, "unit": "px"},
            "flex_direction": "column"
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": brand_name,
                    "title_color": COLORS['gold'],
                    "typography_typography": "custom",
                    "typography_font_family": TYPOGRAPHY['font_family'],
                    "typography_font_size": {"size": TYPOGRAPHY['h3_size'], "unit": "px"},
                    "typography_font_weight": "300",
                    "typography_letter_spacing": {"size": 6, "unit": "px"}
                }
            }
        ]
    }


def _create_footer_nav_columns():
    nav_cols = [
        ["Apartments", "Penthouses", "Villas", "Townhouses"],
        ["Off-Plan", "Catalogs", "Area Guides", "Sell"],
        ["Rent", "Developers", "AX CORPORATE", "Reviews"],
        ["Careers", "Contact Us"]
    ]

    col_elements = []
    for items in nav_cols:
        link_elements = []
        for item in items:
            link_elements.append({
                "id": gen_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f'<p style="color: {COLORS["text_muted"]}; font-size: {TYPOGRAPHY["small_size"]}px; margin-bottom: 14px; cursor: pointer;">{item}</p>'
                }
            })

        col_elements.append({
            "id": gen_id(),
            "elType": "container",
            "settings": {
                "content_width": "full",
                "width": {"size": 130 if len(items) > 2 else 100, "unit": "px"},
                "flex_direction": "column"
            },
            "elements": link_elements
        })

    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 550, "unit": "px"},
            "flex_direction": "row",
            "flex_justify_content": "space-between",
            "padding": {"top": "10", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
        },
        "elements": col_elements
    }


def _create_footer_contact():
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 300, "unit": "px"},
            "flex_direction": "column",
            "flex_align_items": "flex-end"
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": "CONTACTS",
                    "align": "right",
                    "title_color": COLORS['gold'],
                    "typography_typography": "custom",
                    "typography_font_family": TYPOGRAPHY['font_family'],
                    "typography_font_size": {"size": 22, "unit": "px"},
                    "typography_font_weight": "300",
                    "typography_letter_spacing": {"size": 4, "unit": "px"}
                }
            },
            {
                "id": gen_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": "Dubai, UAE",
                    "align": "right",
                    "title_color": COLORS['white'],
                    "typography_typography": "custom",
                    "typography_font_family": TYPOGRAPHY['font_family'],
                    "typography_font_size": {"size": 18, "unit": "px"},
                    "typography_font_weight": "300",
                    "_margin": {"top": "30", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                }
            },
            {
                "id": gen_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f'<p style="text-align: right; color: {COLORS["text_subtle"]}; font-size: {TYPOGRAPHY["small_size"]}px; line-height: 1.6;">14th Floor, Westburry Office,<br>Business Bay</p>',
                    "_margin": {"top": "8", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                }
            },
            {
                "id": gen_id(),
                "elType": "widget",
                "widgetType": "button",
                "settings": {
                    "text": "CALL US",
                    "align": "right",
                    "typography_typography": "custom",
                    "typography_font_family": TYPOGRAPHY['font_family'],
                    "typography_font_size": {"size": TYPOGRAPHY['label_size'], "unit": "px"},
                    "typography_font_weight": "400",
                    "typography_letter_spacing": {"size": 3, "unit": "px"},
                    "button_text_color": COLORS['text_muted'],
                    "background_color": "transparent",
                    "border_border": "solid",
                    "border_width": {"top": "1", "right": "1", "bottom": "1", "left": "1", "unit": "px", "isLinked": True},
                    "border_color": "rgba(255,255,255,0.25)",
                    "border_radius": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": True},
                    "button_padding": {"top": "16", "right": "60", "bottom": "16", "left": "60", "unit": "px", "isLinked": False},
                    "_margin": {"top": "24", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                }
            }
        ]
    }


def _create_footer_search():
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "boxed",
            "boxed_width": {"size": 600, "unit": "px"},
            "padding": {"top": "50", "right": "40", "bottom": "0", "left": "40", "unit": "px", "isLinked": False}
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f'<p style="color: {COLORS["text_faint"]}; font-size: {TYPOGRAPHY["small_size"]}px; padding: 14px 0; border-bottom: 1px solid {COLORS["border_subtle"]};"><span style="margin-right: 14px; opacity: 0.6;">&#128269;</span>Properties or locations</p>'
                }
            }
        ]
    }


# =============================================================================
# CONSULTATION / CTA SECTION
# =============================================================================

def create_consultation_section():
    """Consultation/CTA section with form"""
    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "content_width": {"size": 1400, "unit": "px"},
            "gap": "no",
            "padding": {"top": "100", "right": "0", "bottom": "100", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": COLORS['dark_alt']
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "boxed",
                            "boxed_width": {"size": 800, "unit": "px"},
                            "flex_direction": "column",
                            "flex_align_items": "center",
                            "padding": {"top": "0", "right": "40", "bottom": "0", "left": "40", "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "BOOK A CONSULTATION",
                                    "align": "center",
                                    "title_color": COLORS['gold'],
                                    "typography_typography": "custom",
                                    "typography_font_family": TYPOGRAPHY['font_family'],
                                    "typography_font_size": {"size": TYPOGRAPHY['label_size'], "unit": "px"},
                                    "typography_font_weight": "500",
                                    "typography_letter_spacing": {"size": 4, "unit": "px"}
                                }
                            },
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "Get Expert Advice",
                                    "header_size": "h2",
                                    "align": "center",
                                    "title_color": COLORS['white'],
                                    "typography_typography": "custom",
                                    "typography_font_family": TYPOGRAPHY['font_family'],
                                    "typography_font_size": {"size": TYPOGRAPHY['h2_size'], "unit": "px"},
                                    "typography_font_weight": "300",
                                    "_margin": {"top": "16", "right": "0", "bottom": "20", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {COLORS["text_subtle"]}; font-size: {TYPOGRAPHY["body_size"]}px; line-height: 1.7;">Schedule a free consultation with our real estate experts to discuss your investment goals.</p>',
                                    "_margin": {"top": "0", "right": "0", "bottom": "40", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "button",
                                "settings": {
                                    "text": "Schedule Now",
                                    "align": "center",
                                    "background_color": COLORS['gold'],
                                    "button_text_color": COLORS['dark'],
                                    "border_radius": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": True},
                                    "typography_typography": "custom",
                                    "typography_font_family": TYPOGRAPHY['font_family'],
                                    "typography_font_size": {"size": TYPOGRAPHY['small_size'], "unit": "px"},
                                    "typography_font_weight": "500",
                                    "typography_letter_spacing": {"size": 2, "unit": "px"},
                                    "button_padding": {"top": "18", "right": "50", "bottom": "18", "left": "50", "unit": "px", "isLinked": False}
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }


# =============================================================================
# MAIN GENERATOR CLASS
# =============================================================================

class UltimateV1Generator:
    """
    Ultimate V1 Page Generator
    Generates desktop-optimized pages matching the perfected AX Capital style
    """

    def __init__(self):
        self.colors = COLORS
        self.typography = TYPOGRAPHY
        self.spacing = SPACING
        self.images = IMAGES

    def generate_page(self, config=None):
        """Generate a complete page with all sections"""
        if config is None:
            config = {}

        sections = []

        # Add sections based on config or defaults
        if config.get('services', True):
            sections.append(create_services_section(config.get('services_items')))

        if config.get('consultation', True):
            sections.append(create_consultation_section())

        if config.get('footer', True):
            sections.append(create_footer(config.get('brand_name', 'BRAND')))

        return sections

    def export_json(self, sections):
        """Export sections to JSON string for Elementor"""
        return json.dumps(sections)


# =============================================================================
# QUICK TEST
# =============================================================================

if __name__ == "__main__":
    generator = UltimateV1Generator()
    sections = generator.generate_page({
        'brand_name': 'AX CAPITAL',
        'services': True,
        'consultation': True,
        'footer': True
    })

    print(f"Generated {len(sections)} sections")
    print("Sections:", [s['elType'] for s in sections])
    print("\nUltimate V1 Template ready!")
