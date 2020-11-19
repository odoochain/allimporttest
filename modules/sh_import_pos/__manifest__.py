# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import POS from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Point of Sale",
    "summary": "import pos",
    "description": """
    
        Import POS

                    """,
    "version": "14.0.1",
    "depends": [
        "sh_message",
        "point_of_sale"
    ],
    "application": True,
    "data": [
        'security/import_pos_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_pos_wizard.xml',
        'views/pos_view.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "live_test_url": "https://youtu.be/Dx_0flM7o8c",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 15,
    "currency": "EUR"
}
