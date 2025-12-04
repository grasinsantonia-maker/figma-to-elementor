#!/usr/bin/env python3
"""
PRO-LEVEL Elementor Generator - Creates stunning, agency-quality pages
Inspired by AX Capital, ThriveState.io, premium real estate & SaaS sites
"""

import json
import random
import string

class ElementorProGenerator:
    def __init__(self):
        self.id_counter = 0

        # Industry-specific configurations
        self.industry_configs = {
            'real_estate': {
                'nav_items': ['Buy', 'Rent', 'Sell', 'Off-Plan', 'Catalogs', 'Agents', 'About'],
                'hero_headline': 'INVEST IN DUBAI REAL ESTATE WITH',
                'hero_subheadline': 'We bring Due Diligence at Your service',
                'cta_primary': 'Leave a request',
                'cta_secondary': 'Already an owner?',
                'search_tabs': ['Primary', 'Secondary'],
                'search_fields': [
                    {'label': 'Property type', 'placeholder': 'Property type', 'type': 'dropdown'},
                    {'label': 'Bedrooms', 'placeholder': 'Bedrooms', 'type': 'dropdown'},
                    {'label': 'Currency', 'options': ['GBP', 'CNY', 'EUR', 'AED', 'USD'], 'type': 'buttons'},
                    {'label': 'Price Range', 'min': 'Min 40 000', 'max': 'Max 150 000 000', 'type': 'range'}
                ],
                'search_button': 'Show 81 projects',
                'secondary_button': 'Properties on map',
                'colors': {
                    'primary': '#C9A87C',
                    'secondary': '#1a1a2e',
                    'background': '#0a0a0f',
                    'accent': '#C9A87C',
                    'text': '#ffffff'
                }
            },
            'default': {
                'nav_items': ['Services', 'About', 'Portfolio', 'Contact'],
                'hero_headline': 'Transform Your Business',
                'hero_subheadline': 'We deliver innovative solutions to help you succeed.',
                'cta_primary': 'Get Started',
                'cta_secondary': 'Learn More',
                'search_tabs': ['Primary', 'Secondary'],
                'search_fields': [
                    {'label': 'Service type', 'placeholder': 'Select service type', 'type': 'dropdown'},
                    {'label': 'Category', 'placeholder': 'Select category', 'type': 'dropdown'}
                ],
                'search_button': 'Search Services',
                'colors': {
                    'primary': '#C9A87C',
                    'secondary': '#1a1a2e',
                    'background': '#0a0a0f',
                    'accent': '#C9A87C',
                    'text': '#ffffff'
                }
            }
        }

    def _get_industry_config(self, design_spec):
        """Get industry-specific configuration"""
        industry = design_spec.get('industry', 'default')
        return self.industry_configs.get(industry, self.industry_configs['default'])

    def _generate_id(self):
        """Generate unique Elementor element ID"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

    def generate_page(self, design_spec):
        """Generate complete pro-level Elementor page"""
        sections = []

        # 1. COMBINED: Hero with integrated floating header (AX Capital style)
        if design_spec.get('hero', True):
            sections.append(self._create_premium_hero_with_header(design_spec))

        # 2. Trusted by / logos section
        sections.append(self._create_trusted_by_section(design_spec))

        # 3. Generate content sections
        for section in design_spec.get('sections', []):
            section_type = section.get('type', 'generic')

            if section_type == 'services':
                sections.append(self._create_pro_services(design_spec, section))
            elif section_type == 'about':
                sections.append(self._create_pro_about(design_spec, section))
            elif section_type == 'testimonials':
                sections.append(self._create_pro_testimonials(design_spec, section))
            elif section_type == 'features':
                sections.append(self._create_pro_features(design_spec, section))
            elif section_type == 'cta':
                sections.append(self._create_pro_cta(design_spec, section))
            elif section_type == 'contact':
                sections.append(self._create_pro_contact(design_spec, section))
            elif section_type == 'pricing':
                sections.append(self._create_pro_pricing(design_spec, section))
            elif section_type == 'faq':
                sections.append(self._create_pro_faq(design_spec, section))

        # 4. Final CTA section
        sections.append(self._create_final_cta(design_spec))

        # 5. Pro footer
        if design_spec.get('footer', True):
            sections.append(self._create_pro_footer(design_spec))

        return {
            'content': sections,
            'page_settings': {
                'hide_title': 'yes',
                'template': 'elementor_canvas',
                'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'custom_css': 'html, body { margin: 0 !important; padding: 0 !important; } .elementor { margin-top: 0 !important; }'
            },
            'version': '0.4',
            'type': 'page'
        }

    def _get_colors(self, design_spec):
        """Extract colors with premium defaults (AX Capital inspired)"""
        colors = design_spec.get('colors', {})

        def get_color(key, default):
            val = colors.get(key, default)
            if isinstance(val, list):
                return val[0] if val else default
            return val

        return {
            'primary': get_color('primary', '#C9A87C'),  # Elegant gold/bronze
            'secondary': get_color('secondary', '#1a1a2e'),  # Deep navy
            'text': get_color('text', '#ffffff'),
            'text_light': 'rgba(255,255,255,0.7)',
            'text_dark': '#1a1a2e',
            'background': get_color('background', '#0a0a0f'),  # Near black
            'background_alt': '#f8f6f3',  # Warm off-white
            'accent': get_color('accent', '#C9A87C'),  # Gold accent
            'dark': '#0a0a0f',
            'cta_primary': '#C9A87C',  # Gold CTA
            'cta_secondary': 'transparent',
            'overlay': 'rgba(0,0,0,0.5)',
            'gradient_start': '#1a1a2e',  # For gradient sections
            'gradient_end': '#C9A87C'
        }

    def _get_fonts(self, design_spec):
        """Get font - returns empty string to use theme defaults (avoids Elementor Pro font errors)"""
        # NOTE: Removed custom font family to avoid "Illegal offset type" error in Elementor Pro
        # The page will use the theme's default fonts
        return ''

    def _get_typography_settings(self, font, size, weight='400', line_height='1.4', letter_spacing='0'):
        """Generate proper Elementor typography settings - without font family to avoid errors"""
        # NOTE: Removed typography_font_family to avoid Elementor Pro fonts-manager.php error
        return {
            'typography_typography': 'custom',
            'typography_font_size': {'unit': 'px', 'size': size},
            'typography_font_weight': str(weight),
            'typography_line_height': {'unit': 'em', 'size': float(line_height)},
            'typography_letter_spacing': {'unit': 'px', 'size': float(letter_spacing)}
        }

    # ==================== PREMIUM HERO - FULL WIDTH 1920px DESKTOP ====================
    def _create_premium_hero_with_header(self, design_spec):
        """Create FULL-WIDTH hero (1920px) with AX Capital style - DESKTOP FIRST"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        industry_config = self._get_industry_config(design_spec)
        hero = design_spec.get('hero', {})
        site_name = design_spec.get('site_name', 'AX Capital')

        # Use industry-specific content
        nav_items = industry_config['nav_items']
        headline = industry_config['hero_headline']
        subheadline = industry_config['hero_subheadline']
        cta_text = industry_config['cta_primary']
        cta_secondary = industry_config['cta_secondary']

        # Build the complete hero section - TRUE FULL WIDTH
        return {
            'id': self._generate_id(),
            'elType': 'section',
            'settings': {
                'layout': 'full_width',
                'content_width': {'unit': 'px', 'size': 1920},
                'stretch_section': 'section-stretched',
                'height': 'min-height',
                'custom_height': {'unit': 'vh', 'size': 100},
                'column_position': 'middle',
                'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'background_background': 'classic',
                'background_image': {
                    'url': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=1920&q=80',
                    'id': ''
                },
                'background_position': 'center center',
                'background_size': 'cover',
                'background_overlay_background': 'classic',
                'background_overlay_color': 'rgba(0, 0, 0, 0.5)'
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'column',
                    'settings': {
                        '_column_size': 100,
                        'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
                    },
                    'elements': [
                        # ===== HEADER ROW =====
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'full',
                                'flex_direction': 'row',
                                'flex_justify_content': 'space-between',
                                'flex_align_items': 'center',
                                'padding': {'unit': 'px', 'top': '30', 'right': '80', 'bottom': '30', 'left': '80'}
                            },
                            'elements': [
                                # Logo
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'heading',
                                    'settings': {
                                        'title': site_name,
                                        'header_size': 'h4',
                                        'title_color': colors['primary'],
                                        'typography_typography': 'custom',
                                        'typography_font_weight': '300',
                                        'typography_font_size': {'unit': 'px', 'size': 28},
                                        'typography_letter_spacing': {'unit': 'px', 'size': 2}
                                    }
                                },
                                # Navigation container
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'content_width': 'full',
                                        'flex_direction': 'row',
                                        'flex_justify_content': 'center',
                                        'flex_align_items': 'center',
                                        'flex_gap': {'unit': 'px', 'size': 35}
                                    },
                                    'elements': [
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': nav_items[0], 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 13}, 'typography_font_weight': '400'}},
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': nav_items[1], 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 13}, 'typography_font_weight': '400'}},
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': nav_items[2], 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 13}, 'typography_font_weight': '400'}},
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': nav_items[3], 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 13}, 'typography_font_weight': '400'}},
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': nav_items[4], 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 13}, 'typography_font_weight': '400'}},
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': nav_items[5], 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 13}, 'typography_font_weight': '400'}},
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': nav_items[6], 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 13}, 'typography_font_weight': '400'}}
                                    ]
                                },
                                # Right side CTAs
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'flex_direction': 'row',
                                        'flex_gap': {'unit': 'px', 'size': 25}
                                    },
                                    'elements': [
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': 'FOLLOW US', 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 11}, 'typography_font_weight': '500', 'typography_letter_spacing': {'unit': 'px', 'size': 1}}},
                                        {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': {'title': 'CALL US', 'header_size': 'span', 'title_color': '#ffffff', 'typography_typography': 'custom', 'typography_font_size': {'unit': 'px', 'size': 11}, 'typography_font_weight': '500', 'typography_letter_spacing': {'unit': 'px', 'size': 1}}}
                                    ]
                                }
                            ]
                        },
                        # ===== HERO CONTENT - TWO COLUMNS =====
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'boxed',
                                'boxed_width': {'unit': 'px', 'size': 1400},
                                'min_height': {'unit': 'vh', 'size': 75},
                                'flex_direction': 'row',
                                'flex_justify_content': 'space-between',
                                'flex_align_items': 'center',
                                'flex_gap': {'unit': 'px', 'size': 80},
                                'padding': {'unit': 'px', 'top': '40', 'right': '40', 'bottom': '60', 'left': '40'}
                            },
                            'elements': [
                                # LEFT COLUMN - Text content
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'width': {'unit': '%', 'size': 55},
                                        'flex_direction': 'column',
                                        'flex_align_items': 'flex-start'
                                    },
                                    'elements': [
                                        # Headline
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'heading',
                                            'settings': {
                                                'title': headline,
                                                'header_size': 'h1',
                                                'align': 'left',
                                                'title_color': '#ffffff',
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 56},
                                                'typography_font_weight': '300',
                                                'typography_line_height': {'unit': 'em', 'size': 1.1},
                                                'typography_text_transform': 'uppercase'
                                            }
                                        },
                                        # Brand name
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'heading',
                                            'settings': {
                                                'title': site_name.upper(),
                                                'header_size': 'h1',
                                                'align': 'left',
                                                'title_color': colors['primary'],
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 56},
                                                'typography_font_weight': '300',
                                                'typography_line_height': {'unit': 'em', 'size': 1.1},
                                                'typography_text_transform': 'uppercase',
                                                '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '30', 'left': '0'}
                                            }
                                        },
                                        # Subheadline
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'text-editor',
                                            'settings': {
                                                'editor': f'<p>{subheadline}</p>',
                                                'text_color': 'rgba(255,255,255,0.7)',
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 16},
                                                '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '40', 'left': '0'}
                                            }
                                        },
                                        # CTA Buttons
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'container',
                                            'settings': {
                                                'flex_direction': 'column',
                                                'flex_gap': {'unit': 'px', 'size': 15}
                                            },
                                            'elements': [
                                                {
                                                    'id': self._generate_id(),
                                                    'elType': 'widget',
                                                    'widgetType': 'button',
                                                    'settings': {
                                                        'text': cta_text,
                                                        'background_color': colors['primary'],
                                                        'button_text_color': '#1a1a1a',
                                                        'border_radius': {'unit': 'px', 'size': 0},
                                                        'typography_typography': 'custom',
                                                        'typography_font_size': {'unit': 'px', 'size': 14},
                                                        'typography_font_weight': '500',
                                                        'button_padding': {'unit': 'px', 'top': '18', 'right': '50', 'bottom': '18', 'left': '50'}
                                                    }
                                                },
                                                {
                                                    'id': self._generate_id(),
                                                    'elType': 'widget',
                                                    'widgetType': 'button',
                                                    'settings': {
                                                        'text': cta_secondary,
                                                        'background_color': 'transparent',
                                                        'button_text_color': colors['primary'],
                                                        'border_border': 'solid',
                                                        'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1'},
                                                        'border_color': colors['primary'],
                                                        'border_radius': {'unit': 'px', 'size': 0},
                                                        'typography_typography': 'custom',
                                                        'typography_font_size': {'unit': 'px', 'size': 14},
                                                        'typography_font_weight': '500',
                                                        'button_padding': {'unit': 'px', 'top': '18', 'right': '50', 'bottom': '18', 'left': '50'}
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                },
                                # RIGHT COLUMN - Search form
                                self._create_search_form(design_spec, colors, font, industry_config)
                            ]
                        }
                    ]
                }
            ]
        }

    def _create_search_form(self, design_spec, colors, font, industry_config):
        """Create the search form based on industry type"""
        industry = design_spec.get('industry', 'default')

        # Build form fields based on industry
        form_elements = []

        # Tab buttons (Primary/Secondary)
        tabs = industry_config.get('search_tabs', ['Primary', 'Secondary'])
        tab_elements = []
        for i, tab in enumerate(tabs):
            tab_elements.append({
                'id': self._generate_id(),
                'elType': 'widget',
                'widgetType': 'button',
                'settings': {
                    'text': tab,
                    'background_color': colors['primary'] if i == 0 else 'transparent',
                    'button_text_color': '#1a1a2e' if i == 0 else '#666666',
                    'border_radius': {'unit': 'px', 'size': 30},
                    'typography_typography': 'custom',
                    'typography_font_size': {'unit': 'px', 'size': 14},
                    'typography_font_weight': '500',
                    'button_padding': {'unit': 'px', 'top': '14', 'right': '32', 'bottom': '14', 'left': '32'}
                }
            })

        form_elements.append({
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'flex_direction': 'row',
                'flex_gap': {'unit': 'px', 'size': 0},
                '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '30', 'left': '0'}
            },
            'elements': tab_elements
        })

        # Add search fields based on industry
        search_fields = industry_config.get('search_fields', [])

        for field in search_fields:
            if field['type'] == 'dropdown':
                # Label
                form_elements.append({
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': f'<p style="margin-bottom: 8px;">{field["label"]}</p>',
                        'text_color': '#999999',
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 13}
                    }
                })
                # Dropdown
                form_elements.append({
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': f'<p style="padding: 14px 0; border-bottom: 1px solid #e5e5e5; cursor: pointer;">{field["placeholder"]} <span style="float: right;">▾</span></p>',
                        'text_color': '#1a1a2e',
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 15},
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '24', 'left': '0'}
                    }
                })

            elif field['type'] == 'buttons':
                # Currency selector row (AX Capital style)
                form_elements.append({
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': f'<p style="margin-bottom: 12px;">{field["label"]}</p>',
                        'text_color': '#999999',
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 13}
                    }
                })

                # Currency options
                currency_html = '<p style="display: flex; gap: 24px; margin-bottom: 20px;">'
                for j, opt in enumerate(field.get('options', [])):
                    style = f'color: {"#1a1a2e" if j == len(field["options"])-2 else "#999"}; cursor: pointer;'
                    currency_html += f'<span style="{style}">{opt}</span>'
                currency_html += '</p>'

                form_elements.append({
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': currency_html,
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 14},
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '10', 'left': '0'}
                    }
                })

            elif field['type'] == 'range':
                # Price range inputs
                form_elements.append({
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_gap': {'unit': 'px', 'size': 20},
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '30', 'left': '0'}
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': f'<p style="padding: 14px 16px; background: #f5f5f5; border-radius: 4px;">{field["min"]}</p>',
                                'text_color': '#1a1a2e',
                                'typography_typography': 'custom',
                                'typography_font_size': {'unit': 'px', 'size': 14}
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': f'<p style="padding: 14px 16px; background: #f5f5f5; border-radius: 4px;">{field["max"]}</p>',
                                'text_color': '#1a1a2e',
                                'typography_typography': 'custom',
                                'typography_font_size': {'unit': 'px', 'size': 14}
                            }
                        }
                    ]
                })

        # Search button
        form_elements.append({
            'id': self._generate_id(),
            'elType': 'widget',
            'widgetType': 'button',
            'settings': {
                'text': industry_config.get('search_button', 'Search'),
                'link': {'url': '#search'},
                'background_color': colors['primary'],
                'button_text_color': '#1a1a2e',
                'border_radius': {'unit': 'px', 'size': 0},
                'typography_typography': 'custom',
                'typography_font_size': {'unit': 'px', 'size': 15},
                'typography_font_weight': '500',
                'button_padding': {'unit': 'px', 'top': '18', 'right': '0', 'bottom': '18', 'left': '0'},
                'align': 'stretch',
                '_element_width': 'full'
            }
        })

        # Secondary button if exists (Properties on map)
        if industry_config.get('secondary_button'):
            form_elements.append({
                'id': self._generate_id(),
                'elType': 'widget',
                'widgetType': 'button',
                'settings': {
                    'text': industry_config['secondary_button'],
                    'link': {'url': '#map'},
                    'background_color': '#ffffff',
                    'button_text_color': '#1a1a2e',
                    'border_border': 'solid',
                    'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1'},
                    'border_color': '#e5e5e5',
                    'border_radius': {'unit': 'px', 'size': 0},
                    'typography_typography': 'custom',
                    'typography_font_size': {'unit': 'px', 'size': 15},
                    'typography_font_weight': '500',
                    'button_padding': {'unit': 'px', 'top': '18', 'right': '0', 'bottom': '18', 'left': '0'},
                    'align': 'stretch',
                    '_element_width': 'full',
                    '_margin': {'unit': 'px', 'top': '12', 'right': '0', 'bottom': '0', 'left': '0'}
                }
            })

        # Return the form container - DESKTOP OPTIMIZED (400px min width)
        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'width': {'unit': '%', 'size': 40},
                'min_width': {'unit': 'px', 'size': 380},
                'max_width': {'unit': 'px', 'size': 440},
                'padding': {'unit': 'px', 'top': '32', 'right': '32', 'bottom': '32', 'left': '32'},
                'background_background': 'classic',
                'background_color': '#ffffff',
                'border_radius': {'unit': 'px', 'size': 4},
                'flex_direction': 'column',
                'flex_shrink': 0,
                'box_shadow_box_shadow_type': 'yes',
                'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 15, 'blur': 50, 'spread': 0, 'color': 'rgba(0,0,0,0.2)'}
            },
            'elements': form_elements
        }

    # ==================== TRUSTED BY - FULL WIDTH 1920px - DARK LUXURY THEME ====================
    def _create_trusted_by_section(self, design_spec):
        """Create full-width logos/trusted by section - DARK LUXURY STYLE"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        industry = design_spec.get('industry', 'default')

        # Industry-specific logos
        if industry == 'real_estate':
            logos = ['Emirates NBD', 'DAMAC', 'Emaar', 'Nakheel', 'Meraas']
            tagline = 'Partnered with leading developers'
        else:
            logos = ['Google', 'Microsoft', 'Amazon', 'Meta', 'Apple']
            tagline = 'Trusted by industry leaders'

        logo_elements = []
        for logo in logos:
            logo_elements.append({
                'id': self._generate_id(),
                'elType': 'widget',
                'widgetType': 'heading',
                'settings': {
                    'title': logo,
                    'header_size': 'h5',
                    'title_color': 'rgba(255,255,255,0.4)',
                    'typography_typography': 'custom',
                    'typography_font_size': {'unit': 'px', 'size': 18},
                    'typography_font_weight': '500',
                    'typography_letter_spacing': {'unit': 'px', 'size': 2},
                    'typography_text_transform': 'uppercase'
                }
            })

        return {
            'id': self._generate_id(),
            'elType': 'section',
            'settings': {
                'layout': 'full_width',
                'content_width': {'unit': 'px', 'size': 1920},
                'stretch_section': 'section-stretched',
                'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'background_background': 'classic',
                'background_color': colors['dark']
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'column',
                    'settings': {
                        '_column_size': 100,
                        'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'boxed',
                                'boxed_width': {'unit': 'px', 'size': 1400},
                                'flex_direction': 'column',
                                'flex_align_items': 'center',
                                'padding': {'unit': 'px', 'top': '60', 'right': '40', 'bottom': '60', 'left': '40'}
                            },
                            'elements': [
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'text-editor',
                                    'settings': {
                                        'editor': f'<p style="text-align: center; text-transform: uppercase; letter-spacing: 3px;">{tagline}</p>',
                                        'align': 'center',
                                        'text_color': colors['primary'],
                                        'typography_typography': 'custom',
                                        'typography_font_size': {'unit': 'px', 'size': 12},
                                        'typography_font_weight': '500',
                                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '35', 'left': '0'}
                                    }
                                },
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'content_width': 'full',
                                        'flex_direction': 'row',
                                        'flex_justify_content': 'space-around',
                                        'flex_align_items': 'center',
                                        'flex_wrap': 'nowrap',
                                        'flex_gap': {'unit': 'px', 'size': 80}
                                    },
                                    'elements': logo_elements
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    # ==================== ULTIMATE V1 SERVICES - IMAGE CARDS WITH GRADIENT ====================
    def _create_pro_services(self, design_spec, section_spec):
        """
        ULTIMATE V1 Services Section - Desktop Optimized
        - 6 cards in 2 rows (3 per row)
        - 32% width cards with responsive breakpoints
        - Background images with gradient overlays
        - Full-width via elType: "section" + stretch_section
        """
        colors = self._get_colors(design_spec)
        industry = design_spec.get('industry', 'default')

        # High-quality Unsplash images for real estate
        service_images = [
            'https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&q=80',
            'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80',
            'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80',
            'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800&q=80',
            'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80',
            'https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=800&q=80',
        ]

        # Industry-specific services
        if industry == 'real_estate':
            services = section_spec.get('items', [
                {'title': 'Property Search', 'description': "Access exclusive listings across Dubai's premium neighborhoods"},
                {'title': 'Investment Advisory', 'description': 'Expert guidance on high-yield real estate opportunities'},
                {'title': 'Property Management', 'description': 'Full-service management for your real estate portfolio'},
                {'title': 'Legal Services', 'description': 'Comprehensive due diligence and transaction support'},
                {'title': 'Luxury Rentals', 'description': 'Premium furnished apartments and villas for rent'},
                {'title': 'Off-Plan Projects', 'description': "Early access to Dubai's most anticipated developments"},
            ])
            section_tagline = 'WHY CHOOSE US'
            section_title = section_spec.get('title', 'Our Services')
            section_subtitle = "Comprehensive real estate solutions tailored to your investment goals in Dubai's dynamic property market."
        else:
            services = section_spec.get('items', [
                {'title': 'Lightning Fast', 'description': 'Built for speed with optimized performance'},
                {'title': 'Secure by Default', 'description': 'Enterprise-grade security with encryption'},
                {'title': 'Scalable Infrastructure', 'description': 'Grows with your business seamlessly'},
                {'title': 'AI-Powered Analytics', 'description': 'Smart insights powered by machine learning'},
                {'title': '24/7 Expert Support', 'description': 'Dedicated support team available around the clock'},
                {'title': 'API & Integrations', 'description': 'Connect with 500+ tools and build custom workflows'},
            ])
            section_tagline = 'WHY CHOOSE US'
            section_title = section_spec.get('title', 'Our Services')
            section_subtitle = 'Powerful features designed to help you build, launch, and grow your business faster than ever.'

        # Create ULTIMATE V1 image cards with gradient overlays
        service_cards = []
        for i, service in enumerate(services):
            image_url = service.get('image', service_images[i % len(service_images)])
            service_cards.append({
                'id': self._generate_id(),
                'elType': 'container',
                'settings': {
                    'content_width': 'full',
                    'width': {'size': 32, 'unit': '%'},
                    'width_tablet': {'size': 48, 'unit': '%'},
                    'width_mobile': {'size': 100, 'unit': '%'},
                    'min_height': {'size': 280, 'unit': 'px'},
                    'flex_direction': 'column',
                    'flex_justify_content': 'flex-end',
                    'padding': {'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'unit': 'px', 'isLinked': True},
                    'border_radius': {'top': '8', 'right': '8', 'bottom': '8', 'left': '8', 'unit': 'px', 'isLinked': True},
                    'overflow': 'hidden',
                    'background_background': 'classic',
                    'background_image': {'url': image_url, 'id': ''},
                    'background_position': 'center center',
                    'background_size': 'cover',
                    'box_shadow_box_shadow_type': 'yes',
                    'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 10, 'blur': 30, 'spread': 0, 'color': 'rgba(0,0,0,0.3)'}
                },
                'elements': [{
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'content_width': 'full',
                        'padding': {'top': '100', 'right': '24', 'bottom': '24', 'left': '24', 'unit': 'px', 'isLinked': False},
                        'background_background': 'gradient',
                        'background_color': 'transparent',
                        'background_color_b': 'rgba(10,10,15,0.9)',
                        'background_gradient_type': 'linear',
                        'background_gradient_angle': {'size': 180, 'unit': 'deg'}
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'heading',
                            'settings': {
                                'title': service.get('title', 'Feature'),
                                'header_size': 'h4',
                                'title_color': '#ffffff',
                                'typography_typography': 'custom',
                                'typography_font_family': 'Montserrat',
                                'typography_font_size': {'size': 20, 'unit': 'px'},
                                'typography_font_weight': '600'
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': f'<p style="color: rgba(255,255,255,0.7); font-size: 14px; line-height: 1.6; margin-top: 8px;">{service.get("description", "Description")}</p>'
                            }
                        }
                    ]
                }]
            })

        return {
            'id': self._generate_id(),
            'elType': 'section',
            'settings': {
                'stretch_section': 'section-stretched',
                'layout': 'full_width',
                'content_width': {'size': 1400, 'unit': 'px'},
                'gap': 'no',
                'padding': {'top': '100', 'right': '0', 'bottom': '100', 'left': '0', 'unit': 'px', 'isLinked': False},
                'background_background': 'classic',
                'background_color': colors['dark']
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'column',
                    'settings': {'_column_size': 100},
                    'elements': [
                        # Section Header
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'boxed',
                                'boxed_width': {'size': 1400, 'unit': 'px'},
                                'flex_direction': 'column',
                                'flex_align_items': 'center',
                                'padding': {'top': '0', 'right': '40', 'bottom': '60', 'left': '40', 'unit': 'px', 'isLinked': False}
                            },
                            'elements': [
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'heading',
                                    'settings': {
                                        'title': section_tagline,
                                        'align': 'center',
                                        'title_color': colors['primary'],
                                        'typography_typography': 'custom',
                                        'typography_font_family': 'Montserrat',
                                        'typography_font_size': {'size': 13, 'unit': 'px'},
                                        'typography_font_weight': '500',
                                        'typography_letter_spacing': {'size': 4, 'unit': 'px'}
                                    }
                                },
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'heading',
                                    'settings': {
                                        'title': section_title,
                                        'header_size': 'h2',
                                        'align': 'center',
                                        'title_color': '#ffffff',
                                        'typography_typography': 'custom',
                                        'typography_font_family': 'Montserrat',
                                        'typography_font_size': {'size': 48, 'unit': 'px'},
                                        'typography_font_weight': '300',
                                        'typography_letter_spacing': {'size': 1, 'unit': 'px'},
                                        '_margin': {'top': '16', 'right': '0', 'bottom': '0', 'left': '0', 'unit': 'px', 'isLinked': False}
                                    }
                                },
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'text-editor',
                                    'settings': {
                                        'editor': f'<p style="text-align: center; color: rgba(255,255,255,0.5); font-size: 16px; max-width: 600px; line-height: 1.7;">{section_subtitle}</p>',
                                        '_margin': {'top': '20', 'right': '0', 'bottom': '0', 'left': '0', 'unit': 'px', 'isLinked': False}
                                    }
                                }
                            ]
                        },
                        # Cards Grid - 3 per row using percentage widths
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'boxed',
                                'boxed_width': {'size': 1400, 'unit': 'px'},
                                'flex_direction': 'row',
                                'flex_wrap': 'wrap',
                                'flex_justify_content': 'space-between',
                                'flex_gap': {'size': 24, 'unit': 'px', 'column': '24', 'row': '24'},
                                'padding': {'top': '0', 'right': '40', 'bottom': '0', 'left': '40', 'unit': 'px', 'isLinked': False}
                            },
                            'elements': service_cards
                        }
                    ]
                }
            ]
        }

    # ==================== PRO ABOUT - DARK LUXURY THEME ====================
    def _create_pro_about(self, design_spec, section_spec):
        """Create modern about/feature highlight section - DARK LUXURY STYLE"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        industry = design_spec.get('industry', 'default')

        # Industry-specific content
        if industry == 'real_estate':
            tagline = 'About Us'
            title = section_spec.get('title', 'Your Trusted Partner in Dubai Real Estate')
            description = section_spec.get('description', 'With over a decade of experience in Dubai luxury real estate, we provide unparalleled service to investors and homebuyers worldwide. Our team of expert advisors brings deep market knowledge and a commitment to excellence in every transaction.')
            stats = [
                {'number': '500+', 'label': 'Properties Sold'},
                {'number': '$2B+', 'label': 'Transaction Volume'},
                {'number': '15+', 'label': 'Years Experience'}
            ]
        else:
            tagline = 'About Us'
            title = section_spec.get('title', 'We help businesses reach their full potential')
            description = section_spec.get('description', 'Founded with a mission to democratize technology, we have helped over 10,000 businesses transform their digital presence. Our team of experts combines innovation with experience to deliver results that matter.')
            stats = [
                {'number': '10K+', 'label': 'Happy Clients'},
                {'number': '98%', 'label': 'Success Rate'},
                {'number': '24/7', 'label': 'Support'}
            ]

        return {
            'id': self._generate_id(),
            'elType': 'section',
            'settings': {
                'layout': 'full_width',
                'content_width': {'unit': 'px', 'size': 1920},
                'stretch_section': 'section-stretched',
                'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'background_background': 'classic',
                'background_color': '#0d0d12'
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'column',
                    'settings': {
                        '_column_size': 100,
                        'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'boxed',
                                'boxed_width': {'unit': 'px', 'size': 1400},
                                'flex_direction': 'row',
                                'flex_align_items': 'center',
                                'flex_gap': {'unit': 'px', 'size': 80},
                                'padding': {'unit': 'px', 'top': '100', 'right': '40', 'bottom': '100', 'left': '40'}
                            },
                            'elements': [
                                # Left content
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'width': {'unit': '%', 'size': 55},
                                        'flex_direction': 'column'
                                    },
                                    'elements': [
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'text-editor',
                                            'settings': {
                                                'editor': f'<p style="text-transform: uppercase; letter-spacing: 3px;">{tagline}</p>',
                                                'text_color': colors['primary'],
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 12},
                                                'typography_font_weight': '500',
                                                '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '20', 'left': '0'}
                                            }
                                        },
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'heading',
                                            'settings': {
                                                'title': title,
                                                'header_size': 'h2',
                                                'title_color': '#ffffff',
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 42},
                                                'typography_font_weight': '300',
                                                'typography_line_height': {'unit': 'em', 'size': 1.2}
                                            }
                                        },
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'text-editor',
                                            'settings': {
                                                'editor': f"<p>{description}</p>",
                                                'text_color': 'rgba(255,255,255,0.6)',
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 16},
                                                'typography_line_height': {'unit': 'em', 'size': 1.8},
                                                '_margin': {'unit': 'px', 'top': '24', 'right': '0', 'bottom': '40', 'left': '0'}
                                            }
                                        },
                                        # Stats row
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'container',
                                            'settings': {
                                                'flex_direction': 'row',
                                                'flex_gap': {'unit': 'px', 'size': 60}
                                            },
                                            'elements': [
                                                self._create_stat_item_dark(stats[0]['number'], stats[0]['label'], colors),
                                                self._create_stat_item_dark(stats[1]['number'], stats[1]['label'], colors),
                                                self._create_stat_item_dark(stats[2]['number'], stats[2]['label'], colors)
                                            ]
                                        }
                                    ]
                                },
                                # Right image placeholder
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'width': {'unit': '%', 'size': 45},
                                        'min_height': {'unit': 'px', 'size': 450},
                                        'background_background': 'classic',
                                        'background_image': {
                                            'url': 'https://images.unsplash.com/photo-1582407947304-fd86f028f716?w=800&q=80',
                                            'id': ''
                                        },
                                        'background_position': 'center center',
                                        'background_size': 'cover',
                                        'border_radius': {'unit': 'px', 'size': 4}
                                    },
                                    'elements': []
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def _create_stat_item_dark(self, number, label, colors):
        """Create individual stat item for dark theme"""
        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {'flex_direction': 'column'},
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': number,
                        'header_size': 'h3',
                        'title_color': colors['primary'],
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '300'
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': f'<p>{label}</p>',
                        'text_color': 'rgba(255,255,255,0.5)',
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 14},
                        'typography_text_transform': 'uppercase',
                        'typography_letter_spacing': {'unit': 'px', 'size': 1}
                    }
                }
            ]
        }

    def _create_stat_item(self, number, label, colors, font):
        """Create individual stat item"""
        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {'flex_direction': 'column'},
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': number,
                        'header_size': 'h3',
                        'title_color': colors['primary'],
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 36},
                        'typography_font_weight': '800'
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': f'<p>{label}</p>',
                        'text_color': colors['text_light'],
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 14}
                    }
                }
            ]
        }

    # ==================== PRO TESTIMONIALS - DARK LUXURY THEME ====================
    def _create_pro_testimonials(self, design_spec, section_spec):
        """Create modern testimonials section - DARK LUXURY STYLE"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        industry = design_spec.get('industry', 'default')

        # Industry-specific testimonials
        if industry == 'real_estate':
            testimonials = section_spec.get('items', [
                {'content': 'AX Capital made our investment in Dubai seamless. Their expertise and due diligence gave us complete confidence in our purchase.', 'name': 'James Morrison', 'title': 'Investor, London'},
                {'content': 'Outstanding service from start to finish. The team found us the perfect property and handled everything professionally.', 'name': 'Sophie Laurent', 'title': 'Buyer, Paris'},
                {'content': 'Their market knowledge is exceptional. We achieved 15% ROI in our first year thanks to their investment guidance.', 'name': 'Ahmed Al-Rashid', 'title': 'Portfolio Manager, Riyadh'}
            ])
            section_title = 'What Our Clients Say'
        else:
            testimonials = section_spec.get('items', [
                {'content': 'This platform completely transformed how we work. The results speak for themselves - 300% growth in just 6 months.', 'name': 'Sarah Chen', 'title': 'CEO, TechStart'},
                {'content': 'The best investment we have made. Their team went above and beyond to ensure our success. Highly recommended!', 'name': 'Michael Rodriguez', 'title': 'Founder, ScaleUp'},
                {'content': 'Incredible support and even better results. We could not have scaled without them. A true partner in growth.', 'name': 'Emily Watson', 'title': 'CMO, GrowthCo'}
            ])
            section_title = 'Loved by thousands of customers'

        testimonial_cards = []
        for t in testimonials:
            testimonial_cards.append({
                'id': self._generate_id(),
                'elType': 'container',
                'settings': {
                    'width': {'unit': '%', 'size': 31},
                    'min_width': {'unit': 'px', 'size': 320},
                    'padding': {'unit': 'px', 'top': '40', 'right': '36', 'bottom': '40', 'left': '36'},
                    'background_background': 'classic',
                    'background_color': 'rgba(255,255,255,0.03)',
                    'border_radius': {'unit': 'px', 'size': 4},
                    'border_border': 'solid',
                    'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1'},
                    'border_color': 'rgba(255,255,255,0.08)',
                    'flex_direction': 'column'
                },
                'elements': [
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'icon',
                        'settings': {
                            'selected_icon': {'value': 'fas fa-quote-left', 'library': 'fa-solid'},
                            'primary_color': colors['primary'],
                            'icon_size': {'unit': 'px', 'size': 28},
                            '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '20', 'left': '0'}
                        }
                    },
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'text-editor',
                        'settings': {
                            'editor': f'<p>{t.get("content", "Great experience!")}</p>',
                            'text_color': 'rgba(255,255,255,0.8)',
                            'typography_typography': 'custom',
                            'typography_font_size': {'unit': 'px', 'size': 16},
                            'typography_line_height': {'unit': 'em', 'size': 1.7},
                            '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '30', 'left': '0'}
                        }
                    },
                    {
                        'id': self._generate_id(),
                        'elType': 'container',
                        'settings': {
                            'flex_direction': 'row',
                            'flex_align_items': 'center',
                            'flex_gap': {'unit': 'px', 'size': 16}
                        },
                        'elements': [
                            {
                                'id': self._generate_id(),
                                'elType': 'container',
                                'settings': {
                                    'width': {'unit': 'px', 'size': 48},
                                    'height': {'unit': 'px', 'size': 48},
                                    'background_background': 'classic',
                                    'background_color': colors['primary'],
                                    'border_radius': {'unit': '%', 'size': 50},
                                    'flex_justify_content': 'center',
                                    'flex_align_items': 'center'
                                },
                                'elements': [{
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'heading',
                                    'settings': {
                                        'title': t.get('name', 'N')[0],
                                        'header_size': 'h5',
                                        'title_color': colors['dark'],
                                        'typography_font_weight': '600'
                                    }
                                }]
                            },
                            {
                                'id': self._generate_id(),
                                'elType': 'container',
                                'settings': {'flex_direction': 'column'},
                                'elements': [
                                    {
                                        'id': self._generate_id(),
                                        'elType': 'widget',
                                        'widgetType': 'heading',
                                        'settings': {
                                            'title': t.get('name', 'Client'),
                                            'header_size': 'h5',
                                            'title_color': '#ffffff',
                                            'typography_typography': 'custom',
                                            'typography_font_size': {'unit': 'px', 'size': 16},
                                            'typography_font_weight': '500'
                                        }
                                    },
                                    {
                                        'id': self._generate_id(),
                                        'elType': 'widget',
                                        'widgetType': 'text-editor',
                                        'settings': {
                                            'editor': f"<p>{t.get('title', 'Position')}</p>",
                                            'text_color': 'rgba(255,255,255,0.5)',
                                            'typography_typography': 'custom',
                                            'typography_font_size': {'unit': 'px', 'size': 13}
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            })

        return {
            'id': self._generate_id(),
            'elType': 'section',
            'settings': {
                'layout': 'full_width',
                'content_width': {'unit': 'px', 'size': 1920},
                'stretch_section': 'section-stretched',
                'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'background_background': 'classic',
                'background_color': colors['dark']
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'column',
                    'settings': {
                        '_column_size': 100,
                        'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'boxed',
                                'boxed_width': {'unit': 'px', 'size': 1400},
                                'flex_direction': 'column',
                                'padding': {'unit': 'px', 'top': '100', 'right': '40', 'bottom': '100', 'left': '40'}
                            },
                            'elements': [
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'flex_direction': 'column',
                                        'flex_align_items': 'center',
                                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '60', 'left': '0'}
                                    },
                                    'elements': [
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'text-editor',
                                            'settings': {
                                                'editor': '<p style="text-align: center; text-transform: uppercase; letter-spacing: 3px;">Testimonials</p>',
                                                'align': 'center',
                                                'text_color': colors['primary'],
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 12},
                                                'typography_font_weight': '500',
                                                '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '20', 'left': '0'}
                                            }
                                        },
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'heading',
                                            'settings': {
                                                'title': section_title,
                                                'header_size': 'h2',
                                                'align': 'center',
                                                'title_color': '#ffffff',
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 42},
                                                'typography_font_weight': '300'
                                            }
                                        }
                                    ]
                                },
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'flex_direction': 'row',
                                        'flex_wrap': 'wrap',
                                        'flex_justify_content': 'center',
                                        'flex_gap': {'unit': 'px', 'size': 24}
                                    },
                                    'elements': testimonial_cards
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    # ==================== PRO CONTACT ====================
    def _create_pro_contact(self, design_spec, section_spec):
        """Create modern contact section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'row',
                'flex_gap': {'unit': 'px', 'size': 80},
                'padding': {'unit': 'px', 'top': '120', 'right': '40', 'bottom': '120', 'left': '40'},
                'background_background': 'classic',
                'background_color': '#ffffff'
            },
            'elements': [
                # Left content
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'width': {'unit': '%', 'size': 45},
                        'flex_direction': 'column'
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': '<p style="text-transform: uppercase; letter-spacing: 3px;">Contact Us</p>',
                                'text_color': colors['primary'],
                                'typography_typography': 'custom',
                                'typography_font_size': {'unit': 'px', 'size': 14},
                                'typography_font_weight': '700',
                                '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '16', 'left': '0'}
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'heading',
                            'settings': {
                                'title': "Let's start a conversation",
                                'header_size': 'h2',
                                'title_color': colors['dark'],
                                'typography_typography': 'custom',
                                'typography_font_size': {'unit': 'px', 'size': 42},
                                'typography_font_weight': '800'
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': '<p>Have a project in mind? Fill out the form and we will get back to you within 24 hours.</p>',
                                'text_color': colors['text_light'],
                                'typography_typography': 'custom',
                                'typography_font_size': {'unit': 'px', 'size': 18},
                                '_margin': {'unit': 'px', 'top': '20', 'right': '0', 'bottom': '40', 'left': '0'}
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'icon-list',
                            'settings': {
                                'icon_list': [
                                    {'text': 'hello@company.com', 'selected_icon': {'value': 'fas fa-envelope', 'library': 'fa-solid'}},
                                    {'text': '+1 (555) 123-4567', 'selected_icon': {'value': 'fas fa-phone', 'library': 'fa-solid'}},
                                    {'text': '123 Business Ave, Suite 100', 'selected_icon': {'value': 'fas fa-map-marker-alt', 'library': 'fa-solid'}}
                                ],
                                'icon_color': colors['primary'],
                                'text_color': colors['text_light'],
                                'space_between': {'unit': 'px', 'size': 20}
                            }
                        }
                    ]
                },
                # Form
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'width': {'unit': '%', 'size': 55},
                        'padding': {'unit': 'px', 'top': '48', 'right': '48', 'bottom': '48', 'left': '48'},
                        'background_background': 'classic',
                        'background_color': '#f8fafc',
                        'border_radius': {'unit': 'px', 'size': 24}
                    },
                    'elements': [{
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'form',
                        'settings': {
                            'form_name': 'Contact Form',
                            'form_fields': [
                                {'custom_id': 'name', 'field_type': 'text', 'field_label': 'Full Name', 'placeholder': 'John Doe', 'required': 'yes', 'width': '50'},
                                {'custom_id': 'email', 'field_type': 'email', 'field_label': 'Email', 'placeholder': 'john@company.com', 'required': 'yes', 'width': '50'},
                                {'custom_id': 'company', 'field_type': 'text', 'field_label': 'Company', 'placeholder': 'Your Company', 'width': '100'},
                                {'custom_id': 'message', 'field_type': 'textarea', 'field_label': 'Message', 'placeholder': 'Tell us about your project...', 'required': 'yes', 'rows': 5}
                            ],
                            'button_text': 'Send Message',
                            'button_size': 'lg',
                            'button_background_color': colors['primary'],
                            'button_border_radius': {'unit': 'px', 'size': 10},
                            'button_text_color': '#ffffff'
                        }
                    }]
                }
            ]
        }

    # ==================== FINAL CTA - FULL WIDTH 1920px ====================
    def _create_final_cta(self, design_spec):
        """Create full-width final CTA section - 1920px desktop"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        industry = design_spec.get('industry', 'default')

        # Industry-specific CTA content
        if industry == 'real_estate':
            headline = 'Ready to invest in Dubai?'
            subtext = 'Schedule a consultation with our expert advisors and discover premium properties tailored to your investment goals.'
            cta_primary = 'Schedule Consultation'
            cta_secondary = 'View Properties'
        else:
            headline = 'Ready to get started?'
            subtext = 'Join thousands of satisfied customers and transform your business today.'
            cta_primary = 'Start Free Trial'
            cta_secondary = 'Talk to Sales'

        return {
            'id': self._generate_id(),
            'elType': 'section',
            'settings': {
                'layout': 'full_width',
                'content_width': {'unit': 'px', 'size': 1920},
                'stretch_section': 'section-stretched',
                'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'background_background': 'gradient',
                'background_color': colors['dark'],
                'background_color_b': colors['gradient_start'],
                'background_gradient_type': 'linear',
                'background_gradient_angle': {'unit': 'deg', 'size': 135}
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'column',
                    'settings': {
                        '_column_size': 100,
                        'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'boxed',
                                'boxed_width': {'unit': 'px', 'size': 1000},
                                'flex_direction': 'column',
                                'flex_align_items': 'center',
                                'padding': {'unit': 'px', 'top': '120', 'right': '40', 'bottom': '120', 'left': '40'}
                            },
                            'elements': [
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'heading',
                                    'settings': {
                                        'title': headline,
                                        'header_size': 'h2',
                                        'align': 'center',
                                        'title_color': '#ffffff',
                                        'typography_typography': 'custom',
                                        'typography_font_size': {'unit': 'px', 'size': 52},
                                        'typography_font_weight': '300',
                                        'typography_letter_spacing': {'unit': 'px', 'size': 1}
                                    }
                                },
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'text-editor',
                                    'settings': {
                                        'editor': f'<p style="text-align: center;">{subtext}</p>',
                                        'align': 'center',
                                        'text_color': 'rgba(255,255,255,0.8)',
                                        'typography_typography': 'custom',
                                        'typography_font_size': {'unit': 'px', 'size': 20},
                                        'typography_line_height': {'unit': 'em', 'size': 1.6},
                                        '_margin': {'unit': 'px', 'top': '20', 'right': '0', 'bottom': '40', 'left': '0'}
                                    }
                                },
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'flex_direction': 'row',
                                        'flex_justify_content': 'center',
                                        'flex_gap': {'unit': 'px', 'size': 20}
                                    },
                                    'elements': [
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'button',
                                            'settings': {
                                                'text': cta_primary,
                                                'link': {'url': '#contact'},
                                                'background_color': colors['primary'],
                                                'button_text_color': colors['dark'],
                                                'border_radius': {'unit': 'px', 'size': 4},
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 16},
                                                'typography_font_weight': '500',
                                                'button_padding': {'unit': 'px', 'top': '18', 'right': '40', 'bottom': '18', 'left': '40'}
                                            }
                                        },
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'button',
                                            'settings': {
                                                'text': cta_secondary,
                                                'link': {'url': '#properties'},
                                                'background_color': 'transparent',
                                                'button_text_color': '#ffffff',
                                                'border_border': 'solid',
                                                'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1'},
                                                'border_color': 'rgba(255,255,255,0.3)',
                                                'border_radius': {'unit': 'px', 'size': 4},
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 16},
                                                'typography_font_weight': '500',
                                                'button_padding': {'unit': 'px', 'top': '18', 'right': '40', 'bottom': '18', 'left': '40'}
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    # ==================== PRO FOOTER - FULL WIDTH 1920px ====================
    def _create_pro_footer(self, design_spec):
        """Create full-width luxury footer (AX Capital style) - 1920px desktop"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        site_name = design_spec.get('site_name', 'Brand')
        industry_config = self._get_industry_config(design_spec)
        industry = design_spec.get('industry', 'default')

        # Industry-specific footer content
        if industry == 'real_estate':
            brand_text = 'Your trusted partner in Dubai luxury real estate. We bring due diligence and expertise to every investment.'
            col1_title = 'Properties'
            col1_links = ['Buy', 'Rent', 'Off-Plan', 'New Projects']
            col2_title = 'Services'
            col2_links = ['Property Management', 'Investment Advisory', 'Market Analysis', 'Relocation']
            col3_title = 'Company'
            col3_links = ['About Us', 'Our Team', 'Careers', 'Contact']
        else:
            brand_text = 'Building the future of digital experiences. Join us on our mission to transform businesses worldwide.'
            col1_title = 'Product'
            col1_links = ['Features', 'Pricing', 'Integrations', 'API']
            col2_title = 'Company'
            col2_links = ['About', 'Careers', 'Blog', 'Press']
            col3_title = 'Support'
            col3_links = ['Help Center', 'Contact', 'Status', 'Documentation']

        return {
            'id': self._generate_id(),
            'elType': 'section',
            'settings': {
                'layout': 'full_width',
                'content_width': {'unit': 'px', 'size': 1920},
                'stretch_section': 'section-stretched',
                'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                'background_background': 'classic',
                'background_color': colors['dark']
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'column',
                    'settings': {
                        '_column_size': 100,
                        'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
                    },
                    'elements': [
                        # Main footer content container
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'content_width': 'boxed',
                                'boxed_width': {'unit': 'px', 'size': 1400},
                                'flex_direction': 'column',
                                'padding': {'unit': 'px', 'top': '80', 'right': '40', 'bottom': '40', 'left': '40'}
                            },
                            'elements': [
                                # Top section - 4 columns
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'content_width': 'full',
                                        'flex_direction': 'row',
                                        'flex_justify_content': 'space-between',
                                        'flex_wrap': 'nowrap',
                                        'flex_gap': {'unit': 'px', 'size': 60},
                                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '60', 'left': '0'}
                                    },
                                    'elements': [
                                        # Brand column - 35%
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'container',
                                            'settings': {
                                                'width': {'unit': '%', 'size': 35},
                                                'flex_direction': 'column'
                                            },
                                            'elements': [
                                                {
                                                    'id': self._generate_id(),
                                                    'elType': 'widget',
                                                    'widgetType': 'heading',
                                                    'settings': {
                                                        'title': site_name,
                                                        'header_size': 'h4',
                                                        'title_color': colors['primary'],
                                                        'typography_typography': 'custom',
                                                        'typography_font_size': {'unit': 'px', 'size': 28},
                                                        'typography_font_weight': '300',
                                                        'typography_letter_spacing': {'unit': 'px', 'size': 2},
                                                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '20', 'left': '0'}
                                                    }
                                                },
                                                {
                                                    'id': self._generate_id(),
                                                    'elType': 'widget',
                                                    'widgetType': 'text-editor',
                                                    'settings': {
                                                        'editor': f'<p>{brand_text}</p>',
                                                        'text_color': 'rgba(255,255,255,0.6)',
                                                        'typography_typography': 'custom',
                                                        'typography_font_size': {'unit': 'px', 'size': 15},
                                                        'typography_line_height': {'unit': 'em', 'size': 1.7}
                                                    }
                                                }
                                            ]
                                        },
                                        # Links columns - each 18%
                                        self._create_footer_column(col1_title, col1_links, font, colors['primary']),
                                        self._create_footer_column(col2_title, col2_links, font, colors['primary']),
                                        self._create_footer_column(col3_title, col3_links, font, colors['primary'])
                                    ]
                                },
                                # Bottom bar
                                {
                                    'id': self._generate_id(),
                                    'elType': 'container',
                                    'settings': {
                                        'content_width': 'full',
                                        'flex_direction': 'row',
                                        'flex_justify_content': 'space-between',
                                        'flex_align_items': 'center',
                                        'border_border': 'solid',
                                        'border_width': {'unit': 'px', 'top': '1', 'right': '0', 'bottom': '0', 'left': '0'},
                                        'border_color': 'rgba(255,255,255,0.1)',
                                        'padding': {'unit': 'px', 'top': '30', 'right': '0', 'bottom': '0', 'left': '0'}
                                    },
                                    'elements': [
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'widget',
                                            'widgetType': 'text-editor',
                                            'settings': {
                                                'editor': f'<p>© 2024 {site_name}. All rights reserved.</p>',
                                                'text_color': 'rgba(255,255,255,0.5)',
                                                'typography_typography': 'custom',
                                                'typography_font_size': {'unit': 'px', 'size': 14}
                                            }
                                        },
                                        {
                                            'id': self._generate_id(),
                                            'elType': 'container',
                                            'settings': {
                                                'flex_direction': 'row',
                                                'flex_gap': {'unit': 'px', 'size': 20}
                                            },
                                            'elements': [
                                                {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'icon', 'settings': {'selected_icon': {'value': 'fab fa-instagram', 'library': 'fa-brands'}, 'primary_color': 'rgba(255,255,255,0.6)', 'size': {'unit': 'px', 'size': 18}, 'hover_primary_color': colors['primary']}},
                                                {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'icon', 'settings': {'selected_icon': {'value': 'fab fa-linkedin-in', 'library': 'fa-brands'}, 'primary_color': 'rgba(255,255,255,0.6)', 'size': {'unit': 'px', 'size': 18}, 'hover_primary_color': colors['primary']}},
                                                {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'icon', 'settings': {'selected_icon': {'value': 'fab fa-youtube', 'library': 'fa-brands'}, 'primary_color': 'rgba(255,255,255,0.6)', 'size': {'unit': 'px', 'size': 18}, 'hover_primary_color': colors['primary']}},
                                                {'id': self._generate_id(), 'elType': 'widget', 'widgetType': 'icon', 'settings': {'selected_icon': {'value': 'fab fa-whatsapp', 'library': 'fa-brands'}, 'primary_color': 'rgba(255,255,255,0.6)', 'size': {'unit': 'px', 'size': 18}, 'hover_primary_color': colors['primary']}}
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    def _create_footer_column(self, title, links, font, accent_color='#C9A87C'):
        """Create footer links column"""
        link_elements = []
        for link in links:
            link_elements.append({
                'id': self._generate_id(),
                'elType': 'widget',
                'widgetType': 'text-editor',
                'settings': {
                    'editor': f'<p><a href="#{link.lower().replace(" ", "-")}" style="color: rgba(255,255,255,0.6); text-decoration: none;">{link}</a></p>',
                    'text_color': 'rgba(255,255,255,0.6)',
                    'typography_typography': 'custom',
                    'typography_font_size': {'unit': 'px', 'size': 15},
                    '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '10', 'left': '0'}
                }
            })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'flex_direction': 'column',
                'width': {'unit': '%', 'size': 18}
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': title,
                        'header_size': 'h5',
                        'title_color': accent_color,
                        'typography_typography': 'custom',
                        'typography_font_size': {'unit': 'px', 'size': 14},
                        'typography_font_weight': '600',
                        'typography_text_transform': 'uppercase',
                        'typography_letter_spacing': {'unit': 'px', 'size': 1},
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '20', 'left': '0'}
                    }
                },
                *link_elements
            ]
        }

    # Placeholder methods for other section types
    def _create_pro_features(self, design_spec, section_spec):
        return self._create_pro_services(design_spec, section_spec)

    def _create_pro_pricing(self, design_spec, section_spec):
        return self._create_pro_services(design_spec, section_spec)

    def _create_pro_faq(self, design_spec, section_spec):
        return self._create_pro_testimonials(design_spec, section_spec)

    def _create_pro_cta(self, design_spec, section_spec):
        return self._create_final_cta(design_spec)

    def to_json(self, page_data):
        """Convert page data to JSON string"""
        return json.dumps(page_data, indent=2)
