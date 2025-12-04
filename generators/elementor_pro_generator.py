#!/usr/bin/env python3
"""
PRO-LEVEL Elementor Generator - Creates stunning, agency-quality pages
Inspired by top sites like ThriveState.io, Stripe, Linear, etc.
"""

import json
import random
import string

class ElementorProGenerator:
    def __init__(self):
        self.id_counter = 0

    def _generate_id(self):
        """Generate unique Elementor element ID"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

    def generate_page(self, design_spec):
        """Generate complete pro-level Elementor page"""
        sections = []

        # 1. Sticky transparent header
        if design_spec.get('header', True):
            sections.append(self._create_pro_header(design_spec))

        # 2. Full-screen hero with overlay
        if design_spec.get('hero', True):
            sections.append(self._create_pro_hero(design_spec))

        # 3. Trusted by / logos section
        sections.append(self._create_trusted_by_section(design_spec))

        # 4. Generate content sections
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

        # 5. Final CTA section
        sections.append(self._create_final_cta(design_spec))

        # 6. Pro footer
        if design_spec.get('footer', True):
            sections.append(self._create_pro_footer(design_spec))

        return {
            'content': sections,
            'page_settings': {
                'hide_title': 'yes',
                'template': 'elementor_canvas'
            },
            'version': '0.4',
            'type': 'page'
        }

    def _get_colors(self, design_spec):
        """Extract colors with professional defaults"""
        colors = design_spec.get('colors', {})

        def get_color(key, default):
            val = colors.get(key, default)
            if isinstance(val, list):
                return val[0] if val else default
            return val

        return {
            'primary': get_color('primary', '#6366f1'),  # Modern indigo
            'secondary': get_color('secondary', '#0f172a'),  # Dark slate
            'text': get_color('text', '#1e293b'),
            'text_light': '#64748b',
            'background': get_color('background', '#ffffff'),
            'background_alt': '#f8fafc',
            'accent': get_color('accent', '#22d3ee'),  # Cyan accent
            'dark': '#0f172a',
            'gradient_start': get_color('primary', '#6366f1'),
            'gradient_end': '#8b5cf6'  # Purple
        }

    def _get_fonts(self, design_spec):
        """Get font with pro default"""
        fonts = design_spec.get('fonts', ['Inter'])
        return fonts[0] if isinstance(fonts, list) else fonts

    # ==================== PRO HEADER ====================
    def _create_pro_header(self, design_spec):
        """Create sticky transparent header"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        site_name = design_spec.get('site_name', 'Brand')
        nav_items = design_spec.get('nav_items', ['Features', 'Solutions', 'Pricing', 'About'])

        nav_links = []
        for item in nav_items:
            nav_links.append({
                'id': self._generate_id(),
                'elType': 'widget',
                'widgetType': 'button',
                'settings': {
                    'text': item,
                    'link': {'url': f'#{item.lower().replace(" ", "-")}'},
                    'button_type': 'link',
                    'button_text_color': '#ffffff',
                    'typography_typography': 'custom',
                    'typography_font_family': font,
                    'typography_font_size': {'unit': 'px', 'size': 15},
                    'typography_font_weight': '500',
                    'button_padding': {'unit': 'px', 'top': '10', 'right': '20', 'bottom': '10', 'left': '20'},
                    'hover_color': colors['accent']
                }
            })

        # CTA button
        nav_links.append({
            'id': self._generate_id(),
            'elType': 'widget',
            'widgetType': 'button',
            'settings': {
                'text': 'Get Started',
                'link': {'url': '#contact'},
                'background_color': '#ffffff',
                'button_text_color': colors['dark'],
                'border_radius': {'unit': 'px', 'size': 8},
                'typography_typography': 'custom',
                'typography_font_family': font,
                'typography_font_size': {'unit': 'px', 'size': 14},
                'typography_font_weight': '600',
                'button_padding': {'unit': 'px', 'top': '12', 'right': '24', 'bottom': '12', 'left': '24'}
            }
        })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'full',
                'flex_direction': 'row',
                'flex_justify_content': 'space-between',
                'flex_align_items': 'center',
                'padding': {'unit': 'px', 'top': '20', 'right': '60', 'bottom': '20', 'left': '60'},
                'background_background': 'classic',
                'background_color': 'rgba(15, 23, 42, 0.95)',
                'position': 'fixed',
                'z_index': 1000,
                '_element_width': 'full'
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': site_name,
                        'header_size': 'h4',
                        'title_color': '#ffffff',
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_weight': '700',
                        'typography_font_size': {'unit': 'px', 'size': 26}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_align_items': 'center',
                        'flex_gap': {'unit': 'px', 'size': 8}
                    },
                    'elements': nav_links
                }
            ]
        }

    # ==================== PRO HERO ====================
    def _create_pro_hero(self, design_spec):
        """Create stunning full-screen hero with gradient overlay"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        hero = design_spec.get('hero', {})

        headline = hero.get('headline', 'Build Something Amazing')
        subheadline = hero.get('subheadline', 'The all-in-one platform that helps you create, launch, and scale your digital presence with powerful tools and beautiful design.')
        cta_text = hero.get('cta_text', 'Start Free Trial')

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'full',
                'min_height': {'unit': 'vh', 'size': 100},
                'flex_direction': 'column',
                'flex_justify_content': 'center',
                'flex_align_items': 'center',
                'padding': {'unit': 'px', 'top': '140', 'right': '40', 'bottom': '100', 'left': '40'},
                'background_background': 'gradient',
                'background_color': colors['dark'],
                'background_color_b': colors['gradient_start'],
                'background_gradient_type': 'linear',
                'background_gradient_angle': {'unit': 'deg', 'size': 135}
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'content_width': 'boxed',
                        'boxed_width': {'unit': 'px', 'size': 1000},
                        'flex_direction': 'column',
                        'flex_align_items': 'center'
                    },
                    'elements': [
                        # Badge/pill
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'button',
                            'settings': {
                                'text': '✨ Introducing our new platform',
                                'button_type': 'info',
                                'background_color': 'rgba(255,255,255,0.1)',
                                'button_text_color': '#ffffff',
                                'border_radius': {'unit': 'px', 'size': 50},
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 14},
                                'typography_font_weight': '500',
                                'button_padding': {'unit': 'px', 'top': '10', 'right': '24', 'bottom': '10', 'left': '24'},
                                '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '30', 'left': '0'}
                            }
                        },
                        # Main headline
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'heading',
                            'settings': {
                                'title': headline,
                                'header_size': 'h1',
                                'align': 'center',
                                'title_color': '#ffffff',
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 72},
                                'typography_font_size_tablet': {'unit': 'px', 'size': 52},
                                'typography_font_size_mobile': {'unit': 'px', 'size': 38},
                                'typography_font_weight': '800',
                                'typography_line_height': {'unit': 'em', 'size': 1.1},
                                'typography_letter_spacing': {'unit': 'px', 'size': -2}
                            }
                        },
                        # Subheadline
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': f'<p style="text-align: center; max-width: 700px; margin: 0 auto;">{subheadline}</p>',
                                'align': 'center',
                                'text_color': 'rgba(255,255,255,0.8)',
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 20},
                                'typography_line_height': {'unit': 'em', 'size': 1.7},
                                '_margin': {'unit': 'px', 'top': '30', 'right': '0', 'bottom': '50', 'left': '0'}
                            }
                        },
                        # CTA buttons row
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'flex_direction': 'row',
                                'flex_gap': {'unit': 'px', 'size': 16},
                                'flex_justify_content': 'center',
                                'flex_wrap': 'wrap'
                            },
                            'elements': [
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'button',
                                    'settings': {
                                        'text': cta_text,
                                        'link': {'url': '#contact'},
                                        'background_color': '#ffffff',
                                        'button_text_color': colors['dark'],
                                        'border_radius': {'unit': 'px', 'size': 10},
                                        'typography_typography': 'custom',
                                        'typography_font_family': font,
                                        'typography_font_size': {'unit': 'px', 'size': 17},
                                        'typography_font_weight': '600',
                                        'button_padding': {'unit': 'px', 'top': '18', 'right': '36', 'bottom': '18', 'left': '36'},
                                        'box_shadow_box_shadow_type': 'yes',
                                        'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 4, 'blur': 14, 'spread': 0, 'color': 'rgba(0,0,0,0.25)'}
                                    }
                                },
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'button',
                                    'settings': {
                                        'text': 'Watch Demo →',
                                        'link': {'url': '#demo'},
                                        'background_color': 'transparent',
                                        'button_text_color': '#ffffff',
                                        'border_border': 'solid',
                                        'border_width': {'unit': 'px', 'top': '2', 'right': '2', 'bottom': '2', 'left': '2'},
                                        'border_color': 'rgba(255,255,255,0.3)',
                                        'border_radius': {'unit': 'px', 'size': 10},
                                        'typography_typography': 'custom',
                                        'typography_font_family': font,
                                        'typography_font_size': {'unit': 'px', 'size': 17},
                                        'typography_font_weight': '600',
                                        'button_padding': {'unit': 'px', 'top': '16', 'right': '32', 'bottom': '16', 'left': '32'}
                                    }
                                }
                            ]
                        },
                        # Social proof
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': '<p style="text-align: center;">⭐⭐⭐⭐⭐ <strong>4.9/5</strong> from 2,000+ reviews</p>',
                                'align': 'center',
                                'text_color': 'rgba(255,255,255,0.7)',
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 14},
                                '_margin': {'unit': 'px', 'top': '40', 'right': '0', 'bottom': '0', 'left': '0'}
                            }
                        }
                    ]
                }
            ]
        }

    # ==================== TRUSTED BY ====================
    def _create_trusted_by_section(self, design_spec):
        """Create logos/trusted by section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)

        logos = ['Google', 'Microsoft', 'Amazon', 'Meta', 'Apple']
        logo_elements = []

        for logo in logos:
            logo_elements.append({
                'id': self._generate_id(),
                'elType': 'widget',
                'widgetType': 'heading',
                'settings': {
                    'title': logo,
                    'header_size': 'h5',
                    'title_color': '#94a3b8',
                    'typography_typography': 'custom',
                    'typography_font_family': font,
                    'typography_font_size': {'unit': 'px', 'size': 20},
                    'typography_font_weight': '700',
                    'typography_letter_spacing': {'unit': 'px', 'size': 1}
                }
            })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'flex_align_items': 'center',
                'padding': {'unit': 'px', 'top': '80', 'right': '40', 'bottom': '80', 'left': '40'},
                'background_background': 'classic',
                'background_color': '#ffffff'
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': '<p style="text-align: center; text-transform: uppercase; letter-spacing: 2px;">Trusted by industry leaders</p>',
                        'align': 'center',
                        'text_color': '#94a3b8',
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 13},
                        'typography_font_weight': '600',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '40', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_justify_content': 'space-around',
                        'flex_align_items': 'center',
                        'flex_wrap': 'wrap',
                        'flex_gap': {'unit': 'px', 'size': 60}
                    },
                    'elements': logo_elements
                }
            ]
        }

    # ==================== PRO SERVICES ====================
    def _create_pro_services(self, design_spec, section_spec):
        """Create modern services/features section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)

        services = section_spec.get('items', [
            {'title': 'Lightning Fast', 'description': 'Built for speed with optimized performance that loads in milliseconds.', 'icon': 'fas fa-bolt'},
            {'title': 'Secure by Default', 'description': 'Enterprise-grade security with end-to-end encryption and compliance.', 'icon': 'fas fa-shield-alt'},
            {'title': 'Scalable Infrastructure', 'description': 'Grows with your business from startup to enterprise seamlessly.', 'icon': 'fas fa-expand-arrows-alt'},
            {'title': 'AI-Powered Analytics', 'description': 'Smart insights and recommendations powered by machine learning.', 'icon': 'fas fa-brain'},
            {'title': '24/7 Expert Support', 'description': 'Dedicated support team available around the clock to help you succeed.', 'icon': 'fas fa-headset'},
            {'title': 'API & Integrations', 'description': 'Connect with 500+ tools and build custom workflows with our API.', 'icon': 'fas fa-plug'}
        ])

        service_cards = []
        for service in services:
            service_cards.append({
                'id': self._generate_id(),
                'elType': 'container',
                'settings': {
                    'width': {'unit': '%', 'size': 30},
                    'min_width': {'unit': 'px', 'size': 320},
                    'padding': {'unit': 'px', 'top': '40', 'right': '32', 'bottom': '40', 'left': '32'},
                    'background_background': 'classic',
                    'background_color': '#ffffff',
                    'border_radius': {'unit': 'px', 'size': 20},
                    'border_border': 'solid',
                    'border_width': {'unit': 'px', 'top': '1', 'right': '1', 'bottom': '1', 'left': '1'},
                    'border_color': '#e2e8f0',
                    'box_shadow_box_shadow_type': 'yes',
                    'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 4, 'blur': 20, 'spread': 0, 'color': 'rgba(0,0,0,0.05)'},
                    'flex_direction': 'column'
                },
                'elements': [
                    {
                        'id': self._generate_id(),
                        'elType': 'container',
                        'settings': {
                            'width': {'unit': 'px', 'size': 56},
                            'height': {'unit': 'px', 'size': 56},
                            'flex_justify_content': 'center',
                            'flex_align_items': 'center',
                            'background_background': 'classic',
                            'background_color': f"{colors['primary']}15",
                            'border_radius': {'unit': 'px', 'size': 14}
                        },
                        'elements': [{
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'icon',
                            'settings': {
                                'selected_icon': {'value': service.get('icon', 'fas fa-star'), 'library': 'fa-solid'},
                                'primary_color': colors['primary'],
                                'icon_size': {'unit': 'px', 'size': 24}
                            }
                        }]
                    },
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'heading',
                        'settings': {
                            'title': service.get('title', 'Feature'),
                            'header_size': 'h4',
                            'title_color': colors['dark'],
                            'typography_typography': 'custom',
                            'typography_font_family': font,
                            'typography_font_size': {'unit': 'px', 'size': 22},
                            'typography_font_weight': '700',
                            '_margin': {'unit': 'px', 'top': '24', 'right': '0', 'bottom': '12', 'left': '0'}
                        }
                    },
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'text-editor',
                        'settings': {
                            'editor': f"<p>{service.get('description', 'Description')}</p>",
                            'text_color': colors['text_light'],
                            'typography_typography': 'custom',
                            'typography_font_family': font,
                            'typography_font_size': {'unit': 'px', 'size': 16},
                            'typography_line_height': {'unit': 'em', 'size': 1.7}
                        }
                    }
                ]
            })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': '120', 'right': '40', 'bottom': '120', 'left': '40'},
                'background_background': 'classic',
                'background_color': '#f8fafc'
            },
            'elements': [
                # Section header
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'content_width': 'boxed',
                        'boxed_width': {'unit': 'px', 'size': 700},
                        'flex_direction': 'column',
                        'flex_align_items': 'center',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '70', 'left': '0'}
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': '<p style="text-align: center; text-transform: uppercase; letter-spacing: 3px;">Why Choose Us</p>',
                                'align': 'center',
                                'text_color': colors['primary'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
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
                                'title': section_spec.get('title', 'Everything you need to succeed'),
                                'header_size': 'h2',
                                'align': 'center',
                                'title_color': colors['dark'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 48},
                                'typography_font_weight': '800',
                                'typography_line_height': {'unit': 'em', 'size': 1.2}
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': '<p style="text-align: center;">Powerful features designed to help you build, launch, and grow your business faster than ever.</p>',
                                'align': 'center',
                                'text_color': colors['text_light'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 18},
                                '_margin': {'unit': 'px', 'top': '20', 'right': '0', 'bottom': '0', 'left': '0'}
                            }
                        }
                    ]
                },
                # Cards grid
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_wrap': 'wrap',
                        'flex_justify_content': 'center',
                        'flex_gap': {'unit': 'px', 'size': 24}
                    },
                    'elements': service_cards
                }
            ]
        }

    # ==================== PRO ABOUT ====================
    def _create_pro_about(self, design_spec, section_spec):
        """Create modern about/feature highlight section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'row',
                'flex_align_items': 'center',
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
                        'width': {'unit': '%', 'size': 50},
                        'flex_direction': 'column'
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': '<p style="text-transform: uppercase; letter-spacing: 3px;">About Us</p>',
                                'text_color': colors['primary'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
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
                                'title': section_spec.get('title', 'We help businesses reach their full potential'),
                                'header_size': 'h2',
                                'title_color': colors['dark'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 42},
                                'typography_font_weight': '800',
                                'typography_line_height': {'unit': 'em', 'size': 1.2}
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': f"<p>{section_spec.get('description', 'Founded with a mission to democratize technology, we have helped over 10,000 businesses transform their digital presence. Our team of experts combines innovation with experience to deliver results that matter.')}</p>",
                                'text_color': colors['text_light'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 18},
                                'typography_line_height': {'unit': 'em', 'size': 1.8},
                                '_margin': {'unit': 'px', 'top': '24', 'right': '0', 'bottom': '32', 'left': '0'}
                            }
                        },
                        # Stats row
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'flex_direction': 'row',
                                'flex_gap': {'unit': 'px', 'size': 48}
                            },
                            'elements': [
                                self._create_stat_item('10K+', 'Happy Clients', colors, font),
                                self._create_stat_item('98%', 'Success Rate', colors, font),
                                self._create_stat_item('24/7', 'Support', colors, font)
                            ]
                        }
                    ]
                },
                # Right image placeholder
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'width': {'unit': '%', 'size': 50},
                        'min_height': {'unit': 'px', 'size': 500},
                        'background_background': 'classic',
                        'background_color': '#f1f5f9',
                        'border_radius': {'unit': 'px', 'size': 24}
                    },
                    'elements': [{
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'text-editor',
                        'settings': {
                            'editor': '<p style="text-align: center; padding-top: 200px; opacity: 0.5;">Image Placeholder</p>',
                            'align': 'center',
                            'text_color': colors['text_light']
                        }
                    }]
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
                        'typography_font_family': font,
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
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 14}
                    }
                }
            ]
        }

    # ==================== PRO TESTIMONIALS ====================
    def _create_pro_testimonials(self, design_spec, section_spec):
        """Create modern testimonials section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)

        testimonials = section_spec.get('items', [
            {'content': 'This platform completely transformed how we work. The results speak for themselves - 300% growth in just 6 months.', 'name': 'Sarah Chen', 'title': 'CEO, TechStart'},
            {'content': 'The best investment we have made. Their team went above and beyond to ensure our success. Highly recommended!', 'name': 'Michael Rodriguez', 'title': 'Founder, ScaleUp'},
            {'content': 'Incredible support and even better results. We could not have scaled without them. A true partner in growth.', 'name': 'Emily Watson', 'title': 'CMO, GrowthCo'}
        ])

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
                    'background_color': '#ffffff',
                    'border_radius': {'unit': 'px', 'size': 20},
                    'box_shadow_box_shadow_type': 'yes',
                    'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 10, 'blur': 40, 'spread': 0, 'color': 'rgba(0,0,0,0.08)'},
                    'flex_direction': 'column'
                },
                'elements': [
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'text-editor',
                        'settings': {
                            'editor': '⭐⭐⭐⭐⭐',
                            'typography_font_size': {'unit': 'px', 'size': 18},
                            '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '20', 'left': '0'}
                        }
                    },
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'text-editor',
                        'settings': {
                            'editor': f'<p>"{t.get("content", "Great experience!")}"</p>',
                            'text_color': colors['dark'],
                            'typography_typography': 'custom',
                            'typography_font_family': font,
                            'typography_font_size': {'unit': 'px', 'size': 17},
                            'typography_line_height': {'unit': 'em', 'size': 1.7},
                            'typography_font_style': 'italic',
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
                                        'title_color': '#ffffff',
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
                                            'title_color': colors['dark'],
                                            'typography_typography': 'custom',
                                            'typography_font_family': font,
                                            'typography_font_size': {'unit': 'px', 'size': 16},
                                            'typography_font_weight': '600'
                                        }
                                    },
                                    {
                                        'id': self._generate_id(),
                                        'elType': 'widget',
                                        'widgetType': 'text-editor',
                                        'settings': {
                                            'editor': f"<p>{t.get('title', 'Position')}</p>",
                                            'text_color': colors['text_light'],
                                            'typography_typography': 'custom',
                                            'typography_font_family': font,
                                            'typography_font_size': {'unit': 'px', 'size': 14}
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
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': '120', 'right': '40', 'bottom': '120', 'left': '40'},
                'background_background': 'classic',
                'background_color': '#f8fafc'
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'column',
                        'flex_align_items': 'center',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '70', 'left': '0'}
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
                                'typography_font_family': font,
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
                                'title': 'Loved by thousands of customers',
                                'header_size': 'h2',
                                'align': 'center',
                                'title_color': colors['dark'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 48},
                                'typography_font_weight': '800'
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
                                'typography_font_family': font,
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
                                'typography_font_family': font,
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
                                'typography_font_family': font,
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

    # ==================== FINAL CTA ====================
    def _create_final_cta(self, design_spec):
        """Create final CTA section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'full',
                'flex_direction': 'column',
                'flex_align_items': 'center',
                'padding': {'unit': 'px', 'top': '120', 'right': '40', 'bottom': '120', 'left': '40'},
                'background_background': 'gradient',
                'background_color': colors['dark'],
                'background_color_b': colors['gradient_start'],
                'background_gradient_type': 'linear',
                'background_gradient_angle': {'unit': 'deg', 'size': 135}
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': 'Ready to get started?',
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': '#ffffff',
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 52},
                        'typography_font_weight': '800'
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': '<p style="text-align: center;">Join thousands of satisfied customers and transform your business today.</p>',
                        'align': 'center',
                        'text_color': 'rgba(255,255,255,0.8)',
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 20},
                        '_margin': {'unit': 'px', 'top': '20', 'right': '0', 'bottom': '40', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_gap': {'unit': 'px', 'size': 16}
                    },
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'button',
                            'settings': {
                                'text': 'Start Free Trial',
                                'link': {'url': '#contact'},
                                'background_color': '#ffffff',
                                'button_text_color': colors['dark'],
                                'border_radius': {'unit': 'px', 'size': 10},
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 17},
                                'typography_font_weight': '600',
                                'button_padding': {'unit': 'px', 'top': '18', 'right': '36', 'bottom': '18', 'left': '36'}
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'button',
                            'settings': {
                                'text': 'Talk to Sales',
                                'link': {'url': '#contact'},
                                'background_color': 'transparent',
                                'button_text_color': '#ffffff',
                                'border_border': 'solid',
                                'border_width': {'unit': 'px', 'top': '2', 'right': '2', 'bottom': '2', 'left': '2'},
                                'border_color': 'rgba(255,255,255,0.3)',
                                'border_radius': {'unit': 'px', 'size': 10},
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 17},
                                'typography_font_weight': '600',
                                'button_padding': {'unit': 'px', 'top': '16', 'right': '32', 'bottom': '16', 'left': '32'}
                            }
                        }
                    ]
                }
            ]
        }

    # ==================== PRO FOOTER ====================
    def _create_pro_footer(self, design_spec):
        """Create modern footer"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        site_name = design_spec.get('site_name', 'Brand')

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': '80', 'right': '40', 'bottom': '40', 'left': '40'},
                'background_background': 'classic',
                'background_color': colors['dark']
            },
            'elements': [
                # Top section
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_justify_content': 'space-between',
                        'flex_wrap': 'wrap',
                        'flex_gap': {'unit': 'px', 'size': 60},
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '60', 'left': '0'}
                    },
                    'elements': [
                        # Brand column
                        {
                            'id': self._generate_id(),
                            'elType': 'container',
                            'settings': {
                                'width': {'unit': '%', 'size': 30},
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
                                        'title_color': '#ffffff',
                                        'typography_typography': 'custom',
                                        'typography_font_family': font,
                                        'typography_font_size': {'unit': 'px', 'size': 24},
                                        'typography_font_weight': '700',
                                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '16', 'left': '0'}
                                    }
                                },
                                {
                                    'id': self._generate_id(),
                                    'elType': 'widget',
                                    'widgetType': 'text-editor',
                                    'settings': {
                                        'editor': '<p>Building the future of digital experiences. Join us on our mission to transform businesses worldwide.</p>',
                                        'text_color': 'rgba(255,255,255,0.6)',
                                        'typography_typography': 'custom',
                                        'typography_font_family': font,
                                        'typography_font_size': {'unit': 'px', 'size': 15},
                                        'typography_line_height': {'unit': 'em', 'size': 1.7}
                                    }
                                }
                            ]
                        },
                        # Links columns
                        self._create_footer_column('Product', ['Features', 'Pricing', 'Integrations', 'API'], font),
                        self._create_footer_column('Company', ['About', 'Careers', 'Blog', 'Press'], font),
                        self._create_footer_column('Support', ['Help Center', 'Contact', 'Status', 'Documentation'], font)
                    ]
                },
                # Bottom bar
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
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
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 14}
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'social-icons',
                            'settings': {
                                'social_icon_list': [
                                    {'social_icon': {'value': 'fab fa-twitter', 'library': 'fa-brands'}, 'link': {'url': '#'}},
                                    {'social_icon': {'value': 'fab fa-linkedin-in', 'library': 'fa-brands'}, 'link': {'url': '#'}},
                                    {'social_icon': {'value': 'fab fa-github', 'library': 'fa-brands'}, 'link': {'url': '#'}},
                                    {'social_icon': {'value': 'fab fa-instagram', 'library': 'fa-brands'}, 'link': {'url': '#'}}
                                ],
                                'icon_color': 'custom',
                                'icon_primary_color': 'rgba(255,255,255,0.6)',
                                'icon_size': {'unit': 'px', 'size': 18}
                            }
                        }
                    ]
                }
            ]
        }

    def _create_footer_column(self, title, links, font):
        """Create footer links column"""
        link_elements = []
        for link in links:
            link_elements.append({
                'id': self._generate_id(),
                'elType': 'widget',
                'widgetType': 'button',
                'settings': {
                    'text': link,
                    'link': {'url': f'#{link.lower().replace(" ", "-")}'},
                    'button_type': 'link',
                    'button_text_color': 'rgba(255,255,255,0.6)',
                    'typography_typography': 'custom',
                    'typography_font_family': font,
                    'typography_font_size': {'unit': 'px', 'size': 15},
                    'button_padding': {'unit': 'px', 'top': '6', 'right': '0', 'bottom': '6', 'left': '0'},
                    'hover_color': '#ffffff'
                }
            })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'flex_direction': 'column',
                'width': {'unit': '%', 'size': 15}
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': title,
                        'header_size': 'h5',
                        'title_color': '#ffffff',
                        'typography_typography': 'custom',
                        'typography_font_family': font,
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
