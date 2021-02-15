{
    'name' : 'Hospital Management',
    'version': '1.3',
    'Summary': 'to test how to create a module',
    # 'sequence': '10',
    # 'category': 'Extra Tools',
    'description': 'First module is created',
    'license': 'LGPL-3',
    'depends': [
        'sale_management','website','account_accountant'
    ],    
    'data': [
       #all the path of XML files are present here
       'views/patient.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}