# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Reordering Rules from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Warehouse",
    "summary": "Import Reordering Rules From CSV Module, Import Reordering Rules From Excel App, import Reordering Rules From XLS, Reordering Rules From XLSX Odoo",
    "description": """This module is useful to import Reordering Rules from CSV/Excel. You can import custom fields from CSV or Excel.""",
    "version": "14.0.1",
    "depends": [
        "sh_message",
        "stock",
    ],
    "application": True,
    "data": [
        "security/import_reordering_rule_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_reordering_rule_wizard.xml",
        "views/stock_view.xml",
    ],
    "external_dependencies": {
        "python": ["xlrd"],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/vTFbpCpxhpc",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR"
}
