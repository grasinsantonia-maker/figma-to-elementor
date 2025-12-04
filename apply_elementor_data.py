#!/usr/bin/env python3
"""
Apply Elementor data to WordPress page via REST API
"""

import requests
import json
from requests.auth import HTTPBasicAuth

# WordPress credentials
WP_URL = "https://wordpress-1097675-6048787.cloudwaysapps.com"
USERNAME = "grasinsantonia@gmail.com"
APP_PASSWORD = "7Fbg xKjQ fdKi JCNk JQIv ESxr"
PAGE_ID = 97

# Load the Elementor template
with open('/Users/antoniasepulvedagrasins/figma-to-elementor/output_elementor_template.json', 'r') as f:
    template_data = json.load(f)

# Extract just the content array for Elementor
elementor_data = template_data['content']

# Create auth
auth = HTTPBasicAuth(USERNAME, APP_PASSWORD)

# First, let's update the page template to Elementor Canvas
print("Step 1: Updating page template to Elementor Canvas...")
page_update = {
    "template": "elementor_canvas",
    "status": "publish",
    "meta": {
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "wp-page",
        "_elementor_version": "3.25.0",
        "_elementor_data": json.dumps(elementor_data)
    }
}

response = requests.post(
    f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
    json=page_update,
    auth=auth,
    headers={"Content-Type": "application/json"}
)

print(f"Page update response: {response.status_code}")
if response.status_code == 200:
    print("Page updated successfully!")
    print(f"Edit URL: {WP_URL}/wp-admin/post.php?post={PAGE_ID}&action=elementor")
else:
    print(f"Error: {response.text}")

# Try alternative approach - create Elementor Library template
print("\nStep 2: Creating Elementor Library template...")

# Create a library template post
library_template = {
    "title": "Figma Landing Page",
    "status": "publish",
    "type": "elementor_library",
    "meta": {
        "_elementor_edit_mode": "builder",
        "_elementor_template_type": "page",
        "_elementor_version": "3.25.0",
        "_elementor_data": json.dumps(elementor_data)
    }
}

# Try using elementor_library post type endpoint
response = requests.get(
    f"{WP_URL}/wp-json/wp/v2/types",
    auth=auth
)
print(f"Available post types: {response.status_code}")
if response.status_code == 200:
    types = response.json()
    if 'elementor_library' in types:
        print("Elementor Library post type exists!")
        library_endpoint = types['elementor_library']['rest_base']
        print(f"Library endpoint: {library_endpoint}")

        # Create library template
        response = requests.post(
            f"{WP_URL}/wp-json/wp/v2/{library_endpoint}",
            json=library_template,
            auth=auth,
            headers={"Content-Type": "application/json"}
        )
        print(f"Library template creation: {response.status_code}")
        if response.status_code == 201:
            lib_data = response.json()
            print(f"Library template created! ID: {lib_data.get('id')}")
        else:
            print(f"Error: {response.text[:500]}")

# Final step - verify page state
print("\nStep 3: Verifying page state...")
response = requests.get(
    f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
    auth=auth
)
if response.status_code == 200:
    page = response.json()
    print(f"Page Title: {page.get('title', {}).get('rendered')}")
    print(f"Page Template: {page.get('template')}")
    print(f"Page Status: {page.get('status')}")
    print(f"\nView Page: {page.get('link')}")
    print(f"Edit in Elementor: {WP_URL}/wp-admin/post.php?post={PAGE_ID}&action=elementor")
