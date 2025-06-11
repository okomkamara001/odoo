# -*- coding: utf-8 -*-

{
    'name': "Hospital Management System",

    'summary': "By IdtLabs SOftware Solutions",

    'description': """
Long description of module's purpose
    """,

    'author': "IdtLabs",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '17.0.1.1',


    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'mail', 'product', 'account', 'hr', 'stock', 'sale_management'],

    # always loadedaction_hospital_patient
    'data': [
        #'security/security.xml',
        'security/base_hospital_management_groups.xml',
        # 'security/patient_booking_security.xml',
        # 'security/patient_lab_test_security.xml',
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/website_data.xml',
        'data/ir_sequence.xml',
        'views/patient_views.xml',
        'views/booking_success_templates.xml',
        'views/patient_readonly_views.xml',
        'views/appointment_views.xml',
        'views/doctor_allocation_views.xml',
        'views/appointment_line_views.xml',
        'views/hr_employee_views.xml',
        'views/blood_bank_views.xml',
        'views/contract_indication_views.xml',
        'views/hospital_insurance_views.xml',
        'views/patient_tag.xml',
        'views/medicine_brand_views.xml',
        'views/patient_lab_test_views.xml',
        'views/lab_test_result_views.xml',
        'views/lab_test_views.xml',
        'views/lab_test_line_views.xml',
        'views/patient_room_views.xml',
        'views/hospital_ward_views.xml',
        'views/hospital_bed_views.xml',
        'views/hospital_degree_views.xml',
        'views/inpatient_surgery_views.xml',
        'views/hospital_vaccination_views.xml',
        'views/hospital_laboratory_views.xml',
        'views/hospital_pharmacy_views.xml',
        'views/doctor_specialization_views.xml',
        'views/hospital_inpatient_views.xml',
        'views/hospital_outpatient_views.xml',
        'views/hospital_building_views.xml',
        'views/account_move_views.xml',
        'views/patient_booking_template.xml',
        'views/product_template.xml',
        'views/room_facility.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    "demo": ["demo/hr_job_demo.xml"],
    "assets": {
        "web.assets_frontend": [
            # "base_hospital_management/static/src/js/prescription.js",
            # "base_hospital_management/static/src/js/website_page.js",
        ],
        "web.assets_backend": [
            # "base_hospital_management_groups/static/src/css/doctor_dashboard.css",
            # "base_hospital_management/static/src/css/reception_dashboard.css",
            # "base_hospital_management/static/src/css/lab_dashboard.css",
            # "base_hospital_management/static/src/css/pharmacy_dashboard.css",
            # "base_hospital_management/static/src/xml/lab_dashboard_templates.xml",
            # "base_hospital_management/static/src/xml/doctor_dashboard_templates.xml",
            # "base_hospital_management/static/src/js/lab_dashboard.js",
            # "base_hospital_management/static/src/js/doctor_dashboard.js",
            # "base_hospital_management/static/src/xml/pharmacy_orderlines.xml",
            # "base_hospital_management/static/src/js/pharmacy_orderlines.js",
            # "base_hospital_management/static/src/xml/pharmacy_dashboard_templates.xml",
            # "base_hospital_management/static/src/js/pharmacy_dashboard.js",
            # "base_hospital_management/static/src/xml/reception_dashboard_templates.xml",
            # "base_hospital_management/static/src/js/reception_dashboard.js",
        ],
    },
    "external_dependencies": {"python": ["python-barcode"]},
    "images": ["static/description/banner.jpg"],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}

