# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class account_invoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        assert len(self) == 1, 'This option should only be used for a single id at a time.'
        self.sent = True
        return self.env['report'].get_action(self, 'ode_custom_invoice.report_invoice')

account_invoice()


