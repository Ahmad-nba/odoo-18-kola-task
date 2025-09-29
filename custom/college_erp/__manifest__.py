
{
    'name': 'College ERP',
    'version': '1.0.0',
    'summary': 'An ERP system for managing college operations',
    'description': """
College ERP
===========

A module to manage students, courses, departments, and staff in a college.
    """,
    'author': 'Ahamada Shamuran',
    'website': 'https://github.com/Ahmad-nba/odoo-18-kola-task.git',
    'category': 'Education',
    'license': 'LGPL-3',

    # Dependencies: core modules your app relies on
    'depends': [
        'base',  # always include base
    ],

    # Data files loaded at module installation
    'data': [
        # security files first
        # 'security/ir.model.access.csv',
        # XML views, menus, actions
        # 'views/student_views.xml',
        # 'views/course_views.xml',
    ],

    # Demo data (optional, for testing)
    'demo': [
        # 'demo/demo.xml',
    ],

    'sequence': 1,
    'installable': True,
    'application': True,
    'auto_install': False,
}
