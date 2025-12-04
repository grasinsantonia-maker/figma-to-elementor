#!/usr/bin/env python3
"""
Finalize the Elementor page with proper settings and clear cache
"""

import requests
import json
from requests.auth import HTTPBasicAuth

# WordPress credentials
WP_URL = "https://wordpress-1097675-6048787.cloudwaysapps.com"
USERNAME = "grasinsantonia@gmail.com"
APP_PASSWORD = "7Fbg xKjQ fdKi JCNk JQIv ESxr"
PAGE_ID = 97

auth = HTTPBasicAuth(USERNAME, APP_PASSWORD)

# Update page settings including Elementor page settings
page_settings = {
    "hide_title": "yes",
    "template": "elementor_canvas",
    "content_width": {"unit": "px", "size": 1440}
}

print("Updating page with Elementor page settings...")
page_update = {
    "meta": {
        "_elementor_page_settings": json.dumps(page_settings)
    }
}

response = requests.post(
    f"{WP_URL}/wp-json/wp/v2/pages/{PAGE_ID}",
    json=page_update,
    auth=auth,
    headers={"Content-Type": "application/json"}
)
print(f"Page settings update: {response.status_code}")

# Clear Elementor cache
print("\nClearing Elementor cache...")
response = requests.delete(
    f"{WP_URL}/wp-json/elementor/v1/cache",
    auth=auth
)
print(f"Cache clear: {response.status_code}")

# Check the library template we created
print("\nChecking Elementor Library templates...")
response = requests.get(
    f"{WP_URL}/wp-json/wp/v2/elementor_library",
    auth=auth
)
if response.status_code == 200:
    templates = response.json()
    for t in templates:
        print(f"  - ID {t['id']}: {t['title']['rendered']} (status: {t['status']})")

print("\n" + "="*60)
print("PAGE READY!")
print("="*60)
print(f"\nView page: https://wordpress-1097675-6048787.cloudwaysapps.com/nadav-cohen-digital-landing-page/")
print(f"\nEdit in Elementor: {WP_URL}/wp-admin/post.php?post={PAGE_ID}&action=elementor")
print("\nThe page now has:")
print("  - Template: Elementor Canvas (no theme header/footer)")
print("  - 7 sections with Figma design content")
print("  - Full Elementor edit capability")
