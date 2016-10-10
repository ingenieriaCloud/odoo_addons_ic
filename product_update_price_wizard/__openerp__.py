# -*- encoding: utf-8 -*-
##############################################################################
#    product_update_price_wizard
#    Copyright (c) 2016 Francisco Manuel García Claramonte <francisco@garciac.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Update product price from pricelist',
    'version': '8.0.0.1.2',
    'category': 'Product',
    'description': """
Module for update product price
===============================


Publicado bajo licencia AGPL-v3.

Copyright (c) 2016 Ingeniería Cloud

Copyright (c) 2016 Francisco Manuel García Claramonte

    """,
    'author': 'Francisco M. García Claramonte',
    'website': 'http://www.garciac.es',
    'depends': [
        'product',
    ],
    'data': [
        'views/product_update_price_wizard_view.xml',
    ],
    "installable": True,
}
