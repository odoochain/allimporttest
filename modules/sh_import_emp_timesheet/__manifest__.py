# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Employee Timesheet from CSV/Excel file",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Human Resources",
    "summary": "Import Employee Timesheet From CSV Module, Import Employee Timesheet From Excel, Import User timetable From CSV, import user timetable from excel, import employee schedule From XLS, import employee from XLSX Odoo",
    "description": """
    This module is useful to import employee timesheet from CSV/Excel. You can import custom fields from CSV or Excel.
 Import Employee Timesheet From CSV Odoo, Import Employee Timesheet From excel Odoo
 Import Employee Timesheet From CSV Module, Import Employee Timesheet From Excel, Import User timetable From CSV, Import User timetable From Excel, Import Employee schedule From XLS XLSX Odoo.
 Import Employee Timesheet From CSV Module, Import Employee Timesheet From Excel, Import User timetable From CSV App, import user timetable from excel, import employee schedule From XLS XLSX Odoo . 
Importar hoja de horas de empleados de CSV Odoo, Importar hoja de horas de empleados de Excel Odoo
Importar hoja de tiempo de empleado del módulo CSV, Importar hoja de tiempo de empleado de Excel, Importar horario de usuario de CSV, Importar horario de usuario de Excel, Importar horario de empleado de XLS XLSX Odoo.
 Importar hoja de tiempo de empleado del módulo CSV, Importar hoja de tiempo de empleado de Excel, Importar horario de usuario de la aplicación CSV, importar horario de usuario de Excel, importar horario de empleado de XLS XLSX Odoo.
                    """,
    "version": "14.0.1",
    "depends": [
        "hr_timesheet",
        "sh_message"
    ],
    "application": True,
    "data": [
        "security/import_emp_timesheet_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_emp_timesheet_wizard.xml",
        "views/timesheet_view.xml",

    ],
    'external_dependencies': {
        'python': ['xlrd'],
    },
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/0yMRhxsIskE",
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 15,
    "currency": "EUR"
}
