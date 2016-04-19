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

class SaleOrderLine(orm.Model):
    _inherit = "sale.order.line"

    _columns = {
        'quant_id': fields.many2one('stock.quant', 'Quant'),
        'trazabilidad': fields.boolean(readonly=True, default=False)
    }


    
class SaleOrder(orm.Model):
    _inherit = "sale.order"


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

                if linea.trazabilidad:
                    val = {
                        'scrap' : customer,
                        'sale_order_trazabilidad' : order,
                        'sale_date_trazabilidad' : date,
                        'gestionado' : True,
                    }
                else:
                    # EL DCS hay que no se hereda en ventas de salida. (requisitos: 18 abril)
                    #dcs = self._get_DCS(cr, uid, linea.lot_id.id ,context=context)
                     val = {
                        'transportista_sal': transp,
                        'matricula_sal': matric,
                        #'dcs_salida': dcs,
                        'customer' : customer,
                        'sale_order': order,
                        'sale_date': date,
                    }
                quants_obj.write(cr,uid, quant, val, context=context)

                    
        return super(SaleOrder, self).action_button_confirm(cr, uid, ids, context=context)




SaleOrderLine()
SaleOrder()
