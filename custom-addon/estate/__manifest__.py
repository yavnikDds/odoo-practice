{
    'name':'estate',
    'depends':[
        'base','estate_dep'
    ],
    # by adding this all the depends module are going to be installed before this module is installed
    'data':[
        'security/ir.model.access.csv', # any other data files you have
        'views/estate_property_actions.xml',    
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
    ],
    'application':True,
    'installable': True,
    'version':'1.1',
    'auto_install':True,
    # If a module has `auto_install: True` and all its dependencies are installed, Odoo will automatically install the module. However, if any dependency is missing, the module won't be installed.
}