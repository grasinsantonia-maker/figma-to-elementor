"""
Figma Parser - Extracts design data from Figma nodes
"""

class FigmaParser:
    """Parse Figma node data into a standardized format for conversion"""

    def __init__(self, figma_data: dict):
        self.raw_data = figma_data
        self.elements = []
        self.design_tokens = {
            "colors": {},
            "typography": {},
            "spacing": {},
            "radii": {}
        }

    def parse(self) -> dict:
        """Main parsing method - extracts all design information"""
        self._extract_design_tokens()
        self._parse_children(self.raw_data.get("children", []))

        return {
            "elements": self.elements,
            "design_tokens": self.design_tokens,
            "metadata": {
                "name": self.raw_data.get("name", "Untitled"),
                "width": self.raw_data.get("absoluteBoundingBox", {}).get("width", 1440),
                "height": self.raw_data.get("absoluteBoundingBox", {}).get("height", 900)
            }
        }

    def _extract_design_tokens(self):
        """Extract colors, fonts, spacing from the design"""
        self._collect_colors(self.raw_data)
        self._collect_typography(self.raw_data)

    def _collect_colors(self, node: dict):
        """Recursively collect all colors used in the design"""
        # Extract fill colors
        for fill in node.get("fills", []):
            if fill.get("type") == "SOLID":
                color = fill.get("color", "")
                if color and color not in self.design_tokens["colors"]:
                    self.design_tokens["colors"][color] = self._generate_color_name(color)

        # Extract stroke colors
        for stroke in node.get("strokes", []):
            if stroke.get("type") == "SOLID":
                color = stroke.get("color", "")
                if color and color not in self.design_tokens["colors"]:
                    self.design_tokens["colors"][color] = self._generate_color_name(color)

        # Recurse into children
        for child in node.get("children", []):
            self._collect_colors(child)

    def _collect_typography(self, node: dict):
        """Collect typography styles"""
        if node.get("type") == "TEXT":
            style = node.get("style", {})
            font_key = f"{style.get('fontFamily', 'Inter')}-{style.get('fontSize', 16)}-{style.get('fontWeight', 400)}"
            if font_key not in self.design_tokens["typography"]:
                self.design_tokens["typography"][font_key] = {
                    "family": style.get("fontFamily", "Inter"),
                    "size": style.get("fontSize", 16),
                    "weight": style.get("fontWeight", 400),
                    "lineHeight": style.get("lineHeightPx", 24)
                }

        for child in node.get("children", []):
            self._collect_typography(child)

    def _generate_color_name(self, hex_color: str) -> str:
        """Generate a semantic name for a color"""
        # Simple naming based on common patterns
        hex_lower = hex_color.lower()
        if hex_lower in ["#ffffff", "#fff"]:
            return "white"
        elif hex_lower in ["#000000", "#000", "#1a1a1a"]:
            return "dark"
        elif "0485b2" in hex_lower:
            return "primary"
        elif hex_lower.startswith("#f") or hex_lower.startswith("#e"):
            return "light-gray"
        elif hex_lower.startswith("#7") or hex_lower.startswith("#8"):
            return "gray"
        return f"color-{hex_color[1:7]}"

    def _parse_children(self, children: list, parent_type: str = "root"):
        """Recursively parse child nodes"""
        for child in children:
            element = self._parse_node(child)
            if element:
                self.elements.append(element)

    def _parse_node(self, node: dict) -> dict:
        """Parse a single Figma node into our intermediate format"""
        node_type = node.get("type", "")

        base_element = {
            "id": node.get("id", ""),
            "name": node.get("name", ""),
            "figma_type": node_type,
            "position": self._extract_position(node),
            "size": self._extract_size(node),
            "styles": self._extract_styles(node),
            "children": []
        }

        # Type-specific parsing
        if node_type == "FRAME":
            base_element["element_type"] = self._determine_frame_type(node)
            # Parse children
            for child in node.get("children", []):
                child_element = self._parse_node(child)
                if child_element:
                    base_element["children"].append(child_element)

        elif node_type == "TEXT":
            base_element["element_type"] = "text"
            base_element["content"] = node.get("characters", "")
            base_element["typography"] = self._extract_typography(node)

        elif node_type == "RECTANGLE":
            base_element["element_type"] = "rectangle"

        elif node_type == "ELLIPSE":
            base_element["element_type"] = "ellipse"

        else:
            base_element["element_type"] = "unknown"

        return base_element

    def _determine_frame_type(self, node: dict) -> str:
        """Determine what type of element a FRAME should become"""
        name = node.get("name", "").lower()

        # Check for common patterns
        if "nav" in name:
            return "navigation"
        elif "hero" in name:
            return "hero_section"
        elif "section" in name:
            return "section"
        elif "card" in name:
            return "card"
        elif "button" in name or "cta" in name:
            return "button"
        elif "footer" in name:
            return "footer"
        elif "image" in name:
            return "image_placeholder"
        elif "logo" in name:
            return "logo_placeholder"
        else:
            return "container"

    def _extract_position(self, node: dict) -> dict:
        """Extract position from bounding box"""
        bbox = node.get("absoluteBoundingBox", {})
        return {
            "x": bbox.get("x", 0),
            "y": bbox.get("y", 0)
        }

    def _extract_size(self, node: dict) -> dict:
        """Extract size from bounding box"""
        bbox = node.get("absoluteBoundingBox", {})
        return {
            "width": bbox.get("width", 0),
            "height": bbox.get("height", 0)
        }

    def _extract_styles(self, node: dict) -> dict:
        """Extract visual styles from a node"""
        styles = {}

        # Background/Fill
        fills = node.get("fills", [])
        if fills:
            for fill in fills:
                if fill.get("type") == "SOLID":
                    styles["background_color"] = fill.get("color", "")
                    if fill.get("opacity"):
                        styles["background_opacity"] = fill.get("opacity")

        # Border/Stroke
        strokes = node.get("strokes", [])
        if strokes:
            for stroke in strokes:
                if stroke.get("type") == "SOLID":
                    styles["border_color"] = stroke.get("color", "")

        # Corner radius
        if node.get("cornerRadius"):
            styles["border_radius"] = node.get("cornerRadius")

        return styles

    def _extract_typography(self, node: dict) -> dict:
        """Extract typography styles from a text node"""
        style = node.get("style", {})
        fills = node.get("fills", [])

        typo = {
            "font_family": style.get("fontFamily", "Inter"),
            "font_size": style.get("fontSize", 16),
            "font_weight": style.get("fontWeight", 400),
            "line_height": style.get("lineHeightPx", 24),
            "text_align": style.get("textAlignHorizontal", "LEFT").lower(),
            "letter_spacing": style.get("letterSpacing", 0)
        }

        # Text color
        if fills:
            for fill in fills:
                if fill.get("type") == "SOLID":
                    typo["color"] = fill.get("color", "#000000")

        return typo
