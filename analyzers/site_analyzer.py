#!/usr/bin/env python3
"""
Site Analyzer - Extracts design patterns from inspiration websites
Analyzes: colors, typography, structure, UX patterns, section layouts
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
import json
from collections import Counter

class SiteAnalyzer:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }

    def analyze_site(self, url):
        """Main method to analyze a website"""
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            analysis = {
                'url': url,
                'colors': self._extract_colors(soup, response.text),
                'typography': self._extract_typography(soup, response.text),
                'structure': self._extract_structure(soup),
                'sections': self._extract_sections(soup),
                'ux_patterns': self._extract_ux_patterns(soup),
                'images': self._extract_image_patterns(soup, url),
                'buttons': self._extract_button_styles(soup, response.text),
                'spacing': self._extract_spacing_patterns(response.text)
            }

            return analysis
        except Exception as e:
            return {'error': str(e), 'url': url}

    def _extract_colors(self, soup, css_text):
        """Extract color palette from the site"""
        colors = {
            'primary': [],
            'secondary': [],
            'background': [],
            'text': [],
            'accent': [],
            'all_colors': []
        }

        # Find all hex colors
        hex_pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'
        hex_colors = re.findall(hex_pattern, css_text)

        # Find all rgb/rgba colors
        rgb_pattern = r'rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*[\d.]+)?\s*\)'
        rgb_colors = re.findall(rgb_pattern, css_text)

        # Convert rgb to hex
        for r, g, b in rgb_colors:
            hex_color = '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))
            hex_colors.append(hex_color)

        # Normalize and count colors
        color_counts = Counter([c.lower() for c in hex_colors])

        # Filter out common defaults
        ignore_colors = ['#fff', '#ffffff', '#000', '#000000', '#ccc', '#cccccc']
        filtered_colors = {k: v for k, v in color_counts.items() if k not in ignore_colors}

        # Sort by frequency
        sorted_colors = sorted(filtered_colors.items(), key=lambda x: x[1], reverse=True)
        colors['all_colors'] = [c[0] for c in sorted_colors[:15]]

        # Categorize colors
        for color, count in sorted_colors[:10]:
            r, g, b = self._hex_to_rgb(color)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255

            if luminance > 0.9:
                colors['background'].append(color)
            elif luminance < 0.2:
                colors['text'].append(color)
            elif self._is_saturated(r, g, b):
                if not colors['primary']:
                    colors['primary'].append(color)
                elif not colors['accent']:
                    colors['accent'].append(color)
                else:
                    colors['secondary'].append(color)

        # Set defaults if empty
        if not colors['primary']:
            colors['primary'] = colors['all_colors'][:1] if colors['all_colors'] else ['#0066cc']
        if not colors['text']:
            colors['text'] = ['#333333']
        if not colors['background']:
            colors['background'] = ['#ffffff']

        return colors

    def _hex_to_rgb(self, hex_color):
        """Convert hex to RGB"""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join([c*2 for c in hex_color])
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def _is_saturated(self, r, g, b):
        """Check if color is saturated (not grayscale)"""
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        if max_c == 0:
            return False
        saturation = (max_c - min_c) / max_c
        return saturation > 0.3

    def _extract_typography(self, soup, css_text):
        """Extract typography patterns"""
        typography = {
            'fonts': [],
            'headings': [],
            'body_size': '16px',
            'line_height': '1.6'
        }

        # Find Google Fonts
        for link in soup.find_all('link', href=True):
            if 'fonts.googleapis.com' in link['href']:
                font_match = re.search(r'family=([^:&]+)', link['href'])
                if font_match:
                    font_name = font_match.group(1).replace('+', ' ')
                    typography['fonts'].append(font_name)

        # Find font-family in CSS
        font_pattern = r'font-family:\s*["\']?([^;"\']+)'
        fonts_in_css = re.findall(font_pattern, css_text)
        for font in fonts_in_css:
            clean_font = font.split(',')[0].strip().strip('"\'')
            if clean_font and clean_font not in typography['fonts']:
                typography['fonts'].append(clean_font)

        # Extract heading sizes
        heading_sizes = []
        for i in range(1, 7):
            h_pattern = rf'h{i}\s*\{{[^}}]*font-size:\s*(\d+)'
            matches = re.findall(h_pattern, css_text)
            if matches:
                heading_sizes.append({'tag': f'h{i}', 'size': f'{matches[0]}px'})
        typography['headings'] = heading_sizes or [
            {'tag': 'h1', 'size': '48px'},
            {'tag': 'h2', 'size': '36px'},
            {'tag': 'h3', 'size': '28px'},
            {'tag': 'h4', 'size': '22px'}
        ]

        # Default fonts if none found
        if not typography['fonts']:
            typography['fonts'] = ['Inter', 'system-ui', 'sans-serif']

        return typography

    def _extract_structure(self, soup):
        """Extract page structure - header, sections, footer"""
        structure = {
            'has_header': False,
            'has_footer': False,
            'has_hero': False,
            'section_count': 0,
            'layout_type': 'single_column',
            'sections_order': []
        }

        # Check for header
        header = soup.find('header') or soup.find(class_=re.compile(r'header|nav', re.I))
        structure['has_header'] = header is not None

        # Check for footer
        footer = soup.find('footer') or soup.find(class_=re.compile(r'footer', re.I))
        structure['has_footer'] = footer is not None

        # Check for hero section
        hero = soup.find(class_=re.compile(r'hero|banner|jumbotron', re.I))
        structure['has_hero'] = hero is not None

        # Count and identify sections
        sections = soup.find_all(['section', 'div'], class_=re.compile(r'section|block|container', re.I))
        structure['section_count'] = len(sections)

        # Identify section types
        section_types = []
        for section in sections[:10]:  # Limit to first 10
            section_class = ' '.join(section.get('class', []))
            section_id = section.get('id', '')
            combined = f"{section_class} {section_id}".lower()

            if re.search(r'hero|banner|intro', combined):
                section_types.append('hero')
            elif re.search(r'service|feature|benefit', combined):
                section_types.append('services')
            elif re.search(r'about|story|who', combined):
                section_types.append('about')
            elif re.search(r'testimonial|review|client', combined):
                section_types.append('testimonials')
            elif re.search(r'team|people|staff', combined):
                section_types.append('team')
            elif re.search(r'contact|cta|action', combined):
                section_types.append('cta')
            elif re.search(r'pricing|plan|package', combined):
                section_types.append('pricing')
            elif re.search(r'portfolio|work|project|gallery', combined):
                section_types.append('portfolio')
            elif re.search(r'faq|question|accordion', combined):
                section_types.append('faq')
            elif re.search(r'blog|news|article|post', combined):
                section_types.append('blog')

        structure['sections_order'] = list(dict.fromkeys(section_types))  # Remove duplicates, keep order

        return structure

    def _extract_sections(self, soup):
        """Extract detailed section information"""
        sections = []

        # Find all major sections
        for section in soup.find_all(['section', 'div'], class_=re.compile(r'section|block', re.I))[:8]:
            section_info = {
                'type': 'generic',
                'columns': 1,
                'has_image': False,
                'has_icon': False,
                'text_align': 'left',
                'background': 'light'
            }

            # Check for columns
            cols = section.find_all(class_=re.compile(r'col-|column|grid', re.I))
            if cols:
                section_info['columns'] = min(len(cols), 4)

            # Check for images
            images = section.find_all('img')
            section_info['has_image'] = len(images) > 0

            # Check for icons (svg or icon classes)
            icons = section.find_all(['svg', 'i'], class_=re.compile(r'icon|fa-|svg', re.I))
            section_info['has_icon'] = len(icons) > 0

            # Detect section type from content
            text_content = section.get_text().lower()
            if re.search(r'contact|get in touch|reach out', text_content):
                section_info['type'] = 'contact'
            elif re.search(r'service|what we do|offer', text_content):
                section_info['type'] = 'services'
            elif re.search(r'about|who we are|our story', text_content):
                section_info['type'] = 'about'
            elif re.search(r'testimonial|client|review|said', text_content):
                section_info['type'] = 'testimonials'

            sections.append(section_info)

        return sections

    def _extract_ux_patterns(self, soup):
        """Extract UX patterns - navigation, CTAs, forms"""
        patterns = {
            'nav_style': 'horizontal',
            'has_sticky_nav': False,
            'cta_count': 0,
            'has_contact_form': False,
            'has_social_links': False,
            'has_search': False,
            'has_hamburger_menu': False
        }

        # Navigation style
        nav = soup.find('nav')
        if nav:
            nav_class = ' '.join(nav.get('class', []))
            if 'vertical' in nav_class.lower():
                patterns['nav_style'] = 'vertical'
            if 'sticky' in nav_class.lower() or 'fixed' in nav_class.lower():
                patterns['has_sticky_nav'] = True

        # Count CTAs
        cta_buttons = soup.find_all(['a', 'button'], class_=re.compile(r'btn|button|cta', re.I))
        patterns['cta_count'] = len(cta_buttons)

        # Check for form
        forms = soup.find_all('form')
        patterns['has_contact_form'] = len(forms) > 0

        # Check for social links
        social_links = soup.find_all('a', href=re.compile(r'facebook|twitter|linkedin|instagram', re.I))
        patterns['has_social_links'] = len(social_links) > 0

        # Check for search
        search = soup.find(['input', 'form'], attrs={'type': 'search'}) or \
                 soup.find(class_=re.compile(r'search', re.I))
        patterns['has_search'] = search is not None

        # Check for hamburger menu
        hamburger = soup.find(class_=re.compile(r'hamburger|mobile-menu|menu-toggle', re.I))
        patterns['has_hamburger_menu'] = hamburger is not None

        return patterns

    def _extract_image_patterns(self, soup, base_url):
        """Extract image usage patterns"""
        patterns = {
            'hero_image': False,
            'background_images': 0,
            'inline_images': 0,
            'icon_style': 'none',
            'image_shapes': 'rectangular'
        }

        # Count images
        images = soup.find_all('img')
        patterns['inline_images'] = len(images)

        # Check for hero image
        hero = soup.find(class_=re.compile(r'hero|banner', re.I))
        if hero:
            hero_img = hero.find('img') or hero.get('style', '')
            patterns['hero_image'] = bool(hero_img)

        # Check for SVG icons vs font icons
        svg_icons = soup.find_all('svg')
        font_icons = soup.find_all('i', class_=re.compile(r'fa-|icon-', re.I))
        if len(svg_icons) > len(font_icons):
            patterns['icon_style'] = 'svg'
        elif font_icons:
            patterns['icon_style'] = 'font'

        # Check for rounded images
        rounded_imgs = soup.find_all('img', class_=re.compile(r'round|circle', re.I))
        if rounded_imgs:
            patterns['image_shapes'] = 'rounded'

        return patterns

    def _extract_button_styles(self, soup, css_text):
        """Extract button styling patterns"""
        styles = {
            'shape': 'rectangular',
            'style': 'solid',
            'has_hover_effect': True,
            'border_radius': '4px'
        }

        # Check for rounded buttons
        btn_radius = re.search(r'\.btn[^{]*\{[^}]*border-radius:\s*(\d+)', css_text)
        if btn_radius:
            radius = int(btn_radius.group(1))
            styles['border_radius'] = f'{radius}px'
            if radius >= 20:
                styles['shape'] = 'pill'
            elif radius > 0:
                styles['shape'] = 'rounded'

        # Check button style (solid, outline, ghost)
        if re.search(r'\.btn[^{]*\{[^}]*background:\s*(transparent|none)', css_text):
            styles['style'] = 'outline'

        return styles

    def _extract_spacing_patterns(self, css_text):
        """Extract spacing/padding patterns"""
        spacing = {
            'section_padding': '80px',
            'element_gap': '30px',
            'content_width': '1200px'
        }

        # Find common padding values
        padding_pattern = r'padding[^:]*:\s*(\d+)px'
        paddings = [int(p) for p in re.findall(padding_pattern, css_text)]
        if paddings:
            common_padding = max(set(paddings), key=paddings.count)
            if common_padding > 40:
                spacing['section_padding'] = f'{common_padding}px'

        # Find max-width/container width
        width_pattern = r'max-width:\s*(\d+)px'
        widths = [int(w) for w in re.findall(width_pattern, css_text)]
        if widths:
            common_width = max(widths)
            spacing['content_width'] = f'{common_width}px'

        return spacing

    def analyze_multiple(self, urls):
        """Analyze multiple sites and combine insights"""
        all_analyses = []
        combined = {
            'colors': {'primary': [], 'secondary': [], 'all': []},
            'fonts': [],
            'common_sections': [],
            'ux_patterns': {},
            'button_styles': []
        }

        for url in urls:
            analysis = self.analyze_site(url)
            if 'error' not in analysis:
                all_analyses.append(analysis)

                # Combine colors
                combined['colors']['primary'].extend(analysis['colors'].get('primary', []))
                combined['colors']['all'].extend(analysis['colors'].get('all_colors', []))

                # Combine fonts
                combined['fonts'].extend(analysis['typography'].get('fonts', []))

                # Track section patterns
                combined['common_sections'].extend(analysis['structure'].get('sections_order', []))

        # Find most common elements
        combined['colors']['primary'] = list(set(combined['colors']['primary']))[:3]
        combined['fonts'] = list(dict.fromkeys(combined['fonts']))[:3]  # Unique, preserve order

        # Count section frequency
        section_counts = Counter(combined['common_sections'])
        combined['recommended_sections'] = [s[0] for s in section_counts.most_common(6)]

        return {
            'individual_analyses': all_analyses,
            'combined_insights': combined
        }


if __name__ == "__main__":
    # Test the analyzer
    analyzer = SiteAnalyzer()

    # Test with a sample site
    test_url = "https://stripe.com"
    print(f"Analyzing {test_url}...")
    result = analyzer.analyze_site(test_url)
    print(json.dumps(result, indent=2, default=str))
