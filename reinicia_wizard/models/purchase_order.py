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

PurchaseOrder()
