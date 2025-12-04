// WebBuilder AI - 4-Step Wizard JavaScript

// Global state
let currentStep = 1;
let designSpec = null;
let analyzedSites = [];
let generatedTemplate = null;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    initDescriptionInput();
    initChips();
    initNavigation();
    updateConnectionStatus();
});

// ============================================
// STEP NAVIGATION
// ============================================

function goToStep(step) {
    // Update panels
    document.querySelectorAll('.step-panel').forEach(panel => {
        panel.classList.remove('active');
    });
    document.getElementById(`step-${step}`).classList.add('active');

    // Update navigation
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        const itemStep = parseInt(item.dataset.step);
        if (itemStep < step) {
            item.classList.add('completed');
        } else {
            item.classList.remove('completed');
        }
    });
    document.querySelector(`.nav-item[data-step="${step}"]`).classList.add('active');

    currentStep = step;

    // Trigger step-specific actions
    if (step === 3) {
        updatePreviewJSON();
    }
}

function initNavigation() {
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const step = parseInt(this.dataset.step);
            goToStep(step);
        });
    });
}

// ============================================
// STEP 1: DESCRIPTION INPUT
// ============================================

function initDescriptionInput() {
    const textarea = document.getElementById('description-input');
    const charCount = document.getElementById('char-count');

    if (textarea && charCount) {
        textarea.addEventListener('input', function() {
            charCount.textContent = this.value.length;
        });
    }
}

function initChips() {
    document.querySelectorAll('.chip').forEach(chip => {
        chip.addEventListener('click', function() {
            this.classList.toggle('active');
            updateDescriptionWithChips();
        });
    });
}

function updateDescriptionWithChips() {
    const textarea = document.getElementById('description-input');
    const activeChips = document.querySelectorAll('.chip.active');

    if (activeChips.length > 0) {
        const sections = Array.from(activeChips).map(c => c.dataset.section);
        const currentText = textarea.value;

        // Check if sections are already mentioned
        const sectionMentions = sections.filter(s =>
            !currentText.toLowerCase().includes(s.toLowerCase())
        );

        if (sectionMentions.length > 0) {
            const addText = `\n\nInclude sections: ${sectionMentions.join(', ')}.`;
            if (!currentText.includes('Include sections:')) {
                textarea.value = currentText + addText;
            }
        }

        document.getElementById('char-count').textContent = textarea.value.length;
    }
}

// ============================================
// STEP 2: INSPIRATION SITES
// ============================================

function addInspirationField() {
    const list = document.getElementById('inspiration-list');
    const newItem = document.createElement('div');
    newItem.className = 'inspiration-item';
    newItem.innerHTML = `
        <input type="url" class="inspiration-url" placeholder="https://example.com">
        <button class="btn btn-icon btn-analyze" onclick="analyzeSite(this)">
            <span class="spinner hidden"></span>
            <span class="btn-text">Analyze</span>
        </button>
        <div class="analysis-result hidden"></div>
    `;
    list.appendChild(newItem);
}

async function analyzeSite(button) {
    const item = button.closest('.inspiration-item');
    const urlInput = item.querySelector('.inspiration-url');
    const resultDiv = item.querySelector('.analysis-result');
    const spinner = button.querySelector('.spinner');
    const btnText = button.querySelector('.btn-text');

    const url = urlInput.value.trim();
    if (!url) {
        showResult(resultDiv, 'error', 'Please enter a URL');
        return;
    }

    // Show loading
    spinner.classList.remove('hidden');
    btnText.textContent = 'Analyzing...';
    button.disabled = true;

    try {
        const response = await fetch('/api/analyze-site', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url })
        });

        const result = await response.json();

        if (result.success) {
            analyzedSites.push(result.analysis);
            showResult(resultDiv, 'success',
                `✓ Found ${result.analysis.colors.all_colors.length} colors, ` +
                `${result.analysis.typography.fonts.length} fonts, ` +
                `${result.analysis.structure.sections_order.length} sections`
            );
            updateAnalysisSummary();
        } else {
            showResult(resultDiv, 'error', result.error || 'Analysis failed');
        }
    } catch (error) {
        showResult(resultDiv, 'error', 'Network error: ' + error.message);
    }

    // Hide loading
    spinner.classList.add('hidden');
    btnText.textContent = 'Analyze';
    button.disabled = false;
}

function showResult(element, type, message) {
    element.className = `analysis-result ${type}`;
    element.textContent = message;
    element.classList.remove('hidden');
}

