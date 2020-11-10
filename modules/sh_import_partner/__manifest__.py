# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Customers from CSV File | Import Suppliers From Excel file | Import Customers from Excel File | Import Suppliers From CSV file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Sales",
    "summary": "Import Customer From CSV Module, Import Supplier From Excel App, import Partner From XLS, import client from XLSX Odoo ",
    "description": """
   This module is useful to import Customers/Suppliers from CSV/Excel. You can import custom fields from CSV or Excel.
 Import Customer / Supplier From CSV , Excel Odoo
 Import Customer / Supplier From CSV Module, Import Customer / Supplier From Excel, Import Customer / Supplier From XLS XLSX Odoo.
 Import Customer / Supplier From CSV Module, Import Customer / Supplier From Excel App, import Partner / Customer From XLS XLSX Odoo 
Importar cliente / proveedor desde CSV, Excel Odoo
 Importar cliente / proveedor desde el módulo CSV, Importar cliente / proveedor desde Excel, Importar cliente / proveedor desde XLS XLSX Odoo.
 Importar cliente / proveedor desde el módulo CSV, Importar cliente / proveedor desde la aplicación Excel, importar socio / cliente desde XLS XLSX Odoo
                    """,
    "version": "14.0.1",
    "depends": [
        "sale_management",
        "sh_message",
    ],
    "application": True,
    "data": [
        'security/import_partner_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_partner_wizard.xml',
        'views/sale_view.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/0novDMKcRoE",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR"
}
