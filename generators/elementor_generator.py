"""
Elementor JSON Generator - Converts parsed Figma data to Elementor format
"""

import json
import uuid
from typing import List, Dict, Any


class ElementorGenerator:
    """Generate Elementor-compatible JSON from parsed Figma data"""

    def __init__(self, parsed_data: dict):
        self.parsed_data = parsed_data
        self.elements = parsed_data.get("elements", [])
        self.design_tokens = parsed_data.get("design_tokens", {})
        self.metadata = parsed_data.get("metadata", {})

    def generate(self) -> dict:
        """Main generation method - creates Elementor JSON structure"""
        elementor_data = []

        # Group elements by section
        sections = self._group_into_sections()

        for section in sections:
            elementor_section = self._create_section(section)
            elementor_data.append(elementor_section)

        return {
            "content": elementor_data,
            "page_settings": self._generate_page_settings(),
            "version": "0.4",
            "title": self.metadata.get("name", "Imported from Figma"),
            "type": "page"
        }

    def _generate_id(self) -> str:
        """Generate a unique Elementor-style ID"""
        return uuid.uuid4().hex[:7]

    def _group_into_sections(self) -> List[Dict]:
        """Group elements into logical sections based on their types"""
        sections = []
        current_section = None

        for element in self.elements:
            element_type = element.get("element_type", "")

            # These types start new sections
            if element_type in ["navigation", "hero_section", "section", "footer"]:
                if current_section:
                    sections.append(current_section)
                current_section = {
                    "type": element_type,
                    "element": element,
                    "children": element.get("children", [])
                }
            elif current_section:
                current_section["children"].append(element)

        if current_section:
            sections.append(current_section)

        return sections

    def _create_section(self, section_data: dict) -> dict:
        """Create an Elementor section from grouped data"""
        section_type = section_data.get("type", "section")
        element = section_data.get("element", {})
        children = section_data.get("children", [])

        # Create section wrapper
        section = {
            "id": self._generate_id(),
            "elType": "section",
            "settings": self._get_section_settings(element, section_type),
            "elements": []
        }

        # Create column(s) inside section
        column = {
            "id": self._generate_id(),
            "elType": "column",
            "settings": {
                "_column_size": 100
            },
            "elements": []
        }

        # Add widgets based on section type
        if section_type == "navigation":
            column["elements"].extend(self._create_navigation_widgets(element, children))
        elif section_type == "hero_section":
            column["elements"].extend(self._create_hero_widgets(element, children))
        elif section_type == "footer":
            column["elements"].extend(self._create_footer_widgets(element, children))
        else:
            column["elements"].extend(self._create_generic_widgets(children))

        section["elements"].append(column)
        return section

    def _get_section_settings(self, element: dict, section_type: str) -> dict:
        """Generate section settings from element styles"""
        styles = element.get("styles", {})
        size = element.get("size", {})

        settings = {
            "layout": "full_width",
            "content_width": {
                "unit": "px",
                "size": 1200
            },
            "gap": "no",
            "structure": "10"
        }

        # Background
        if styles.get("background_color"):
            settings["background_background"] = "classic"
            settings["background_color"] = styles["background_color"]

        # Padding based on section type
        if section_type == "navigation":
            settings["padding"] = {"unit": "px", "top": "15", "right": "0", "bottom": "15", "left": "0"}
        elif section_type == "hero_section":
            settings["padding"] = {"unit": "px", "top": "100", "right": "0", "bottom": "100", "left": "0"}
            settings["min_height"] = {"unit": "px", "size": 600}
        elif section_type == "footer":
            settings["padding"] = {"unit": "px", "top": "60", "right": "0", "bottom": "40", "left": "0"}

        return settings

    def _create_navigation_widgets(self, element: dict, children: list) -> list:
        """Create navigation widgets"""
        widgets = []

        # Find text elements that look like nav items
        nav_items = []
        cta_button = None

        for child in children:
            if child.get("element_type") == "text":
                name = child.get("name", "").lower()
                if "nav" in name and "cta" not in name:
                    nav_items.append(child)
            elif child.get("element_type") == "button":
                cta_button = child

        # Create nav menu widget
        if nav_items:
            menu_widget = {
                "id": self._generate_id(),
                "elType": "widget",
                "widgetType": "nav-menu",
                "settings": {
                    "menu": "main-menu",
                    "layout": "horizontal",
                    "align": "right",
                    "pointer": "none",
                    "typography_typography": "custom",
                    "typography_font_family": "Inter",
                    "typography_font_size": {"unit": "px", "size": 16}
                }
            }
            widgets.append(menu_widget)

        # Create CTA button
        if cta_button:
            widgets.append(self._create_button_widget(cta_button, children))

        return widgets

    def _create_hero_widgets(self, element: dict, children: list) -> list:
        """Create hero section widgets"""
        widgets = []

        # Find headings
        headings = [c for c in children if c.get("element_type") == "text" and c.get("typography", {}).get("font_size", 0) > 40]
        subtitles = [c for c in children if c.get("element_type") == "text" and 18 <= c.get("typography", {}).get("font_size", 0) <= 24]
        buttons = [c for c in children if c.get("element_type") == "button"]

        # Create heading widgets
        for i, heading in enumerate(headings[:2]):
            typo = heading.get("typography", {})
            widget = {
                "id": self._generate_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": heading.get("content", ""),
                    "size": "xl",
                    "header_size": "h1" if i == 0 else "h2",
                    "align": typo.get("text_align", "left"),
                    "title_color": typo.get("color", "#1a1a1a"),
                    "typography_typography": "custom",
                    "typography_font_family": typo.get("font_family", "Inter"),
                    "typography_font_size": {"unit": "px", "size": typo.get("font_size", 72)},
                    "typography_font_weight": str(typo.get("font_weight", 400))
                }
            }
            widgets.append(widget)

        # Create subtitle/text widget
        for subtitle in subtitles[:1]:
            typo = subtitle.get("typography", {})
            widget = {
                "id": self._generate_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f"<p>{subtitle.get('content', '')}</p>",
                    "align": typo.get("text_align", "left"),
                    "text_color": typo.get("color", "#737373"),
                    "typography_typography": "custom",
                    "typography_font_family": typo.get("font_family", "Inter"),
                    "typography_font_size": {"unit": "px", "size": typo.get("font_size", 20)}
                }
            }
            widgets.append(widget)

        # Create button widgets
        for button in buttons[:2]:
            widgets.append(self._create_button_widget(button, children))

        return widgets

    def _create_footer_widgets(self, element: dict, children: list) -> list:
        """Create footer widgets"""
        widgets = []

        # Group children by type
        text_elements = [c for c in children if c.get("element_type") == "text"]

        # Create inner section with columns for footer
        inner_section = {
            "id": self._generate_id(),
            "elType": "section",
            "isInner": True,
            "settings": {
                "structure": "30"
            },
            "elements": []
        }

        # Create columns
        for i in range(3):
            col = {
                "id": self._generate_id(),
                "elType": "column",
                "settings": {"_column_size": 33},
                "elements": []
            }

            # Add text widgets to columns
            start_idx = i * (len(text_elements) // 3)
            end_idx = start_idx + (len(text_elements) // 3)
            for text_el in text_elements[start_idx:end_idx]:
                typo = text_el.get("typography", {})
                widget = {
                    "id": self._generate_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": f"<p>{text_el.get('content', '')}</p>",
                        "text_color": typo.get("color", "#999999"),
                        "typography_font_family": typo.get("font_family", "Inter"),
                        "typography_font_size": {"unit": "px", "size": typo.get("font_size", 14)}
                    }
                }
                col["elements"].append(widget)

            inner_section["elements"].append(col)

        widgets.append(inner_section)
        return widgets

    def _create_generic_widgets(self, children: list) -> list:
        """Create widgets for generic sections"""
        widgets = []

        for child in children:
            element_type = child.get("element_type", "")

            if element_type == "text":
                widgets.append(self._create_text_widget(child))
            elif element_type == "button":
                widgets.append(self._create_button_widget(child, []))
            elif element_type == "card":
                widgets.append(self._create_card_widget(child))
            elif element_type == "image_placeholder":
                widgets.append(self._create_image_widget(child))

        return widgets

    def _create_text_widget(self, element: dict) -> dict:
        """Create a text/heading widget"""
        typo = element.get("typography", {})
        font_size = typo.get("font_size", 16)

        # Determine if heading or text
        if font_size >= 32:
            return {
                "id": self._generate_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": element.get("content", ""),
                    "header_size": "h2" if font_size >= 40 else "h3",
                    "title_color": typo.get("color", "#1a1a1a"),
                    "typography_typography": "custom",
                    "typography_font_family": typo.get("font_family", "Inter"),
                    "typography_font_size": {"unit": "px", "size": font_size},
                    "typography_font_weight": str(typo.get("font_weight", 400))
                }
            }
        else:
            return {
                "id": self._generate_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f"<p>{element.get('content', '')}</p>",
                    "text_color": typo.get("color", "#333333"),
                    "typography_font_family": typo.get("font_family", "Inter"),
                    "typography_font_size": {"unit": "px", "size": font_size}
                }
            }

    def _create_button_widget(self, element: dict, siblings: list) -> dict:
        """Create a button widget"""
        styles = element.get("styles", {})
        size = element.get("size", {})

        # Find button text from siblings or children
        button_text = "Click Here"
        for sibling in siblings:
            if sibling.get("element_type") == "text":
                name = sibling.get("name", "").lower()
                if "cta" in name or "button" in name:
                    button_text = sibling.get("content", "Click Here")
                    break

        # Check children too
        for child in element.get("children", []):
            if child.get("element_type") == "text":
                button_text = child.get("content", button_text)

        return {
            "id": self._generate_id(),
            "elType": "widget",
            "widgetType": "button",
            "settings": {
                "text": button_text,
                "align": "left",
                "size": "md",
                "button_type": "default",
                "background_color": styles.get("background_color", "#0485b2"),
                "button_text_color": "#ffffff",
                "border_radius": {
                    "unit": "px",
                    "top": str(styles.get("border_radius", 28)),
                    "right": str(styles.get("border_radius", 28)),
                    "bottom": str(styles.get("border_radius", 28)),
                    "left": str(styles.get("border_radius", 28))
                },
                "typography_typography": "custom",
                "typography_font_family": "Inter",
                "typography_font_weight": "500"
            }
        }

    def _create_card_widget(self, element: dict) -> dict:
        """Create a card-like widget (using inner section)"""
        styles = element.get("styles", {})
        children = element.get("children", [])

        card = {
            "id": self._generate_id(),
            "elType": "section",
            "isInner": True,
            "settings": {
                "background_background": "classic",
                "background_color": styles.get("background_color", "#f5f5f2"),
                "border_radius": {
                    "unit": "px",
                    "top": str(styles.get("border_radius", 16)),
                    "right": str(styles.get("border_radius", 16)),
                    "bottom": str(styles.get("border_radius", 16)),
                    "left": str(styles.get("border_radius", 16))
                },
                "padding": {"unit": "px", "top": "30", "right": "30", "bottom": "30", "left": "30"}
            },
            "elements": [{
                "id": self._generate_id(),
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [self._create_text_widget(c) for c in children if c.get("element_type") == "text"]
            }]
        }

        return card

    def _create_image_widget(self, element: dict) -> dict:
        """Create an image placeholder widget"""
        size = element.get("size", {})
        styles = element.get("styles", {})

        return {
            "id": self._generate_id(),
            "elType": "widget",
            "widgetType": "image",
            "settings": {
                "image": {
                    "url": "https://via.placeholder.com/640x520",
                    "id": ""
                },
                "image_size": "full",
                "width": {"unit": "px", "size": size.get("width", 640)},
                "height": {"unit": "px", "size": size.get("height", 520)},
                "border_radius": {
                    "unit": "px",
                    "top": str(styles.get("border_radius", 16)),
                    "right": str(styles.get("border_radius", 16)),
                    "bottom": str(styles.get("border_radius", 16)),
                    "left": str(styles.get("border_radius", 16))
                }
            }
        }

    def _generate_page_settings(self) -> dict:
        """Generate page-level settings"""
        return {
            "hide_title": "yes",
            "template": "elementor_canvas",
            "content_width": 1440
        }

    def export_json(self, filepath: str):
        """Export the generated data to a JSON file"""
        data = self.generate()
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        return filepath
