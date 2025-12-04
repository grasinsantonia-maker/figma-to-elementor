"""
Figma to Elementor Converter - Flask Web Application
"""

import os
import json
from flask import Flask, render_template, request, jsonify, send_file
from dotenv import load_dotenv

from parsers.figma_parser import FigmaParser
from generators.elementor_generator import ElementorGenerator
from connectors.wordpress_connector import WordPressConnector

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.environ.get('SECRET_KEY', 'figma-to-elementor-secret')

# Store session data (in production, use proper session/database)
conversion_cache = {}


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/convert', methods=['POST'])
def convert_figma():
    """
    Convert Figma JSON to Elementor format.

    Expects JSON body with:
    - figma_data: The Figma node data (from MCP or API)
    """
    try:
        data = request.get_json()
        figma_data = data.get('figma_data', {})

        if not figma_data:
            return jsonify({
                'success': False,
                'error': 'No Figma data provided'
            }), 400

        # Parse Figma data
        parser = FigmaParser(figma_data)
        parsed = parser.parse()

        # Generate Elementor JSON
        generator = ElementorGenerator(parsed)
        elementor_data = generator.generate()

        # Cache the result
        cache_id = f"conv_{len(conversion_cache)}"
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


@app.route('/api/download/<cache_id>', methods=['GET'])
def download_json(cache_id):
    """Download the converted Elementor JSON file"""
    if cache_id not in conversion_cache:
        return jsonify({'error': 'Conversion not found'}), 404

    elementor_data = conversion_cache[cache_id]

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


@app.route('/api/wordpress/push', methods=['POST'])
def push_to_wordpress():
    """Push converted template to WordPress"""
    try:
        data = request.get_json()

        # WordPress credentials
        site_url = data.get('site_url', '')
        username = data.get('username', '')
        app_password = data.get('app_password', '')

        # Template data
        cache_id = data.get('cache_id', '')
        page_title = data.get('page_title', 'Imported from Figma')
        create_as = data.get('create_as', 'page')  # 'page' or 'template'
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

        elementor_data = conversion_cache[cache_id]
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


# CSS Variables generator endpoint
@app.route('/api/css-variables', methods=['POST'])
def generate_css_variables():
    """Generate CSS variables from design tokens"""
    try:
        data = request.get_json()
        design_tokens = data.get('design_tokens', {})

        css_lines = [':root {']

        # Colors
        for color, name in design_tokens.get('colors', {}).items():
            css_lines.append(f'  --color-{name}: {color};')

        # Typography
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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
