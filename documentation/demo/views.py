from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import json
from django_components_ui import Toast, ToastSuccess, ToastError, ToastWarning, ToastInfo
from .forms import LoginForm
import time

def index(request):
    return render(request, "demo/index.html")

def components(request):
    """Components showcase page - grid view of all available components"""
    return render(request, "demo/components.html")

def docs(request):
    # Vérifier si la requête vient d'HTMX
    is_htmx = request.headers.get('HX-Request', False)
    
    if is_htmx:
        # For HTMX, return only the partial introduction content
        return render(request, "demo/docs/partials/introduction.html")
    else:
        # For direct requests, return the complete page
        return render(request, "demo/docs/index.html")

def docs_page(request, section, page):
    """Generic view to serve all documentation pages."""
    # Vérifier si la requête vient d'HTMX
    is_htmx = request.headers.get('HX-Request', False)
    
    # Prepare the base context
    context = {
        'section': section,
        'page': page,
    }
    
    # Add specific data depending on the page
    if section == 'components' and page == 'filters':
        # Sample data for filters documentation
        context.update({
            'products': [
                {
                    'name': 'iPhone 15 Pro',
                    'category': 'electronics',
                    'price': 1199,
                    'status': 'available',
                    'brand': 'Apple',
                    'description': 'Apple\'s latest flagship smartphone with A17 Pro chip and revolutionary camera system.'
                },
                {
                    'name': 'MacBook Air M3',
                    'category': 'electronics',
                    'price': 1299,
                    'status': 'available',
                    'brand': 'Apple',
                    'description': 'Ultra-thin laptop with the new M3 chip for exceptional performance.'
                },
                {
                    'name': 'Casque Sony WH-1000XM5',
                    'category': 'electronics',
                    'price': 399,
                    'status': 'sold',
                    'brand': 'Sony',
                    'description': 'Wireless headset with world-class active noise cancellation.'
                },
                {
                    'name': 'Clean Code',
                    'category': 'books',
                    'price': 45,
                    'status': 'available',
                    'brand': 'O\'Reilly',
                    'description': 'Practical guide for writing clean and maintainable code by Robert C. Martin.'
                },
                {
                    'name': 'Python Crash Course',
                    'category': 'books',
                    'price': 35,
                    'status': 'available',
                    'brand': 'No Starch Press',
                    'description': 'Python crash course for beginners with practical projects.'
                },
                {
                    'name': 'Design Patterns',
                    'category': 'books',
                    'price': 55,
                    'status': 'sold',
                    'brand': 'Addison-Wesley',
                    'description': 'Essential design patterns by the Gang of Four.'
                },
                {
                    'name': 'T-shirt Django',
                    'category': 'clothing',
                    'price': 25,
                    'status': 'available',
                    'brand': 'Dev Gear',
                    'description': 'Organic cotton t-shirt with Django logo for passionate developers.'
                },
                {
                    'name': 'Hoodie React',
                    'category': 'clothing',
                    'price': 65,
                    'status': 'available',
                    'brand': 'Dev Gear',
                    'description': 'Comfortable hoodie with modern React design.'
                },
                {
                    'name': 'Casquette Vue.js',
                    'category': 'clothing',
                    'price': 20,
                    'status': 'sold',
                    'brand': 'Dev Gear',
                    'description': 'Adjustable cap with quality Vue.js embroidery.'
                },
                {
                    'name': 'Samsung Galaxy S24',
                    'category': 'electronics',
                    'price': 899,
                    'status': 'available',
                    'brand': 'Samsung',
                    'description': 'Android flagship smartphone with integrated AI and 200MP camera.'
                },
                {
                    'name': 'Dell XPS 13',
                    'category': 'electronics',
                    'price': 1099,
                    'status': 'available',
                    'brand': 'Dell',
                    'description': 'Premium Ultrabook with InfinityEdge display and exceptional performance.'
                },
                {
                    'name': 'JavaScript: The Good Parts',
                    'category': 'books',
                    'price': 30,
                    'status': 'available',
                    'brand': 'O\'Reilly',
                    'description': 'Concise guide to JavaScript best practices by Douglas Crockford.'
                },
                {
                    'name': 'Veste Softshell',
                    'category': 'clothing',
                    'price': 89,
                    'status': 'available',
                    'brand': 'Tech Wear',
                    'description': 'Waterproof and breathable technical jacket for active developers.'
                },
                {
                    'name': 'AirPods Pro 2',
                    'category': 'electronics',
                    'price': 279,
                    'status': 'sold',
                    'brand': 'Apple',
                    'description': 'Wireless earbuds with adaptive noise cancellation and spatial audio.'
                },
                {
                    'name': 'Polo Python',
                    'category': 'clothing',
                    'price': 45,
                    'status': 'available',
                    'brand': 'Code Style',
                    'description': 'Elegant polo with discreet Python logo for professional occasions.'
                }
            ]
        })
    if section == 'components' and page == 'filters':
        # Also add employee data for table examples
        context.update({
            'employees': [
                {
                    'id': 1,
                    'name': 'Sarah Connor',
                    'email': 'sarah.connor@company.com',
                    'department': 'Engineering',
                    'role': 'Senior Developer',
                    'salary': 95000,
                    'location': 'San Francisco',
                    'status': 'active',
                    'join_date': '2022-01-15'
                },
                {
                    'id': 2,
                    'name': 'John Smith', 
                    'email': 'john.smith@company.com',
                    'department': 'Design',
                    'role': 'UI/UX Designer',
                    'salary': 78000,
                    'location': 'New York',
                    'status': 'active',
                    'join_date': '2023-03-22'
                },
                {
                    'id': 3,
                    'name': 'Michael Johnson',
                    'email': 'michael.johnson@company.com', 
                    'department': 'Engineering',
                    'role': 'DevOps Engineer',
                    'salary': 88000,
                    'location': 'Austin',
                    'status': 'inactive',
                    'join_date': '2021-11-08'
                },
                {
                    'id': 4,
                    'name': 'Emily Davis',
                    'email': 'emily.davis@company.com',
                    'department': 'Marketing', 
                    'role': 'Marketing Manager',
                    'salary': 72000,
                    'location': 'Los Angeles',
                    'status': 'active',
                    'join_date': '2023-07-15'
                },
                {
                    'id': 5,
                    'name': 'Robert Wilson',
                    'email': 'robert.wilson@company.com',
                    'department': 'Sales',
                    'role': 'Sales Director', 
                    'salary': 105000,
                    'location': 'Chicago',
                    'status': 'active',
                    'join_date': '2020-09-03'
                },
                {
                    'id': 6,
                    'name': 'Lisa Anderson',
                    'email': 'lisa.anderson@company.com',
                    'department': 'Engineering',
                    'role': 'Frontend Developer',
                    'salary': 82000,
                    'location': 'Seattle',
                    'status': 'inactive',
                    'join_date': '2022-05-20'
                }
            ]
        })
    elif section == 'components' and page == 'table':
        # Sample data for table component documentation
        context.update({
            'employees': [
                {
                    'id': 1,
                    'name': 'Sarah Connor',
                    'email': 'sarah.connor@company.com',
                    'department': 'Engineering',
                    'role': 'Senior Developer',
                    'salary': 95000,
                    'location': 'San Francisco',
                    'status': 'not sure',
                    'join_date': '2022-01-15'
                },
                {
                    'id': 2,
                    'name': 'John Smith',
                    'email': 'john.smith@company.com',
                    'department': 'Design',
                    'role': 'UX Designer',
                    'salary': 78000,
                    'location': 'New York',
                    'status': 'active',
                    'join_date': '2021-08-20'
                },
                {
                    'id': 3,
                    'name': 'Maria Garcia',
                    'email': 'maria.garcia@company.com',
                    'department': 'Marketing',
                    'role': 'Marketing Manager',
                    'salary': 85000,
                    'location': 'Austin',
                    'status': 'active',
                    'join_date': '2020-03-10'
                },
                {
                    'id': 4,
                    'name': 'David Chen',
                    'email': 'david.chen@company.com',
                    'department': 'Engineering',
                    'role': 'DevOps Engineer',
                    'salary': 92000,
                    'location': 'Seattle',
                    'status': 'inactive',
                    'join_date': '2019-11-05'
                },
                {
                    'id': 5,
                    'name': 'Emily Johnson',
                    'email': 'emily.johnson@company.com',
                    'department': 'Sales',
                    'role': 'Sales Representative',
                    'salary': 65000,
                    'location': 'Chicago',
                    'status': 'active',
                    'join_date': '2023-02-28'
                }
            ],
            'products': [
                {
                    'id': 'PRD-001',
                    'name': 'Wireless Headphones',
                    'category': 'Electronics',
                    'price': 299.99,
                    'stock': 45,
                    'rating': 4.8,
                    'featured': True
                },
                {
                    'id': 'PRD-002', 
                    'name': 'Laptop Stand',
                    'category': 'Accessories',
                    'price': 89.99,
                    'stock': 23,
                    'rating': 4.5,
                    'featured': False
                },
                {
                    'id': 'PRD-003',
                    'name': 'Mechanical Keyboard',
                    'category': 'Electronics',
                    'price': 159.99,
                    'stock': 0,
                    'rating': 4.9,
                    'featured': True
                }
            ]
        })
    
    if is_htmx:
        # For HTMX, return only the partial content
        template_name = f"demo/docs/{section}/{page}.html"
        return render(request, template_name, context)
    else:
        # For direct requests, return the complete page
        context['content_template'] = f"demo/docs/{section}/{page}.html"
        return render(request, "demo/docs/base_page.html", context)