function updateAnalysisSummary() {
    if (analyzedSites.length === 0) return;

    const summary = document.getElementById('analysis-summary');
    summary.classList.remove('hidden');

    // Collect all colors
    const allColors = [];
    const allFonts = [];
    const allSections = [];

    analyzedSites.forEach(site => {
        allColors.push(...(site.colors.all_colors || []));
        allFonts.push(...(site.typography.fonts || []));
        allSections.push(...(site.structure.sections_order || []));
    });

    // Unique colors (top 6)
    const uniqueColors = [...new Set(allColors)].slice(0, 6);
    const colorsDiv = document.getElementById('common-colors');
    colorsDiv.innerHTML = uniqueColors.map(c =>
        `<div class="color-swatch" style="background: ${c};" title="${c}"></div>`
    ).join('');

    // Unique fonts
    const uniqueFonts = [...new Set(allFonts)].slice(0, 4);
    document.getElementById('common-fonts').innerHTML =
        uniqueFonts.map(f => `<div>${f}</div>`).join('');

    // Common sections
    const sectionCounts = {};
    allSections.forEach(s => sectionCounts[s] = (sectionCounts[s] || 0) + 1);
    const topSections = Object.entries(sectionCounts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5)
        .map(([s]) => s);

    document.getElementById('recommended-sections').innerHTML =
        topSections.map(s => `<div>${s.charAt(0).toUpperCase() + s.slice(1)}</div>`).join('');
}

// ============================================
// GENERATE DESIGN
// ============================================

async function generateDesign() {
    const description = document.getElementById('description-input').value.trim();

    if (!description) {
        alert('Please enter a description of your website');
        return;
    }

    const spinner = document.getElementById('generate-spinner');
    const btnText = document.getElementById('generate-text');

    spinner.classList.remove('hidden');
    btnText.textContent = 'Generating...';

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                description: description,
                inspirations: analyzedSites
            })
        });

        const result = await response.json();

        if (result.success) {
            designSpec = result.design_spec;
            generatedTemplate = result.elementor_template;

            // Update customization UI
            updateCustomizationUI();

            // Go to step 3
            goToStep(3);
        } else {
            alert('Generation failed: ' + (result.error || 'Unknown error'));
        }
    } catch (error) {
        alert('Network error: ' + error.message);
    }

    spinner.classList.add('hidden');
    btnText.textContent = 'Generate Design →';
}

// ============================================
// STEP 3: CUSTOMIZATION
// ============================================

function updateCustomizationUI() {
    if (!designSpec) return;

    // Update color pickers
    if (designSpec.colors) {
        if (designSpec.colors.primary) {
            document.getElementById('color-primary').value = designSpec.colors.primary;
        }
        if (designSpec.colors.secondary) {
            document.getElementById('color-secondary').value = designSpec.colors.secondary;
        }
        if (designSpec.colors.accent) {
            document.getElementById('color-accent').value = designSpec.colors.accent;
        }
        if (designSpec.colors.background) {
            document.getElementById('color-background').value = designSpec.colors.background;
        }
    }

    // Update font select
    if (designSpec.fonts && designSpec.fonts.primary) {
        const fontSelect = document.getElementById('font-select');
        const fontName = designSpec.fonts.primary;
        for (let option of fontSelect.options) {
            if (option.value.toLowerCase() === fontName.toLowerCase()) {
                fontSelect.value = option.value;
                break;
            }
        }
    }

    // Update button style
    if (designSpec.button_style) {
        const style = designSpec.button_style;
        const radio = document.querySelector(`input[name="button-style"][value="${style}"]`);
        if (radio) radio.checked = true;
    }

    // Update sections list
    updateSectionsList();

    // Update preview
    updatePreviewJSON();
}

function updateSectionsList() {
    const container = document.getElementById('section-list');
    if (!designSpec || !designSpec.sections) return;

    container.innerHTML = designSpec.sections.map((section, index) => `
        <div class="section-item" draggable="true" data-index="${index}">
            <span class="drag-handle">⋮⋮</span>
            <span class="section-name">${section.type.charAt(0).toUpperCase() + section.type.slice(1)}</span>
            <input type="checkbox" class="section-toggle" checked>
        </div>
    `).join('');

    // Initialize drag and drop
    initDragAndDrop();
}

function initDragAndDrop() {
    const items = document.querySelectorAll('.section-item');
    let draggedItem = null;

    items.forEach(item => {
        item.addEventListener('dragstart', function() {
            draggedItem = this;
            this.classList.add('dragging');
        });

        item.addEventListener('dragend', function() {
            this.classList.remove('dragging');
            reorderSections();
        });

        item.addEventListener('dragover', function(e) {
            e.preventDefault();
            const afterElement = getDragAfterElement(document.getElementById('section-list'), e.clientY);
            const container = document.getElementById('section-list');
            if (afterElement == null) {
                container.appendChild(draggedItem);
            } else {
                container.insertBefore(draggedItem, afterElement);
            }
        });
    });
}

function getDragAfterElement(container, y) {
    const draggableElements = [...container.querySelectorAll('.section-item:not(.dragging)')];

    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const offset = y - box.top - box.height / 2;
        if (offset < 0 && offset > closest.offset) {
            return { offset: offset, element: child };
        } else {
            return closest;
        }
    }, { offset: Number.NEGATIVE_INFINITY }).element;
}

function reorderSections() {
    const items = document.querySelectorAll('.section-item');
    const newOrder = [];

    items.forEach((item, newIndex) => {
        const oldIndex = parseInt(item.dataset.index);
        newOrder.push(designSpec.sections[oldIndex]);
        item.dataset.index = newIndex;
    });

    designSpec.sections = newOrder;
    regenerateTemplate();
}

