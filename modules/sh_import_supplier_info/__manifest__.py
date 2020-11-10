# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Vendor Details in Product from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Purchases",
    "summary": "Import Vendor Details In Product From CSV Module, Import Vendor Details From Excel App, import Vendor Details From XLS, import Vendor from XLSX Odoo",
    "description": """This module is useful to import vendor details in product from CSV/Excel. You can import custom fields from CSV or Excel.""",
    "version": "14.0.1",
    "depends": [
        "sh_message",
        "purchase"
    ],
    "application": True,
    "data": [
        'security/import_supplier_info_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_supplier_info_wizard.xml',
        'views/purchase_view.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/qZszX1TuEqY",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR"
}
