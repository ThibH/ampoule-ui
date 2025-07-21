"""
Context processors pour l'application demo.
Fournit des données globales à tous les templates.
"""

def command_palette_data(request):
    """
    Context processor qui fournit les données de la command palette globale.
    """
    return {
        'global_command_palette_groups': [
            {
                'id': 'navigation',
                'label': 'Navigation',
                'items': [
                    {
                        'id': 'home',
                        'label': 'Accueil',
                        'icon': 'home',
                        'suffix': 'Retourner à la page d\'accueil',
                        'kbd': ['Ctrl', 'H'],
                        'onSelect': 'window.location.href = "/";'
                    },
                    {
                        'id': 'docs',
                        'label': 'Documentation',
                        'icon': 'book-open',
                        'suffix': 'Parcourir la documentation',
                        'kbd': ['Ctrl', 'D'],
                        'onSelect': 'window.location.href = "/docs/";'
                    }
                ]
            },
            {
                'id': 'components',
                'label': 'Composants',
                'items': [
                    {
                        'id': 'button',
                        'label': 'Button',
                        'icon': 'square',
                        'suffix': 'Composant bouton',
                        'onSelect': 'window.location.href = "/docs/components/button/";'
                    },
                    {
                        'id': 'badge',
                        'label': 'Badge',
                        'icon': 'tag',
                        'suffix': 'Composant badge',
                        'onSelect': 'window.location.href = "/docs/components/badge/";'
                    },
                    {
                        'id': 'command-palette',
                        'label': 'Command Palette',
                        'icon': 'terminal',
                        'suffix': 'Composant palette de commandes',
                        'onSelect': 'window.location.href = "/docs/components/command-palette/";'
                    },
                    {
                        'id': 'modal',
                        'label': 'Modal',
                        'icon': 'square',
                        'suffix': 'Composant modal',
                        'onSelect': 'window.location.href = "/docs/components/modal/";'
                    },
                    {
                        'id': 'toast',
                        'label': 'Toast',
                        'icon': 'bell',
                        'suffix': 'Composant notification',
                        'onSelect': 'window.location.href = "/docs/components/toast/";'
                    },
                    {
                        'id': 'progress',
                        'label': 'Progress',
                        'icon': 'activity',
                        'suffix': 'Composant barre de progression',
                        'onSelect': 'window.location.href = "/docs/components/progress/";'
                    },
                    {
                        'id': 'avatar',
                        'label': 'Avatar',
                        'icon': 'user-circle',
                        'suffix': 'Composant avatar avec image ou initiales',
                        'onSelect': 'window.location.href = "/docs/components/avatar/";'
                    }
                ]
            },
            {
                'id': 'layouts',
                'label': 'Layouts',
                'items': [
                    {
                        'id': 'navbar',
                        'label': 'Navbar',
                        'icon': 'menu',
                        'suffix': 'Layout navigation',
                        'onSelect': 'window.location.href = "/demo/docs/layouts/navbar/";'
                    },
                    {
                        'id': 'sidebar',
                        'label': 'Sidebar',
                        'icon': 'sidebar',
                        'suffix': 'Layout sidebar',
                        'onSelect': 'window.location.href = "/demo/docs/layouts/sidebar/";'
                    },
                    {
                        'id': 'footer',
                        'label': 'Footer',
                        'icon': 'minus',
                        'suffix': 'Layout footer',
                        'onSelect': 'window.location.href = "/demo/docs/layouts/footer/";'
                    }
                ]
            }
        ]
    }