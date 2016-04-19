# -*- coding: utf-8 -*-
##############################################################################
#    Reinicia-custom.
#    Copyright (c) 2015-2016 Francisco Manuel García Claramonte <francisco@garciac.es>
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
from openerp import models, fields, api
from openerp.tools.translate import _



class product_template(models.Model):
    _name = 'product.template'
    _description = 'Product'
    _inherit = ['product.template']

    product_trazabilidad = fields.Many2one('product.template', string='Producto para trazabilidad', required=False)



class matricula_trans(models.Model):
    _name = 'reinicia_custom.matricula_trans'
    name = fields.Char(string='Matrícula')


    
class stock_production_lot(models.Model):
    _name = 'stock.production.lot'
    _inherit = ['stock.production.lot']
    _description = 'Lot/Serial'

    purchase_order = fields.Many2one('purchase.order', string="Pedido de compra")
    dcs_entrada = fields.Char(string='DCS Entrada')
    transportista_ent = fields.Many2one('res.partner', string="Transportista", domain=[('supplier','=',True)])
    matricula_ent = fields.Many2one('reinicia_custom.matricula_trans', string="Matrícula entrada", ondelete='set null', required=False)
    purchase_date = fields.Datetime(string='Fecha', store=True, related="purchase_order.date_order")
    



class stock_quant(models.Model):
    _name = 'stock.quant'
    _inherit = ['stock.quant']
    _description = 'Quants'

    supplier = fields.Many2one('res.partner',  string="Proveedor")
    dcs_entrada = fields.Char(string='DCS Entrada')
    transportista_ent = fields.Many2one('res.partner', string='Transportista de entrada', domain=[('supplier','=',True)])
    matricula_ent = fields.Many2one('reinicia_custom.matricula_trans', string="Matrícula entrada", ondelete='set null', required=False)
    purchase_order = fields.Many2one('purchase.order',  string="Pedido de compra")
    purchase_date = fields.Datetime(string='Fecha', store=True, related="purchase_order.date_order")

    dcs_salida = fields.Char(string='DCS Salida')
    transportista_sal = fields.Many2one('res.partner', string='Transportista de salida', domain=[('supplier','=',True)])
    matricula_sal = fields.Many2one('reinicia_custom.matricula_trans', string="Matrícula salida", ondelete='set null', required=False)
    customer = fields.Many2one('res.partner',  string="Cliente")
    sale_order = fields.Many2one('sale.order', string="Pedido de venta")
    sale_date = fields.Datetime(string='Fecha', store=True, related="sale_order.date_order")

    #account_invoice = fields.Many2one('account.invoice', string="Factura")
    #invoice_date = fields.Date(string='Fecha', store=True, related="account_invoice.date_invoice")
    sale_order_trazabilidad = fields.Many2one('sale.order', string="Pedido de venta")
    sale_date_trazabilidad = fields.Datetime(string='Fecha', store=True, related="sale_order_trazabilidad.date_order")
    scrap = fields.Many2one('res.partner', string='SCRAP')
    gestionado = fields.Boolean(string='Gestionado')
    

    empresa = fields.Many2one('res.partner', string='Empresa')
    certificado = fields.Char(string='Certificado')
    date_quant = fields.Date(string="Fecha") 
    
    


class sale_order(models.Model):
    _name = 'sale.order'
    _description = 'Sale order'
    _inherit = ['sale.order']

    transportista_sal = fields.Many2one('res.partner',  string="Transportista", domain=[('supplier','=',True)])
    matricula_sal = fields.Many2one('reinicia_custom.matricula_trans', string="Matrícula", ondelete='set null', required=False)

    

class purchase_order(models.Model):
    _name = 'purchase.order'
    _description = 'Purchase order'
    _inherit = ['purchase.order']


    #lote = fields.char('Lote de pedido')
    transportista_ent = fields.Many2one('res.partner',  string="Transportista", domain=[('supplier','=',True)])
    matricula_ent = fields.Many2one('reinicia_custom.matricula_trans', string="Matrícula", ondelete='set null', required=False)


    
   
    '''
    def create(self, cr, uid, vals, context=None):
        partner = self.pool.get('purchase.order.partner_id')
        
        # Hace falta todos los productos.
        order_lines = self.pool.get('purchase.order.order_line')

        prod = ""
        for o in order_lines:
            prod += " "+o.product_id
        date_o = self.pool.get('purchase.order.date_order')

        
        
        if vals.get('lote'):
             vals['lote'] = '%s %s %s' % (prod, date_o, partner)
             
        context = dict(context or {})
        order =  super(purchase_order, self).create(cr, uid, vals, context=context)

        return order
    '''

    
product_template()
stock_production_lot()
stock_quant()
sale_order()
purchase_order()
