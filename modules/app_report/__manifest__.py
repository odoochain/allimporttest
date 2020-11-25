{
    'name' : 'Tax Reports',
    'version': '1.1',
    'Summary': 'Tax Report Prints',
    'description': 'To print the new report',
    'license': 'LGPL-3',
    'depends': [
        'sale_management','website'
    ],    
    'data': [
        #'data/data.xml',
        'reports/report_tax_invoice.xml',
        'reports/reports.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}