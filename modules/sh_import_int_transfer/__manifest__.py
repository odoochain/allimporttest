# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Internal Transfer from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Warehouse",
    "summary": "import internal transfer app, internal transfer from csv, internal transfer from excel, internal transfer from xls, internal transfer xlsx module, internal transfer odoo",
    "description": """This module useful to import internal transfer from csv/excel. 
 import internal transfer app, internal transfer from csv, internal transfer from excel, internal transfer from xls, internal transfer xlsx module, internal transfer odoo """,
    "version": "14.0.1",
    "depends": [
        "sh_message",
        "stock",
    ],
    "application": True,
    "data": [
        "security/import_int_transfer_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_int_transfer_wizard.xml",
        "views/stock_view.xml",
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/jm-QgQpytC8",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR"
}
