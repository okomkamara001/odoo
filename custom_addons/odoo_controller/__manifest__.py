# -*- coding: utf-8 -*-
{
    'name': "Controller",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Idtlabs",
    "company": "IdtLabs Consultant Company",
    "maintainer": "IdtLabs Consultant Company",
    'website': "https://www.idtlabs.sl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '17.0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/parent_template_views.xml',
        'views/partner_templates.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
'   css': [],
    'license': "LGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}

