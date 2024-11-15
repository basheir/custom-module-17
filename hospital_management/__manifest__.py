{
    "name": "Hospital Management",
    "category": "sales",
    "license": "LGPL-3",
    "author": "Bashir",
    "website": "haybis.com",
    "installable": True,
    "application": True,
    'depends': ['base', 'mail'],

    "data": [
        'security/ir.model.access.csv',
        "data/sequence.xml",
        "views/all.doctors.view.xml",
        'views/doctors.view.xml',
        'views/patient_views.xml',
        "views/appointment.view.xml",
        'views/menu.xml'
    ],

}