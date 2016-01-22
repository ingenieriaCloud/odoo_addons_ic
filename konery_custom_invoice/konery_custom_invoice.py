# -*- coding: utf-8 -*-
from openerp import models, fields, api

class account_invoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def invoice_print(self):
        assert len(self) == 1, 'This option should only be used for a single id at a time.'
        self.sent = True
        return self.env['report'].get_action(self, 'konery_custom_invoice.report_invoice')

account_invoice()


