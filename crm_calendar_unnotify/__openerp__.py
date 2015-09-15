# -*- coding: utf-8 -*-
#################################################################
# antonio.gonzalez                                  #
#################################################################

{
    'name' : 'Evitar notificaciones calendario',
    'version': '1.0',
    'depends': [
        'base', 'base_setup'
    ],
    'author': 'Ingeniería Cloud',
    'website':'http://ingenieriacloud.com',
    'category': 'Ingeniería Cloud',
    'description': """
Evitar notificaciones del calendario. Establece la variable de sistema calendar.block_mail a True.
Además añade una opción en el menú Configuración-> Configuración General para activar/desactivar las notificaciones
    """,
    'website': '',
    'data': [
        'calendar_unnotify_data.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': True
}
