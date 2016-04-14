# -*- encoding: utf-8 -*-

from openerp.osv import orm, fields

class SaleOrderLine(orm.Model):
    _inherit = "sale.order.line"

    _columns = {
        'quant_id': fields.many2one('stock.quant', 'Quant'), 
    }


    
class SaleOrder(orm.Model):
    _inherit = "sale.order"

    '''
    def copy(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        if context.get('quant'):
            default['customer'] = context['customer']
        return super(SaleOrder, self).copy(cr, uid, id, default=default,
                                                context=context)
    '''

    def _get_DCS(self, cr, uid, line_order_lot, context=None):
        if context is None:
            context = {}

        dcs = None
        stock_prod_lot_obj = self.pool.get('stock.production.lot')
        for l in stock_prod_lot_obj.browse(cr, uid, [line_order_lot], context=context):
            dcs = l.dcs_entrada

        return dcs
    
    def action_button_confirm(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        val = {}        
        quants_obj = self.pool.get('stock.quant')

        for this in self.browse(cr, uid, ids, context=context):
            transp = this.transportista_sal.id
            matric = this.matricula_sal.id
            customer = this.partner_id.id
            order = this.id
            date = this.date_order
            for linea in this.order_line:
                quant_id = linea.quant_id.id
                quant = quants_obj.search(cr,uid,[('id', '=', quant_id)],context=context)
                # EL DCS hay que sacarlo del lote
                dcs = self._get_DCS(cr, uid, linea.lot_id.id ,context=context)
                val = {
                    'transportista_sal': transp,
                    'matricula_sal': matric,
                    'dcs_salida': dcs,
                    'customer' : customer,
                    'sale_order': order,
                    'sale_date': date,
                }
                quants_obj.write(cr,uid, quant, val, context=context)
     

        return super(SaleOrder, self).action_button_confirm(cr, uid, ids, context=context)




SaleOrderLine()
SaleOrder()
