##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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

class partner(models.Model):
    _inherit = ["res.partner"]
    
    account_owner_ids = fields.One2many('account.analytic.account', 'product_owner', string='Contratos Propietario')
    accounts_owner_count = fields.Integer(string='Total contratos propietario', store=False, compute='_get_accounts_owner_count')
    owner = fields.Boolean(string='Propietario', default=False)
    
    @api.one
    @api.depends('account_owner_ids')
    def _get_accounts_owner_count(self):
        domain = [('product_owner', '=', self.id)]
        count = self.env['account.analytic.account'].search_count(domain)
        self.accounts_owner_count = count

    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

