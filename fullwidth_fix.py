#!/usr/bin/env python3
"""
Full-width fix: Services + Footer spanning full 1920px screen
Using Elementor SECTION with stretch_section for true full-width
"""

import requests
import json
import random
import string

WP_URL = "https://wordpress-1097675-6048787.cloudwaysapps.com"
USERNAME = "grasinsantonia@gmail.com"
APP_PASSWORD = "7Fbg xKjQ fdKi JCNk JQIv ESxr"
PAGE_ID = 110

def gen_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def create_service_card(title, desc, image_url):
    """Service card optimized for 3 per row"""
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
            "box_shadow_box_shadow": {"horizontal": 0, "vertical": 10, "blur": 30, "spread": 0, "color": "rgba(0,0,0,0.3)"}
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
                        "title_color": "#FFFFFF",
                        "typography_typography": "custom",
                        "typography_font_family": "Montserrat",
                        "typography_font_size": {"size": 20, "unit": "px"},
                        "typography_font_weight": "600"
                    }
                },
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": f'<p style="color: rgba(255,255,255,0.7); font-size: 14px; line-height: 1.6; margin-top: 8px;">{desc}</p>'
                    }
                }
            ]
        }]
    }

def create_services_section():
    """Full-width services section using Elementor section with stretch"""
    services = [
        ("Property Search", "Access exclusive listings across Dubai's premium neighborhoods", "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80"),
        ("Investment Advisory", "Expert guidance on high-yield real estate opportunities", "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80"),
        ("Property Management", "Full-service management for your real estate portfolio", "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80"),
        ("Legal Services", "Comprehensive due diligence and transaction support", "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80"),
        ("Luxury Rentals", "Premium furnished apartments and villas for rent", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80"),
        ("Off-Plan Projects", "Early access to Dubai's most anticipated developments", "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=800&q=80"),
    ]

    cards = [create_service_card(t, d, i) for t, d, i in services]

    # Use SECTION element for true full-width stretch
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
            "background_color": "#0a0a0f"
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    # Header
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
                                    "title_color": "#c9a962",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": 13, "unit": "px"},
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
                                    "title_color": "#FFFFFF",
                                    "typography_typography": "custom",
                                    "typography_font_family": "Montserrat",
                                    "typography_font_size": {"size": 48, "unit": "px"},
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
                                    "editor": '<p style="text-align: center; color: rgba(255,255,255,0.5); font-size: 16px; max-width: 600px; line-height: 1.7;">Comprehensive real estate solutions tailored to your investment goals in Dubai\'s dynamic property market.</p>',
                                    "_margin": {"top": "20", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            }
                        ]
                    },
                    # Cards grid - 3 per row using percentage width
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "boxed",
                            "boxed_width": {"size": 1400, "unit": "px"},
                            "flex_direction": "row",
                            "flex_wrap": "wrap",
                            "flex_justify_content": "space-between",
                            "flex_gap": {"size": 24, "unit": "px", "column": "24", "row": "24"},
                            "padding": {"top": "0", "right": "40", "bottom": "0", "left": "40", "unit": "px", "isLinked": False}
                        },
                        "elements": cards
                    }
                ]
            }
        ]
    }

