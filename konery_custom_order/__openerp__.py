# -*- coding: utf-8 -*-
##############################################################################
#    Konery-custom-order
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
   'name': 'Personalización de informe de Presupuestos de Konery',
   'version': '8.0.1.1.4',
   'author': 'Ingeniería Cloud',
   'category': 'Ingeniería Cloud',
   'depends': [
       'sale',
       'sale_layout',
   ],
   'website': 'https://www.serincloud.org',
   'description': """
Módulo para personalizar el informe de Pedido/Presupuesto
==========================================================

    Este módulo permite personalizar, de forma sencilla, el informe de pedido y presupuesto para imprimir.
    
    Publicado bajo licencia AGPL-v3
   
    Copyright (c) 2015-2016 Ingeniería Cloud

    Copyright (c) 2015-2016 Francisco Manuel García Claramonte

    """,
   'data': [
       'views/report_saleorder.xml',
       'views/sale_view.xml',
   ]

}
