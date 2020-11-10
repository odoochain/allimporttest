# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Product Variant from CSV/Excel file-Multiple Barcodes",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Productivity",
    "summary": "Import Product Variant From CSV,  Import  Product Variant Excel App,Import  Product Variant XLS, Import  Product Variant From XLSX Moule, Product Variant From Excel With Multi Barcode,  Product Variant From CSV Odoo",
    "description": """Do you want to import products with product variants From CSV/Excel? This module helps to import products with product variants from the CSV or Excel files. This module provides a facility to import custom fields also. Here you can create or update product variants(image, price, color, size) from CSV/Excel.""",
    "version": "14.0.1",
    "depends": [
        "sale_management",
        "sh_message",
        "stock",
        "sh_product_multi_barcode"
    ],
    "application": True,
    "data": [
        'security/import_product_var_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_product_var_wizard.xml',
        'views/sale_view.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 40,
    "currency": "EUR"
}
