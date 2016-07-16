# -*- encoding: utf-8 -*-
##############################################################################
#    codigo_gs1_128
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
    'name': 'Código extra GS1-128 para productos',
    'version': '8.0.0.0.1',
    'category': 'Product',
    'description': """
Código GS1-128 para productos
==============================


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
        'views/product_view.xml',
    ],
    "installable": True,
}
