# -*- coding: utf-8 -*-

{
    'name': "Hospital",

    'summary': """This Module Helps to Manage Patients Records, Doctors Details,
     Lab Management , Employee Management etc.""",

    'description': """
    The hospital management module can be used to handle 
     the day-to-day activities of the hospital. Managing patient scheduling, 
     making patient ID cards, creating patient lab test results, and adding 
     doctors, patients, prescriptions, vaccines, etc. are all made easier 
     with the help of this module. This app offers a different dashboards for 
     different users.
    """,

    'author': "IdtLabs",
    "company": "IdtLabs Consultant Company",
    "maintainer": "IdtLabs Consultant Company",
    'website': "https://www.idtlabs.sl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '17.0.1.1',


    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail'],

    # always loadedaction_hospital_patient
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'views/controller_template.xml',
        'views/template_views.xml',
        # 'views/res_partner_views.xml',
        'views/patient_root_views.xml',
        'views/patient_template.xml',
        'report/patient_report_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'css': [],
    'license': "LGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}

