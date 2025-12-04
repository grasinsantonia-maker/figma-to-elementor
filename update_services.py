#!/usr/bin/env python3
"""
Update WordPress page with professional Services section
AX Capital lifestyle-style design with real estate imagery
"""

import requests
import json

# WordPress credentials
WP_URL = "https://wordpress-1097675-6048787.cloudwaysapps.com"
USERNAME = "grasinsantonia@gmail.com"
APP_PASSWORD = "7Fbg xKjQ fdKi JCNk JQIv ESxr"
PAGE_ID = 110

# High-quality Unsplash real estate images
IMAGES = {
    "luxury_villa": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80",
    "dubai_skyline": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80",
    "modern_interior": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80",
    "investment": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80",
    "penthouse": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80",
    "waterfront": "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=800&q=80",
}

def get_page_data():
    """Get current page data"""
    response = requests.get(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        auth=(USERNAME, APP_PASSWORD)
    )
    if response.status_code == 200:
        return response.json()
    print(f"Error getting page: {response.status_code}")
    print(response.text)
    return None

def create_services_section():
    """Create a professional services section with AX Capital lifestyle style"""

    services = [
        {
            "title": "Property Search",
            "desc": "Access exclusive listings across Dubai's premium neighborhoods",
            "image": IMAGES["luxury_villa"]
        },
        {
            "title": "Investment Advisory",
            "desc": "Expert guidance on high-yield real estate opportunities",
            "image": IMAGES["dubai_skyline"]
        },
        {
            "title": "Property Management",
            "desc": "Full-service management for your real estate portfolio",
            "image": IMAGES["modern_interior"]
        },
        {
            "title": "Legal Services",
            "desc": "Comprehensive due diligence and transaction support",
            "image": IMAGES["investment"]
        },
        {
            "title": "Luxury Rentals",
            "desc": "Premium furnished apartments and villas for rent",
            "image": IMAGES["penthouse"]
        },
        {
            "title": "Off-Plan Projects",
            "desc": "Early access to Dubai's most anticipated developments",
            "image": IMAGES["waterfront"]
        }
    ]

    # Create individual service cards with images
    service_cards = []
    for i, service in enumerate(services):
        card = {
            "id": f"svc{i}",
            "elType": "container",
            "settings": {
                "content_width": "full",
                "width": {"size": 31, "unit": "%"},
                "min_height": {"size": 320, "unit": "px"},
                "padding": {"top": "0", "right": "0", "bottom": "0", "left": "0", "unit": "px"},
                "margin": {"top": "0", "right": "0", "bottom": "20", "left": "0", "unit": "px"},
                "border_radius": {"top": "8", "right": "8", "bottom": "8", "left": "8", "unit": "px"},
                "overflow": "hidden",
                "background_background": "classic",
                "background_image": {
                    "url": service["image"],
                    "id": ""
                },
                "background_position": "center center",
                "background_size": "cover",
                "box_shadow_box_shadow_type": "yes",
                "box_shadow_box_shadow": {
                    "horizontal": 0,
                    "vertical": 10,
                    "blur": 30,
                    "spread": 0,
                    "color": "rgba(0,0,0,0.15)"
                },
                "flex_direction": "column",
                "flex_justify_content": "flex-end",
                "_css_classes": "service-card"
            },
            "elements": [
                {
                    "id": f"svcoverlay{i}",
                    "elType": "container",
                    "settings": {
                        "content_width": "full",
                        "width": {"size": 100, "unit": "%"},
                        "padding": {"top": "24", "right": "24", "bottom": "24", "left": "24", "unit": "px"},
                        "background_background": "gradient",
                        "background_color": "transparent",
                        "background_color_b": "rgba(10,10,15,0.95)",
                        "background_gradient_type": "linear",
                        "background_gradient_angle": {"size": 0, "unit": "deg"},
                        "background_gradient_position": "center center"
                    },
                    "elements": [
                        {
                            "id": f"svctitle{i}",
                            "elType": "widget",
                            "widgetType": "heading",
                            "settings": {
                                "title": service["title"],
                                "header_size": "h4",
                                "title_color": "#FFFFFF",
                                "typography_font_family": "Montserrat",
                                "typography_font_size": {"size": 18, "unit": "px"},
                                "typography_font_weight": "600",
                                "typography_letter_spacing": {"size": 0.5, "unit": "px"}
                            }
                        },
                        {
                            "id": f"svcdesc{i}",
                            "elType": "widget",
                            "widgetType": "text-editor",
                            "settings": {
                                "editor": f'<p style="color: rgba(255,255,255,0.7); font-size: 14px; line-height: 1.6; margin: 8px 0 0 0;">{service["desc"]}</p>'
                            }
                        }
                    ]
                }
            ]
        }
        service_cards.append(card)

    # Main services section
    services_section = {
        "id": "services_section_new",
        "elType": "container",
        "settings": {
            "content_width": "full",
            "stretch_section": "section-stretched",
            "padding": {"top": "80", "right": "5", "bottom": "80", "left": "5", "unit": "px"},
            "background_background": "classic",
            "background_color": "#0a0a0f"
        },
        "elements": [
            # Section header
            {
                "id": "svc_header",
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "width": {"size": 1200, "unit": "px"},
                    "padding": {"top": "0", "right": "20", "bottom": "50", "left": "20", "unit": "px"},
                    "flex_direction": "column",
                    "flex_align_items": "center"
                },
                "elements": [
                    {
                        "id": "svc_tagline",
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {
                            "editor": '<p style="text-align: center; text-transform: uppercase; letter-spacing: 3px; color: #c9a962; font-size: 13px; margin-bottom: 16px;">Why Choose Us</p>'
                        }
                    },
                    {
                        "id": "svc_title",
                        "elType": "widget",
                        "widgetType": "heading",
                        "settings": {
                            "title": "Our Services",
                            "header_size": "h2",
                            "align": "center",
                            "title_color": "#FFFFFF",
                            "typography_font_family": "Montserrat",
                            "typography_font_size": {"size": 42, "unit": "px"},
                            "typography_font_weight": "300",
                            "typography_letter_spacing": {"size": 1, "unit": "px"}
                        }
                    },
                    {
                        "id": "svc_subtitle",
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {
                            "editor": '<p style="text-align: center; color: rgba(255,255,255,0.6); font-size: 16px; max-width: 600px; margin: 16px auto 0;">Comprehensive real estate solutions tailored to your investment goals in Dubai\'s dynamic property market.</p>'
                        }
                    }
                ]
            },
            # Services grid - row 1
            {
                "id": "svc_grid_row1",
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "width": {"size": 1200, "unit": "px"},
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_justify_content": "space-between",
                    "flex_gap": {"size": 20, "unit": "px"},
                    "padding": {"top": "0", "right": "20", "bottom": "0", "left": "20", "unit": "px"}
                },
                "elements": service_cards[:3]
            },
            # Services grid - row 2
            {
                "id": "svc_grid_row2",
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "width": {"size": 1200, "unit": "px"},
                    "flex_direction": "row",
                    "flex_wrap": "wrap",
                    "flex_justify_content": "space-between",
                    "flex_gap": {"size": 20, "unit": "px"},
                    "padding": {"top": "20", "right": "20", "bottom": "0", "left": "20", "unit": "px"}
                },
                "elements": service_cards[3:]
            }
        ]
    }

    return services_section

