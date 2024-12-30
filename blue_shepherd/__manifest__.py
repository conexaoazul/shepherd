{
    'name': 'Blue Shepherd',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Create custom onboarding tours in Odoo web interface',
    'sequence': 1,
    'author': 'OpenHands',
    'website': 'https://github.com/shipshapecode/shepherd',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/blue_shepherd_tour_views.xml',
        'views/blue_shepherd_step_views.xml',
        'views/blue_shepherd_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'blue_shepherd/static/src/js/shepherd.min.js',
            'blue_shepherd/static/src/js/tour_manager.js',
            'blue_shepherd/static/src/scss/shepherd.scss',
            'blue_shepherd/static/src/xml/tour_templates.xml',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'description': '''
        Blue Shepherd Module for Odoo
        ============================
        This module integrates the Shepherd.js library with Odoo to create
        customizable onboarding tours in the web interface.
        
        Features:
        ---------
        * Create and manage custom onboarding tours
        * Define multiple steps for each tour
        * Customize step appearance and behavior
        * Trigger tours based on specific actions or events
        * Track tour completion status
    ''',
}