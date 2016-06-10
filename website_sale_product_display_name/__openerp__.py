# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Sale Product Display Name',
    'summary': 'Use product display name instead of name in website sale.',
    'version': '9.0.1.0.0',
    'category': 'Website',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'website_sale',
    ],
    'data': [
        'views/website_sale_template.xml',
    ],
}
