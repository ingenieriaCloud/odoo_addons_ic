# -*- coding: utf-8 -*-
##############################################################################
#    reinicia-custom
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
   'name': 'Personalización de gestión para Reinicia',
   'version': '8.0.0.1.8',
   'author': 'Ingeniería Cloud',
   'category': 'Ingeniería Cloud',
   'depends': [
       'product',
       'purchase',
       'sale',
       'stock',
       'account',
   ],
   'website': 'http://www.serincloud.org',
   'description': """
Módulo para personalización de modelo de trabajo de Reinicia
============================================================


Este módulo añade campos específicos y funcionalidades para la gestión de Reinicia.

Publicado bajo licencia AGPL-v3.

Copyright (c) 2015-2016 Ingeniería Cloud

Copyright (c) 2015-2016 Francisco Manuel García Claramonte

    """,
   'data': [
       'views/product_view.xml',
       'views/stock_quant.xml',
       'views/production_lot.xml',
       'views/purchase_order_view.xml',
       'views/sale_order_view.xml',
       'security/ir.model.access.csv',
    ]
}
