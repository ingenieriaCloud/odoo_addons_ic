# -*- encoding: utf-8 -*-

from openerp.osv import orm, fields


class SaleOrder(orm.Model):
    _inherit = "sale.order"

    def copy(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        if context.get('customer'):
            default['customer'] = context['customer']
        return super(SaleOrder, self).copy(cr, uid, id, default=default,
                                                context=context)
