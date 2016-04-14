# -*- encoding: utf-8 -*-

from openerp.osv import orm, fields

class StockQuant(orm.Model):
    _inherit = "stock.quant"

    def create(self, cr, user, vals, context=None):
        context = context or {}

        lote_id = vals.get('lot_id', context)

        stock_prod_lot_obj = self.pool.get('stock.production.lot')
        purchase_order_obj = self.pool.get('purchase.order')

        for lot in stock_prod_lot_obj.browse(cr, user, lote_id, context=context):
            vals['purchase_order'] = lot.purchase_order.id
            vals['purchase_date'] = lot.purchase_date
            vals['transportista_ent'] = lot.transportista_ent.id
            vals['matricula_ent'] = lot.matricula_ent.id
            vals['dcs_entrada'] = lot.dcs_entrada
            vals['supplier'] = purchase_order_obj.browse(cr, user, lot.purchase_order.id, context=context).partner_id.id
            
        return super(StockQuant, self).create(cr, user, vals, context)

StockQuant()
