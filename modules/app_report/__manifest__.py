{
    'name' : 'Tax Reports',
    'version': '1.2',
    'Summary': 'Tax Report Prints',
    'description': 'To print the new report',
    'license': 'LGPL-3',
    'depends': [
        'sale_management','website','account_accountant','report'
    ],    
    'data': [
        #'data/data.xml',
        'reports/report_tax_invoice.xml',
        'reports/reports.xml',
        'views/account_report.xml',
        'views/report_without_prices.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}