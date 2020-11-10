# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Attendance From CSV/Excel",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Human Resources",
    "license": "OPL-1",
    "summary": " Import Attendance From CSV Module, Import Daily Attendance From Excel, Import Employee Attendance From CSV App, import Attendance From XLS XLSX Odoo",
    "description": """
Nowadays, many companies have multiple branches so managing daily attendance is a little time-consuming task, currently, in odoo, there is no kind of facility for importing attendance from CSV or Excel sheet. This module will help to import attendance from CSV/Excel sheet, also you can import attendance based on employee id or employee badge. You can import custom fields from CSV or Excel.

 Import Attendance From CSV Odoo, Import Attendance From excel Odoo
 Import Attendance From CSV Module, Import Attendance From Excel, Import Daily Attendance From CSV, Import Daily Attendance From Excel, Import Employee Attendance From CSV, Import Employee Attendance From Excel, Import Attendance From XLS XLSX Odoo.
 Import Attendance From CSV Module, Import Daily Attendance From Excel, Import Employee Attendance From CSV App, import Attendance From XLS XLSX Odoo
Importar asistencia de CSV Odoo, Importar asistencia de Excel Odoo
 Importar asistencia del módulo CSV, Importar asistencia de Excel, Importar asistencia diaria de CSV, Importar asistencia diaria de Excel, Importar asistencia de empleados de CSV, Importar asistencia de empleados de Excel, Importar asistencia de XLS XLSX Odoo.
 Importar asistencia desde el módulo CSV, importar asistencia diaria desde Excel, importar asistencia de empleados desde la aplicación CSV, importar asistencia desde XLS XLSX Odoo
                    """,
    "version": "14.0.1",
    "depends": [
        "hr_attendance",
        "sh_message",
    ],
    "application": True,
    "data": [
        "security/import_attendance_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_attendance_wizard.xml",
    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://www.youtube.com/watch?v=9gk_MI6pOYs&feature=youtu.be",
    "auto_install": False,
    "installable": True,
    "price": 20,
    "currency": "EUR"
}
