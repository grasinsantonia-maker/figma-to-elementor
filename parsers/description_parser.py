#!/usr/bin/env python3
"""
Description Parser - Converts natural language descriptions to design specifications
Parses user input to extract: style preferences, sections needed, content, colors, etc.
"""

import re
from typing import Dict, List, Any

class DescriptionParser:
    def __init__(self):
        # Color keywords mapping
        self.color_keywords = {
            'blue': '#0066cc',
            'dark blue': '#003366',
            'light blue': '#66b3ff',
            'navy': '#001f3f',
            'green': '#28a745',
            'dark green': '#155724',
            'light green': '#90EE90',
            'red': '#dc3545',
            'orange': '#fd7e14',
            'yellow': '#ffc107',
            'purple': '#6f42c1',
            'pink': '#e83e8c',
            'black': '#1a1a1a',
            'dark': '#333333',
            'gray': '#6c757d',
            'grey': '#6c757d',
            'light gray': '#f8f9fa',
            'light grey': '#f8f9fa',
            'white': '#ffffff',
            'cream': '#fffdd0',
            'beige': '#f5f5dc',
            'teal': '#20c997',
            'cyan': '#17a2b8',
            'gold': '#ffd700',
            'silver': '#c0c0c0',
            'coral': '#ff7f50',
            'salmon': '#fa8072',
            'turquoise': '#40e0d0',
            'mint': '#98ff98',
            'lavender': '#e6e6fa',
            'maroon': '#800000',
            'olive': '#808000'
        }

        # Industry/style keywords
        self.industry_styles = {
            'tech': {'colors': ['#0066cc', '#333333'], 'fonts': ['Inter', 'Roboto'], 'style': 'modern'},
            'technology': {'colors': ['#0066cc', '#333333'], 'fonts': ['Inter', 'Roboto'], 'style': 'modern'},
            'startup': {'colors': ['#6f42c1', '#333333'], 'fonts': ['Poppins', 'Inter'], 'style': 'modern'},
            'corporate': {'colors': ['#003366', '#333333'], 'fonts': ['Open Sans', 'Lato'], 'style': 'professional'},
            'business': {'colors': ['#0066cc', '#333333'], 'fonts': ['Open Sans', 'Lato'], 'style': 'professional'},
            'agency': {'colors': ['#ff6600', '#333333'], 'fonts': ['Montserrat', 'Raleway'], 'style': 'creative'},
            'creative': {'colors': ['#e83e8c', '#333333'], 'fonts': ['Playfair Display', 'Raleway'], 'style': 'creative'},
            'medical': {'colors': ['#17a2b8', '#333333'], 'fonts': ['Open Sans', 'Lato'], 'style': 'clean'},
            'healthcare': {'colors': ['#28a745', '#333333'], 'fonts': ['Open Sans', 'Lato'], 'style': 'clean'},
            'legal': {'colors': ['#003366', '#333333'], 'fonts': ['Merriweather', 'Open Sans'], 'style': 'professional'},
            'law': {'colors': ['#003366', '#333333'], 'fonts': ['Merriweather', 'Open Sans'], 'style': 'professional'},
            'finance': {'colors': ['#003366', '#28a745'], 'fonts': ['Roboto', 'Open Sans'], 'style': 'professional'},
            'fintech': {'colors': ['#6f42c1', '#28a745'], 'fonts': ['Inter', 'Roboto'], 'style': 'modern'},
            'real estate': {'colors': ['#C9A87C', '#1a1a2e'], 'fonts': ['Poppins', 'Lato'], 'style': 'luxury', 'industry': 'real_estate'},
            'property': {'colors': ['#C9A87C', '#1a1a2e'], 'fonts': ['Poppins', 'Lato'], 'style': 'luxury', 'industry': 'real_estate'},
            'realty': {'colors': ['#C9A87C', '#1a1a2e'], 'fonts': ['Poppins', 'Lato'], 'style': 'luxury', 'industry': 'real_estate'},
            'dubai': {'colors': ['#C9A87C', '#1a1a2e'], 'fonts': ['Poppins', 'Lato'], 'style': 'luxury', 'industry': 'real_estate'},
            'luxury': {'colors': ['#C9A87C', '#1a1a2e'], 'fonts': ['Poppins', 'Lato'], 'style': 'luxury', 'industry': 'real_estate'},
            'restaurant': {'colors': ['#dc3545', '#333333'], 'fonts': ['Playfair Display', 'Lato'], 'style': 'warm'},
            'food': {'colors': ['#fd7e14', '#333333'], 'fonts': ['Poppins', 'Open Sans'], 'style': 'warm'},
            'fashion': {'colors': ['#1a1a1a', '#ffffff'], 'fonts': ['Playfair Display', 'Montserrat'], 'style': 'elegant'},
            'beauty': {'colors': ['#e83e8c', '#333333'], 'fonts': ['Cormorant Garamond', 'Lato'], 'style': 'elegant'},
            'fitness': {'colors': ['#dc3545', '#1a1a1a'], 'fonts': ['Oswald', 'Open Sans'], 'style': 'bold'},
            'sports': {'colors': ['#fd7e14', '#1a1a1a'], 'fonts': ['Oswald', 'Roboto'], 'style': 'bold'},
            'education': {'colors': ['#0066cc', '#333333'], 'fonts': ['Open Sans', 'Lato'], 'style': 'friendly'},
            'nonprofit': {'colors': ['#28a745', '#333333'], 'fonts': ['Open Sans', 'Lato'], 'style': 'friendly'},
            'ecommerce': {'colors': ['#fd7e14', '#333333'], 'fonts': ['Poppins', 'Open Sans'], 'style': 'modern'},
            'saas': {'colors': ['#6f42c1', '#333333'], 'fonts': ['Inter', 'Roboto'], 'style': 'modern'},
            'consulting': {'colors': ['#003366', '#333333'], 'fonts': ['Lato', 'Open Sans'], 'style': 'professional'},
            'marketing': {'colors': ['#ff6600', '#333333'], 'fonts': ['Montserrat', 'Open Sans'], 'style': 'creative'},
            'seo': {'colors': ['#28a745', '#333333'], 'fonts': ['Inter', 'Roboto'], 'style': 'modern'},
            'photography': {'colors': ['#1a1a1a', '#ffffff'], 'fonts': ['Playfair Display', 'Lato'], 'style': 'minimal'},
            'portfolio': {'colors': ['#1a1a1a', '#ffffff'], 'fonts': ['Montserrat', 'Open Sans'], 'style': 'minimal'}
        }

        # Section keywords
        self.section_keywords = {
            'services': ['services', 'service', 'what we do', 'what we offer', 'offerings', 'solutions'],
            'about': ['about', 'about us', 'who we are', 'our story', 'company', 'team story'],
            'testimonials': ['testimonials', 'reviews', 'client feedback', 'what clients say', 'customer reviews'],
            'team': ['team', 'our team', 'meet the team', 'staff', 'people', 'employees'],
            'portfolio': ['portfolio', 'work', 'projects', 'case studies', 'gallery', 'our work'],
            'pricing': ['pricing', 'prices', 'plans', 'packages', 'cost', 'rates'],
            'faq': ['faq', 'questions', 'frequently asked', 'q&a', 'help'],
            'contact': ['contact', 'get in touch', 'reach us', 'contact us', 'reach out'],
            'cta': ['cta', 'call to action', 'get started', 'sign up', 'subscribe'],
            'stats': ['stats', 'statistics', 'numbers', 'achievements', 'metrics', 'results'],
            'clients': ['clients', 'partners', 'brands', 'logos', 'trusted by', 'companies'],
            'blog': ['blog', 'articles', 'news', 'posts', 'updates', 'insights']
        }

        # Style/mood keywords
        self.style_keywords = {
            'modern': {'border_radius': '8', 'spacing': 'medium'},
            'minimal': {'border_radius': '0', 'spacing': 'large'},
            'minimalist': {'border_radius': '0', 'spacing': 'large'},
            'clean': {'border_radius': '4', 'spacing': 'medium'},
            'bold': {'border_radius': '0', 'spacing': 'small'},
            'elegant': {'border_radius': '4', 'spacing': 'large'},
            'playful': {'border_radius': '16', 'spacing': 'medium'},
            'professional': {'border_radius': '4', 'spacing': 'medium'},
            'friendly': {'border_radius': '12', 'spacing': 'medium'},
            'luxury': {'border_radius': '0', 'spacing': 'large'},
            'creative': {'border_radius': '12', 'spacing': 'medium'},
            'warm': {'border_radius': '8', 'spacing': 'medium'},
            'corporate': {'border_radius': '4', 'spacing': 'medium'},
            'rounded': {'border_radius': '24', 'spacing': 'medium'},
            'sharp': {'border_radius': '0', 'spacing': 'medium'}
        }

    def parse(self, description: str, inspirations: List[Dict] = None) -> Dict[str, Any]:
        """
        Parse a natural language description into a design specification

        Args:
            description: User's text description of the desired website
            inspirations: Optional list of analyzed inspiration sites

        Returns:
            Design specification dictionary
        """
        description_lower = description.lower()

        # Extract site name
        site_name = self._extract_site_name(description)

        # Extract colors
        colors = self._extract_colors(description_lower, inspirations)

        # Extract industry/style
        industry_style = self._extract_industry_style(description_lower)

        # Extract fonts
        fonts = self._extract_fonts(description_lower, industry_style, inspirations)

        # Extract sections
        sections = self._extract_sections(description_lower)

        # Extract button style
        button_style = self._extract_button_style(description_lower)

        # Extract spacing
        spacing = self._extract_spacing(description_lower)

        # Extract hero content
        hero = self._extract_hero_content(description)

        # Build design spec
        design_spec = {
            'site_name': site_name,
            'colors': colors,
            'fonts': fonts,
            'button_style': button_style,
            'spacing': spacing,
            'header': True,
            'hero': hero,
            'sections': sections,
            'footer': True,
            'style': industry_style.get('style', 'modern'),
            'industry': industry_style.get('industry', 'default')
        }

        # Merge with inspiration insights if provided
        if inspirations:
            design_spec = self._merge_with_inspirations(design_spec, inspirations)

        return design_spec

    def _extract_site_name(self, description: str) -> str:
        """Extract site/brand name from description"""
        # Look for patterns like "for [Name]", "called [Name]", "[Name] website"
        patterns = [
            r'(?:for|called|named)\s+["\']?([A-Z][A-Za-z\s]+)["\']?',
            r'([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?)\s+(?:website|site|page)',
            r'(?:brand|company|business)\s+(?:is\s+)?["\']?([A-Z][A-Za-z\s]+)["\']?'
        ]

        for pattern in patterns:
            match = re.search(pattern, description)
            if match:
                return match.group(1).strip()

        return 'Brand'

    def _extract_colors(self, description: str, inspirations: List[Dict] = None) -> Dict[str, str]:
        """Extract color preferences from description"""
        # Check for real estate / luxury keywords first
        if any(keyword in description for keyword in ['real estate', 'property', 'realty', 'dubai', 'luxury']):
            colors = {
                'primary': '#C9A87C',
                'secondary': '#1a1a2e',
                'text': '#ffffff',
                'background': '#0a0a0f',
                'accent': '#C9A87C'
            }
            return colors

        colors = {
            'primary': '#0066cc',
            'secondary': '#333333',
            'text': '#333333',
            'background': '#ffffff',
            'accent': '#ff6600'
        }

        # Check for explicit color mentions
        for color_name, hex_value in self.color_keywords.items():
            if color_name in description:
                # Check context for which type of color
                if any(word in description for word in ['primary', 'main', 'brand']):
                    if color_name in description.split('primary')[0][-30:] or \
                       color_name in description.split('main')[0][-30:]:
                        colors['primary'] = hex_value
                elif 'accent' in description:
                    colors['accent'] = hex_value
                elif 'background' in description:
                    colors['background'] = hex_value
                else:
                    # Default to primary
                    colors['primary'] = hex_value

        # Check for hex colors in description
        hex_matches = re.findall(r'#[0-9a-fA-F]{6}', description)
        if hex_matches:
            colors['primary'] = hex_matches[0]
            if len(hex_matches) > 1:
                colors['accent'] = hex_matches[1]

        # Merge with inspiration colors if available
        if inspirations and 'combined_insights' in inspirations:
            combined = inspirations['combined_insights']
            if combined.get('colors', {}).get('primary'):
                insp_primary = combined['colors']['primary']
                if isinstance(insp_primary, list) and insp_primary:
                    colors['primary'] = insp_primary[0]

        return colors

    def _extract_industry_style(self, description: str) -> Dict:
        """Extract industry-specific styling"""
        for industry, style_info in self.industry_styles.items():
            if industry in description:
                return style_info

        # Default modern style
        return {'colors': ['#0066cc', '#333333'], 'fonts': ['Inter'], 'style': 'modern'}

    def _extract_fonts(self, description: str, industry_style: Dict, inspirations: List[Dict] = None) -> List[str]:
        """Extract font preferences"""
        fonts = []

        # Check for explicit font mentions
        font_patterns = [
            r'(?:font|typography)[:\s]+([A-Za-z\s]+)',
            r'use\s+([A-Za-z]+)\s+font'
        ]

        for pattern in font_patterns:
            match = re.search(pattern, description)
            if match:
                fonts.append(match.group(1).strip())

        # Use industry defaults if no explicit fonts
        if not fonts:
            fonts = industry_style.get('fonts', ['Inter'])

        # Merge with inspiration fonts
        if inspirations and 'combined_insights' in inspirations:
            insp_fonts = inspirations['combined_insights'].get('fonts', [])
            if insp_fonts:
                fonts = insp_fonts[:2] + fonts

        return list(dict.fromkeys(fonts))[:3]  # Unique, max 3

    def _extract_sections(self, description: str) -> List[Dict]:
        """Extract desired sections from description"""
        sections = []

        # Check for explicit section mentions
        for section_type, keywords in self.section_keywords.items():
            for keyword in keywords:
                if keyword in description:
                    section = {'type': section_type, 'title': section_type.replace('_', ' ').title()}

                    # Extract custom title if provided
                    title_match = re.search(rf'{keyword}\s+(?:section\s+)?(?:called|titled|named)\s+["\']?([^"\']+)["\']?', description)
                    if title_match:
                        section['title'] = title_match.group(1)

                    sections.append(section)
                    break

        # Default sections if none specified
        if not sections:
            sections = [
                {'type': 'services', 'title': 'Our Services'},
                {'type': 'about', 'title': 'About Us'},
                {'type': 'testimonials', 'title': 'What Our Clients Say'},
                {'type': 'contact', 'title': 'Get In Touch'}
            ]

        return sections

    def _extract_button_style(self, description: str) -> Dict:
        """Extract button styling preferences"""
        button_style = {
            'shape': 'rounded',
            'border_radius': '8'
        }

        # Check for style keywords
        for style, props in self.style_keywords.items():
            if style in description:
                button_style['border_radius'] = props['border_radius']
                if props['border_radius'] == '0':
                    button_style['shape'] = 'rectangular'
                elif int(props['border_radius']) >= 16:
                    button_style['shape'] = 'pill'
                break

        # Check for explicit button descriptions
        if 'rounded button' in description or 'round button' in description:
            button_style = {'shape': 'pill', 'border_radius': '24'}
        elif 'square button' in description or 'sharp button' in description:
            button_style = {'shape': 'rectangular', 'border_radius': '0'}

        return button_style

    def _extract_spacing(self, description: str) -> Dict:
        """Extract spacing preferences"""
        spacing = {
            'section_padding': '80',
            'element_gap': '30'
        }

        if 'compact' in description or 'dense' in description:
            spacing = {'section_padding': '50', 'element_gap': '20'}
        elif 'spacious' in description or 'airy' in description or 'breathing room' in description:
            spacing = {'section_padding': '120', 'element_gap': '40'}

        return spacing

    def _extract_hero_content(self, description: str) -> Dict:
        """Extract hero section content"""
        hero = {
            'headline': 'Transform Your Business',
            'subheadline': 'We deliver innovative solutions to help you succeed.',
            'cta_text': 'Get Started',
            'background_color': '#ffffff'
        }

        # Look for headline patterns
        headline_patterns = [
            r'headline[:\s]+["\']?([^"\'\.]+)["\']?',
            r'main\s+text[:\s]+["\']?([^"\'\.]+)["\']?',
            r'hero\s+(?:text|title)[:\s]+["\']?([^"\'\.]+)["\']?'
        ]

        for pattern in headline_patterns:
            match = re.search(pattern, description, re.IGNORECASE)
            if match:
                hero['headline'] = match.group(1).strip()
                break

        # Look for CTA patterns
        cta_patterns = [
            r'(?:cta|button|call to action)[:\s]+["\']?([^"\'\.]+)["\']?',
            r'button\s+(?:text|says)[:\s]+["\']?([^"\'\.]+)["\']?'
        ]

        for pattern in cta_patterns:
            match = re.search(pattern, description, re.IGNORECASE)
            if match:
                hero['cta_text'] = match.group(1).strip()
                break

        return hero

    def _merge_with_inspirations(self, design_spec: Dict, inspirations: Dict) -> Dict:
        """Merge design spec with insights from inspiration sites"""
        if 'combined_insights' not in inspirations:
            return design_spec

        combined = inspirations['combined_insights']

        # Use recommended sections from inspirations
        if combined.get('recommended_sections') and not design_spec.get('sections'):
            design_spec['sections'] = [
                {'type': s, 'title': s.replace('_', ' ').title()}
                for s in combined['recommended_sections']
            ]

        return design_spec


# Test the parser
if __name__ == "__main__":
    parser = DescriptionParser()

    test_description = """
    I want a modern tech startup website for TechFlow with blue and white colors.
    It should have a services section, about us, testimonials, and a contact form.
    Use Inter font, rounded buttons, and make it feel spacious and clean.
    The headline should be "Innovate Your Future" with a "Start Free Trial" button.
    """

    result = parser.parse(test_description)
    import json
    print(json.dumps(result, indent=2))
