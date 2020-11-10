# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Images From Zip File",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Extra Tools",
    "summary": "import images from zip odoo, put icons from zip ,pics from zip, from zip import photographs, mass photos app, change pictures module, update image from zip Odoo",
    "description": """
This module will help you to import the bulk of images from a zip file. If you have many images and you want to update that all on one shot so our module will help you to archive that very easily. you just need to manage all image files in one zip and need to select that zip and import it, it will auto-update all images. this module will be useful to update image for the product, customer/vendor/contact and employes. you can import images by name, reference, barcode and IDS depends on partner, product and employee.
 Import Bulk of Images from zip Odoo.
 feature of import images from zip odoo,  module for put icons or pics from zip , from zip import photographs .
 mass photos app,  change pictures module, update images.
                   
                   """,
    "version": "14.0.1",
    "depends": [
        "sale_management",
        "sh_message",
        "product",
        "hr",
    ],
    "application": True,
    "data": [

        "security/import_img_zip_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_img_zip_wizard.xml",
        "views/sale_view.xml",

    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR"
}
