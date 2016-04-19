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
