# -*- coding: utf-8 -*-
{
    'name': "student",
    # 'name': The name of the module, visible in the Odoo interface.

    'summary': "this is a student module and it will contain all student related stuff",
    # 'summary': A short description of the module’s purpose.

    'description': """
Long description of module's purpose
this is a student module and it will contain all student related stuff
    """,
    # 'description': A longer, detailed description of the module.

    'author': "Yavnik",
    # 'author': The author or creator of the module.
    
    'website': "https://www.yourcompany.com",
    # 'website': The URL of the website related to the module or company.

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'category': 'education',
    # 'category': The category under which the module will be listed in Odoo.

    'version': '0.1',
    # 'version': The version of the module.
    # any module necessary for this one to work correctly

    'depends': ['base'],
    # 'depends': List of other modules that this module depends on to work correctly.

    # always loaded

    'data': [
        # 'security/ir.model.access.csv',
        'views/student_views.xml'
    ],
    # 'data': List of data files (e.g., views, templates, security rules) to be loaded when the module is installed.
    'installable': True,
    'application': True,
}
# Here’s a brief one-line note for each key in the __manifest__ file:


