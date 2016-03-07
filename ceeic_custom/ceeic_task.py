# -*- coding: utf-8 -*-
##############################################################################
#    Ceeic-task.
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
import openerp.addons.decimal_precision as dp


'''
Tipo de proyecto
'''

class origen_idea(models.Model):
    _name = 'ceeic.origen_idea'
    name = fields.Char(string='Origen idea')

class via(models.Model):
    _name = 'ceeic.via'
    name = fields.Char(string='Via')

class perfil(models.Model):
    _name = 'ceeic.perfil'
    name = fields.Char(string='Perfil innovador')


class sector_proyecto(models.Model):
    _name = 'ceeic.sector_proyecto'
    name = fields.Char(string='Sector del proyecto')
    
class origen_proyecto(models.Model):
    _name = 'ceeic.origen_proyecto'
    name = fields.Char(string='Origen del proyecto')

    
class ambito(models.Model):
    _name = 'ceeic.ambito'
    name = fields.Char(string='Ámbito')


'''
Datos de empresa
'''
    
class sector_empresa(models.Model):
    _name = 'ceeic.sector_empresa'
    name = fields.Char(string='Sector')


''' 
Innovación
'''

class grado_inno(models.Model):
    _name = 'ceeic.grado_inno'
    name = fields.Char(string='Grado')

class origen_inno(models.Model):
    _name = 'ceeic.origen_inno'
    name = fields.Char(string='Origen innovación')

class area_inno(models.Model):
    _name = 'ceeic.area_inno'
    name = fields.Char(string='Area innovación')

class proteccion(models.Model):
    _name = 'ceeic.proteccion'
    name = fields.Char(string='Protección')

'''
Necesidades
'''
class consultas(models.Model):
    _name = 'ceeic.consultas'
    name = fields.Char(string='Consultas')
    # Es una lista múltiple.
    # Llamar :
    #  'category_id': fields.many2many('res.partner.category', id1='partner_id', id2='category_id', string='Tags')
    # En la vista :
    #  <field name="category_id" widget="many2many_tags" placeholder="Tags..."/>


class intermediacion(models.Model):
    _name = 'ceeic.intermediacion'
    name = fields.Char(string='Intermediación')
    # multiseleccion


class ubicacion(models.Model):
    _name = 'ceeic.ubicacion'
    name = fields.Char(string='Ubicación')
    # multiseleccion


class consultoria(models.Model):
    _name = 'ceeic.consultoria'
    name = fields.Char(string='Consultoría')
    # multiseleccion

class formacion_empre(models.Model):
    _name = 'ceeic.formacion_empre'
    name = fields.Char(string='Formación')
    # multiseleccion

'''
Financiación
'''

class linea_financiera(models.Model):
    _name = 'ceeic.linea_financiera'
    name = fields.Char(string='Linea financiera')


class ceeic_project(models.Model):
    _name = 'project.project'
    _description = "Proyectos de emprendimiento"
    _inherit = ['project.project']

    tipo_emprendimiento = fields.Boolean(string='Proyecto de emprendimiento', default=True)
    

class ceeic_task(models.Model):
    _name = 'project.task'
    _description = 'Tareas de emprendimiento CEEIC'
    _inherit = ['project.task']
    
    origen_idea = fields.Many2one('ceeic.origen_idea', string='Origen de idea', ondelete='set null', required=False)
    via = fields.Many2one('ceeic.via', string='Via', ondelete='set null', required=False)
    perfil = fields.Many2one('ceeic.perfil', string='Perfil innovador', ondelete='set null', required=False)
    sector_proyecto = fields.Many2one('ceeic.sector_proyecto', string='Sector del proyecto', ondelete='set null', required=False)
    origen_proyecto = fields.Many2one('ceeic.origen_proyecto', string='Origen del proyecto', ondelete='set null', required=False)
    ambito = fields.Many2one('ceeic.ambito', string='Ámbito', ondelete='set null', required=False)
    
    anyo = fields.Char('Año de creación')
    mes = fields.Selection([
        ('enero', "Enero"),
        ('febrero', "Febrero"),
        ('marzo', "Marzo"),
        ('abril', "Abril"),
        ('mayo', "Mayo"),
        ('junio', "Junio"),
        ('julio', "Julio"),                
        ('agosto', "Agosto"),
        ('septiembre', "Septiembre"),
        ('octubre', "Octubre"),
        ('noviembre', "Noviembre"),
        ('diciembre', "Diciembre"),
    ], default='enero')

    inversion = fields.Float(string='Inversión', digits_compute= dp.get_precision('Account'))
    puestos = fields.Integer(string='Puestos de trabajo')
    sector_empresa = fields.Many2one('ceeic.sector_empresa', string='Sector', ondelete='set null', required=False)

    grado_inno = fields.Many2one('ceeic.grado_inno', string='Grado', ondelete='set null', required=False)
    origen_inno = fields.Many2one('ceeic.origen_inno', string='Origen innovación', ondelete='set null', required=False)
    area_inno = fields.Many2one('ceeic.area_inno', string='Área de innovación', ondelete='set null', required=False)
    proteccion = fields.Many2one('ceeic.proteccion', string='Protección', ondelete='set null', required=False)

    consultas = fields.Many2many('ceeic.consultas', string="Consultas")
    intermediacion = fields.Many2many('ceeic.intermediacion', string="Intermediación")
    ubicacion = fields.Many2many('ceeic.ubicacion', string="Ubicación")
    consultoria = fields.Many2many('ceeic.consultoria', string="Consultoría")
    formacion_empre = fields.Many2many('ceeic.formacion_empre', string="Formación")

    linea_financiera = fields.Many2one('ceeic.linea_financiera', string='Linea financiera', ondelete='set null', required=False)
    importe_solicitado = fields.Float('Importe solicitado', digits_compute= dp.get_precision('Account'))
    anyo_concesion = fields.Integer('Año de concesión')

    tipo_emprendimiento = fields.Boolean(string="Tarea de emprendimiento", related='project_id.tipo_emprendimiento')



ceeic_project()
ceeic_task()



