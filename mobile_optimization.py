#!/usr/bin/env python3
"""
MOBILE OPTIMIZATION - Creates mobile-only sections while preserving desktop
============================================================================
Strategy:
1. Hide existing desktop sections on mobile (add hide_mobile setting)
2. Create new mobile-optimized sections visible ONLY on mobile
3. Push both to WordPress

Mobile Best Practices Applied:
- Touch targets: 44x44px minimum
- Font sizes: 16px minimum body, 28-32px headings
- Full-width cards (100%)
- Reduced padding (40-60px sections)
- Single column layouts
- Thumb-zone friendly CTA placement
- Simplified navigation (hamburger concept)
"""

import requests
import json
import random
import string

WP_URL = "https://wordpress-1097675-6048787.cloudwaysapps.com"
USERNAME = "grasinsantonia@gmail.com"
APP_PASSWORD = "7Fbg xKjQ fdKi JCNk JQIv ESxr"
PAGE_ID = 110

# =============================================================================
# MOBILE DESIGN SYSTEM
# =============================================================================

MOBILE_COLORS = {
    'dark': '#0a0a0f',
    'dark_alt': '#0d0d12',
    'gold': '#c9a962',
    'white': '#FFFFFF',
    'text_muted': 'rgba(255,255,255,0.7)',
    'text_subtle': 'rgba(255,255,255,0.5)',
}

MOBILE_TYPOGRAPHY = {
    'h1': 32,           # Hero headline
    'h2': 28,           # Section titles
    'h3': 22,           # Card titles
    'h4': 18,           # Subsection titles
    'body': 16,         # Body text (never smaller!)
    'small': 14,        # Secondary text
    'label': 12,        # Labels, caps
    'button': 16,       # Button text
}

MOBILE_SPACING = {
    'section_padding_y': 60,    # Top/bottom section padding
    'section_padding_x': 20,    # Left/right padding
    'card_gap': 16,             # Gap between cards
    'element_gap': 16,          # Gap between elements
}

# Touch-friendly sizes
TOUCH_TARGET_MIN = 44  # Minimum 44x44px for buttons


