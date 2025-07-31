from django.urls import path
from . import views

app_name = "demo"

urlpatterns = [
    path("", views.index, name="index"),
    path("components/", views.components, name="components"),
    path("docs/", views.docs, name="docs"),
    
    # Dynamic documentation routes
    path("docs/<str:section>/<str:page>/", views.docs_page, name="docs_page"),
    
    # Demo routes
    path("demo-spinner/", views.demo_spinner, name="demo_spinner"),
    path("nutriassiette/", views.nutriassiette, name="nutriassiette"),

    # Preferences demo routes
    path("preferences/", views.save_preferences_demo, name="save_preferences_demo"),
    
    # Layout demo routes
    path("layouts/navbar/demo1/", views.navbar_demo1, name="navbar_demo1"),
    path("layouts/navbar/demo2/", views.navbar_demo2, name="navbar_demo2"),
    path("layouts/sidebar/demo1/", views.sidebar_demo1, name="sidebar_demo1"),
    path("layouts/sidebar/demo2/", views.sidebar_demo2, name="sidebar_demo2"),
    
    # Legacy routes
    path("templates/sidebar/", views.sidebar, name="sidebar"),
    path("templates/navbar/", views.navbar, name="navbar"),
    path("toast-action/", views.toast_action, name="toast_action"),
    path("login/", views.login_form, name="login"),
    path("get-options/", views.get_options, name="get_options"),
    
    # UI Blocks page
    path("ui-blocks/", views.ui_blocks, name="ui_blocks"),
    path("ui-blocks/<str:category>/", views.ui_blocks_category, name="ui_blocks_category"),
    path("ui-blocks/<str:category>/<str:block_id>/", views.ui_blocks_detail, name="ui_blocks_detail"),
    
]