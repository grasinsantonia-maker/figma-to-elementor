#!/usr/bin/env python3
"""
Enhanced Elementor Pro Generator - Creates Elementor Pro JSON from design specs
Supports ALL Elementor Pro native widgets - NO CODE approach
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
        """Generate complete Elementor page from design specification"""
        sections = []

        # Generate sections based on spec
        if design_spec.get('header'):
            sections.append(self._create_header(design_spec))

        if design_spec.get('hero'):
            sections.append(self._create_hero_section(design_spec))

        for section in design_spec.get('sections', []):
            section_type = section.get('type', 'generic')

            if section_type == 'services':
                sections.append(self._create_services_section(design_spec, section))
            elif section_type == 'about':
                sections.append(self._create_about_section(design_spec, section))
            elif section_type == 'testimonials':
                sections.append(self._create_testimonials_section(design_spec, section))
            elif section_type == 'team':
                sections.append(self._create_team_section(design_spec, section))
            elif section_type == 'portfolio':
                sections.append(self._create_portfolio_section(design_spec, section))
            elif section_type == 'pricing':
                sections.append(self._create_pricing_section(design_spec, section))
            elif section_type == 'faq':
                sections.append(self._create_faq_section(design_spec, section))
            elif section_type == 'cta':
                sections.append(self._create_cta_section(design_spec, section))
            elif section_type == 'contact':
                sections.append(self._create_contact_section(design_spec, section))
            elif section_type == 'stats':
                sections.append(self._create_stats_section(design_spec, section))
            elif section_type == 'clients':
                sections.append(self._create_clients_section(design_spec, section))
            elif section_type == 'blog':
                sections.append(self._create_blog_section(design_spec, section))

        if design_spec.get('footer'):
            sections.append(self._create_footer(design_spec))

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
        """Extract colors from design spec"""
        colors = design_spec.get('colors', {})
        return {
            'primary': colors.get('primary', ['#0066cc'])[0] if isinstance(colors.get('primary'), list) else colors.get('primary', '#0066cc'),
            'secondary': colors.get('secondary', ['#333333'])[0] if isinstance(colors.get('secondary'), list) else colors.get('secondary', '#333333'),
            'text': colors.get('text', ['#333333'])[0] if isinstance(colors.get('text'), list) else colors.get('text', '#333333'),
            'background': colors.get('background', ['#ffffff'])[0] if isinstance(colors.get('background'), list) else colors.get('background', '#ffffff'),
            'accent': colors.get('accent', ['#ff6600'])[0] if isinstance(colors.get('accent'), list) else colors.get('accent', '#ff6600')
        }

    def _get_fonts(self, design_spec):
        """Extract fonts from design spec"""
        fonts = design_spec.get('fonts', ['Inter'])
        return fonts[0] if isinstance(fonts, list) else fonts

    def _get_spacing(self, design_spec):
        """Extract spacing from design spec"""
        return design_spec.get('spacing', {
            'section_padding': '80',
            'element_gap': '30'
        })

    def _get_button_style(self, design_spec):
        """Extract button style from design spec"""
        return design_spec.get('button_style', {
            'shape': 'rounded',
            'border_radius': '8'
        })

    # ============== SECTION CREATORS ==============

    def _create_header(self, design_spec):
        """Create navigation header section with text links (no menu required)"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        btn_style = self._get_button_style(design_spec)

        # Get navigation items from design spec or use defaults
        nav_items = design_spec.get('nav_items', ['Home', 'Services', 'About', 'Contact'])

        # Create nav link widgets
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
                    'button_text_color': colors['text'],
                    'typography_typography': 'custom',
                    'typography_font_family': font,
                    'typography_font_size': {'unit': 'px', 'size': 15},
                    'typography_font_weight': '500',
                    'button_padding': {'unit': 'px', 'top': '10', 'right': '16', 'bottom': '10', 'left': '16'},
                    'hover_color': colors['primary']
                }
            })

        # Add CTA button at the end
        nav_links.append({
            'id': self._generate_id(),
            'elType': 'widget',
            'widgetType': 'button',
            'settings': {
                'text': design_spec.get('header_cta', 'Get Started'),
                'link': {'url': '#contact'},
                'background_color': colors['primary'],
                'button_text_color': '#ffffff',
                'border_radius': {'unit': 'px', 'size': int(btn_style.get('border_radius', '8').replace('px', ''))},
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
                'padding': {'unit': 'px', 'top': '15', 'right': '50', 'bottom': '15', 'left': '50'},
                'background_background': 'classic',
                'background_color': colors['background'],
                'position': 'fixed',
                'z_index': 100,
                'box_shadow_box_shadow_type': 'yes',
                'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 2, 'blur': 10, 'spread': 0, 'color': 'rgba(0,0,0,0.05)'}
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': design_spec.get('site_name', 'Brand'),
                        'header_size': 'h4',
                        'title_color': colors['primary'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_weight': '700',
                        'typography_font_size': {'unit': 'px', 'size': 24}
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

    def _create_hero_section(self, design_spec):
        """Create hero section with heading, subtext, and CTA"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)
        btn_style = self._get_button_style(design_spec)
        hero = design_spec.get('hero', {})

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'min_height': {'unit': 'vh', 'size': 80},
                'flex_direction': 'column',
                'flex_justify_content': 'center',
                'flex_align_items': 'flex-start',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '100'), 'right': '50', 'bottom': spacing.get('section_padding', '100'), 'left': '50'},
                'background_background': 'classic',
                'background_color': hero.get('background_color', colors['background'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': hero.get('headline', 'Transform Your Business'),
                        'header_size': 'h1',
                        'title_color': colors['text'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 64},
                        'typography_font_weight': '700',
                        'typography_line_height': {'unit': 'em', 'size': 1.2}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': f"<p>{hero.get('subheadline', 'We help businesses grow with innovative solutions.')}</p>",
                        'text_color': colors['secondary'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 20},
                        '_margin': {'unit': 'px', 'top': '20', 'right': '0', 'bottom': '30', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'button',
                    'settings': {
                        'text': hero.get('cta_text', 'Get Started'),
                        'link': {'url': hero.get('cta_link', '#contact')},
                        'button_type': 'primary',
                        'background_color': colors['primary'],
                        'button_text_color': '#ffffff',
                        'border_radius': {'unit': 'px', 'size': int(btn_style.get('border_radius', '8').replace('px', ''))},
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_weight': '600',
                        'button_padding': {'unit': 'px', 'top': '16', 'right': '32', 'bottom': '16', 'left': '32'}
                    }
                }
            ]
        }

    def _create_services_section(self, design_spec, section_spec):
        """Create services section with icon boxes"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        services = section_spec.get('items', [
            {'title': 'Service 1', 'description': 'Description of service 1', 'icon': 'fas fa-rocket'},
            {'title': 'Service 2', 'description': 'Description of service 2', 'icon': 'fas fa-cog'},
            {'title': 'Service 3', 'description': 'Description of service 3', 'icon': 'fas fa-chart-line'}
        ])

        service_widgets = []
        for service in services:
            service_widgets.append({
                'id': self._generate_id(),
                'elType': 'container',
                'settings': {
                    'width': {'unit': '%', 'size': 33},
                    'padding': {'unit': 'px', 'top': '30', 'right': '20', 'bottom': '30', 'left': '20'}
                },
                'elements': [{
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'icon-box',
                    'settings': {
                        'selected_icon': {'value': service.get('icon', 'fas fa-star'), 'library': 'fa-solid'},
                        'title_text': service.get('title', 'Service'),
                        'description_text': service.get('description', 'Service description'),
                        'position': 'top',
                        'primary_color': colors['primary'],
                        'title_color': colors['text'],
                        'description_color': colors['secondary'],
                        'title_typography_typography': 'custom',
                        'title_typography_font_family': font,
                        'title_typography_font_weight': '600',
                        'description_typography_typography': 'custom',
                        'description_typography_font_family': font
                    }
                }]
            })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['background'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'Our Services'),
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': colors['text'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '700',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '50', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_wrap': 'wrap',
                        'flex_justify_content': 'center',
                        'flex_gap': {'unit': 'px', 'size': 30}
                    },
                    'elements': service_widgets
                }
            ]
        }

    def _create_about_section(self, design_spec, section_spec):
        """Create about section with image and text"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'row',
                'flex_align_items': 'center',
                'flex_gap': {'unit': 'px', 'size': 60},
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['background'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {'width': {'unit': '%', 'size': 50}},
                    'elements': [{
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'image',
                        'settings': {
                            'image': {'url': section_spec.get('image_url', 'https://via.placeholder.com/600x400')},
                            'image_size': 'large',
                            'border_radius': {'unit': 'px', 'size': 12}
                        }
                    }]
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {'width': {'unit': '%', 'size': 50}},
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'heading',
                            'settings': {
                                'title': section_spec.get('title', 'About Us'),
                                'header_size': 'h2',
                                'title_color': colors['text'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 42},
                                'typography_font_weight': '700'
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': f"<p>{section_spec.get('description', 'We are a team of dedicated professionals committed to delivering exceptional results.')}</p>",
                                'text_color': colors['secondary'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 18},
                                '_margin': {'unit': 'px', 'top': '20', 'right': '0', 'bottom': '0', 'left': '0'}
                            }
                        }
                    ]
                }
            ]
        }

    def _create_testimonials_section(self, design_spec, section_spec):
        """Create testimonials section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        testimonials = section_spec.get('items', [
            {'content': 'Great service!', 'name': 'John Doe', 'title': 'CEO'},
            {'content': 'Highly recommended!', 'name': 'Jane Smith', 'title': 'Manager'},
            {'content': 'Exceeded expectations!', 'name': 'Bob Johnson', 'title': 'Director'}
        ])

        testimonial_widgets = []
        for t in testimonials:
            testimonial_widgets.append({
                'id': self._generate_id(),
                'elType': 'container',
                'settings': {
                    'width': {'unit': '%', 'size': 33},
                    'padding': {'unit': 'px', 'top': '30', 'right': '25', 'bottom': '30', 'left': '25'},
                    'background_background': 'classic',
                    'background_color': '#ffffff',
                    'border_radius': {'unit': 'px', 'size': 12},
                    'box_shadow_box_shadow_type': 'yes',
                    'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 4, 'blur': 20, 'spread': 0, 'color': 'rgba(0,0,0,0.08)'}
                },
                'elements': [{
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'testimonial',
                    'settings': {
                        'testimonial_content': t.get('content', 'Great experience!'),
                        'testimonial_name': t.get('name', 'Client Name'),
                        'testimonial_job': t.get('title', 'Position'),
                        'testimonial_alignment': 'center',
                        'content_content_color': colors['text'],
                        'name_text_color': colors['text'],
                        'title_text_color': colors['secondary'],
                        'content_typography_typography': 'custom',
                        'content_typography_font_family': font,
                        'name_typography_typography': 'custom',
                        'name_typography_font_family': font,
                        'name_typography_font_weight': '600'
                    }
                }]
            })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', '#f8f9fa')
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'What Our Clients Say'),
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': colors['text'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '700',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '50', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_wrap': 'wrap',
                        'flex_justify_content': 'center',
                        'flex_gap': {'unit': 'px', 'size': 30}
                    },
                    'elements': testimonial_widgets
                }
            ]
        }

    def _create_team_section(self, design_spec, section_spec):
        """Create team section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        members = section_spec.get('items', [
            {'name': 'Team Member 1', 'title': 'CEO', 'image': 'https://via.placeholder.com/300x300'},
            {'name': 'Team Member 2', 'title': 'CTO', 'image': 'https://via.placeholder.com/300x300'},
            {'name': 'Team Member 3', 'title': 'Designer', 'image': 'https://via.placeholder.com/300x300'}
        ])

        member_widgets = []
        for member in members:
            member_widgets.append({
                'id': self._generate_id(),
                'elType': 'container',
                'settings': {
                    'width': {'unit': '%', 'size': 25},
                    'flex_direction': 'column',
                    'flex_align_items': 'center',
                    'padding': {'unit': 'px', 'top': '20', 'right': '15', 'bottom': '20', 'left': '15'}
                },
                'elements': [
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'image',
                        'settings': {
                            'image': {'url': member.get('image', 'https://via.placeholder.com/300x300')},
                            'image_size': 'medium',
                            'border_radius': {'unit': '%', 'size': 50},
                            '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '20', 'left': '0'}
                        }
                    },
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'heading',
                        'settings': {
                            'title': member.get('name', 'Name'),
                            'header_size': 'h4',
                            'align': 'center',
                            'title_color': colors['text'],
                            'typography_typography': 'custom',
                            'typography_font_family': font,
                            'typography_font_weight': '600'
                        }
                    },
                    {
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'text-editor',
                        'settings': {
                            'editor': f"<p>{member.get('title', 'Position')}</p>",
                            'align': 'center',
                            'text_color': colors['secondary'],
                            'typography_typography': 'custom',
                            'typography_font_family': font
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
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['background'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'Meet Our Team'),
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': colors['text'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '700',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '50', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_wrap': 'wrap',
                        'flex_justify_content': 'center',
                        'flex_gap': {'unit': 'px', 'size': 30}
                    },
                    'elements': member_widgets
                }
            ]
        }

    def _create_portfolio_section(self, design_spec, section_spec):
        """Create portfolio/gallery section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['background'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'Our Work'),
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': colors['text'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '700',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '50', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'gallery',
                    'settings': {
                        'gallery_type': 'single',
                        'columns': 3,
                        'gallery_gap': {'unit': 'px', 'size': 20}
                    }
                }
            ]
        }

    def _create_pricing_section(self, design_spec, section_spec):
        """Create pricing section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        plans = section_spec.get('items', [
            {'name': 'Basic', 'price': '$29', 'period': '/month', 'features': ['Feature 1', 'Feature 2', 'Feature 3']},
            {'name': 'Pro', 'price': '$59', 'period': '/month', 'features': ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'], 'featured': True},
            {'name': 'Enterprise', 'price': '$99', 'period': '/month', 'features': ['All Features', 'Priority Support']}
        ])

        plan_widgets = []
        for plan in plans:
            is_featured = plan.get('featured', False)
            plan_widgets.append({
                'id': self._generate_id(),
                'elType': 'container',
                'settings': {
                    'width': {'unit': '%', 'size': 30},
                    'flex_direction': 'column',
                    'flex_align_items': 'center',
                    'padding': {'unit': 'px', 'top': '40', 'right': '30', 'bottom': '40', 'left': '30'},
                    'background_background': 'classic',
                    'background_color': colors['primary'] if is_featured else '#ffffff',
                    'border_radius': {'unit': 'px', 'size': 12},
                    'box_shadow_box_shadow_type': 'yes',
                    'box_shadow_box_shadow': {'horizontal': 0, 'vertical': 10, 'blur': 40, 'spread': 0, 'color': 'rgba(0,0,0,0.1)'}
                },
                'elements': [{
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'price-table',
                    'settings': {
                        'heading': plan.get('name', 'Plan'),
                        'currency_symbol': '$',
                        'price': plan.get('price', '$0').replace('$', ''),
                        'period': plan.get('period', '/month'),
                        'features_list': [{'item_text': f} for f in plan.get('features', [])],
                        'button_text': 'Get Started'
                    }
                }]
            })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', '#f8f9fa')
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'Pricing Plans'),
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': colors['text'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '700',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '50', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'flex_direction': 'row',
                        'flex_wrap': 'wrap',
                        'flex_justify_content': 'center',
                        'flex_gap': {'unit': 'px', 'size': 30}
                    },
                    'elements': plan_widgets
                }
            ]
        }

    def _create_faq_section(self, design_spec, section_spec):
        """Create FAQ section with accordion"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        faqs = section_spec.get('items', [
            {'question': 'What services do you offer?', 'answer': 'We offer a wide range of services...'},
            {'question': 'How much does it cost?', 'answer': 'Our pricing varies based on your needs...'},
            {'question': 'How long does it take?', 'answer': 'Project timelines depend on scope...'}
        ])

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 900},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['background'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'Frequently Asked Questions'),
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': colors['text'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '700',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '50', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'accordion',
                    'settings': {
                        'tabs': [{'tab_title': faq['question'], 'tab_content': faq['answer']} for faq in faqs],
                        'title_color': colors['text'],
                        'content_color': colors['secondary']
                    }
                }
            ]
        }

    def _create_cta_section(self, design_spec, section_spec):
        """Create call-to-action section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)
        btn_style = self._get_button_style(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 900},
                'flex_direction': 'column',
                'flex_align_items': 'center',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['primary'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'Ready to Get Started?'),
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': '#ffffff',
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '700'
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'text-editor',
                    'settings': {
                        'editor': f"<p>{section_spec.get('description', 'Contact us today.')}</p>",
                        'align': 'center',
                        'text_color': 'rgba(255,255,255,0.9)',
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 18},
                        '_margin': {'unit': 'px', 'top': '15', 'right': '0', 'bottom': '30', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'button',
                    'settings': {
                        'text': section_spec.get('button_text', 'Contact Us'),
                        'link': {'url': section_spec.get('button_link', '#contact')},
                        'background_color': '#ffffff',
                        'button_text_color': colors['primary'],
                        'border_radius': {'unit': 'px', 'size': int(btn_style.get('border_radius', '8').replace('px', ''))},
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_weight': '600',
                        'button_padding': {'unit': 'px', 'top': '16', 'right': '40', 'bottom': '16', 'left': '40'}
                    }
                }
            ]
        }

    def _create_contact_section(self, design_spec, section_spec):
        """Create contact section with form"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'row',
                'flex_gap': {'unit': 'px', 'size': 60},
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['background'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {'width': {'unit': '%', 'size': 50}},
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'heading',
                            'settings': {
                                'title': section_spec.get('title', 'Get In Touch'),
                                'header_size': 'h2',
                                'title_color': colors['text'],
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_size': {'unit': 'px', 'size': 42},
                                'typography_font_weight': '700'
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': f"<p>{section_spec.get('description', 'Have a question? We would love to hear from you.')}</p>",
                                'text_color': colors['secondary'],
                                '_margin': {'unit': 'px', 'top': '20', 'right': '0', 'bottom': '30', 'left': '0'}
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'icon-list',
                            'settings': {
                                'icon_list': [
                                    {'text': section_spec.get('email', 'hello@example.com'), 'selected_icon': {'value': 'fas fa-envelope', 'library': 'fa-solid'}},
                                    {'text': section_spec.get('phone', '+1 234 567 890'), 'selected_icon': {'value': 'fas fa-phone', 'library': 'fa-solid'}},
                                    {'text': section_spec.get('address', '123 Business St, City'), 'selected_icon': {'value': 'fas fa-map-marker-alt', 'library': 'fa-solid'}}
                                ],
                                'icon_color': colors['primary'],
                                'text_color': colors['text']
                            }
                        }
                    ]
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {
                        'width': {'unit': '%', 'size': 50},
                        'padding': {'unit': 'px', 'top': '40', 'right': '40', 'bottom': '40', 'left': '40'},
                        'background_background': 'classic',
                        'background_color': '#f8f9fa',
                        'border_radius': {'unit': 'px', 'size': 12}
                    },
                    'elements': [{
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'form',
                        'settings': {
                            'form_name': 'Contact Form',
                            'form_fields': [
                                {'custom_id': 'name', 'field_type': 'text', 'field_label': 'Name', 'placeholder': 'Your Name', 'required': 'yes', 'width': '50'},
                                {'custom_id': 'email', 'field_type': 'email', 'field_label': 'Email', 'placeholder': 'Your Email', 'required': 'yes', 'width': '50'},
                                {'custom_id': 'message', 'field_type': 'textarea', 'field_label': 'Message', 'placeholder': 'Your Message', 'required': 'yes', 'rows': 5}
                            ],
                            'button_text': 'Send Message',
                            'button_background_color': colors['primary'],
                            'button_color': '#ffffff'
                        }
                    }]
                }
            ]
        }

    def _create_stats_section(self, design_spec, section_spec):
        """Create statistics section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        stats = section_spec.get('items', [
            {'number': '500+', 'label': 'Clients'},
            {'number': '1000+', 'label': 'Projects'},
            {'number': '50+', 'label': 'Awards'},
            {'number': '10+', 'label': 'Years'}
        ])

        stat_widgets = []
        for stat in stats:
            stat_widgets.append({
                'id': self._generate_id(),
                'elType': 'container',
                'settings': {
                    'width': {'unit': '%', 'size': 25},
                    'flex_direction': 'column',
                    'flex_align_items': 'center'
                },
                'elements': [{
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'counter',
                    'settings': {
                        'starting_number': 0,
                        'ending_number': int(''.join(filter(str.isdigit, stat.get('number', '0')))) or 100,
                        'suffix': '+' if '+' in stat.get('number', '') else '',
                        'title': stat.get('label', 'Stat'),
                        'number_color': '#ffffff',
                        'title_color': 'rgba(255,255,255,0.8)',
                        'number_typography_typography': 'custom',
                        'number_typography_font_family': font,
                        'number_typography_font_size': {'unit': 'px', 'size': 48},
                        'number_typography_font_weight': '700'
                    }
                }]
            })

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'row',
                'flex_justify_content': 'space-around',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '60'), 'right': '30', 'bottom': spacing.get('section_padding', '60'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['primary'])
            },
            'elements': stat_widgets
        }

    def _create_clients_section(self, design_spec, section_spec):
        """Create clients/logos section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'flex_align_items': 'center',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '60'), 'right': '30', 'bottom': spacing.get('section_padding', '60'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', '#f8f9fa')
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'Trusted By'),
                        'header_size': 'h4',
                        'align': 'center',
                        'title_color': colors['secondary'],
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '30', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'image-carousel',
                    'settings': {
                        'slides_to_show': '5',
                        'autoplay': 'yes',
                        'navigation': 'none',
                        'pagination': 'none'
                    }
                }
            ]
        }

    def _create_blog_section(self, design_spec, section_spec):
        """Create blog posts section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)
        spacing = self._get_spacing(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'column',
                'padding': {'unit': 'px', 'top': spacing.get('section_padding', '80'), 'right': '30', 'bottom': spacing.get('section_padding', '80'), 'left': '30'},
                'background_background': 'classic',
                'background_color': section_spec.get('background_color', colors['background'])
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'heading',
                    'settings': {
                        'title': section_spec.get('title', 'Latest Articles'),
                        'header_size': 'h2',
                        'align': 'center',
                        'title_color': colors['text'],
                        'typography_typography': 'custom',
                        'typography_font_family': font,
                        'typography_font_size': {'unit': 'px', 'size': 42},
                        'typography_font_weight': '700',
                        '_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '50', 'left': '0'}
                    }
                },
                {
                    'id': self._generate_id(),
                    'elType': 'widget',
                    'widgetType': 'posts',
                    'settings': {
                        'posts_per_page': 3,
                        'columns': 3,
                        'show_image': 'yes',
                        'show_title': 'yes',
                        'show_excerpt': 'yes',
                        'show_read_more': 'yes'
                    }
                }
            ]
        }

    def _create_footer(self, design_spec):
        """Create footer section"""
        colors = self._get_colors(design_spec)
        font = self._get_fonts(design_spec)

        return {
            'id': self._generate_id(),
            'elType': 'container',
            'settings': {
                'content_width': 'boxed',
                'boxed_width': {'unit': 'px', 'size': 1200},
                'flex_direction': 'row',
                'flex_justify_content': 'space-between',
                'flex_wrap': 'wrap',
                'padding': {'unit': 'px', 'top': '60', 'right': '30', 'bottom': '40', 'left': '30'},
                'background_background': 'classic',
                'background_color': '#1a1a1a'
            },
            'elements': [
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {'width': {'unit': '%', 'size': 30}},
                    'elements': [
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'heading',
                            'settings': {
                                'title': design_spec.get('site_name', 'Brand'),
                                'header_size': 'h4',
                                'title_color': '#ffffff',
                                'typography_typography': 'custom',
                                'typography_font_family': font,
                                'typography_font_weight': '700'
                            }
                        },
                        {
                            'id': self._generate_id(),
                            'elType': 'widget',
                            'widgetType': 'text-editor',
                            'settings': {
                                'editor': '<p>Building exceptional digital experiences.</p>',
                                'text_color': 'rgba(255,255,255,0.7)',
                                '_margin': {'unit': 'px', 'top': '15', 'right': '0', 'bottom': '0', 'left': '0'}
                            }
                        }
                    ]
                },
                {
                    'id': self._generate_id(),
                    'elType': 'container',
                    'settings': {'width': {'unit': '%', 'size': 25}},
                    'elements': [{
                        'id': self._generate_id(),
                        'elType': 'widget',
                        'widgetType': 'social-icons',
                        'settings': {
                            'social_icon_list': [
                                {'social_icon': {'value': 'fab fa-facebook-f', 'library': 'fa-brands'}, 'link': {'url': '#'}},
                                {'social_icon': {'value': 'fab fa-twitter', 'library': 'fa-brands'}, 'link': {'url': '#'}},
                                {'social_icon': {'value': 'fab fa-instagram', 'library': 'fa-brands'}, 'link': {'url': '#'}},
                                {'social_icon': {'value': 'fab fa-linkedin-in', 'library': 'fa-brands'}, 'link': {'url': '#'}}
                            ],
                            'icon_color': 'custom',
                            'icon_primary_color': 'rgba(255,255,255,0.7)'
                        }
                    }]
                }
            ]
        }

    def to_json(self, page_data):
        """Convert page data to JSON string"""
        return json.dumps(page_data, indent=2)
