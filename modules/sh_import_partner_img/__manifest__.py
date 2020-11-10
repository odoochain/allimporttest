# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Customer Image from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Sales",
    "summary": """import customer image from csv, customer image from excel app, vendor picture from csv module, vendor pictures from excel, partner pics from excel odoo, partner photos from xls, customer image from XLSX Odoo""",
    "description": """
    
    This module useful to import partners (customer or vendors) images by csv/excel file. 
    Easily you can import images by url or from local system path.
    
     
    import customer image from csv, customer image from excel app, vendor picture from csv module, vendor pictures from excel, partner pics from excel odoo, partner photos from xls xlsx

                    """,
    "version": "14.0.1",
    "depends": [
        "sale_management",
        "sh_message"
    ],
    "application": True,
    "data": [

        "security/import_partner_img.xml",
        "security/ir.model.access.csv",
        "wizard/import_partner_img_wizard.xml",
        "views/sale_view.xml",

    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/jzwQa8oGSic",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR"
}
