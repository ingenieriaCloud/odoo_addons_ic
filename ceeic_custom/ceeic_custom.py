# -*- coding: utf-8 -*-
##############################################################################
#    Ceeic-custom.
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

class formacion(models.Model):
    _name = 'ceeic.formacion'
    name = fields.Char(string='Formación')


class experiencia(models.Model):
    _name = 'ceeic.experiencia'
    name = fields.Char(string='Experiencia')

class procedencia(models.Model):
    _name = 'ceeic.procedencia'
    name = fields.Char(string='Procedencia')

class edad(models.Model):
    _name = 'ceeic.edad'
    name = fields.Char(string='Edad')

    



class ceeic_partner(models.Model):
    _name = 'res.partner'
    _description = 'Contacto personalizado de CEEIC'
    _inherit = ['res.partner']

    formacion = fields.Many2one('ceeic.formacion', string='Formación', ondelete='set null', required=False)
    experiencia = fields.Many2one('ceeic.experiencia', string='Experiencia', ondelete='set null', required=False)
    procedencia = fields.Many2one('ceeic.procedencia', string='Procedencia', ondelete='set null', required=False)
    sexo = fields.Selection([
        ('hombre', "Hombre"),
        ('mujer', "Mujer"),
    ], default='hombre')
    edad = fields.Many2one('ceeic.edad', string='Edad', ondelete='set null', required=False)


ceeic_partner()



