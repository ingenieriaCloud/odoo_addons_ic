# -*- coding: utf-8 -*-
##############################################################################
#    partner_sales_goal
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
   'name': 'Objetivos comerciales',
   'version': '8.0.0.1.0',
   'author': 'Ingeniería Cloud',
   'category': 'Ingeniería Cloud',
   'depends': [
       'sale',
       'base',
   ],
   'website': 'https://www.serincloud.org',
   'description': """
Modulo para gestionar objetivos comerciales
===========================================

Este módulo es para gestionar objetivos de estimación de ventas a clientes.
  
  Copyright (c) 2015-2016 Ingeniería Cloud

  Copyright (c) 2015-2016 Francisco Manuel García Claramonte


   """,
   'data': [
       'views/partner_sales_goal_view.xml',
       'security/ir.model.access.csv',
   ],
}
