#!/usr/bin/env python3
"""
ULTIMATE V1 TEMPLATE - Desktop + Mobile Optimized Elementor Generator
======================================================================
This is the LOCKED, PERFECTED template with BOTH desktop and mobile versions.
All future pages should match this quality and structure.

DESKTOP FEATURES:
- Full-width sections (1920px stretch via elType: "section" + stretch_section)
- Service cards: 6 cards, 3 per row (32% width with responsive breakpoints)
- Gradient overlays on image cards for text readability
- AX Capital-style footer with 5 columns
- Montserrat typography system
- Color system: Dark (#0a0a0f), Gold (#c9a962)
- High-quality Unsplash images

MOBILE FEATURES (Duplicate Section Strategy):
- Desktop sections: hide_mobile setting (preserved untouched)
- Mobile sections: hide_desktop + hide_tablet (optimized for touch)
- Touch targets: 44x44px minimum buttons
- Font sizes: 16px body minimum, 28-32px headings
- Cards: 100% width, stacked vertically
- Section padding: 40-60px (reduced from 80-100px)
- Layout: Single column throughout
- CTAs: Full-width buttons in thumb zone
- Navigation: Hamburger menu concept
- Footer: Single column, touch-friendly links

Version: 1.1 ULTIMATE (Desktop + Mobile)
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

# =============================================================================
# DESKTOP TYPOGRAPHY - DO NOT MODIFY
# =============================================================================
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

# =============================================================================
# DESKTOP SPACING - DO NOT MODIFY
# =============================================================================
SPACING = {
    'section_padding': 100,
    'container_padding': 40,
    'card_gap': 24,
    'element_gap': 20,
}

# =============================================================================
# MOBILE TYPOGRAPHY - Optimized for touch devices
# =============================================================================
MOBILE_TYPOGRAPHY = {
    'font_family': 'Montserrat',
    'h1_size': 32,           # Hero headline (reduced from 56)
    'h2_size': 28,           # Section titles (reduced from 48)
    'h3_size': 22,           # Card titles (reduced from 36)
    'h4_size': 18,           # Subsection titles (reduced from 20)
    'body_size': 16,         # Body text - NEVER smaller than 16px!
    'small_size': 14,        # Secondary text
    'label_size': 12,        # Labels, uppercase
    'button_size': 16,       # Button text - readable
}

# =============================================================================
# MOBILE SPACING - Reduced for mobile screens
# =============================================================================
MOBILE_SPACING = {
    'section_padding_y': 60,     # Top/bottom (reduced from 100)
    'section_padding_x': 20,     # Left/right padding
    'card_gap': 16,              # Gap between cards (reduced from 24)
    'element_gap': 16,           # Gap between elements
    'button_min_height': 44,     # Touch target minimum
}

# =============================================================================
# MOBILE VISIBILITY SETTINGS
# =============================================================================
DESKTOP_VISIBILITY = {
    'hide_mobile': 'hidden-mobile'  # Hide on mobile only
}

MOBILE_VISIBILITY = {
    'hide_desktop': 'hidden-desktop',  # Hide on desktop
    'hide_tablet': 'hidden-tablet'     # Hide on tablet
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
# MOBILE HERO SECTION
# =============================================================================

def create_mobile_hero(brand_name="AX CAPITAL"):
    """
    Mobile-optimized hero section
    - Simplified single-column layout
    - Hamburger menu concept
    - Full-width CTA buttons
    - Touch-friendly targets (44px min)
    """
    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "gap": "no",
            "height": "min-height",
            "custom_height": {"size": 100, "unit": "vh"},
            "padding": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": True},
            "background_background": "classic",
            "background_image": {"url": IMAGES['hero'], "id": ""},
            "background_position": "center center",
            "background_size": "cover",
            "background_overlay_background": "classic",
            "background_overlay_color": "rgba(0, 0, 0, 0.6)",
            # MOBILE ONLY
            **MOBILE_VISIBILITY
        },
        "elements": [{
            "id": gen_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [
                # Mobile Header
                {
                    "id": gen_id(),
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "flex_direction": "row",
                        "flex_justify_content": "space-between",
                        "flex_align_items": "center",
                        "padding": {"top": "20", "right": "20", "bottom": "20", "left": "20", "unit": "px", "isLinked": False}
                    },
                    "elements": [
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                            "title": brand_name, "header_size": "h4",
                            "title_color": COLORS['gold'],
                            "typography_typography": "custom",
                            "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                            "typography_font_size": {"size": 20, "unit": "px"},
                            "typography_font_weight": "300",
                            "typography_letter_spacing": {"size": 2, "unit": "px"}
                        }},
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                            "title": "☰", "header_size": "span",
                            "title_color": COLORS['white'],
                            "typography_typography": "custom",
                            "typography_font_size": {"size": 28, "unit": "px"}
                        }}
                    ]
                },
                # Hero Content
                {
                    "id": gen_id(),
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "min_height": {"size": 70, "unit": "vh"},
                        "flex_direction": "column",
                        "flex_justify_content": "center",
                        "flex_align_items": "center",
                        "padding": {"top": "40", "right": "24", "bottom": "40", "left": "24", "unit": "px", "isLinked": False}
                    },
                    "elements": [
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                            "title": "INVEST IN DUBAI REAL ESTATE",
                            "header_size": "h1", "align": "center",
                            "title_color": COLORS['white'],
                            "typography_typography": "custom",
                            "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h1_size'], "unit": "px"},
                            "typography_font_weight": "300",
                            "typography_line_height": {"size": 1.2, "unit": "em"},
                            "typography_text_transform": "uppercase"
                        }},
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                            "title": f"WITH {brand_name}",
                            "header_size": "h2", "align": "center",
                            "title_color": COLORS['gold'],
                            "typography_typography": "custom",
                            "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h2_size'], "unit": "px"},
                            "typography_font_weight": "300",
                            "_margin": {"top": "8", "right": "0", "bottom": "24", "left": "0", "unit": "px", "isLinked": False}
                        }},
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {
                            "editor": f'<p style="text-align: center; color: {COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body_size"]}px; line-height: 1.6;">We bring Due Diligence at Your service</p>',
                            "_margin": {"top": "0", "right": "0", "bottom": "32", "left": "0", "unit": "px", "isLinked": False}
                        }},
                        # Full-width CTA buttons
                        {
                            "id": gen_id(),
                            "elType": "container",
                            "settings": {"content_width": "full", "flex_direction": "column", "flex_gap": {"size": 12, "unit": "px"}},
                            "elements": [
                                {"id": gen_id(), "elType": "widget", "widgetType": "button", "settings": {
                                    "text": "Leave a Request", "align": "stretch",
                                    "background_color": COLORS['gold'],
                                    "button_text_color": "#1a1a1a",
                                    "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                                    "typography_typography": "custom",
                                    "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['button_size'], "unit": "px"},
                                    "typography_font_weight": "600",
                                    "button_padding": {"top": "18", "right": "24", "bottom": "18", "left": "24", "unit": "px", "isLinked": False}
                                }},
                                {"id": gen_id(), "elType": "widget", "widgetType": "button", "settings": {
                                    "text": "Already an Owner?", "align": "stretch",
                                    "background_color": "transparent",
                                    "button_text_color": COLORS['gold'],
                                    "border_border": "solid",
                                    "border_width": {"top": "1", "right": "1", "bottom": "1", "left": "1", "unit": "px", "isLinked": True},
                                    "border_color": COLORS['gold'],
                                    "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                                    "typography_typography": "custom",
                                    "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['button_size'], "unit": "px"},
                                    "typography_font_weight": "500",
                                    "button_padding": {"top": "18", "right": "24", "bottom": "18", "left": "24", "unit": "px", "isLinked": False}
                                }}
                            ]
                        }
                    ]
                }
            ]
        }]
    }


# =============================================================================
# MOBILE SERVICE CARD
# =============================================================================

def create_mobile_service_card(title, description, image_url):
    """Mobile service card - 100% width, stacked vertically"""
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 100, "unit": "%"},
            "min_height": {"size": 220, "unit": "px"},
            "flex_direction": "column",
            "flex_justify_content": "flex-end",
            "border_radius": {"top": "12", "right": "12", "bottom": "12", "left": "12", "unit": "px", "isLinked": True},
            "overflow": "hidden",
            "background_background": "classic",
            "background_image": {"url": image_url, "id": ""},
            "background_position": "center center",
            "background_size": "cover",
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {"horizontal": 0, "vertical": 8, "blur": 24, "spread": 0, "color": "rgba(0,0,0,0.4)"}
        },
        "elements": [{
            "id": gen_id(),
            "elType": "container",
            "settings": {
                "content_width": "full",
                "padding": {"top": "80", "right": "20", "bottom": "20", "left": "20", "unit": "px", "isLinked": False},
                "background_background": "gradient",
                "background_color": "transparent",
                "background_color_b": "rgba(10,10,15,0.95)",
                "background_gradient_type": "linear",
                "background_gradient_angle": {"size": 180, "unit": "deg"}
            },
            "elements": [
                {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                    "title": title, "header_size": "h4",
                    "title_color": COLORS['white'],
                    "typography_typography": "custom",
                    "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h4_size'], "unit": "px"},
                    "typography_font_weight": "600"
                }},
                {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {
                    "editor": f'<p style="color: {COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body_size"]}px; line-height: 1.5; margin-top: 8px;">{description}</p>'
                }}
            ]
        }]
    }


# =============================================================================
# MOBILE SERVICES SECTION
# =============================================================================

def create_mobile_services_section(services=None):
    """Mobile services section - cards stacked vertically"""
    if services is None:
        services = [
            ("Property Search", "Access exclusive listings across Dubai's premium neighborhoods", IMAGES['services'][0]),
            ("Investment Advisory", "Expert guidance on high-yield real estate opportunities", IMAGES['services'][1]),
            ("Property Management", "Full-service management for your real estate portfolio", IMAGES['services'][2]),
            ("Legal Services", "Comprehensive due diligence and transaction support", IMAGES['services'][3]),
            ("Luxury Rentals", "Premium furnished apartments and villas for rent", IMAGES['services'][4]),
            ("Off-Plan Projects", "Early access to Dubai's most anticipated developments", IMAGES['services'][5]),
        ]

    cards = [create_mobile_service_card(t, d, i) for t, d, i in services]

    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "gap": "no",
            "padding": {"top": str(MOBILE_SPACING['section_padding_y']), "right": "0", "bottom": str(MOBILE_SPACING['section_padding_y']), "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": COLORS['dark'],
            **MOBILE_VISIBILITY
        },
        "elements": [{
            "id": gen_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [
                # Header
                {
                    "id": gen_id(),
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "flex_direction": "column",
                        "flex_align_items": "center",
                        "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "32", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                    },
                    "elements": [
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                            "title": "WHY CHOOSE US", "align": "center",
                            "title_color": COLORS['gold'],
                            "typography_typography": "custom",
                            "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['label_size'], "unit": "px"},
                            "typography_font_weight": "500",
                            "typography_letter_spacing": {"size": 3, "unit": "px"}
                        }},
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                            "title": "Our Services", "header_size": "h2", "align": "center",
                            "title_color": COLORS['white'],
                            "typography_typography": "custom",
                            "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h2_size'], "unit": "px"},
                            "typography_font_weight": "300",
                            "_margin": {"top": "12", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                        }},
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {
                            "editor": f'<p style="text-align: center; color: {COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["body_size"]}px; line-height: 1.6;">Comprehensive real estate solutions tailored to your investment goals.</p>',
                            "_margin": {"top": "16", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                        }}
                    ]
                },
                # Cards - stacked
                {
                    "id": gen_id(),
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "flex_direction": "column",
                        "flex_gap": {"size": MOBILE_SPACING['card_gap'], "unit": "px"},
                        "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "0", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                    },
                    "elements": cards
                }
            ]
        }]
    }


# =============================================================================
# MOBILE CONSULTATION SECTION
# =============================================================================

def create_mobile_consultation_section():
    """Mobile CTA section with full-width buttons"""
    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "gap": "no",
            "padding": {"top": str(MOBILE_SPACING['section_padding_y']), "right": "0", "bottom": str(MOBILE_SPACING['section_padding_y']), "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": COLORS['dark_alt'],
            **MOBILE_VISIBILITY
        },
        "elements": [{
            "id": gen_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [{
                "id": gen_id(),
                "elType": "container",
                "settings": {
                    "content_width": "full",
                    "flex_direction": "column",
                    "flex_align_items": "center",
                    "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "0", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                },
                "elements": [
                    {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                        "title": "BOOK A CONSULTATION", "align": "center",
                        "title_color": COLORS['gold'],
                        "typography_typography": "custom",
                        "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                        "typography_font_size": {"size": MOBILE_TYPOGRAPHY['label_size'], "unit": "px"},
                        "typography_font_weight": "500",
                        "typography_letter_spacing": {"size": 3, "unit": "px"}
                    }},
                    {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                        "title": "Get Expert Advice", "header_size": "h2", "align": "center",
                        "title_color": COLORS['white'],
                        "typography_typography": "custom",
                        "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                        "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h2_size'], "unit": "px"},
                        "typography_font_weight": "300",
                        "_margin": {"top": "12", "right": "0", "bottom": "16", "left": "0", "unit": "px", "isLinked": False}
                    }},
                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {
                        "editor": f'<p style="text-align: center; color: {COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["body_size"]}px; line-height: 1.6;">Schedule a free consultation with our real estate experts.</p>',
                        "_margin": {"top": "0", "right": "0", "bottom": "32", "left": "0", "unit": "px", "isLinked": False}
                    }},
                    {"id": gen_id(), "elType": "widget", "widgetType": "button", "settings": {
                        "text": "Schedule Now", "align": "stretch",
                        "background_color": COLORS['gold'],
                        "button_text_color": COLORS['dark'],
                        "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                        "typography_typography": "custom",
                        "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                        "typography_font_size": {"size": MOBILE_TYPOGRAPHY['button_size'], "unit": "px"},
                        "typography_font_weight": "600",
                        "button_padding": {"top": "18", "right": "24", "bottom": "18", "left": "24", "unit": "px", "isLinked": False}
                    }},
                    {"id": gen_id(), "elType": "widget", "widgetType": "button", "settings": {
                        "text": "Call Us: +971 4 123 4567", "align": "stretch",
                        "background_color": "transparent",
                        "button_text_color": COLORS['text_muted'],
                        "border_border": "solid",
                        "border_width": {"top": "1", "right": "1", "bottom": "1", "left": "1", "unit": "px", "isLinked": True},
                        "border_color": "rgba(255,255,255,0.2)",
                        "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                        "typography_typography": "custom",
                        "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                        "typography_font_size": {"size": MOBILE_TYPOGRAPHY['body_size'], "unit": "px"},
                        "typography_font_weight": "400",
                        "button_padding": {"top": "16", "right": "24", "bottom": "16", "left": "24", "unit": "px", "isLinked": False},
                        "_margin": {"top": "12", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                    }}
                ]
            }]
        }]
    }


# =============================================================================
# MOBILE FOOTER
# =============================================================================

def create_mobile_footer(brand_name="AX CAPITAL"):
    """Mobile footer - single column, touch-friendly"""
    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "gap": "no",
            "padding": {"top": "50", "right": "0", "bottom": "30", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": COLORS['dark'],
            "border_border": "solid",
            "border_width": {"top": "1", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False},
            "border_color": COLORS['border_subtle'],
            **MOBILE_VISIBILITY
        },
        "elements": [{
            "id": gen_id(),
            "elType": "column",
            "settings": {"_column_size": 100},
            "elements": [
                # Logo
                {
                    "id": gen_id(),
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "flex_direction": "column",
                        "flex_align_items": "center",
                        "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "32", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                    },
                    "elements": [
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                            "title": brand_name, "align": "center",
                            "title_color": COLORS['gold'],
                            "typography_typography": "custom",
                            "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                            "typography_font_size": {"size": 24, "unit": "px"},
                            "typography_font_weight": "300",
                            "typography_letter_spacing": {"size": 4, "unit": "px"}
                        }},
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {
                            "editor": f'<p style="text-align: center; color: {COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["small_size"]}px; margin-top: 12px;">Premium Real Estate in Dubai</p>'
                        }}
                    ]
                },
                # Quick links
                {
                    "id": gen_id(),
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "flex_direction": "row",
                        "flex_wrap": "wrap",
                        "flex_justify_content": "center",
                        "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "24", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                    },
                    "elements": [
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f'<p style="text-align: center; color: {COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body_size"]}px; padding: 12px 16px;">Buy</p>'}},
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f'<p style="text-align: center; color: {COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body_size"]}px; padding: 12px 16px;">Rent</p>'}},
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f'<p style="text-align: center; color: {COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body_size"]}px; padding: 12px 16px;">Sell</p>'}},
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f'<p style="text-align: center; color: {COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body_size"]}px; padding: 12px 16px;">Off-Plan</p>'}}
                    ]
                },
                # Contact
                {
                    "id": gen_id(),
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "flex_direction": "column",
                        "flex_align_items": "center",
                        "padding": {"top": "24", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "24", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False},
                        "border_border": "solid",
                        "border_width": {"top": "1", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False},
                        "border_color": COLORS['border_faint']
                    },
                    "elements": [
                        {"id": gen_id(), "elType": "widget", "widgetType": "heading", "settings": {
                            "title": "Dubai, UAE", "align": "center",
                            "title_color": COLORS['white'],
                            "typography_typography": "custom",
                            "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h4_size'], "unit": "px"},
                            "typography_font_weight": "400"
                        }},
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {
                            "editor": f'<p style="text-align: center; color: {COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["small_size"]}px; line-height: 1.6; margin-top: 8px;">14th Floor, Westburry Office<br>Business Bay</p>'
                        }},
                        {"id": gen_id(), "elType": "widget", "widgetType": "button", "settings": {
                            "text": "CALL US", "align": "stretch",
                            "background_color": "transparent",
                            "button_text_color": COLORS['gold'],
                            "border_border": "solid",
                            "border_width": {"top": "1", "right": "1", "bottom": "1", "left": "1", "unit": "px", "isLinked": True},
                            "border_color": COLORS['gold'],
                            "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                            "typography_typography": "custom",
                            "typography_font_family": MOBILE_TYPOGRAPHY['font_family'],
                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['button_size'], "unit": "px"},
                            "typography_font_weight": "500",
                            "button_padding": {"top": "16", "right": "24", "bottom": "16", "left": "24", "unit": "px", "isLinked": False},
                            "_margin": {"top": "20", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                        }}
                    ]
                },
                # Copyright
                {
                    "id": gen_id(),
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "flex_direction": "column",
                        "flex_align_items": "center",
                        "padding": {"top": "16", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "0", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                    },
                    "elements": [
                        {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {
                            "editor": f'<p style="text-align: center; color: {COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["label_size"]}px;">© 2024 {brand_name}. All rights reserved.</p>'
                        }}
                    ]
                }
            ]
        }]
    }


# =============================================================================
# MAIN GENERATOR CLASS
# =============================================================================

class UltimateV1Generator:
    """
    Ultimate V1 Page Generator
    Generates BOTH desktop and mobile optimized pages

    Strategy: Duplicate sections approach
    - Desktop sections: visible on desktop/tablet, hidden on mobile
    - Mobile sections: visible only on mobile
    """

    def __init__(self):
        self.colors = COLORS
        self.typography = TYPOGRAPHY
        self.mobile_typography = MOBILE_TYPOGRAPHY
        self.spacing = SPACING
        self.mobile_spacing = MOBILE_SPACING
        self.images = IMAGES

    def generate_page(self, config=None):
        """Generate a complete page with desktop AND mobile sections"""
        if config is None:
            config = {}

        sections = []
        brand_name = config.get('brand_name', 'BRAND')

        # ========== DESKTOP SECTIONS (hidden on mobile) ==========
        if config.get('services', True):
            desktop_services = create_services_section(config.get('services_items'))
            desktop_services['settings']['hide_mobile'] = 'hidden-mobile'
            sections.append(desktop_services)

        if config.get('consultation', True):
            desktop_consultation = create_consultation_section()
            desktop_consultation['settings']['hide_mobile'] = 'hidden-mobile'
            sections.append(desktop_consultation)

        if config.get('footer', True):
            desktop_footer = create_footer(brand_name)
            desktop_footer['settings']['hide_mobile'] = 'hidden-mobile'
            sections.append(desktop_footer)

        # ========== MOBILE SECTIONS (hidden on desktop/tablet) ==========
        if config.get('mobile', True):
            if config.get('hero', True):
                sections.append(create_mobile_hero(brand_name))

            if config.get('services', True):
                sections.append(create_mobile_services_section(config.get('services_items')))

            if config.get('consultation', True):
                sections.append(create_mobile_consultation_section())

            if config.get('footer', True):
                sections.append(create_mobile_footer(brand_name))

        return sections

    def generate_desktop_only(self, config=None):
        """Generate desktop sections only (original behavior)"""
        if config is None:
            config = {}

        sections = []

        if config.get('services', True):
            sections.append(create_services_section(config.get('services_items')))

        if config.get('consultation', True):
            sections.append(create_consultation_section())

        if config.get('footer', True):
            sections.append(create_footer(config.get('brand_name', 'BRAND')))

        return sections

    def generate_mobile_only(self, config=None):
        """Generate mobile sections only"""
        if config is None:
            config = {}

        brand_name = config.get('brand_name', 'AX CAPITAL')

        return [
            create_mobile_hero(brand_name),
            create_mobile_services_section(config.get('services_items')),
            create_mobile_consultation_section(),
            create_mobile_footer(brand_name)
        ]

    def export_json(self, sections):
        """Export sections to JSON string for Elementor"""
        return json.dumps(sections)


# =============================================================================
# QUICK TEST
# =============================================================================

if __name__ == "__main__":
    generator = UltimateV1Generator()

    # Generate full page with both desktop and mobile sections
    sections = generator.generate_page({
        'brand_name': 'AX CAPITAL',
        'hero': True,
        'services': True,
        'consultation': True,
        'footer': True,
        'mobile': True
    })

    desktop_count = len([s for s in sections if s['settings'].get('hide_mobile')])
    mobile_count = len([s for s in sections if s['settings'].get('hide_desktop')])

    print(f"Generated {len(sections)} total sections")
    print(f"  - Desktop sections: {desktop_count}")
    print(f"  - Mobile sections: {mobile_count}")
    print("\nUltimate V1 Template ready with DESKTOP + MOBILE!")
