# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Task from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Project",
    "summary": "Import Task From CSV Module, Import Task From Excel App, import Task From XLS, import Task From XLSX, import projct Task From CSV, import tasks Odoo",
    "description": """This module is useful to import tasks from CSV/Excel. You can import custom fields from CSV or Excel.""",
    "version": "14.0.1",
    "depends": [
        "project",
        "sh_message",
    ],
    "application": True,
    "data": [
        "security/import_project_task_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_task_wizard.xml",
        "views/project_view.xml",
    ],
    "external_dependencies": {
        "python": ["xlrd"],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/R5FIiIWEZiY",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 20,
    "currency": "EUR"
}
