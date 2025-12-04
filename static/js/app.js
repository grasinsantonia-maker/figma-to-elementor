// Figma to Elementor Converter - Frontend JavaScript

let currentCacheId = null;
let currentElementorData = null;
let currentDesignTokens = null;

// Convert Figma JSON to Elementor
async function convertFigma() {
    const figmaJson = document.getElementById('figma-json').value.trim();

    if (!figmaJson) {
        alert('Please paste Figma JSON data');
        return;
    }

    let figmaData;
    try {
        figmaData = JSON.parse(figmaJson);
    } catch (e) {
        alert('Invalid JSON format. Please check your input.');
        return;
    }

    try {
        const response = await fetch('/api/convert', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ figma_data: figmaData })
        });

        const result = await response.json();

        if (result.success) {
            currentCacheId = result.cache_id;
            currentElementorData = result.elementor_data;
            currentDesignTokens = result.design_tokens;

            // Update stats
            document.getElementById('element-count').textContent = result.element_count;
            document.getElementById('color-count').textContent =
                Object.keys(result.design_tokens.colors || {}).length;
            document.getElementById('font-count').textContent =
                Object.keys(result.design_tokens.typography || {}).length;

            // Show preview
            document.getElementById('elementor-preview').textContent =
                JSON.stringify(result.elementor_data, null, 2);

            // Generate CSS variables
            await generateCSSVariables();

            // Show preview section
            document.getElementById('step-preview').classList.remove('hidden');

            // Scroll to preview
            document.getElementById('step-preview').scrollIntoView({ behavior: 'smooth' });
        } else {
            alert('Conversion failed: ' + result.error);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

// Generate CSS Variables
async function generateCSSVariables() {
    if (!currentDesignTokens) return;

    try {
        const response = await fetch('/api/css-variables', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ design_tokens: currentDesignTokens })
        });

        const result = await response.json();
        if (result.success) {
            document.getElementById('css-preview').textContent = result.css;
        }
    } catch (error) {
        console.error('CSS generation error:', error);
    }
}

// Tab switching
function showTab(tabId) {
    // Update tab buttons
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
    event.target.classList.add('active');

    // Update tab content
    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
    document.getElementById(tabId).classList.add('active');
}

// Download JSON
function downloadJSON() {
    if (!currentCacheId) {
        alert('No conversion available. Please convert first.');
        return;
    }

    window.location.href = `/api/download/${currentCacheId}`;
}

// Show WordPress connection section
function showWordPressConnect() {
    document.getElementById('step-wordpress').classList.remove('hidden');
    document.getElementById('step-wordpress').scrollIntoView({ behavior: 'smooth' });
}

// Test WordPress connection
async function testWordPress() {
    const siteUrl = document.getElementById('wp-url').value.trim();
    const username = document.getElementById('wp-username').value.trim();
    const appPassword = document.getElementById('wp-password').value.trim();

    if (!siteUrl || !username || !appPassword) {
        showStatus('wp-status', 'error', 'Please fill in all fields');
        return;
    }

    try {
        const response = await fetch('/api/wordpress/test', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                site_url: siteUrl,
                username: username,
                app_password: appPassword
            })
        });

        const result = await response.json();

        if (result.success) {
            let message = result.message;
            if (result.elementor_active) {
                message += ' | Elementor detected!';
            } else {
                message += ' | Warning: Elementor not detected';
            }
            showStatus('wp-status', 'success', message);
        } else {
            showStatus('wp-status', 'error', result.message || result.error);
        }
    } catch (error) {
        showStatus('wp-status', 'error', 'Connection error: ' + error.message);
    }
}

// Push to WordPress
async function pushToWordPress() {
    if (!currentCacheId) {
        alert('No conversion available. Please convert first.');
        return;
    }

    const siteUrl = document.getElementById('wp-url').value.trim();
    const username = document.getElementById('wp-username').value.trim();
    const appPassword = document.getElementById('wp-password').value.trim();
    const pageTitle = document.getElementById('page-title').value.trim() || 'Imported from Figma';
    const createAs = document.querySelector('input[name="create-as"]:checked').value;
    const status = document.querySelector('input[name="status"]:checked').value;

    if (!siteUrl || !username || !appPassword) {
        showStatus('push-status', 'error', 'Please fill in WordPress credentials');
        return;
    }

    try {
        const response = await fetch('/api/wordpress/push', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                site_url: siteUrl,
                username: username,
                app_password: appPassword,
                cache_id: currentCacheId,
                page_title: pageTitle,
                create_as: createAs,
                status: status
            })
        });

        const result = await response.json();

        if (result.success) {
            let message = result.message;
            if (result.edit_url) {
                message += ` <a href="${result.edit_url}" target="_blank">Open in Elementor</a>`;
            }
            showStatus('push-status', 'success', message);
        } else {
            showStatus('push-status', 'error', result.message || result.error);
        }
    } catch (error) {
        showStatus('push-status', 'error', 'Push error: ' + error.message);
    }
}

// Show status message
function showStatus(elementId, type, message) {
    const statusEl = document.getElementById(elementId);
    statusEl.className = `status ${type}`;
    statusEl.innerHTML = message;
    statusEl.classList.remove('hidden');
}
