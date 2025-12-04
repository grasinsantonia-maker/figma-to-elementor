"""
WebBuilder AI - Ultimate Web Design App
Converts natural language descriptions + inspiration sites into Elementor Pro templates
"""

import os
import json
from flask import Flask, render_template, request, jsonify, send_file
from dotenv import load_dotenv

# Import our custom modules
from analyzers.site_analyzer import SiteAnalyzer
from parsers.description_parser import DescriptionParser
from generators.elementor_pro_generator import ElementorProGenerator
from connectors.wordpress_connector import WordPressConnector

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.environ.get('SECRET_KEY', 'webbuilder-ai-secret')

# Store session data (in production, use proper session/database)
conversion_cache = {}

# Initialize components
site_analyzer = SiteAnalyzer()
description_parser = DescriptionParser()
elementor_generator = ElementorProGenerator()


@app.route('/')
def index():
    """Main page - 4-step wizard"""
    return render_template('index.html')


# ============================================
# STEP 2: ANALYZE INSPIRATION SITES
# ============================================

@app.route('/api/analyze-site', methods=['POST'])
def analyze_site():
    """Analyze a single inspiration website"""
    try:
        data = request.get_json()
        url = data.get('url', '')

        if not url:
            return jsonify({
                'success': False,
                'error': 'URL is required'
            }), 400

        # Analyze the site
        analysis = site_analyzer.analyze_site(url)

        if 'error' in analysis:
            return jsonify({
                'success': False,
                'error': analysis['error']
            }), 400

        return jsonify({
            'success': True,
            'analysis': analysis
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/analyze-multiple', methods=['POST'])
def analyze_multiple_sites():
    """Analyze multiple inspiration websites and combine insights"""
    try:
        data = request.get_json()
        urls = data.get('urls', [])

        if not urls:
            return jsonify({
                'success': False,
                'error': 'At least one URL is required'
            }), 400

        # Analyze all sites
        result = site_analyzer.analyze_multiple(urls)

        return jsonify({
            'success': True,
            'analyses': result['individual_analyses'],
            'combined': result['combined_insights']
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# ============================================
# GENERATE DESIGN FROM DESCRIPTION
# ============================================

@app.route('/api/generate', methods=['POST'])
def generate_design():
    """
    Generate Elementor template from description + inspirations
    """
    try:
        data = request.get_json()
        description = data.get('description', '')
        inspirations = data.get('inspirations', [])

        if not description:
            return jsonify({
                'success': False,
                'error': 'Description is required'
            }), 400

        # Parse the description into design spec
        design_spec = description_parser.parse(description, inspirations)

        # Generate Elementor template
        elementor_template = elementor_generator.generate_page(design_spec)

        # Cache the result
        cache_id = f"gen_{len(conversion_cache)}"
        conversion_cache[cache_id] = {
            'design_spec': design_spec,
            'elementor_template': elementor_template
        }

        return jsonify({
            'success': True,
            'cache_id': cache_id,
            'design_spec': design_spec,
            'elementor_template': elementor_template
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/regenerate', methods=['POST'])
def regenerate_template():
    """Regenerate template with updated design spec"""
    try:
        data = request.get_json()
        design_spec = data.get('design_spec', {})

        if not design_spec:
            return jsonify({
                'success': False,
                'error': 'Design spec is required'
            }), 400

        # Regenerate Elementor template
        elementor_template = elementor_generator.generate_page(design_spec)

        return jsonify({
            'success': True,
            'elementor_template': elementor_template
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# ============================================
# WORDPRESS CONNECTION & PUBLISHING
# ============================================

@app.route('/api/wordpress/test', methods=['POST'])
def test_wordpress():
    """Test WordPress connection"""
    try:
        data = request.get_json()
        site_url = data.get('site_url', '')
        username = data.get('username', '')
        app_password = data.get('app_password', '')

        if not all([site_url, username, app_password]):
            return jsonify({
                'success': False,
                'error': 'Missing credentials'
            }), 400

        connector = WordPressConnector(site_url, username, app_password)
        result = connector.test_connection()

        if result['success']:
            result['elementor_active'] = connector.check_elementor_active()

        return jsonify(result)

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/wordpress/publish', methods=['POST'])
def publish_to_wordpress():
    """Publish generated template to WordPress"""
    try:
        data = request.get_json()

        # WordPress credentials
        site_url = data.get('site_url', '')
        username = data.get('username', '')
        app_password = data.get('app_password', '')

        # Template data
        elementor_data = data.get('elementor_data', {})
        page_title = data.get('page_title', 'Generated Website')
        create_as = data.get('create_as', 'page')
        status = data.get('status', 'publish')

        if not all([site_url, username, app_password]):
            return jsonify({
                'success': False,
                'error': 'Missing WordPress credentials'
            }), 400

        if not elementor_data:
            return jsonify({
                'success': False,
                'error': 'No template data provided'
            }), 400

        connector = WordPressConnector(site_url, username, app_password)

        if create_as == 'template':
            result = connector.create_elementor_template(page_title, elementor_data)
        else:
            result = connector.create_page(page_title, elementor_data, status)

        return jsonify(result)

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/wordpress/pages', methods=['POST'])
def get_wordpress_pages():
    """Get list of pages from WordPress"""
    try:
        data = request.get_json()
        site_url = data.get('site_url', '')
        username = data.get('username', '')
        app_password = data.get('app_password', '')

        connector = WordPressConnector(site_url, username, app_password)
        result = connector.get_pages()

        return jsonify(result)

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# ============================================
# DOWNLOAD & UTILITY ENDPOINTS
# ============================================

@app.route('/api/download/<cache_id>', methods=['GET'])
def download_json(cache_id):
    """Download the generated Elementor JSON file"""
    if cache_id not in conversion_cache:
        return jsonify({'error': 'Template not found'}), 404

    cached = conversion_cache[cache_id]
    elementor_data = cached.get('elementor_template', cached)

    # Create temp file
    filepath = f'/tmp/elementor_template_{cache_id}.json'
    with open(filepath, 'w') as f:
        json.dump(elementor_data, f, indent=2)

    return send_file(
        filepath,
        as_attachment=True,
        download_name='elementor_template.json',
        mimetype='application/json'
    )


# Legacy endpoints for backwards compatibility
@app.route('/api/convert', methods=['POST'])
def convert_figma():
    """Legacy: Convert Figma JSON to Elementor format"""
    try:
        from parsers.figma_parser import FigmaParser
        from generators.elementor_generator import ElementorGenerator

        data = request.get_json()
        figma_data = data.get('figma_data', {})

        if not figma_data:
            return jsonify({
                'success': False,
                'error': 'No Figma data provided'
            }), 400

        parser = FigmaParser(figma_data)
        parsed = parser.parse()

        generator = ElementorGenerator(parsed)
        elementor_data = generator.generate()

        cache_id = f"figma_{len(conversion_cache)}"
        conversion_cache[cache_id] = elementor_data

        return jsonify({
            'success': True,
            'cache_id': cache_id,
            'elementor_data': elementor_data,
            'design_tokens': parsed.get('design_tokens', {}),
            'element_count': len(parsed.get('elements', []))
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/css-variables', methods=['POST'])
def generate_css_variables():
    """Generate CSS variables from design tokens"""
    try:
        data = request.get_json()
        design_tokens = data.get('design_tokens', {})

        css_lines = [':root {']

        for color, name in design_tokens.get('colors', {}).items():
            css_lines.append(f'  --color-{name}: {color};')

        for key, typo in design_tokens.get('typography', {}).items():
            safe_key = key.replace('-', '_').replace(' ', '_')
            css_lines.append(f'  --font-{safe_key}-family: {typo.get("family", "Inter")};')
            css_lines.append(f'  --font-{safe_key}-size: {typo.get("size", 16)}px;')
            css_lines.append(f'  --font-{safe_key}-weight: {typo.get("weight", 400)};')

        css_lines.append('}')

        return jsonify({
            'success': True,
            'css': '\n'.join(css_lines)
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/push', methods=['POST'])
def push_to_wordpress_legacy():
    """Legacy: Push converted template to WordPress"""
    try:
        data = request.get_json()

        site_url = data.get('site_url', '')
        username = data.get('username', '')
        app_password = data.get('app_password', '')
        cache_id = data.get('cache_id', '')
        page_title = data.get('page_title', 'Imported from Figma')
        create_as = data.get('create_as', 'page')
        status = data.get('status', 'draft')

        if not all([site_url, username, app_password, cache_id]):
            return jsonify({
                'success': False,
                'error': 'Missing required fields'
            }), 400

        if cache_id not in conversion_cache:
            return jsonify({
                'success': False,
                'error': 'Conversion not found. Please convert again.'
            }), 404

        cached = conversion_cache[cache_id]
        elementor_data = cached.get('elementor_template', cached)

        connector = WordPressConnector(site_url, username, app_password)

        if create_as == 'template':
            result = connector.create_elementor_template(page_title, elementor_data)
        else:
            result = connector.create_page(page_title, elementor_data, status)

        return jsonify(result)

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