def update_page():
    """Update the WordPress page with new services section"""

    # Get current page
    page_data = get_page_data()
    if not page_data:
        return False

    print(f"Page title: {page_data.get('title', {}).get('rendered', 'Unknown')}")
    print(f"Page status: {page_data.get('status', 'Unknown')}")

    # Get current Elementor data
    response = requests.get(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}?context=edit",
        auth=(USERNAME, APP_PASSWORD)
    )

    if response.status_code != 200:
        print(f"Error getting page context: {response.status_code}")
        return False

    edit_data = response.json()
    meta = edit_data.get('meta', {})
    elementor_data_str = meta.get('_elementor_data', '[]')

    try:
        elementor_data = json.loads(elementor_data_str) if elementor_data_str else []
    except:
        elementor_data = []

    print(f"Current sections: {len(elementor_data)}")

    # Find and replace the services section (look for "Services" or "Why Choose Us")
    new_services = create_services_section()
    services_replaced = False

    new_elementor_data = []
    for section in elementor_data:
        # Check if this is the services section by looking for specific IDs or content
        section_str = json.dumps(section)
        if 'l43pqfl' in section_str or 'Services' in section_str or 'Why Choose Us' in section_str:
            if not services_replaced:
                new_elementor_data.append(new_services)
                services_replaced = True
                print("Replaced services section")
        else:
            new_elementor_data.append(section)

    if not services_replaced:
        # Insert after the second section (after trusted by)
        if len(new_elementor_data) >= 2:
            new_elementor_data.insert(2, new_services)
        else:
            new_elementor_data.append(new_services)
        print("Added new services section")

    # Update the page
    update_payload = {
        "meta": {
            "_elementor_data": json.dumps(new_elementor_data),
            "_elementor_edit_mode": "builder"
        }
    }

    response = requests.post(
        f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
        auth=(USERNAME, APP_PASSWORD),
        json=update_payload,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        print("Page updated successfully!")
        print(f"View at: {WP_URL}/?p={PAGE_ID}")
        return True
    else:
        print(f"Error updating page: {response.status_code}")
        print(response.text[:500])
        return False

if __name__ == "__main__":
    update_page()
