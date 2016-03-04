# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _

class sale_order(osv.osv):
    _inherit = "sale.order"
    
    _columns = {
        'note': fields.text('Terms and conditions'),
        'observaciones': fields.text('Observaciones')
    }

    _defaults = {
        'note': 'Al contado fecha factura',
        'observaciones': 'El presente presupuesto no incluye IVA ni otros impuestos.\nLa validez del presente documento es de 30 días',
    }

    '''
    def print_quotation(self, cr, uid, ids, context=None):
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        self.signal_workflow(cr, uid, ids, 'quotation_sent')
        return self.pool['report'].get_action(cr, uid, ids, 'konery_custom_order.report_saleorder', context=context)
    '''
sale_order()
