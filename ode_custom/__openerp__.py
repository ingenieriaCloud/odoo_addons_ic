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
   'name': 'Personalización de tareas para gestión de Ode24',
   'version': '1.11',
   'author': 'Ingeniería Cloud',
   'category': 'Ingeniería Cloud',
   'depends': ['project','product_brand','project_task_code'],
    'website': 'http://www.ingenieriacloud.com',
    'description': """
Módulo para personalización de tareas de proyectos
===================================================

Este módulo añade campos específicos para gestión de tareas de proyectos para Ode24.

El módulo añade el modelo de datos necesario para gestionar tareas de reparación de
productos electrónicos.
Imprime los informes de etiquetas y resguardos de entrega.

Publicado bajo licencia AGPL-v3.

Copyright (c) 2015-2016 Ingeniería Cloud

Copyright (c) 2015-2016 Francisco Manuel García Claramonte

    """,
   'data': [
       'views/ode_custom_view.xml',
       'ode_custom_data.xml',
       'views/ode_parte_report.xml',
       'views/ode_parte_plantilla.xml',
       'views/ode_etiqueta_report.xml',
       'views/ode_etiqueta_plantilla.xml',
       'security/ir.model.access.csv',
        ]

}
