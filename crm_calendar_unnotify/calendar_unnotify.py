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

import logging
_logger = logging.getLogger(__name__)

class base_config_settings(models.Model):
    _inherit = 'base.config.settings'

    calendar_unnotify = fields.Boolean(string='Evitar Noficaciones en eventos', default=True)

    @api.one
    @api.depends('calendar_unnotify')
    def execute(self):
        domain = [('key', '=', 'calendar.block_mail')]
        conf = self.env['ir.config_parameter'].search(domain, limit=1)
        _logger.info("Valor de conf.key:" + conf.value)

        #conf.write({'value':'False'})
        if self.calendar_unnotify == True:
            conf.value = 'True'
        else:
            conf.value = 'False'