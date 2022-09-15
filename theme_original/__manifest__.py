{
    'name': 'Theme Training Simon',
    'version': '1.0',
    'summary': 'Training Theme to get used to Odoo Theme Development',
    'description': 'Training Theme to get used to Odoo Theme Development',
    'category': 'Theme',
    'author': 'Auguria',
    'sequence': 3,
    'company': 'Auguria',
    'maintainer': 'Auguria',
    'depends': ['base', 'website'],
    'data': [
        'views/template.xml',
        'views/odoo_theme.xml',
        'views/layout.xml',
        'views/footer.xml',
        'views/header.xml',
        'views/page.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/theme_original/static/src/css/style.css',
            '/theme_original/static/src/js/odoo_theme.js',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
}
