# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Product Images from Excel (from Path and URL)",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Productivity",
    "summary": "import product image from csv, import product image fromexcel, import product picture from csv, import product pics from excel, import product photos from xls, import product photo from xlsx Odoo",
    "description": """This module useful to import product image from csv/excel. """,
    "version": "14.0.1",
    "depends": [
        "sale_management",
        "sh_message",
    ],
    "application": True,
    "data": [
        "security/import_product_img_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_product_img_wizard.xml",
        "views/sale_view.xml",
    ],
    "external_dependencies": {
        "python": ["xlrd"],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/Bz5FytlKvSk",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 20,
    "currency": "EUR"
}
