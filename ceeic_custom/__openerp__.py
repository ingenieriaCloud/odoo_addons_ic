# -*- coding: utf-8 -*-
##############################################################################
#    ceeic-custom
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
   'name': 'Personalización de contactos y tareas para CEEIC',
   'version': '8.0.0.1.14',
   'author': 'Ingeniería Cloud',
   'category': 'Ingeniería Cloud',
   'depends': [
       'base',
       'project',
   ],
   'website': 'http://www.serincloud.org',
   'description': """
Módulo para personalización de Contactos y tareas
==================================================


Este módulo añade campos específicos para gestión de contactos y tareas de proyectos para CEEIC.

(Versión Alpha, solo para pruebas)

Publicado bajo licencia AGPL-v3.

Copyright (c) 2015-2016 Ingeniería Cloud

Copyright (c) 2015-2016 Francisco Manuel García Claramonte

    """,
   'data': [
       'views/res_partner_view.xml',
       'views/project_view.xml',
       'security/ir.model.access.csv',
       'data/ceeic_custom_data.xml',
       'data/ceeic_task_data.xml',
   ]
}
