#!/usr/bin/env python3
"""
Complete fix: Services section (3 per row, 1920px desktop) + AX Capital style footer
"""

import requests
import json
import random
import string

# WordPress credentials
WP_URL = "https://wordpress-1097675-6048787.cloudwaysapps.com"
USERNAME = "grasinsantonia@gmail.com"
APP_PASSWORD = "7Fbg xKjQ fdKi JCNk JQIv ESxr"
PAGE_ID = 110

def gen_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def create_service_card(title, desc, image_url):
    """Service card - 370px width for 3 per row in 1200px container"""
    return {
        "id": gen_id(),
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 370, "unit": "px"},
            "width_tablet": {"size": 48, "unit": "%"},
            "width_mobile": {"size": 100, "unit": "%"},
            "min_height": {"size": 260, "unit": "px"},
            "flex_direction": "column",
            "flex_justify_content": "flex-end",
            "padding": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": True},
            "border_radius": {"top": "6", "right": "6", "bottom": "6", "left": "6", "unit": "px", "isLinked": True},
            "overflow": "hidden",
            "background_background": "classic",
            "background_image": {"url": image_url, "id": ""},
            "background_position": "center center",
            "background_size": "cover",
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {"horizontal": 0, "vertical": 8, "blur": 24, "spread": 0, "color": "rgba(0,0,0,0.2)"}
        },
        "elements": [{
            "id": gen_id(),
            "elType": "container",
            "settings": {
                "content_width": "full",
                "padding": {"top": "80", "right": "20", "bottom": "20", "left": "20", "unit": "px", "isLinked": False},
                "background_background": "gradient",
                "background_color": "transparent",
                "background_color_b": "rgba(10,10,15,0.85)",
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
                        "typography_font_size": {"size": 18, "unit": "px"},
                        "typography_font_weight": "600"
                    }
                },
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": f'<p style="color: rgba(255,255,255,0.65); font-size: 13px; line-height: 1.5; margin-top: 6px;">{desc}</p>'
                    }
                }
            ]
        }]
    }

def create_services_section():
    """Services section - 3 cards per row, 1920px desktop optimized"""
    services = [
        ("Property Search", "Access exclusive listings across Dubai's premium neighborhoods", "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=600&q=80"),
        ("Investment Advisory", "Expert guidance on high-yield real estate opportunities", "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=600&q=80"),
        ("Property Management", "Full-service management for your real estate portfolio", "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600&q=80"),
        ("Legal Services", "Comprehensive due diligence and transaction support", "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600&q=80"),
        ("Luxury Rentals", "Premium furnished apartments and villas for rent", "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80"),
        ("Off-Plan Projects", "Early access to Dubai's most anticipated developments", "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=600&q=80"),
    ]

    cards = [create_service_card(t, d, i) for t, d, i in services]

    return {
        "id": gen_id(),
        "elType": "container",
        "isInner": False,
        "settings": {
            "content_width": "full",
            "flex_direction": "column",
            "padding": {"top": "80", "right": "0", "bottom": "80", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": "#0a0a0f"
        },
        "elements": [
            # Header
            {
                "id": gen_id(),
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "boxed_width": {"size": 1200, "unit": "px"},
                    "flex_direction": "column",
                    "flex_align_items": "center",
                    "padding": {"top": "0", "right": "20", "bottom": "50", "left": "20", "unit": "px", "isLinked": False}
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
                            "typography_font_size": {"size": 12, "unit": "px"},
                            "typography_font_weight": "500",
                            "typography_letter_spacing": {"size": 3, "unit": "px"}
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
                            "typography_font_size": {"size": 42, "unit": "px"},
                            "typography_font_weight": "300",
                            "_margin": {"top": "12", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                        }
                    },
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {
                            "editor": '<p style="text-align: center; color: rgba(255,255,255,0.5); font-size: 15px; max-width: 550px; line-height: 1.6;">Comprehensive real estate solutions tailored to your investment goals.</p>',
                            "_margin": {"top": "16", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                        }
                    }
                ]
            },
            # Cards grid - 3 per row
            {
                "id": gen_id(),
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "boxed_width": {"size": 1200, "unit": "px"},
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_justify_content": "space-between",
                    "flex_gap": {"size": 20, "unit": "px", "column": "20", "row": "20"},
                    "padding": {"top": "0", "right": "20", "bottom": "0", "left": "20", "unit": "px", "isLinked": False}
                },
                "elements": cards
            }
        ]
    }

