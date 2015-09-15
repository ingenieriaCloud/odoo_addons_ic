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

class product_template(models.Model):
    _inherit = ["product.template"]
    
    owner = fields.Many2one('res.partner', string='Propietario')
    account_ids = fields.One2many('account.analytic.account', 'product', string='Contratos')
    accounts_count = fields.Integer(string='Total contratos', store=False, compute='_get_accounts_count')
    
    
    @api.one
    @api.depends('account_ids')
    def _get_accounts_count(self):
        domain = [('product', '=', self.id)]
        count = self.env['account.analytic.account'].search_count(domain)
        self.accounts_count = count
    
    #def action_view_account(self, cr, uid, ids, context=None):
    #    result = self.pool['ir.model.data'].xmlid_to_res_id(cr, uid, 'account.view_account_analytic_account_list', raise_if_not_found=True)
    #    result = self.pool['ir.actions.act_window'].read(cr, uid, [result], context=context)[0]
    #    result['domain'] = "[('product','in',[" + ','.join(map(str, ids)) + "])]"
    #    return result
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

