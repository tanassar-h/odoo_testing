# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Triplek Employee Management',
    'version':'0.1',
    'author': 'Triplek Tech',
    'website': 'https://triplek.tech',
   'description': """ <p>This is a detailed description of my module.</p> <p>It includes <b>bold</b> text, <i>italic</i> text, and <u>underlined</u> text.</p> <p>It also includes <a href="http://example.com">links</a> and headings:</p> <h1>Heading 1</h1> <h2>Heading 2</h2> """
    ,
    'category':'Human Resources',
    'license':'LGPL-3',
    'summary':'For Testing Purpose',
  
    'data' : [
        'security/ir.model.access.csv',
        'views/triplek_view.xml'
    ],
    
#     'images':'https://www.triplek.tech/assets/logos/lo.svg',
    'icon': 'https://www.triplek.tech/assets/logos/lo.svg',
    'web_icon': 'https://www.triplek.tech/assets/logos/lo.svg',
    'installable': True,
    'application': True,
    'auto_install':False,
    


}  