def create_footer():
    """AX Capital style footer"""
    return {
        "id": gen_id(),
        "elType": "container",
        "isInner": False,
        "settings": {
            "content_width": "full",
            "flex_direction": "column",
            "padding": {"top": "60", "right": "0", "bottom": "40", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": "#0a0a0f"
        },
        "elements": [
            # Main footer content
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
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "full",
                            "width": {"size": 200, "unit": "px"},
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
                                    "typography_font_size": {"size": 32, "unit": "px"},
                                    "typography_font_weight": "300",
                                    "typography_letter_spacing": {"size": 4, "unit": "px"}
                                }
                            }
                        ]
                    },
                    # Nav columns container
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "full",
                            "width": {"size": 500, "unit": "px"},
                            "flex_direction": "row",
                            "flex_justify_content": "space-between",
                            "padding": {"top": "20", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                        },
                        "elements": [
                            # Column 1
                            {
                                "id": gen_id(),
                                "elType": "container",
                                "settings": {"content_width": "full", "width": {"size": 120, "unit": "px"}, "flex_direction": "column"},
                                "elements": [
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Apartments</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Penthouses</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Villas</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Townhouses</p>'}}
                                ]
                            },
                            # Column 2
                            {
                                "id": gen_id(),
                                "elType": "container",
                                "settings": {"content_width": "full", "width": {"size": 120, "unit": "px"}, "flex_direction": "column"},
                                "elements": [
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Off-Plan</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Catalogs</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Area Guides</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Sell</p>'}}
                                ]
                            },
                            # Column 3
                            {
                                "id": gen_id(),
                                "elType": "container",
                                "settings": {"content_width": "full", "width": {"size": 120, "unit": "px"}, "flex_direction": "column"},
                                "elements": [
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Rent</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Developers</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Corporate</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Reviews</p>'}}
                                ]
                            },
                            # Column 4
                            {
                                "id": gen_id(),
                                "elType": "container",
                                "settings": {"content_width": "full", "width": {"size": 100, "unit": "px"}, "flex_direction": "column"},
                                "elements": [
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Careers</p>'}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": '<p style="color: rgba(255,255,255,0.6); font-size: 14px; margin-bottom: 12px; cursor: pointer;">Contact Us</p>'}}
                                ]
                            }
                        ]
                    },
                    # Contact column (right side)
                    {
                        "id": gen_id(),
                        "elType": "container",
                        "settings": {
                            "content_width": "full",
                            "width": {"size": 320, "unit": "px"},
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
                                    "typography_font_size": {"size": 24, "unit": "px"},
                                    "typography_font_weight": "300",
                                    "typography_letter_spacing": {"size": 3, "unit": "px"}
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
                                    "typography_font_size": {"size": 20, "unit": "px"},
                                    "typography_font_weight": "300",
                                    "_margin": {"top": "24", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "widgetType": "text-editor",
                                "settings": {
                                    "editor": '<p style="text-align: right; color: rgba(255,255,255,0.6); font-size: 14px;">14th Floor, Business Bay Tower</p>',
                                    "_margin": {"top": "8", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            },
                            # Social icons row
                            {
                                "id": gen_id(),
                                "elType": "container",
                                "settings": {
                                    "content_width": "full",
                                    "flex_direction": "row",
                                    "flex_justify_content": "flex-end",
                                    "flex_gap": {"size": 16, "unit": "px"},
                                    "padding": {"top": "20", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                },
                                "elements": [
                                    {"id": gen_id(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "fab fa-facebook-f", "library": "fa-brands"}, "primary_color": "rgba(255,255,255,0.6)", "size": {"size": 16, "unit": "px"}}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "fab fa-twitter", "library": "fa-brands"}, "primary_color": "rgba(255,255,255,0.6)", "size": {"size": 16, "unit": "px"}}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "fab fa-linkedin-in", "library": "fa-brands"}, "primary_color": "rgba(255,255,255,0.6)", "size": {"size": 16, "unit": "px"}}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "fab fa-whatsapp", "library": "fa-brands"}, "primary_color": "rgba(255,255,255,0.6)", "size": {"size": 16, "unit": "px"}}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "fab fa-instagram", "library": "fa-brands"}, "primary_color": "rgba(255,255,255,0.6)", "size": {"size": 16, "unit": "px"}}},
                                    {"id": gen_id(), "elType": "widget", "widgetType": "icon", "settings": {"selected_icon": {"value": "fab fa-youtube", "library": "fa-brands"}, "primary_color": "rgba(255,255,255,0.6)", "size": {"size": 16, "unit": "px"}}}
                                ]
                            },
                            # Call Us button
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
                                    "typography_letter_spacing": {"size": 2, "unit": "px"},
                                    "button_text_color": "rgba(255,255,255,0.7)",
                                    "background_color": "transparent",
                                    "border_border": "solid",
                                    "border_width": {"top": "1", "right": "1", "bottom": "1", "left": "1", "unit": "px", "isLinked": True},
                                    "border_color": "rgba(255,255,255,0.3)",
                                    "border_radius": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": True},
                                    "button_padding": {"top": "14", "right": "50", "bottom": "14", "left": "50", "unit": "px", "isLinked": False},
                                    "_margin": {"top": "20", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                                }
                            }
                        ]
                    }
                ]
            },
            # Search bar row
            {
                "id": gen_id(),
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "boxed_width": {"size": 1400, "unit": "px"},
                    "padding": {"top": "40", "right": "40", "bottom": "0", "left": "40", "unit": "px", "isLinked": False}
                },
                "elements": [
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {
                            "editor": '<p style="color: rgba(255,255,255,0.4); font-size: 14px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.15);"><span style="margin-right: 12px;">🔍</span>Properties or locations</p>'
                        }
                    }
                ]
            }
        ]
    }

def update_page():
    """Get current data, fix services, add footer"""
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

    # Rebuild page structure
    new_elements = []
    services_added = False

    for el in elements:
        el_str = json.dumps(el)

        # Skip old services section
        if 'Services' in el_str or 'Why Choose Us' in el_str or 'Lightning Fast' in el_str or 'l43pqfl' in el_str:
            if not services_added:
                new_elements.append(create_services_section())
                services_added = True
                print("Replaced services section")
            continue

        # Skip old footer (anything with CONTACTS, footer links, etc)
        if 'CONTACTS' in el_str or 'footer' in el_str.lower() or 'Apartments' in el_str and 'Penthouses' in el_str:
            print("Skipped old footer")
            continue

        new_elements.append(el)

    # Add services if not added
    if not services_added:
        # Insert after position 1 (after header/hero)
        if len(new_elements) >= 2:
            new_elements.insert(2, create_services_section())
        else:
            new_elements.append(create_services_section())
        print("Added new services section")

    # Add footer at end
    new_elements.append(create_footer())
    print("Added footer")

    print(f"Final sections: {len(new_elements)}")

    # Update
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
        print("\nOpen in Elementor and click UPDATE to regenerate CSS")
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text[:300])
        return False

if __name__ == "__main__":
    update_page()