function regenerateTemplate() {
    // Get updated values from UI
    designSpec.colors = {
        primary: document.getElementById('color-primary').value,
        secondary: document.getElementById('color-secondary').value,
        accent: document.getElementById('color-accent').value,
        background: document.getElementById('color-background').value
    };
    designSpec.fonts = {
        primary: document.getElementById('font-select').value
    };
    designSpec.button_style = document.querySelector('input[name="button-style"]:checked').value;

    // Regenerate template with new settings
    fetch('/api/regenerate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ design_spec: designSpec })
    })
    .then(res => res.json())
    .then(result => {
        if (result.success) {
            generatedTemplate = result.elementor_template;
            updatePreviewJSON();
        }
    })
    .catch(console.error);
}

function updatePreviewJSON() {
    const preview = document.getElementById('preview-json');
    if (preview && generatedTemplate) {
        preview.textContent = JSON.stringify(generatedTemplate, null, 2);
    }
}

function downloadTemplate() {
    if (!generatedTemplate) {
        alert('No template generated yet');
        return;
    }

    const blob = new Blob([JSON.stringify(generatedTemplate, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'elementor-template.json';
    a.click();
    URL.revokeObjectURL(url);
}

// ============================================
// STEP 4: WORDPRESS PUBLISH
// ============================================

async function testConnection() {
    const spinner = document.getElementById('test-spinner');
    const result = document.getElementById('connection-result');

    const siteUrl = document.getElementById('wp-url').value.trim();
    const username = document.getElementById('wp-username').value.trim();
    const password = document.getElementById('wp-password').value.trim();

    if (!siteUrl || !username || !password) {
        showConnectionResult(result, 'error', 'Please fill in all credentials');
        return;
    }

    spinner.classList.remove('hidden');

    try {
        const response = await fetch('/api/wordpress/test', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                site_url: siteUrl,
                username: username,
                app_password: password
            })
        });

        const data = await response.json();

        if (data.success) {
            let message = '✓ Connected successfully!';
            if (data.elementor_active) {
                message += ' Elementor Pro detected.';
            }
            showConnectionResult(result, 'success', message);
            updateConnectionStatus(true);
        } else {
            showConnectionResult(result, 'error', data.error || 'Connection failed');
            updateConnectionStatus(false);
        }
    } catch (error) {
        showConnectionResult(result, 'error', 'Network error: ' + error.message);
        updateConnectionStatus(false);
    }

    spinner.classList.add('hidden');
}

function showConnectionResult(element, type, message) {
    element.className = `connection-result ${type}`;
    element.textContent = message;
    element.classList.remove('hidden');
}

function updateConnectionStatus(connected = null) {
    const dot = document.querySelector('.status-dot');
    const text = document.querySelector('.status-text');

    if (connected === true) {
        dot.classList.remove('disconnected');
        text.textContent = 'WordPress Connected';
    } else if (connected === false) {
        dot.classList.add('disconnected');
        text.textContent = 'Not Connected';
    }
}

async function publishToWordPress() {
    if (!generatedTemplate) {
        alert('Please generate a design first');
        return;
    }

    const spinner = document.getElementById('publish-spinner');
    const btnText = document.getElementById('publish-text');
    const result = document.getElementById('publish-result');

    const siteUrl = document.getElementById('wp-url').value.trim();
    const username = document.getElementById('wp-username').value.trim();
    const password = document.getElementById('wp-password').value.trim();
    const pageTitle = document.getElementById('page-title').value.trim() || 'Generated Website';
    const createType = document.getElementById('create-type').value;
    const status = document.getElementById('page-status').value;

    if (!siteUrl || !username || !password) {
        alert('Please fill in WordPress credentials');
        return;
    }

    spinner.classList.remove('hidden');
    btnText.textContent = 'Publishing...';

    try {
        const response = await fetch('/api/wordpress/publish', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                site_url: siteUrl,
                username: username,
                app_password: password,
                page_title: pageTitle,
                create_as: createType,
                status: status,
                elementor_data: generatedTemplate
            })
        });

        const data = await response.json();

        if (data.success) {
            result.classList.remove('hidden');
            document.getElementById('view-page-link').href = data.page_url || '#';
            document.getElementById('edit-elementor-link').href = data.edit_url || '#';
        } else {
            alert('Publishing failed: ' + (data.error || 'Unknown error'));
        }
    } catch (error) {
        alert('Network error: ' + error.message);
    }

    spinner.classList.add('hidden');
    btnText.textContent = '🚀 Publish Now';
}

// ============================================
// COLOR PICKER LISTENERS
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Add listeners to color pickers and other customization inputs
    ['color-primary', 'color-secondary', 'color-accent', 'color-background'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('change', regenerateTemplate);
        }
    });

    const fontSelect = document.getElementById('font-select');
    if (fontSelect) {
        fontSelect.addEventListener('change', regenerateTemplate);
    }

    document.querySelectorAll('input[name="button-style"]').forEach(radio => {
        radio.addEventListener('change', regenerateTemplate);
    });
});
