# -*- encoding: utf-8 -*-

from openerp.osv import orm, fields

class PurchaseOrder(orm.Model):
    _inherit = "purchase.order"

    def wkf_confirm_order(self, cr, uid, ids, context=None):
        # tiene que leer el lote de cada linea,
        # En este lote, escribir: num pedido, fecha, transport, matricula
        
        if context is None:
            context = {}

        stock_prod_lot_obj = self.pool.get('stock.production.lot')

        for this in self.browse(cr, uid, ids, context=context):
            transp = this.transportista_ent.id
            matric = this.matricula_ent.id
            #supplier = this.partner_id.id
            order = this.id
            date = this.date_order
            for linea in this.order_line:
                prod_lot = linea.prodlot2_id.id
                lote = stock_prod_lot_obj.search(cr,uid,[('id', '=', prod_lot)],context=context)
                val = {
                    'transportista_ent': transp,
                    'matricula_ent': matric,
                    'purchase_order': order,
                    'purchase_date': date,
                }
                stock_prod_lot_obj.write(cr,uid, lote, val, context=context)

        return super(PurchaseOrder, self).wkf_confirm_order(cr, uid, ids, context=context)

PurchaseOrder()
