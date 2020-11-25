{
    'name' : 'Tax Reports',
    'version': '1.1',
    'Summary': 'Tax Report Prints',
    'description': 'To print the new report',
    'license': 'LGPL-3',
    'depends': [
        'sale_management'
    ],    
    'data': [
        'reports/reports.xml',
        'reports/data.xml',
        #'reports/tax_invoice.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}