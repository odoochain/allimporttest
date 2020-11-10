# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Employee Image from CSV File | Import Employee Image from Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Human Resources",
    "license": "OPL-1",
    "summary": "import employee image from csv, import imagesfrom excel module, import user image from csv app, import user image from excel, employee image from xls odoo, import employee imagefrom xlsx",
    "description": """This module useful to import employee images by csv/excel file.
 Easily you can import images by url or from local system path. 
import employee image from csv, import imagesfrom excel module, import user image from csv app, import user image from excel, employee image from xls odoo, import employee imagefrom xlsx""",
    "version": "14.0.1",
    "depends": [
        "hr",
        "sh_message"
    ],
    "application": True,
    "data": [

        "security/import_emp_img_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_emp_img_wizard.xml",
        "views/hr_view.xml",

    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/9oQVCfMm9rc",
    "auto_install": False,
    "installable": True,
    "price": 19,
    "currency": "EUR"
}
