# -*- coding: utf-8 -*-
#################################################################
# antonio.gonzalez                                  #
#################################################################

{
    'name' : 'Prosumer Customs',
    'version': '1.0',
    'depends': ['website_anonymous_hide_prices_customs', 'product_attribute_value_image'],
    'author': 'Ingeniería Cloud',
    'website':'http://ingenieriacloud.com',
    'category': 'Ingeniería Cloud',
    'description': """
Añade los Assets(JS y CSS) necesarios para el funcionamiento de las calculadoras de PROSUMER en el WEBSITE    """,
    'website': '',
    'data': [
        'views/website_calculator_assets.xml',
        'templates.xml'
    ],
    'auto_install': False,
    'installable': True,
}
