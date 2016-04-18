# -*- encoding: utf-8 -*-
from openerp.osv import orm, fields


class NewSaleLinesQuants(orm.TransientModel):
    _name = 'stock.quant.new_wizard'
    _description = "Creates new sale order lines from Quants"

    _columns = {
        'prods' : fields.many2many('stock.quant', string='Quants')
    }

    def action_new(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        data = self.browse(cr, uid, ids[0], context=context)

        ctx = context.copy()

        vals = {}
        vals['order_id'] = context.get("active_id", False)
        
        sale_order_line_obj = self.pool['sale.order.line']
        quant_list = []
        
        for q in data.prods:
            quant_list.append(q.id)
        dom = [('id','in', quant_list)]
        quants = self.pool.get('stock.quant').search(cr, uid, dom, context=context)
        for quant in self.pool.get('stock.quant').browse(cr, uid, quants, context=context):
            vals['product_id'] = quant.product_id.id
            vals['product_uom_qty'] = quant.qty
            vals['quant_id'] = quant.id
            vals['lot_id'] = quant.lot_id.id
            vals['name'] = quant.product_id.description_sale or quant.product_id.name
            sale_order_line = sale_order_line_obj.create(cr, uid,
                                                         vals,
                                                         context=ctx)
        
        return sale_order_line
