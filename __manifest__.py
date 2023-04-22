# -*- coding: utf-8 -*-
{
    'name': "eacademy",

    'summary': """Short (1 phrase/line) summary of the module's purpose, used as,
     subtitle on nodules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose:
            - Eacademy
                    
    """,

    'author': "Muhammad Azam",


    'category': 'Uncategorized',
    'version': '1.1',

    'depends': ['base'],
    # Always Loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/eacademy.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,


}
