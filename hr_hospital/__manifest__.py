{
    'name': "hr_hospital",
    'summary': "Модуль для автоматизації лікарні: облік лікарів та пацієнтів",
    'author': "VitaliySm",
    'website': "https://github.com/Vitaliy-Sm",
    'category': 'Uncategorized',
    'license': 'OPL-1',
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'wizard/hospital_change_doctor_wizard_views.xml',
        'wizard/hospital_diagnosis_report_wizard_views.xml',

        'views/hr_hospital_menus.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_doctor_specialities_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_illness_views.xml',
        'views/hospital_patient_visits_views.xml',
        'views/hospital_diagnosis_views.xml',
    ],
    'demo': [
        'demo/hospital_doctor_demo.xml',
        'demo/hospital_illness_category_data.xml',
        'demo/hospital_illness_data.xml',
        'demo/hospital_patient_demo.xml',
        'demo/hospital_patient_visit_demo.xml',
        'demo/hospital_diagnosis_demo.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
        'static/description/cover.png',
    ],

    'price': 0,
    'currency': 'EUR',
}
