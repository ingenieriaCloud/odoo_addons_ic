# -*- coding: utf-8 -*-
##############################################################################
#    crm_lead_mail
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

from openerp.osv import fields, osv
from openerp.tools.translate import _

class crm_lead(osv.osv):
    _name ='crm.lead'
    _inherit = ['mail.thread', 'crm.lead']

    
    _columns = {
        'user_id': fields.many2one('res.users', 'Salesperson', select=True, track_visibility='onchange'),

        }
    
    
    def message_new(self, cr, uid, msg, custom_values=None, context=None):

        if custom_values is None:
            custom_values = {}

        defaults = {
            'email_from': False,
            'partner_id': False,
            'contact_name': False,
            'author_id' : False,
        }
      

        if msg.get('from'):
            from_mail = msg.get('from').split('<', 1)[1][:-1]
            user_ids = self.pool.get('res.users').search(cr, uid, [('email', '=', from_mail)], context=context)
            defaults['user_id'] = self.pool.get('res.users').browse(cr, uid, user_ids, context=context).id or False
        else:
            defaults['user_id'] = False
        
        defaults.update(custom_values)
        return super(crm_lead, self).message_new(cr, uid, msg, custom_values=defaults, context=context)

    
crm_lead
