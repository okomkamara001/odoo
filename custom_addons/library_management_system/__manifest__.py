# -*- coding: utf-8 -*-
{
    'name': "Library Management System",

    'summary': "Library Management System",

    'description': """Imagine a library where books come to you, where due dates are 
    automatically tracked, and where you can browse and borrow books with ease.
     That's the Odoo Library App: a symphony of automation and convenience that makes it 
     easier than ever to enjoy the magic of books.
    """,

    'author': "IdtLabs.xyz",
    'website': "https://www.idtlabs.sl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '17.0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'website', 'board', 'mail','contacts', 'account', 'hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/report.xml',
        'views/Books_data.xml',
        'views/Author.xml',
        'views/Book_copies.xml',
        'views/Book_Category.xml',
        'views/Borrows.xml',
        'views/Books_Received.xml',
        'views/Publisher.xml',
        'views/controller_template.xml',
        'views/Dashboard.xml',
        'views/Account_move_views.xml',
        'views/hr_employee_views.xml',
        'views/Employee_Department.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'css': [],
    'images': ['static/description/icon.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True
}

