{
    'name': 'Assistente de Onboarding',
    'version': '17.0.1.0.0',
    'category': 'Ferramentas',
    'summary': 'Crie tours personalizados de onboarding na interface web do Odoo',
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
        Módulo Assistente de Onboarding para Odoo
        ========================================
        Este módulo integra a biblioteca Shepherd.js com o Odoo para criar
        tours personalizados de onboarding na interface web.
        
        Funcionalidades:
        ---------------
        * Crie e gerencie tours personalizados de onboarding
        * Defina múltiplos passos para cada tour
        * Personalize a aparência e comportamento dos passos
        * Acione tours baseados em ações ou eventos específicos
        * Acompanhe o status de conclusão dos tours
    ''',
}