# -*- coding: utf-8 -*-
##############################################################################
#    partner_sales_goal
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
from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import except_orm, Warning, RedirectWarning

'''
Partner sales goal. Fields:
- Year of goal
- Ammount of goal.
- Real ammount sold to customer for this year
'''

class partner_goal(models.Model):
    _name = 'partner.goal'
    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Cliente', change_default=True,
                                 required=True)
    year = fields.Date(string="Año")
    amount_goal = fields.Float(string='Objetivo', digits=dp.get_precision('Account'), store=True)
    amount_sold = fields.Float(string='Total vendido', digits=dp.get_precision('Account'), store=True)

    '''
    @api.multi
    def goal_year_change(self, partner_id=False):
        if not partner_id:
            raise except_orm(_('No Partner Defined!'), _("You must first select a partner!"))
        return True
    
    ''' 


class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    goals = fields.One2many(comodel_name='partner.goal',inverse_name='partner_id')
    
