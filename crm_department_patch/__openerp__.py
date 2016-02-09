# -*- coding: utf-8 -*-
##############################################################################
#    crm_department_patch
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
    'name': 'Parche para crm_department',
    'version': '8.0.0.0.2',
    'author': 'SerInCloud',
    'category': 'SerInCloud',
    'website': 'http://serincloud.org',
    'license': 'AGPL-3',
    'depends': ['crm_department'],
    'description': """
Módulo Temporal para eliminar error de CRM-DEPARTMENT
========================================================

    Este módulo permite crear Oportunidades sin que se genere el error producido por el módulo CRM-DEPARTMENT.

    Publicado bajo licencia AGPL-v3
   
    Copyright (c) 2015-2016 Ingeniería Cloud

    Copyright (c) 2015-2016 Francisco Manuel García Claramonte

    """,
    'data': ['views/crm_department_patch_view.xml'],
}

