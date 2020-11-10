# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Product Template from CSV/Excel file-Multi Barcodes",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Productivity",
    "summary": "import templatefrom csv module, import template from excel app, import template from xls odoo, import template from xlsx,product template with multi barcodes Odoo",
    "description": """This module useful to import product template from csv/excel. 
  Import Product Template From CSV , Import Product Template From excel Odoo
 Import Template From CSV Module, Import Template From Excel, Import Template From XLS XLSX Odoo.
 Import Template From CSV Module, Import Template From Excel App, import Template From XLS XLSX Odoo """,
    "version": "14.0.1",
    "depends": [
        "sh_message",
        "sale_management",
        "stock",
        "sh_product_multi_barcode"
    ],
    "application": True,
    "data": [
        'security/import_product_tmpl_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_product_tmpl_wizard.xml',
        'views/sale_view.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/Qyuv3j1LTKI",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 30,
    "currency": "EUR"
}
