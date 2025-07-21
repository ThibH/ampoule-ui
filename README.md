# Django Components UI

A modern Django component library built with Django Cotton, Tailwind CSS, and DaisyUI.

## 🚀 Quick Installation

### For End Users (Recommended)

**No Node.js required!** All CSS and JavaScript assets are pre-built and included in the package.

#### 1. Install Package

```bash
pip install django-components-ui
```

This automatically installs Django Cotton as a dependency.

#### 2. Configure Django Settings

Add to your `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'django_cotton',           # Required: Django Cotton
    'django_components_ui',    # Django Components UI
    
    # Your apps
    'your_app',
]
```

#### 3. Include Required Assets

**Simple Method (Recommended):**
```html
<!-- In your base.html head section -->
{% include "init-components.html" %}
```

**Manual Method (Optional):**
```html
<!-- In your base.html -->
<head>
    {% load static %}
    
    <!-- Django Components UI CSS (pre-built) -->
    <link rel="stylesheet" href="{% static 'django_components_ui/css/components.css' %}">
    
    <!-- HTMX -->
    <script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.6/dist/htmx.min.js"></script>
    
    <!-- Alpine.js (for reactive components) -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.14.8/dist/cdn.min.js"></script>
    
    <!-- Django Components UI JavaScript -->
    <script src="{% static 'django_components_ui/js/components.js' %}"></script>
</head>
```

#### 4. Start Using Components

```html
<!-- Button component -->
<c-button variant="primary" size="lg">
    Click me!
</c-button>

<!-- Card component -->
<c-card class="max-w-sm">
    <c-slot name="title">Card Title</c-slot>
    <c-slot name="content">
        <p>This is a card content.</p>
    </c-slot>
</c-card>

<!-- Table with filters -->
<c-table :data="employees">
    <c-table.column field="name" label="Name" />
    <c-table.column field="department" label="Department" filterable />
    <c-table.column field="salary" label="Salary" filterable format="currency" />
</c-table>
```

## 🛠️ Development Setup

### For Contributors and Advanced Users

If you want to contribute to the project or customize the CSS build process:

#### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/django-components-ui.git
cd django-components-ui
npm install
npm run build
```

#### 2. Demo Project

```bash
cd demo_project
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ..
python manage.py runserver
```

Visit `http://localhost:8000` to see the demo.

#### 3. Development Commands

```bash
# CSS development with watch mode
npm run dev

# Production build (minified)
npm run build

# Run Django tests
cd demo_project && python manage.py test
```

## 🎯 Available Components

### Form Components
- **Button**: Various styles, sizes, and states
- **Input**: Text inputs with validation support
- **Select/Combobox**: Dropdowns with search and autocomplete
- **Toggle**: Switch components
- **Checkbox/Radio**: Form controls

### Layout Components
- **Card**: Content containers
- **Modal**: Dialog boxes
- **Dropdown**: Contextual menus
- **Tabs**: Navigation tabs
- **Navbar/Sidebar**: Layout navigation

### Data Components
- **Table**: Advanced tables with filtering, sorting, pagination
- **Pagination**: Navigation for large datasets
- **Stats**: Metric displays
- **Progress**: Progress indicators

### Interactive Components
- **Command Palette**: Quick navigation
- **Toast**: Notifications
- **Tooltip**: Contextual help
- **Collapse**: Expandable content

## 🎨 Theming with DaisyUI

The project includes 30+ DaisyUI themes. Change themes by setting the `data-theme` attribute:

```html
<!-- Light theme (default) -->
<html data-theme="light">

<!-- Dark theme -->
<html data-theme="dark">

<!-- Other themes -->
<html data-theme="synthwave">
<html data-theme="cyberpunk">
<html data-theme="valentine">
```

**Available themes**: `light`, `dark`, `cupcake`, `bumblebee`, `emerald`, `corporate`, `synthwave`, `retro`, `cyberpunk`, `valentine`, `halloween`, `garden`, `forest`, `aqua`, `lofi`, `pastel`, `fantasy`, `wireframe`, `black`, `luxury`, `dracula`, `cmyk`, `autumn`, `business`, `acid`, `lemonade`, `night`, `coffee`, `winter`, `dim`, `nord`, `sunset`.

## 📊 Features

### ✅ Ready-to-Use Components
Complete collection of modern UI components for Django applications.

### ✅ HTMX Integration
Native support for HTMX interactions with loading indicators and server-side responses.

### ✅ Pre-built Assets
No Node.js required for end users - all assets are compiled and packaged.

### ✅ Customizable
Full theme support with DaisyUI and Tailwind CSS customization.

### ✅ Accessibility
Built with accessibility best practices and ARIA attributes.

### ✅ TypeScript-like Experience
Component props and slots provide a structured development experience.

## 🏗️ Architecture

### Component System
Built with **Django Cotton** for reusable component composition:

```html
<!-- Component definition -->
<c-vars variant="primary" size="md" />
<button class="btn btn-{{ variant }} btn-{{ size }}">
    {{ slot }}
</button>

<!-- Usage -->
<c-button variant="success" size="lg">Save Changes</c-button>
```

### Styling
- **Tailwind CSS 4.x**: Modern utility-first CSS framework
- **DaisyUI**: Semantic component classes and themes
- **Pre-compiled**: CSS is built and optimized for production

### JavaScript
- **HTMX**: Server-side interactions without complex JavaScript
- **Alpine.js**: Minimal client-side reactivity for complex components
- **Vanilla JS**: Core utilities and component behaviors

## 🔧 Project Structure

```
django-components-ui/
├── django_components_ui/              # Main Python package
│   ├── templates/cotton/              # Component templates
│   │   ├── button.html                # Button component
│   │   ├── table.html                 # Table component
│   │   └── ...                        # Other components
│   ├── static/django_components_ui/
│   │   ├── css/components.css         # Pre-built CSS (Tailwind + DaisyUI)
│   │   └── js/components.js           # JavaScript utilities
│   └── templates/init-components.html # Asset includes
├── demo_project/                      # Demo project
│   ├── demo/                          # Demo app with examples
│   └── manage.py
├── tailwind.config.js                 # Tailwind configuration
├── package.json                       # Node.js dependencies (dev only)
└── pyproject.toml                     # Python package configuration
```

## 🚦 Requirements

- **Python** ≥ 3.8
- **Django** ≥ 5.2
- **django-cotton** ≥ 0.9.0 (automatically installed)

## 🤝 Contributing

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run the development server to test
6. Submit a pull request

## 📄 License

MIT License

---

**Built with Django, Cotton, Tailwind CSS, DaisyUI, HTMX, and Alpine.js**