def demo_spinner(request):
    """Mock view to demonstrate spinner functionality with HTMX."""
    import time
    time.sleep(2)  # Simulate a time-consuming operation
    return HttpResponse("Operation completed successfully!")


def sidebar(request):
    return render(request, "templates/sidebar.html")

def navbar(request):
    return render(request, "templates/navbar.html")


def toast_action(request):
    """Demonstration view for all types of toasts."""
    toast_type = request.GET.get('type', 'success')

    time.sleep(1)

    if toast_type == 'success':
        return ToastSuccess("Operation completed successfully!")
    elif toast_type == 'error':
        return ToastError("An error occurred")
    elif toast_type == 'warning':
        return ToastWarning("Warning, check your data")
    elif toast_type == 'info':
        return ToastInfo("Important information")
    else:
        # Usage with custom parameters
        return Toast(
            content="Custom toast", 
            variant=toast_type,
            duration=5000,  # additional parameter
            dismissible=True
        )


def login_form(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            return HttpResponse("Login successful", headers={'HX-Redirect': '/'})
        else:
            messages.error(request, "Form error")
            return render(request, 'demo/partials/login_form.html', context={'form': form})
    else:
        form = LoginForm(initial={'email': 'test@gmail.com', 'password': 'test1'})
    
    return render(request, 'demo/login.html', context={'form': form})


def get_options(request):
    """View to retrieve selection options."""
    return JsonResponse(['Option 4', 'Option 5', 'Option 6'], safe=False)


def nutriassiette(request):
    """View for NutriAssiette page - nutritional plate composition."""
    # Mock data for demonstration
    context = {
        'categories': [
            {'name': 'All', 'active': True},
            {'name': 'Proteins', 'active': False},
            {'name': 'Carbs', 'active': False},
            {'name': 'Vegetables', 'active': False},
            {'name': 'Fruits', 'active': False},
            {'name': 'Fats', 'active': False},
        ],
        'ingredients': [
            {
                'name': 'Poulet',
                'category': 'Proteins',
                'calories': 165,
                'proteins': 31.0,
                'carbs': 0.0,
                'lipids': 3.6,
                'portion': '100 g'
            },
            {
                'name': 'Saumon',
                'category': 'Proteins', 
                'calories': 208,
                'proteins': 22.0,
                'carbs': 0.0,
                'lipids': 13.0,
                'portion': '100 g'
            },
            {
                'name': 'Eggs',
                'category': 'Proteins',
                'calories': 70,
                'proteins': 6.0,
                'carbs': 0.0,
                'lipids': 0.0,
                'portion': '1 unit'
            },
            {
                'name': 'Tofu',
                'category': 'Proteins',
                'calories': 76,
                'proteins': 8.0,
                'carbs': 0.0,
                'lipids': 0.0,
                'portion': '100 g'
            },
            {
                'name': 'Red lentils',
                'category': 'Proteins',
                'calories': 116,
                'proteins': 9.0,
                'carbs': 0.0,
                'lipids': 0.0,
                'portion': '100 g'
            },
            {
                'name': 'Pois chiches',
                'category': 'Proteins',
                'calories': 164,
                'proteins': 8.9,
                'carbs': 0.0,
                'lipids': 0.0,
                'portion': '100 g'
            },
        ],
        'selected_items': [
            {
                'name': 'Poulet',
                'quantity': 100,
                'unit': 'g',
                'calories': 165,
                'proteins': 31.0,
                'carbs': 0.0,
                'lipids': 3.6,
            },
            {
                'name': 'Saumon', 
                'quantity': 100,
                'unit': 'g',
                'calories': 208,
                'proteins': 22.0,
                'carbs': 0.0,
                'lipids': 13.0,
            }
        ]
    }
    
    return render(request, "demo/nutriassiette.html", context)




# Layout demo views
def navbar_demo1(request):
    """Demo view 1 for navbar layout - Dashboard."""
    return render(request, "demo/layouts/navbar_demo1.html")

def navbar_demo2(request):
    """Demo view 2 for navbar layout - E-commerce."""
    return render(request, "demo/layouts/navbar_demo2.html")

def sidebar_demo1(request):
    """Demo view 1 for sidebar layout - Admin Panel."""
    return render(request, "demo/layouts/sidebar_demo1.html")

def sidebar_demo2(request):
    """Demo view 2 for sidebar layout - Project Management."""
    return render(request, "demo/layouts/sidebar_demo2.html")


def save_preferences_demo(request):
    """Demo view to save preferences."""
    
    # Return successful toast
    return ToastSuccess("Preferences saved successfully!")



def ui_blocks(request):
    """UI Blocks showcase page - collection of ready-to-use UI components"""
    
    # Define the blocks structure with categories
    blocks_data = {
        'marketing_ui': [
            {
                'id': 'headers',
                'name': 'Headers',
                'description': 'Hero sections and navigation headers',
                'components_count': 5,
                'template': 'demo/docs/ui-blocks/headers.html'
            },
            {
                'id': 'cards',
                'name': 'Cards',
                'description': 'Feature cards and content blocks',
                'components_count': 8,
                'template': 'demo/docs/ui-blocks/cards.html'
            }
        ],
        'application_ui': [
            {
                'id': 'dashboards',
                'name': 'Dashboards',
                'description': 'Complete dashboard layouts and analytics',
                'components_count': 6,
                'template': 'demo/docs/ui-blocks/dashboards.html'
            },
            {
                'id': 'stats',
                'name': 'Statistics',
                'description': 'Data visualization and metrics displays',
                'components_count': 4,
                'template': 'demo/docs/ui-blocks/stats.html'
            },
            {
                'id': 'auth-forms',
                'name': 'Authentication',
                'description': 'Login, registration, and auth forms',
                'components_count': 3,
                'template': 'demo/docs/ui-blocks/auth-forms.html'
            }
        ],
        'ecommerce_ui': [
            # Will be populated later
        ]
    }
    
    # Flatten all blocks for the main grid
    all_blocks = []
    for category, blocks in blocks_data.items():
        for block in blocks:
            block['category'] = category
            block['category_name'] = category.replace('_', ' ').title()
            all_blocks.append(block)
    
    context = {
        'all_blocks': all_blocks,
        'blocks_data': blocks_data
    }
    return render(request, 'demo/ui_blocks.html', context)

def ui_blocks_category(request, category):
    """UI Blocks category page"""
    
    # Define the blocks structure
    blocks_data = {
        'marketing-ui': {
            'name': 'Marketing UI',
            'description': 'Landing page sections, hero blocks, and promotional components for marketing websites.',
            'blocks': [
                {
                    'id': 'headers',
                    'name': 'Headers',
                    'description': 'Hero sections and navigation headers',
                    'components_count': 5,
                    'template': 'demo/docs/ui-blocks/headers.html'
                },
                {
                    'id': 'cards',
                    'name': 'Cards',
                    'description': 'Feature cards and content blocks',
                    'components_count': 8,
                    'template': 'demo/docs/ui-blocks/cards.html'
                }
            ]
        },
        'application-ui': {
            'name': 'Application UI',
            'description': 'Dashboard layouts, statistics, and application interface components.',
            'blocks': [
                {
                    'id': 'dashboards',
                    'name': 'Dashboards',
                    'description': 'Complete dashboard layouts and analytics',
                    'components_count': 6,
                    'template': 'demo/docs/ui-blocks/dashboards.html'
                },
                {
                    'id': 'stats',
                    'name': 'Statistics',
                    'description': 'Data visualization and metrics displays',
                    'components_count': 4,
                    'template': 'demo/docs/ui-blocks/stats.html'
                },
                {
                    'id': 'auth-forms',
                    'name': 'Authentication',
                    'description': 'Login, registration, and auth forms',
                    'components_count': 3,
                    'template': 'demo/docs/ui-blocks/auth-forms.html'
                }
            ]
        },
        'ecommerce-ui': {
            'name': 'E-commerce UI',
            'description': 'Product cards, shopping carts, checkout forms, and other e-commerce related UI blocks.',
            'blocks': []
        }
    }
    
    if category not in blocks_data:
        return render(request, '404.html', status=404)
    
    context = {
        'category': category,
        'category_data': blocks_data[category],
        'breadcrumbs': [
            {'name': 'UI Blocks', 'url': 'demo:ui_blocks'},
            {'name': blocks_data[category]['name'], 'url': None}
        ]
    }
    return render(request, 'demo/ui_blocks_category.html', context)

def ui_blocks_detail(request, category, block_id):
    """Individual UI block detail page"""
    
    # Define the blocks structure
    blocks_data = {
        'marketing-ui': {
            'name': 'Marketing UI',
            'blocks': {
                'headers': {
                    'name': 'Headers',
                    'description': 'Hero sections and navigation headers for marketing pages',
                    'template': 'demo/docs/ui-blocks/headers.html'
                },
                'cards': {
                    'name': 'Cards',
                    'description': 'Feature cards and content blocks for showcasing information',
                    'template': 'demo/docs/ui-blocks/cards.html'
                }
            }
        },
        'application-ui': {
            'name': 'Application UI',
            'blocks': {
                'dashboards': {
                    'name': 'Dashboards',
                    'description': 'Complete dashboard layouts with analytics and data visualization',
                    'template': 'demo/docs/ui-blocks/dashboards.html'
                },
                'stats': {
                    'name': 'Statistics',
                    'description': 'Data visualization components and metrics displays',
                    'template': 'demo/docs/ui-blocks/stats.html'
                },
                'auth-forms': {
                    'name': 'Authentication',
                    'description': 'Login, registration, and authentication form components',
                    'template': 'demo/docs/ui-blocks/auth-forms.html'
                }
            }
        },
        'ecommerce-ui': {
            'name': 'E-commerce UI',
            'blocks': {}
        }
    }
    
    if category not in blocks_data or block_id not in blocks_data[category]['blocks']:
        return render(request, '404.html', status=404)
    
    block_data = blocks_data[category]['blocks'][block_id]
    
    context = {
        'category': category,
        'category_name': blocks_data[category]['name'],
        'block_id': block_id,
        'block_data': block_data,
        'breadcrumbs': [
            {'name': 'UI Blocks', 'url': 'demo:ui_blocks'},
            {'name': blocks_data[category]['name'], 'url': f'demo:ui_blocks_category', 'url_args': [category]},
            {'name': block_data['name'], 'url': None}
        ]
    }
    return render(request, 'demo/ui_blocks_detail.html', context)