def gen_id():
    """Generate unique Elementor element ID"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))


# =============================================================================
# MOBILE HERO SECTION
# =============================================================================

def create_mobile_hero():
    """
    Mobile-optimized hero section
    - Simplified layout (single column)
    - Larger touch targets
    - Hamburger menu concept
    - Full-width CTA buttons
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
            "background_image": {
                "url": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=1200&q=80",
                "id": ""
            },
            "background_position": "center center",
            "background_size": "cover",
            "background_overlay_background": "classic",
            "background_overlay_color": "rgba(0, 0, 0, 0.6)",
            # MOBILE ONLY - Hide on desktop and tablet
            "hide_desktop": "hidden-desktop",
            "hide_tablet": "hidden-tablet"
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    # Mobile Header (Logo + Hamburger)
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
                            # Logo
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "AX CAPITAL",
                                    "header_size": "h4",
                                    "title_color": MOBILE_COLORS['gold'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": 20, "unit": "px"},
                                    "typography_font_weight": "300",
                                    "typography_letter_spacing": {"size": 2, "unit": "px"}
                                }
                            },
                            # Hamburger menu icon (3 lines)
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "☰",
                                    "header_size": "span",
                                    "title_color": MOBILE_COLORS['white'],
                                    "typography_typography": "custom",
                                    "typography_font_size": {"size": 28, "unit": "px"}
                                }
                            }
                        ]
                    },
                    # Hero Content - Centered, single column
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
                            # Main headline
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "INVEST IN DUBAI REAL ESTATE",
                                    "header_size": "h1",
                                    "align": "center",
                                    "title_color": MOBILE_COLORS['white'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h1'], "unit": "px"},
                                    "typography_font_weight": "300",
                                    "typography_line_height": {"size": 1.2, "unit": "em"},
                                    "typography_text_transform": "uppercase"
                                }
                            },
                            # Brand accent
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "WITH AX CAPITAL",
                                    "header_size": "h2",
                                    "align": "center",
                                    "title_color": MOBILE_COLORS['gold'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h2'], "unit": "px"},
                                    "typography_font_weight": "300",
                                    "typography_line_height": {"size": 1.2, "unit": "em"},
                                    "_margin": {"top": "8", "right": "0", "bottom": "24", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            # Subheadline
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body"]}px; line-height: 1.6;">We bring Due Diligence at Your service</p>',
                                    "_margin": {"top": "0", "right": "0", "bottom": "32", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            # CTA Buttons - Full width, stacked
                            {
                                "id": gen_id(),
                                "elType": "container",
                                "settings": {
                                    "content_width": "full",
                                    "flex_direction": "column",
                                    "flex_gap": {"size": 12, "unit": "px"}
                                },
                                "elements": [
                                    # Primary CTA - Full width
                                    {
                                        "id": gen_id(),
                                        "elType": "widget",
                                        "widgetType": "button",
                                        "settings": {
                                            "text": "Leave a Request",
                                            "align": "stretch",
                                            "background_color": MOBILE_COLORS['gold'],
                                            "button_text_color": "#1a1a1a",
                                            "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                                            "typography_typography": "custom",
                                            "typography_font_family": "Montserrat",
                                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['button'], "unit": "px"},
                                            "typography_font_weight": "600",
                                            "button_padding": {"top": "18", "right": "24", "bottom": "18", "left": "24", "unit": "px", "isLinked": False}
                                        }
                                    },
                                    # Secondary CTA
                                    {
                                        "id": gen_id(),
                                        "elType": "widget",
                                        "widgetType": "button",
                                        "settings": {
                                            "text": "Already an Owner?",
                                            "align": "stretch",
                                            "background_color": "transparent",
                                            "button_text_color": MOBILE_COLORS['gold'],
                                            "border_border": "solid",
                                            "border_width": {"top": "1", "right": "1", "bottom": "1", "left": "1", "unit": "px", "isLinked": True},
                                            "border_color": MOBILE_COLORS['gold'],
                                            "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                                            "typography_typography": "custom",
                                            "typography_font_family": "Montserrat",
                                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['button'], "unit": "px"},
                                            "typography_font_weight": "500",
                                            "button_padding": {"top": "18", "right": "24", "bottom": "18", "left": "24", "unit": "px", "isLinked": False}
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    # Scroll indicator
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "full",
                            "flex_direction": "column",
                            "flex_align_items": "center",
                            "padding": {"top": "0", "right": "20", "bottom": "30", "left": "20", "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_subtle"]}; font-size: 12px;">Scroll to explore ↓</p>'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }


# =============================================================================
# MOBILE TRUSTED BY SECTION
# =============================================================================

def create_mobile_trusted_by():
    """Mobile-optimized trusted by / logos section"""
    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "gap": "no",
            "padding": {"top": "40", "right": "0", "bottom": "40", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": MOBILE_COLORS['dark'],
            "border_border": "solid",
            "border_width": {"top": "1", "right": "0", "bottom": "1", "left": "0", "unit": "px", "isLinked": False},
            "border_color": "rgba(255,255,255,0.08)",
            # MOBILE ONLY
            "hide_desktop": "hidden-desktop",
            "hide_tablet": "hidden-tablet"
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
                            "content_width": "full",
                            "flex_direction": "column",
                            "flex_align_items": "center",
                            "padding": {"top": "0", "right": "20", "bottom": "0", "left": "20", "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["small"]}px; letter-spacing: 2px; text-transform: uppercase;">Trusted by leading developers</p>'
                                }
                            },
                            # Logos row - simplified for mobile
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_muted"]}; font-size: 18px; margin-top: 16px; letter-spacing: 8px;">EMAAR · DAMAC · MERAAS · SOBHA</p>'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }


# =============================================================================
# MOBILE SERVICE CARD
# =============================================================================

def create_mobile_service_card(title, description, image_url):
    """
    Mobile-optimized service card
    - 100% width (full width, stacked)
    - Larger text for readability
    - Taller card for better touch interaction
    """
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 100, "unit": "%"},
            "min_height": {"size": 220, "unit": "px"},
            "flex_direction": "column",
            "flex_justify_content": "flex-end",
            "padding": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": True},
            "border_radius": {"top": "12", "right": "12", "bottom": "12", "left": "12", "unit": "px", "isLinked": True},
            "overflow": "hidden",
            "background_background": "classic",
            "background_image": {"url": image_url, "id": ""},
            "background_position": "center center",
            "background_size": "cover",
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {
                "horizontal": 0,
                "vertical": 8,
                "blur": 24,
                "spread": 0,
                "color": "rgba(0,0,0,0.4)"
            }
        },
        "elements": [
            # Gradient overlay with content
            {
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
                    # Card title
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "widgetType": "heading",
                        "settings": {
                            "title": title,
                            "header_size": "h4",
                            "title_color": MOBILE_COLORS['white'],
                            "typography_typography": "custom",
                            "typography_font_family": "Montserrat",
                            "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h4'], "unit": "px"},
                            "typography_font_weight": "600"
                        }
                    },
                    # Card description
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {
                            "editor": f'<p style="color: {MOBILE_COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body"]}px; line-height: 1.5; margin-top: 8px;">{description}</p>'
                        }
                    }
                ]
            }
        ]
    }


