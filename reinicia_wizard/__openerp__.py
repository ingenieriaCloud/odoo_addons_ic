# -*- encoding: utf-8 -*-
##############################################################################
#    reinicia-wizard
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
    'name': 'Wizard for new sale order from quants',
    'version': '8.0.0.5.6',
    'category': 'Stock',
    'description': """
Wizard para generar pedido de ventas desde Quants
=================================================


Publicado bajo licencia AGPL-v3.

Copyright (c) 2015-2016 Ingeniería Cloud

Copyright (c) 2015-2016 Francisco Manuel García Claramonte

    """,
    'author': 'Ingeniería Cloud',
    'website': 'http://www.serincloud.org',
    'depends': [
        'base',
        'sale',
        'stock',
        'account',
        'reinicia_custom',
    ],
    'data': [
        'wizard/new_sale_order_view.xml',
        'wizard/new_sale_lines_quants_view.xml',
        'wizard/new_scrap_view.xml',
        'views/stock_quant_view.xml',
        'views/sale_order_view.xml',
        'views/sale_scrap_view.xml',
    ],
    "installable": True,
}
