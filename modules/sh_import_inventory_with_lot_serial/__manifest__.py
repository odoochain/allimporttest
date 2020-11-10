# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Stock Inventory With Lot/Serial Number from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Warehouse",
    "summary": "import stock serial no from csv, inventory lot no from excel, stock serial number from xls, inventory lot number from xlsx app, import stock lot module, import warehouse odoo",
    "description": """This module useful to import stock inventory with lot/serial number from csv/excel.""",
    "version": "14.0.1",
    "depends": [
        "sh_message",
        "stock",
    ],
    "application": True,
    "data": [
        'security/import_inventory_with_lot_serial_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_inventory_with_lot_serial_wizard.xml',
        'views/stock_view.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/fLv25yWhGck",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR"
}
