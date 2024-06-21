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
        'views/hr_hospital_menus.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_illness_views.xml',
        'views/hospital_patient_visits_views.xml',
    ],
    'demo': [
        'demo/hospital_doctor_demo.xml',
        'demo/hospital_illness_data.xml',
        'demo/hospital_patient_demo.xml',
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