def create_footer():
    """Full-width footer matching AX Capital style"""
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
            "background_color": "#0a0a0f",
            "border_border": "solid",
            "border_width": {"top": "1", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False},
            "border_color": "rgba(255,255,255,0.1)"
        },
        "elements": [
            {
                "id": gen_id(),
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    # Main footer row
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
                            # Logo
                            {
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
                                            "title": "BRAND",
                                            "title_color": "#c9a962",
                                            "typography_typography": "custom",
                                            "typography_font_family": "Montserrat",
                                            "typography_font_size": {"size": 36, "unit": "px"},
                                            "typography_font_weight": "300",
                                            "typography_letter_spacing": {"size": 6, "unit": "px"}
                                        }
                                    }
                                ]
                            },
                            # Nav columns
                            {
                                "id": gen_id(),
                                "elType": "container",
                                "settings": {
                                    "content_width": "full",
                                    "width": {"size": 550, "unit": "px"},
                                    "flex_direction": "row",
                                    "flex_justify_content": "space-between",
                                    "padding": {"top": "10", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                },
                                "elements": [
                                    # Col 1
                                    {
                                        "id": gen_id(),
                                        "elType": "container",
                                        "settings": {"content_width": "full", "width": {"size": 130, "unit": "px"}, "flex_direction": "column"},
                                        "elements": [
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer; transition: color 0.3s;">Apartments</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">Penthouses</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">Villas</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; cursor: pointer;">Townhouses</p>'}}
                                        ]
                                    },
                                    # Col 2
                                    {
                                        "id": gen_id(),
                                        "elType": "container",
                                        "settings": {"content_width": "full", "width": {"size": 130, "unit": "px"}, "flex_direction": "column"},
                                        "elements": [
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">Off-Plan</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">Catalogs</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">Area Guides</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; cursor: pointer;">Sell</p>'}}
                                        ]
                                    },
                                    # Col 3
                                    {
                                        "id": gen_id(),
                                        "elType": "container",
                                        "settings": {"content_width": "full", "width": {"size": 130, "unit": "px"}, "flex_direction": "column"},
                                        "elements": [
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">Rent</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">Developers</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">AX CORPORATE</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; cursor: pointer;">Reviews</p>'}}
                                        ]
                                    },
                                    # Col 4
                                    {
                                        "id": gen_id(),
                                        "elType": "container",
                                        "settings": {"content_width": "full", "width": {"size": 100, "unit": "px"}, "flex_direction": "column"},
                                        "elements": [
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 14px; cursor: pointer;">Careers</p>'}},
                                            {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; cursor: pointer;">Contact Us</p>'}}
                                        ]
                                    }
                                ]
                            },
                            # Contact section (right)
                            {
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
                                            "title_color": "#c9a962",
                                            "typography_typography": "custom",
                                            "typography_font_family": "Montserrat",
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
                                            "title_color": "#FFFFFF",
                                            "typography_typography": "custom",
                                            "typography_font_family": "Montserrat",
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
                                            "editor": '<p style="text-align: right; color: rgba(255,255,255,0.5); font-size: 14px; line-height: 1.6;">14th Floor, Westburry Office,<br>Business Bay</p>',
                                            "_margin": {"top": "8", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                        }
                                    },
                                    # Social icons
                                    {
                                        "id": gen_id(),
                                        "elType": "widget",
                                        "widgetType": "text-editor",
                                        "settings": {
                                            "editor": '<p style="text-align: right; color: rgba(255,255,255,0.5); font-size: 18px; letter-spacing: 16px;">✉ f 𝕏 in ☎ ◎ ❖ ▶</p>',
                                            "_margin": {"top": "24", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                        }
                                    },
                                    # Call button
                                    {
                                        "id": gen_id(),
                                        "elType": "widget",
                                        "widgetType": "button",
                                        "settings": {
                                            "text": "CALL US",
                                            "align": "right",
                                            "typography_typography": "custom",
                                            "typography_font_family": "Montserrat",
                                            "typography_font_size": {"size": 13, "unit": "px"},
                                            "typography_font_weight": "400",
                                            "typography_letter_spacing": {"size": 3, "unit": "px"},
                                            "button_text_color": "rgba(255,255,255,0.7)",
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
                        ]
                    },
                    # Search bar
                    {
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
                                    "editor": '<p style="color: rgba(255,255,255,0.4); font-size: 14px; padding: 14px 0; border-bottom: 1px solid rgba(255,255,255,0.15);"><span style="margin-right: 14px; opacity: 0.6;">🔍</span>Properties or locations</p>'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }

def update_page():
    """Update page with full-width sections"""
    print("Fetching current page...")

    response = requests.get(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        auth=(USERNAME, APP_PASSWORD),
        params={"context": "edit"}
    )

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return False

    data = response.json()
    meta = data.get("meta", {})
    elementor_str = meta.get("_elementor_data", "[]")

    try:
        elements = json.loads(elementor_str) if elementor_str else []
    except:
        elements = []

    print(f"Found {len(elements)} sections")

    # Keep only hero and trusted sections, replace services and footer
    new_elements = []

    for el in elements:
        el_str = json.dumps(el)

        # Skip services section
        if 'Services' in el_str or 'Why Choose Us' in el_str or 'WHY CHOOSE US' in el_str:
            print("Skipping old services")
            continue

        # Skip footer
        if 'CONTACTS' in el_str or 'Apartments' in el_str and 'Penthouses' in el_str and 'Villas' in el_str:
            print("Skipping old footer")
            continue

        # Skip any search bar
        if 'Properties or locations' in el_str:
            print("Skipping search bar")
            continue

        new_elements.append(el)

    # Add new full-width services
    new_elements.append(create_services_section())
    print("Added full-width services section")

    # Add new full-width footer
    new_elements.append(create_footer())
    print("Added full-width footer")

    print(f"Final sections: {len(new_elements)}")

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

    if response.status_code == 200:
        print("\n✓ SUCCESS!")
        print(f"View: {WP_URL}/test5-2/")
        print("\n⚠️  IMPORTANT: Open Elementor editor and click UPDATE to see changes!")
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text[:300])
        return False

if __name__ == "__main__":
    update_page()
