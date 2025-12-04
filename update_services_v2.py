#!/usr/bin/env python3
"""
Update WordPress Elementor page with professional Services section
Using direct post meta update approach
"""

import requests
import json
import re

# WordPress credentials
WP_URL = "https://wordpress-1097675-6048787.cloudwaysapps.com"
USERNAME = "grasinsantonia@gmail.com"
APP_PASSWORD = "7Fbg xKjQ fdKi JCNk JQIv ESxr"
PAGE_ID = 110

def generate_id():
    """Generate Elementor-style ID"""
    import random
    import string
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def create_service_card(title, desc, image_url):
    """Create a single service card with image background"""
    card_id = generate_id()
    overlay_id = generate_id()
    title_id = generate_id()
    desc_id = generate_id()

    return {
        "id": card_id,
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"size": 380, "unit": "px"},
            "width_tablet": {"size": 45, "unit": "%"},
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
                "color": "rgba(0,0,0,0.25)"
            }
        },
        "elements": [
            {
                "id": overlay_id,
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
                        "id": title_id,
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
                        "id": desc_id,
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {
                            "editor": f'<p style="color: rgba(255,255,255,0.7); font-size: 14px; line-height: 1.6; margin-top: 8px;">{desc}</p>'
                        }
                    }
                ]
            }
        ]
    }

def create_services_section():
    """Create the complete services section"""

    # High-quality real estate images from Unsplash
    services = [
        {
            "title": "Property Search",
            "desc": "Access exclusive listings across Dubai's premium neighborhoods",
            "image": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80"
        },
        {
            "title": "Investment Advisory",
            "desc": "Expert guidance on high-yield real estate opportunities",
            "image": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80"
        },
        {
            "title": "Property Management",
            "desc": "Full-service management for your real estate portfolio",
            "image": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80"
        },
        {
            "title": "Legal Services",
            "desc": "Comprehensive due diligence and transaction support",
            "image": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80"
        },
        {
            "title": "Luxury Rentals",
            "desc": "Premium furnished apartments and villas for rent",
            "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80"
        },
        {
            "title": "Off-Plan Projects",
            "desc": "Early access to Dubai's most anticipated developments",
            "image": "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=800&q=80"
        }
    ]

    cards = [create_service_card(s["title"], s["desc"], s["image"]) for s in services]

    section = {
        "id": generate_id(),
        "elType": "container",
        "isInner": False,
        "settings": {
            "content_width": "full",
            "flex_direction": "column",
            "padding": {"top": "100", "right": "0", "bottom": "100", "left": "0", "unit": "px", "isLinked": False},
            "background_background": "classic",
            "background_color": "#0a0a0f"
        },
        "elements": [
            # Header container
            {
                "id": generate_id(),
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "boxed_width": {"size": 1200, "unit": "px"},
                    "flex_direction": "column",
                    "flex_align_items": "center",
                    "padding": {"top": "0", "right": "20", "bottom": "60", "left": "20", "unit": "px", "isLinked": False}
                },
                "elements": [
                    {
                        "id": generate_id(),
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
                            "typography_letter_spacing": {"size": 3, "unit": "px"}
                        }
                    },
                    {
                        "id": generate_id(),
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
                        "id": generate_id(),
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {
                            "editor": '<p style="text-align: center; color: rgba(255,255,255,0.6); font-size: 16px; max-width: 600px; line-height: 1.7;">Comprehensive real estate solutions tailored to your investment goals in Dubai\'s dynamic property market.</p>',
                            "_margin": {"top": "20", "right": "0", "bottom": "0", "left": "0", "unit": "px", "isLinked": False}
                        }
                    }
                ]
            },
            # Cards grid
            {
                "id": generate_id(),
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "boxed_width": {"size": 1200, "unit": "px"},
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_justify_content": "center",
                    "flex_gap": {"size": 24, "unit": "px", "column": "24", "row": "24"},
                    "padding": {"top": "0", "right": "20", "bottom": "0", "left": "20", "unit": "px", "isLinked": False}
                },
                "elements": cards
            }
        ]
    }

    return section

def get_current_elementor_data():
    """Get current Elementor data from the page"""
    response = requests.get(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        auth=(USERNAME, APP_PASSWORD),
        params={"context": "edit"}
    )

    if response.status_code != 200:
        print(f"Error fetching page: {response.status_code}")
        return None

    data = response.json()
    meta = data.get("meta", {})
    elementor_data_str = meta.get("_elementor_data", "[]")

    try:
        return json.loads(elementor_data_str) if elementor_data_str else []
    except:
        return []

def find_and_replace_services(elements):
    """Find the services section and replace it"""
    new_elements = []
    replaced = False

    for element in elements:
        element_str = json.dumps(element)

        # Look for the services section by checking for "Why Choose Us", "Services", or the specific element ID
        if ('l43pqfl' in element_str or
            'Services' in element_str or
            'Why Choose Us' in element_str or
            'Lightning Fast' in element_str or
            'Secure by Default' in element_str):

            if not replaced:
                new_elements.append(create_services_section())
                replaced = True
                print("Found and replaced services section")
        else:
            new_elements.append(element)

    if not replaced:
        # Insert after trusted by section (position 2)
        print("Services section not found, inserting at position 2")
        if len(new_elements) >= 2:
            new_elements.insert(2, create_services_section())
        else:
            new_elements.append(create_services_section())

    return new_elements

def update_page():
    """Main update function"""
    print("Fetching current page data...")
    current_data = get_current_elementor_data()

    if current_data is None:
        print("Failed to get current data")
        return False

    print(f"Current sections: {len(current_data)}")

    # Replace services section
    new_data = find_and_replace_services(current_data)
    print(f"New sections: {len(new_data)}")

    # Update the page
    payload = {
        "meta": {
            "_elementor_data": json.dumps(new_data),
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page"
        }
    }

    print("Updating page...")
    response = requests.post(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        auth=(USERNAME, APP_PASSWORD),
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        print("SUCCESS! Page updated.")
        print(f"View at: {WP_URL}/test5-2/")
        print("\nNOTE: You may need to:")
        print("1. Open the page in Elementor editor")
        print("2. Click 'Update' to regenerate CSS")
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text[:500])
        return False

if __name__ == "__main__":
    update_page()
