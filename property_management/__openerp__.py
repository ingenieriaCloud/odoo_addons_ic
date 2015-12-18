# -*- coding: utf-8 -*-
#################################################################
# antonio.gonzalez                                  #
#
# Revisado: 18 diciembre 2015
# Descripción:
#   Se ha añadido dependecia con account_analytic_analysis
#   Se han modificado los campos que necesitan se almacenados para
#   las búsquedas.
# Autor: Francisco M. García Claramonte.
#################################################################

{
    'name' : 'Gestión Inmobiliaria Odoo',
    'version': '1.1',
    'depends': [
        'base', 'mail', 'product', 'crm', 'project', 'account_analytic_analysis'
    ],
    'author': 'Ingeniería Cloud',
    'website':'http://ingenieriacloud.com',
    'category': 'Ingeniería Cloud',
    'description': """
Recibos - Gestión Inmobiliaria
================================================================================
La inmobiliaria alquila una vivienda. 
El propietario paga electricidad y agua mensualmente, y pasa los recibos a la inmobiliaria.
La inmobiliaria ha de gestionar el cobro de los mismos con el inquilino y entregar el dinero al propietario.
No debe hacerse como factura ya que la inmobiliaria no vende estos consumibles ni comisiona..
    """,
    'website': '',
    'data': [
        'security/property_management_security.xml',
        'security/ir.model.access.csv',
        'recibos_view.xml',
        'product_view.xml',
        'analytic_view.xml',
        'crm_lead_view.xml',
        'data/recibos_data.xml',
        'partner_view.xml',
        'menu/recibos_menu.xml'
    ],
    'auto_install': False,
    'installable': True,

}
