# -*- coding: utf-8 -*-
##############################################################################
#    Ode-custom.
#    Copyright (c) 2015-2016 Francisco Manuel García Claramonte <francisco@garciac.es>
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
   'name': 'Personalización de informe de Factura de ODE24',
   'version': '8.0.1.1.0',
   'author': 'Ingeniería Cloud',
   'category': 'Ingeniería Cloud',
   'depends': ['account'],
   'website': 'https://serincloud.org',
   'description': """
Módulo para personalizar el informe de factura ODE24
====================================================

    Este módulo permite personalizar, de forma sencilla, el informe de factura para imprimir.
    
    Publicado bajo licencia AGPL-v3
   
    Copyright (c) 2015-2016 Ingeniería Cloud

    Copyright (c) 2015-2016 Francisco Manuel García Claramonte
    """,
   'data': [
       'views/report_invoice.xml',
       'views/report_paperformat.xml',
       'views/external_layout_header.xml',
       'views/external_layout_footer.xml',
   ]

}