# =============================================================================
# MOBILE SERVICES SECTION
# =============================================================================

def create_mobile_services_section():
    """
    Mobile-optimized services section
    - Cards stacked vertically (1 column)
    - Reduced padding
    - Larger touch-friendly cards
    """
    services = [
        ("Property Search", "Access exclusive listings across Dubai's premium neighborhoods", "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80"),
        ("Investment Advisory", "Expert guidance on high-yield real estate opportunities", "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80"),
        ("Property Management", "Full-service management for your real estate portfolio", "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80"),
        ("Legal Services", "Comprehensive due diligence and transaction support", "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80"),
        ("Luxury Rentals", "Premium furnished apartments and villas for rent", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80"),
        ("Off-Plan Projects", "Early access to Dubai's most anticipated developments", "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=800&q=80"),
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
            "background_color": MOBILE_COLORS['dark'],
            # MOBILE ONLY
            "hide_desktop": "hidden-desktop",
            "hide_tablet": "hidden-tablet"
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
                            "content_width": "full",
                            "flex_direction": "column",
                            "flex_align_items": "center",
                            "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "32", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            # Label
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "WHY CHOOSE US",
                                    "align": "center",
                                    "title_color": MOBILE_COLORS['gold'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['label'], "unit": "px"},
                                    "typography_font_weight": "500",
                                    "typography_letter_spacing": {"size": 3, "unit": "px"}
                                }
                            },
                            # Title
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "Our Services",
                                    "header_size": "h2",
                                    "align": "center",
                                    "title_color": MOBILE_COLORS['white'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h2'], "unit": "px"},
                                    "typography_font_weight": "300",
                                    "_margin": {"top": "12", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            # Description
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["body"]}px; line-height: 1.6;">Comprehensive real estate solutions tailored to your investment goals.</p>',
                                    "_margin": {"top": "16", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            }
                        ]
                    },
                    # Cards container - Single column stacked
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
            }
        ]
    }


# =============================================================================
# MOBILE CONSULTATION / CTA SECTION
# =============================================================================

