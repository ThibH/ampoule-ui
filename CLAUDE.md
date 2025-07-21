# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django component library built with **Django Cotton**, **Tailwind CSS 4.x**, **DaisyUI**, **HTMX**, and **JavaScript** (with minimal Alpine.js). The project provides reusable UI components for Django applications through a clean component-based architecture.

## Architecture

### Core Structure
- **`django_components_ui/`** - Main Python package containing components and assets
- **`demo_project/`** - Django project for demonstrations and documentation
- **`demo_project/demo/`** - Demo app with examples and documentation

### Component System
Components are built using **Django Cotton** and located in `django_components_ui/templates/cotton/`. Usage pattern:
```html
<c-button variant="primary" size="lg">Click me</c-button>
<c-text variant="subtle" color="blue-500">Subtle text</c-text>
```

### Styling Architecture
- **Source**: `django_components_ui/static/django_components_ui/css/input.css` (Tailwind source - add custom CSS here)
- **Output**: `django_components_ui/static/django_components_ui/css/components.css` (auto-generated - DO NOT EDIT)
- **Framework**: Tailwind CSS 4.x + DaisyUI with 30+ themes
- **Build**: Tailwind CLI handles compilation

### JavaScript Stack
- **HTMX**: Server-side dynamic interactions
- **Vanilla JavaScript**: Core component functionality (filters, tables, tabs, sliders)
- **Alpine.js**: Minimal usage for complex state management (toasts, smart navbar themes)
- **Core utilities**: `django_components_ui/static/django_components_ui/js/components.js`

## Development Commands

### Installation (for users)
```bash
pip install django-components-ui              # Install package with dependencies
```

Then add to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django_cotton',           # Required dependency  
    'django_components_ui',    # This package
]
```

Include in templates:
```html
{% include "init-components.html" %}  # Includes all CSS/JS assets
```

### Development Setup (for contributors)
```bash
npm install                                    # Install Node dependencies
npm run build                                  # Build CSS assets
cd demo_project && python -m venv venv        # Create virtual environment
source venv/bin/activate                      # Activate venv (Linux/Mac)
pip install -e ..                             # Install package in dev mode
python manage.py runserver                    # Start Django server
```

### CSS Development
```bash
npm run dev         # Watch mode for CSS development
npm run build       # Production build (minified)
```

### Django Development
```bash
cd demo_project
python manage.py runserver                    # Start development server
python manage.py test                         # Run tests
```

### Creating New Components
1. Create template in `django_components_ui/templates/cotton/[component].html`
2. Add CSS styles to `django_components_ui/static/django_components_ui/css/components.css` if needed
3. Run `npm run build` to recompile CSS
4. Test in `demo_project/demo/`

## Key Configuration Files

- **`package.json`** - Node.js dependencies and build scripts
- **`tailwind.config.js`** - Tailwind CSS configuration with DaisyUI
- **`demo_project/demo_project/settings.py`** - Django settings with required apps
- **`django_components_ui/templates/init-components.html`** - Required includes for CSS/JS

## Required Django Apps
```python
INSTALLED_APPS = [
    'django_cotton',           # Component system
    'django_components_ui',    # This package
]
```

## Component Development Patterns

### Template Structure
Components use `<c-vars>` for default props and support slots:
```html
<c-vars variant="default" size="md" />
<element class="component-{{ variant }} {{ class }}" {{ attrs }}>
    {{ slot }}
