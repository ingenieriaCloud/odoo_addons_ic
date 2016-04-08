# -*- encoding: utf-8 -*-
from openerp.osv import orm, fields


class NewSaleOrderWizard(orm.TransientModel):
    _name = 'sale.order.new_wizard'
    _description = "Creates a new sale order"

    _columns = {
        'customer': fields.many2one('res.partner', 'Cliente'),
        'prods' : fields.many2many('stock.quant', 'product_id')
    }

    def action_new(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        data = self.browse(cr, uid, ids[0], context=context)
        sale_order_obj = self.pool['sale.order']
        ctx = context.copy()

        vals = {}
        
        #ctx['partner_id'] = data.customer
        vals['partner_id'] = data.customer.id
        
        id_sale = sale_order_obj.create(cr, uid,
                                                vals,
                                                context=context)
        vals['order_id'] = id_sale
        sale_order_line_obj = self.pool['sale.order.line']
        for prod in data.prods:
            vals['product_id'] = prod.id
            sale_order_line = sale_order_line_obj.create(cr, uid,
                                                         vals,
                                                         context=context)
        
        
        return id_sale
