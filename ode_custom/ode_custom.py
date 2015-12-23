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
from openerp import models, fields, api

class dispositivos(models.Model):
    _name = 'ode.dispositivos'
    name = fields.Char(string='Dispositivo')


class condiciones(models.Model):
    _name = 'ode.condiciones'
    name = fields.Char(string='Nombre')
    texto = fields.Text(string='Condiciones')

class modelos(models.Model):
    _name = 'ode.modelos'
    name = fields.Char(string='Modelo')


class ode_task(models.Model):
    _name = 'project.task'
    _description = 'Tareas personalizadas para Ode24'
    _inherit = ['project.task']
    
   
    clave = fields.Char(string='Clave acceso', help='Contraseña de acceso al dispositivo')
    dispositivo = fields.Many2one('ode.dispositivos', string='Dispositivo', ondelete='set null', required=False)
    marca = fields.Many2one('product.brand', string='Marca', ondelete='set null')
    modelo = fields.Many2one('ode.modelos', string='Modelo', ondelete='set null')
    observaciones = fields.Char(string='Observaciones')
    reparacion = fields.Text(string='Detalle de arreglo')
    precio_aprox = fields.Char(string='Precio aproximado')
    precio_coste = fields.Float(string='Precio de coste')
    precio_venta = fields.Float(string='Precio de venta')
    condiciones = fields.Many2one('ode.condiciones', string='Condiciones')
    
ode_task()
    
