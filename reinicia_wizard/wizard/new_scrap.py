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


class NewSrapWizard(orm.TransientModel):
    _name = 'sale.order.new_scrap_wizard'
    _description = "Creates a new SCRAP order"

    _columns = {
        'scrap': fields.many2one('res.partner', 'SCRAP'),
      #  'prods' : fields.many2many('stock.quant', 'product_id')
    }

    def action_new(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        data = self.browse(cr, uid, ids[0], context=context)
        
        vals = {}
        vals['partner_id'] = data.scrap.id

        sale_order_obj = self.pool['sale.order']
        id_sale = sale_order_obj.create(cr, uid,
                                        vals,
                                        context=context)
        vals['order_id'] = id_sale

        sale_order_line_obj = self.pool['sale.order.line']

        dom = [('id','in',context.get("active_ids", []))]
        quants = self.pool.get('stock.quant').search(cr, uid, dom, context=context)
        for quant in self.pool.get('stock.quant').browse(cr, uid, quants, context=context):
            vals['product_id'] = quant.product_id.product_trazabilidad.id
            vals['product_uom_qty'] = quant.qty
            vals['quant_id'] = quant.id
            vals['trazabilidad'] = True
            #vals['lot_id'] = quant.lot_id.id
            vals['name'] = quant.product_id.description_sale or quant.product_id.name
            vals['name'] += " Lote: %s" % str(quant.lot_id.name)
            sale_order_line = sale_order_line_obj.create(cr, uid,
                                                         vals,
                                                         context=context)
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'res_model': 'sale.order',
            'res_id': id_sale ,
            'view_type': 'form',
            'view_mode': 'form',
            #'target' : 'new',
        }

        


    
