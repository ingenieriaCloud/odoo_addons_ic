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

from openerp import models, fields, api, osv, _
from uuid import uuid4

class Partner(models.Model):
    _inherit = 'res.partner'

    email_alias = fields.Many2one('mail.alias', 'Email Alias', readonly=True)
    email_alias_email = fields.Char(string='Alias', store=True)


#    @api.model
#    def create(self, vals):
#        ir_model = self.env['ir.model']
#        mail_alias_model = self.env['mail.alias']
#        partner_model_ids = ir_model.search([
#            ('model', '=', 'res.partner')
#        ])
#
#        if self.email_alias_email:
#            alias_name = self.email_alias_email + "-crm"
#        else:
#            alias_name = "{0}-crm2".format(uuid4().hex)
#
#        mail_alias_ids = mail_alias_model.search([
#            ('alias_name', '=', alias_name)
#        ])
#
#        while mail_alias_ids:
#            alias_name = "{0}-crm".format(uuid4().hex)
#            mail_alias_ids = mail_alias_model.search([
#                ('alias_name', '=', alias_name)
#            ])
#        alias = mail_alias_model.create({
#            'alias_name': alias_name,
#            'alias_model_id': partner_model_ids[0].id
#        })
#        vals['email_alias'] = alias.id
#        record = super(Partner, self).create(vals)
#        alias.alias_force_thread_id = record.id
#        return record

    @api.onchange('email_alias_email')
    def _email_alias_email(self):
        if self.email_alias_email:
            ir_model = self.env['ir.model']
            mail_alias_model = self.env['mail.alias']
            partner_model_ids = ir_model.search([
                ('model', '=', 'res.partner')
            ])

            if self.email_alias_email:
                alias_name = self.email_alias_email + "-crm"
            else:
                alias_name = "{0}-crm2".format(uuid4().hex)

            mail_alias_ids = mail_alias_model.search([
                ('alias_name', '=', alias_name)
            ])

            if not mail_alias_ids:
                alias = mail_alias_model.create({
                    'alias_name': alias_name,
                    'alias_model_id': partner_model_ids[0].id
                })

                self.email_alias = alias.id
                self.email_alias_email = None

                alias.alias_force_thread_id = self.id
            else:
                raise osv.except_osv(_('UserError'), _('El Alias ya existe'))

