# -*- coding: utf-8 -*-
##############################################################################
#    crm-lead-group-state
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
   'name': 'Agrupar Iniciativas por Provincia',
   'version': '8.0.0.1.0',
   'author': 'Ingeniería Cloud',
   'category': 'Ingeniería Cloud',
   'depends': [
       'crm',
   ],
   'website': 'https://www.serincloud.org',
   'description': """
Modulo para agrupar iniciativas por provincia
=============================================   


Este módulo permite agrupar las iniciativas y oportunidades por provincia y pais. 

  
  Copyright (c) 2015-2016 Ingeniería Cloud

  Copyright (c) 2015-2016 Francisco Manuel García Claramonte


   """,
   'data': [
      'views/crm_lead_group_state_view.xml',
   ],
}