</element>
```

**Important Django Template Syntax Notes**: 
- Django templates don't support complex boolean expressions with parentheses in `{% if %}` statements
- Use `{% elif %}` instead of `or` with parentheses: `{% if condition1 %}...{% elif condition2 %}...{% endif %}`
- Avoid: `{% if square or (icon and not slot) %}`
- Use: `{% if square %}...{% elif icon and not slot %}...{% endif %}`
- **Variable names can only contain alphanumeric characters and underscores, no colons or other punctuation**
- Avoid: `icon:trailing` (colons not allowed)
- Use: `icon_trailing` (underscores are valid)
- **Boolean attributes**: Only include boolean attributes in `<c-vars>` if their default value is `True`. If default is `False`, omit the attribute entirely from `<c-vars>` and component usage
- Avoid: `<c-vars sortable="false" />` and `<c-component sortable="false">`
- Use: `<c-vars />` (omit entirely) and `<c-component />` (omit entirely) for false values
- Use: `<c-component sortable="true" />` only when you want to enable the feature

### CSS Classes
Components use DaisyUI classes with custom additions. **Always add custom CSS to `input.css`, not `components.css`**. The `components.css` file is auto-generated by Tailwind and should never be edited manually.

### Component Development Guidelines
When creating new components:
- **Django Cotton**: Use `<c-vars>` for component properties and slots for content
- **DaisyUI**: Leverage DaisyUI base classes (btn, input, toggle, card, etc.) for consistent styling
- **Enhanced functionality**: Use vanilla JavaScript for component logic, Alpine.js only for complex state management
- **Component structure**: Follow the pattern of container → DaisyUI base class → modifiers → custom classes
- **CSS Class Optimization**: Use dynamic class names like `toggle-{{ variant }}` and `btn-{{ size }}` instead of long conditional chains
- **Default Values**: Only add modifier classes when they differ from defaults (e.g., `{% if size != 'md' %}btn-{{ size }}{% endif %}`)

### HTMX Integration
Server responses can include toast notifications using `django_components_ui.utils`:
```python
from django_components_ui.utils import ToastSuccess, ToastError
return ToastSuccess("Operation completed!")
```

### JavaScript Integration Notes
- **Vanilla JavaScript**: Most components use vanilla JavaScript classes for functionality (TableFilter, GenericFilter, RangeSlider, etc.)
- **Alpine.js (minimal)**: Used only for complex reactive state (toasts, themes, smart navbar)
- **Element Reference**: In Alpine.js expressions within Cotton components, use `$el` (not `this.$el`) to reference the current element
- **Cotton Attributes**: Alpine attributes can be passed through Cotton components using `{{ attrs }}` on the target element
- **Initialization**: Components auto-initialize on DOMContentLoaded and after HTMX swaps

### Generic Filtering System
The project includes a generic filtering system that extends beyond tables to any type of content (cards, divs, buttons, etc.):

**Usage**:
```html
<c-filter-container target="items-container">
    <c-table.filter-dropdown filter-id="category" label="Catégorie" />
    <c-table.filter-range filter-id="price" label="Prix" format="currency" />
</c-filter-container>

<div id="items-container">
    <div class="card" data-filter-category="electronics" data-filter-price="299">...</div>
    <div class="card" data-filter-category="books" data-filter-price="25">...</div>
</div>
```

**Features**:
- **Auto-detection**: Filters are automatically detected from `data-filter-*` attributes
- **Range filters**: Numeric values automatically become range filters with min/max inputs
- **Dropdown filters**: Text values become multi-select dropdown filters
- **Reusable components**: Uses the same filter dropdown/range components as tables
- **Generic target**: Works with any HTML elements (cards, divs, buttons, etc.)

**Components**:
- `<c-filter-container>`: Main wrapper component (`django_components_ui/templates/cotton/filter_container.html`)
- JavaScript class: `GenericFilter` in `components.js` (vanilla JavaScript)
- Test page: `/generic-filter-test/` route in demo project

## Testing Environment

The `demo_project/` contains comprehensive examples and documentation:
- **Demo views**: Various component demonstrations
- **Documentation**: Component usage examples in `demo/templates/demo/docs/`
- **Layout demos**: Real-world layout examples (navbar, sidebar)

## Dependencies

### Python
- Django ≥5.2
- django-cotton ≥0.9.0

### Node.js (for development only)
- @tailwindcss/cli ^4.1.11
- daisyui ^5.0.46
- lucide icons ^0.525.0 (maintained separately)

**Note**: End users don't need Node.js - all assets are pre-built and included in the Python package.

## CSS Build Process

**Critical**: `django_components_ui/static/django_components_ui/css/components.css` is auto-generated by Tailwind CLI and must never be edited manually. All custom CSS should be added to `django_components_ui/static/django_components_ui/css/input.css`.

Always rebuild CSS after:
- Adding new components
- Modifying Tailwind classes
- Changing theme configuration
- Adding custom CSS to `input.css`

The build process scans all Django templates and compiles a comprehensive CSS file with all used classes.