def create_mobile_consultation_section():
    """Mobile-optimized CTA section"""
    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "gap": "no",
            "padding": {"top": str(MOBILE_SPACING['section_padding_y']), "right": "0", "bottom": str(MOBILE_SPACING['section_padding_y']), "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": MOBILE_COLORS['dark_alt'],
            # MOBILE ONLY
            "hide_desktop": "hidden-desktop",
            "hide_tablet": "hidden-tablet"
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
                            "content_width": "full",
                            "flex_direction": "column",
                            "flex_align_items": "center",
                            "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "0", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            # Label
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "BOOK A CONSULTATION",
                                    "align": "center",
                                    "title_color": MOBILE_COLORS['gold'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['label'], "unit": "px"},
                                    "typography_font_weight": "500",
                                    "typography_letter_spacing": {"size": 3, "unit": "px"}
                                }
                            },
                            # Title
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "Get Expert Advice",
                                    "header_size": "h2",
                                    "align": "center",
                                    "title_color": MOBILE_COLORS['white'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h2'], "unit": "px"},
                                    "typography_font_weight": "300",
                                    "_margin": {"top": "12", "right": "0", "bottom": "16", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            # Description
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["body"]}px; line-height: 1.6;">Schedule a free consultation with our real estate experts.</p>',
                                    "_margin": {"top": "0", "right": "0", "bottom": "32", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            # CTA Button - Full width
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "button",
                                "settings": {
                                    "text": "Schedule Now",
                                    "align": "stretch",
                                    "background_color": MOBILE_COLORS['gold'],
                                    "button_text_color": MOBILE_COLORS['dark'],
                                    "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['button'], "unit": "px"},
                                    "typography_font_weight": "600",
                                    "button_padding": {"top": "18", "right": "24", "bottom": "18", "left": "24", "unit": "px", "isLinked": False}
                                }
                            },
                            # Secondary action
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "button",
                                "settings": {
                                    "text": "Call Us: +971 4 123 4567",
                                    "align": "stretch",
                                    "background_color": "transparent",
                                    "button_text_color": MOBILE_COLORS['text_muted'],
                                    "border_border": "solid",
                                    "border_width": {"top": "1", "right": "1", "bottom": "1", "left": "1", "unit": "px", "isLinked": True},
                                    "border_color": "rgba(255,255,255,0.2)",
                                    "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['body'], "unit": "px"},
                                    "typography_font_weight": "400",
                                    "button_padding": {"top": "16", "right": "24", "bottom": "16", "left": "24", "unit": "px", "isLinked": False},
                                    "_margin": {"top": "12", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }


# =============================================================================
# MOBILE FOOTER
# =============================================================================

def create_mobile_footer():
    """
    Mobile-optimized footer
    - Single column layout
    - Stacked navigation
    - Large touch-friendly links
    - Accordion-style nav groups
    """
    return {
        "id": gen_id(),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "layout": "full_width",
            "gap": "no",
            "padding": {"top": "50", "right": "0", "bottom": "30", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": MOBILE_COLORS['dark'],
            "border_border": "solid",
            "border_width": {"top": "1", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False},
            "border_color": "rgba(255,255,255,0.1)",
            # MOBILE ONLY
            "hide_desktop": "hidden-desktop",
            "hide_tablet": "hidden-tablet"
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    # Logo and tagline
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
                            # Logo
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "AX CAPITAL",
                                    "align": "center",
                                    "title_color": MOBILE_COLORS['gold'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": 24, "unit": "px"},
                                    "typography_font_weight": "300",
                                    "typography_letter_spacing": {"size": 4, "unit": "px"}
                                }
                            },
                            # Tagline
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["small"]}px; margin-top: 12px;">Premium Real Estate in Dubai</p>'
                                }
                            }
                        ]
                    },
                    # Quick links - Grid 2x2
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "full",
                            "flex_direction": "row",
                            "flex_wrap": "wrap",
                            "flex_justify_content": "center",
                            "flex_gap": {"size": 0, "unit": "px"},
                            "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "24", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            # Link items - touch friendly
                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body"]}px; padding: 12px 16px; min-width: 120px;">Buy</p>'}},
                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body"]}px; padding: 12px 16px; min-width: 120px;">Rent</p>'}},
                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body"]}px; padding: 12px 16px; min-width: 120px;">Sell</p>'}},
                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_muted"]}; font-size: {MOBILE_TYPOGRAPHY["body"]}px; padding: 12px 16px; min-width: 120px;">Off-Plan</p>'}},
                        ]
                    },
                    # Divider
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "full",
                            "padding": {"top": "0", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "0", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "divider",
                                "settings": {
                                    "color": "rgba(255,255,255,0.1)",
                                    "weight": {"size": 1, "unit": "px"}
                                }
                            }
                        ]
                    },
                    # Contact info
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "full",
                            "flex_direction": "column",
                            "flex_align_items": "center",
                            "padding": {"top": "24", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "24", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            # Location
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "heading",
                                "settings": {
                                    "title": "Dubai, UAE",
                                    "align": "center",
                                    "title_color": MOBILE_COLORS['white'],
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['h4'], "unit": "px"},
                                    "typography_font_weight": "400"
                                }
                            },
                            # Address
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["small"]}px; line-height: 1.6; margin-top: 8px;">14th Floor, Westburry Office<br>Business Bay</p>'
                                }
                            },
                            # Call button - Full width
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "button",
                                "settings": {
                                    "text": "CALL US",
                                    "align": "stretch",
                                    "background_color": "transparent",
                                    "button_text_color": MOBILE_COLORS['gold'],
                                    "border_border": "solid",
                                    "border_width": {"top": "1", "right": "1", "bottom": "1", "left": "1", "unit": "px", "isLinked": True},
                                    "border_color": MOBILE_COLORS['gold'],
                                    "border_radius": {"top": "4", "right": "4", "bottom": "4", "left": "4", "unit": "px", "isLinked": True},
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": MOBILE_TYPOGRAPHY['button'], "unit": "px"},
                                    "typography_font_weight": "500",
                                    "typography_letter_spacing": {"size": 2, "unit": "px"},
                                    "button_padding": {"top": "16", "right": "24", "bottom": "16", "left": "24", "unit": "px", "isLinked": False},
                                    "_margin": {"top": "20", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            }
                        ]
                    },
                    # Social icons
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "full",
                            "flex_direction": "column",
                            "flex_align_items": "center",
                            "padding": {"top": "16", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "24", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_muted"]}; font-size: 24px; letter-spacing: 20px;">📧 📘 🐦 💼</p>'
                                }
                            }
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
                            "padding": {"top": "16", "right": str(MOBILE_SPACING['section_padding_x']), "bottom": "0", "left": str(MOBILE_SPACING['section_padding_x']), "unit": "px", "isLinked": False},
                            "border_border": "solid",
                            "border_width": {"top": "1", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False},
                            "border_color": "rgba(255,255,255,0.08)"
                        },
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": f'<p style="text-align: center; color: {MOBILE_COLORS["text_subtle"]}; font-size: {MOBILE_TYPOGRAPHY["label"]}px;">© 2024 AX Capital. All rights reserved.</p>'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }


# =============================================================================
# ADD HIDE_MOBILE TO DESKTOP SECTIONS
# =============================================================================

def add_hide_mobile_to_section(section):
    """Add hide_mobile setting to existing desktop section"""
    if section.get('settings'):
        section['settings']['hide_mobile'] = 'hidden-mobile'
    return section


# =============================================================================
# MAIN UPDATE FUNCTION
# =============================================================================

def update_page_with_mobile():
    """Update page with mobile-only sections while preserving desktop"""
    print("=" * 60)
    print("MOBILE OPTIMIZATION - Creating mobile-only sections")
    print("=" * 60)
    print()

    # Fetch current page
    print("Fetching current page...")
    response = requests.get(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        auth=(USERNAME, APP_PASSWORD),
        params={"context": "edit"}
    )

    if response.status_code != 200:
        print(f"Error fetching page: {response.status_code}")
        return False

    data = response.json()
    meta = data.get("meta", {})
    elementor_str = meta.get("_elementor_data", "[]")

    try:
        elements = json.loads(elementor_str) if elementor_str else []
    except:
        elements = []

    print(f"Found {len(elements)} existing sections")

    # Process existing sections - add hide_mobile
    print("\nAdding hide_mobile to desktop sections...")
    desktop_sections = []
    for i, el in enumerate(elements):
        # Add hide_mobile to all existing sections
        el = add_hide_mobile_to_section(el)
        desktop_sections.append(el)
        print(f"  Section {i+1}: Added hide_mobile")

    # Create mobile-only sections
    print("\nCreating mobile-only sections...")
    mobile_sections = []

    # 1. Mobile Hero
    mobile_sections.append(create_mobile_hero())
    print("  ✓ Created mobile Hero")

    # 2. Mobile Trusted By
    mobile_sections.append(create_mobile_trusted_by())
    print("  ✓ Created mobile Trusted By")

    # 3. Mobile Services
    mobile_sections.append(create_mobile_services_section())
    print("  ✓ Created mobile Services (6 cards stacked)")

    # 4. Mobile Consultation/CTA
    mobile_sections.append(create_mobile_consultation_section())
    print("  ✓ Created mobile Consultation/CTA")

    # 5. Mobile Footer
    mobile_sections.append(create_mobile_footer())
    print("  ✓ Created mobile Footer")

    # Combine: Desktop sections first, then mobile sections
    all_sections = desktop_sections + mobile_sections
    print(f"\nTotal sections: {len(all_sections)} ({len(desktop_sections)} desktop + {len(mobile_sections)} mobile)")

    # Update page
    print("\nPushing to WordPress...")
    payload = {
        "meta": {
            "_elementor_data": json.dumps(all_sections),
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page"
        }
    }

    response = requests.post(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        auth=(USERNAME, APP_PASSWORD),
        json=payload
    )

    if response.status_code == 200:
        print("\n" + "=" * 60)
        print("✓ SUCCESS! Mobile optimization complete!")
        print("=" * 60)
        print(f"\nView page: {WP_URL}/test5-2/")
        print(f"Edit page: {WP_URL}/wp-admin/post.php?post={PAGE_ID}&action=elementor")
        print("\n⚠️  IMPORTANT: Open Elementor editor and click UPDATE to see changes!")
        print("\nMobile sections created:")
        print("  - Hero (hamburger menu, centered content, full-width CTAs)")
        print("  - Trusted By (simplified logos)")
        print("  - Services (6 cards stacked vertically)")
        print("  - Consultation CTA (full-width buttons)")
        print("  - Footer (single column, touch-friendly)")
        return True
    else:
        print(f"\nError: {response.status_code}")
        print(response.text[:500])
        return False


if __name__ == "__main__":
    update_page_with_mobile()
