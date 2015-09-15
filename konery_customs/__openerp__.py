# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#                       Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    'name': 'Konery customs',
    'version': '2.0',
    'category': 'Ingeniería Cloud',
    'description': """
Modificaciones específicas para Konery:

 * Informe de factura.
""",
    'author': 'Ingeniería Cloud',
    'website':'http://ingenieriacloud.com',
    'depends': [
        'account',
        'report_webkit',
    ],
    'data': [
        'views/report_invoice_konery.xml',
        'views/external_layout_header_konery.xml',
        'views/external_layout_footer_konery.xml',
    ],
    "installable": True,
}
