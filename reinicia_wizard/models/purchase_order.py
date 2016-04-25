# -*- encoding: utf-8 -*-
##############################################################################
#    reinicia-wizard
#    Copyright (c) 2016 Francisco Manuel García Claramonte <francisco@garciac.es>
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

    
    def onchange_transportista(self, cr, uid, ids, transportista_id, context=None):
        # Se toma el nuevo valor del transportista (res.partner),
        # Para todas las lineas de pedido se actualiza el lote
        # Para cada lote, se actualizan los quant que existan.

        if context is None:
            context = {}

        value = {}
        stock_prod_lot_obj = self.pool.get('stock.production.lot')
        res_partner_obj = self.pool.get('res.partner')

        #value["transportista_ent"] = transportista_id
        value.update({'transportista_ent': transportista_id})
        
        for this in self.browse(cr, uid, ids, context=context):
            matric = this.matricula_ent.id
            #supplier = this.partner_id.id
            order = this.id
            date = this.date_order

            #value["id"] = order
            #value["partner_id"] = this.partner_id.id

            for linea in this.order_line:
                prod_lot = linea.prodlot2_id.id
                lote = stock_prod_lot_obj.search(cr,uid,[('id', '=', prod_lot)],context=context)
                product = linea.product_id.id
                val = {
                    'name' : stock_prod_lot_obj.browse(cr,uid,lote,context=context).name,
                    'product_id' : product,
                    'transportista_ent': transportista_id,
                    'matricula_ent': matric,
                }
                stock_prod_lot_obj.write(cr,uid, lote, val, context=context)
        
        return {'value': value}
        
    def onchange_matricula(self, cr, uid, ids, matricula_id, context=None):

        return True

    
PurchaseOrder()
