# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Leads from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "CRM",
    "summary": "Import Leads from CSV,Import Purchase Order Lines from Excel, Import RFQ Lines From CSV Module, Import RFQ Lines From Excel,Import PO Lines From CSV,import PO Lines From XLS, purchase order from XLSX Odoo",
    "description": """
    
        Import Leads

                    """,
    "version": "14.0.1",
    "depends": [
        "sh_message",
        "crm"
    ],
    "application": True,
    "data": [
        'security/import_lead_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_lead_wizard.xml',
        'views/crm_view.xml',
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "live_test_url": "https://youtu.be/Dx_0flM7o8c",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 15,
    "currency": "EUR"
}
