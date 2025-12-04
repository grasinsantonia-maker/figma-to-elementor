"""
WordPress REST API Connector - Push Elementor templates to WordPress
"""

import requests
import base64
import json
from typing import Optional, Dict, Any


class WordPressConnector:
    """Connect to WordPress REST API and push Elementor templates"""

    def __init__(self, site_url: str, username: str, app_password: str):
        """
        Initialize the WordPress connector.

        Args:
            site_url: WordPress site URL (e.g., https://example.com)
            username: WordPress username
            app_password: WordPress Application Password (not regular password)
        """
        self.site_url = site_url.rstrip('/')
        self.api_base = f"{self.site_url}/wp-json"
        self.username = username
        self.app_password = app_password
        self._auth_header = self._create_auth_header()

    def _create_auth_header(self) -> str:
        """Create Basic Auth header from credentials"""
        credentials = f"{self.username}:{self.app_password}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded}"

    def _get_headers(self) -> dict:
        """Get headers for API requests"""
        return {
            "Authorization": self._auth_header,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def test_connection(self) -> dict:
        """Test the WordPress connection and return user info"""
        try:
            response = requests.get(
                f"{self.api_base}/wp/v2/users/me",
                headers=self._get_headers(),
                timeout=10
            )

            if response.status_code == 200:
                user = response.json()
                return {
                    "success": True,
                    "message": f"Connected as {user.get('name', 'Unknown')}",
                    "user": user
                }
            else:
                return {
                    "success": False,
                    "message": f"Authentication failed: {response.status_code}",
                    "error": response.text
                }
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "message": f"Connection error: {str(e)}",
                "error": str(e)
            }

    def check_elementor_active(self) -> bool:
        """Check if Elementor is active on the WordPress site"""
        try:
            # Try to access Elementor-specific endpoint
            response = requests.get(
                f"{self.api_base}/elementor/v1/globals",
                headers=self._get_headers(),
                timeout=10
            )
            return response.status_code in [200, 401, 403]  # Exists but may need auth
        except:
            return False

    def create_page(self, title: str, elementor_data: dict, status: str = "draft") -> dict:
        """
        Create a new WordPress page with Elementor content.

        Args:
            title: Page title
            elementor_data: Elementor JSON content
            status: 'draft', 'publish', or 'private'

        Returns:
            Result dictionary with success status and page info
        """
        # Prepare page data
        page_data = {
            "title": title,
            "status": status,
            "content": "",  # Elementor takes over content
            "meta": {
                "_elementor_edit_mode": "builder",
                "_elementor_template_type": "wp-page",
                "_elementor_version": "3.18.0",
                "_elementor_data": json.dumps(elementor_data.get("content", []))
            }
        }

        try:
            response = requests.post(
                f"{self.api_base}/wp/v2/pages",
                headers=self._get_headers(),
                json=page_data,
                timeout=30
            )

            if response.status_code in [200, 201]:
                page = response.json()
                return {
                    "success": True,
                    "message": f"Page created successfully",
                    "page_id": page.get("id"),
                    "page_url": page.get("link"),
                    "edit_url": f"{self.site_url}/wp-admin/post.php?post={page.get('id')}&action=elementor"
                }
            else:
                return {
                    "success": False,
                    "message": f"Failed to create page: {response.status_code}",
                    "error": response.text
                }
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "message": f"Request error: {str(e)}",
                "error": str(e)
            }

    def update_page(self, page_id: int, elementor_data: dict) -> dict:
        """
        Update an existing page with new Elementor content.

        Args:
            page_id: WordPress page ID
            elementor_data: New Elementor JSON content

        Returns:
            Result dictionary
        """
        page_data = {
            "meta": {
                "_elementor_data": json.dumps(elementor_data.get("content", []))
            }
        }

        try:
            response = requests.post(
                f"{self.api_base}/wp/v2/pages/{page_id}",
                headers=self._get_headers(),
                json=page_data,
                timeout=30
            )

            if response.status_code == 200:
                page = response.json()
                return {
                    "success": True,
                    "message": "Page updated successfully",
                    "page_id": page_id,
                    "edit_url": f"{self.site_url}/wp-admin/post.php?post={page_id}&action=elementor"
                }
            else:
                return {
                    "success": False,
                    "message": f"Failed to update page: {response.status_code}",
                    "error": response.text
                }
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "message": f"Request error: {str(e)}",
                "error": str(e)
            }

    def create_elementor_template(self, title: str, elementor_data: dict, template_type: str = "page") -> dict:
        """
        Create an Elementor template (saved in Library).

        Args:
            title: Template title
            elementor_data: Elementor JSON content
            template_type: 'page', 'section', 'header', 'footer', etc.

        Returns:
            Result dictionary
        """
        template_data = {
            "title": title,
            "status": "publish",
            "type": "elementor_library",
            "meta": {
                "_elementor_edit_mode": "builder",
                "_elementor_template_type": template_type,
                "_elementor_version": "3.18.0",
                "_elementor_data": json.dumps(elementor_data.get("content", []))
            }
        }

        try:
            # Elementor templates use a custom post type
            response = requests.post(
                f"{self.api_base}/wp/v2/elementor_library",
                headers=self._get_headers(),
                json=template_data,
                timeout=30
            )

            if response.status_code in [200, 201]:
                template = response.json()
                return {
                    "success": True,
                    "message": "Template created successfully",
                    "template_id": template.get("id"),
                    "edit_url": f"{self.site_url}/wp-admin/post.php?post={template.get('id')}&action=elementor"
                }
            else:
                return {
                    "success": False,
                    "message": f"Failed to create template: {response.status_code}",
                    "error": response.text
                }
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "message": f"Request error: {str(e)}",
                "error": str(e)
            }

    def upload_media(self, file_path: str, filename: str) -> dict:
        """
        Upload an image to WordPress media library.

        Args:
            file_path: Local path to the image file
            filename: Desired filename in WordPress

        Returns:
            Result dictionary with media URL
        """
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()

            headers = {
                "Authorization": self._auth_header,
                "Content-Disposition": f'attachment; filename="{filename}"',
                "Content-Type": "image/png"  # Adjust based on file type
            }

            response = requests.post(
                f"{self.api_base}/wp/v2/media",
                headers=headers,
                data=file_content,
                timeout=60
            )

            if response.status_code in [200, 201]:
                media = response.json()
                return {
                    "success": True,
                    "message": "Media uploaded successfully",
                    "media_id": media.get("id"),
                    "url": media.get("source_url"),
                    "sizes": media.get("media_details", {}).get("sizes", {})
                }
            else:
                return {
                    "success": False,
                    "message": f"Failed to upload media: {response.status_code}",
                    "error": response.text
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"Upload error: {str(e)}",
                "error": str(e)
            }

    def get_pages(self, per_page: int = 20) -> dict:
        """Get list of pages from WordPress"""
        try:
            response = requests.get(
                f"{self.api_base}/wp/v2/pages",
                headers=self._get_headers(),
                params={"per_page": per_page},
                timeout=10
            )

            if response.status_code == 200:
                return {
                    "success": True,
                    "pages": response.json()
                }
            else:
                return {
                    "success": False,
                    "error": response.text
                }
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e)
            }
