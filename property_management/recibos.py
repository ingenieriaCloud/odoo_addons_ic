# -*- coding: utf-8 -*-
#################################################################
# antonio.gonzalez                               #
#################################################################

# Importaciones
import sys

from openerp import models, fields, api, _

# Configuramos
reload(sys)
sys.setdefaultencoding('iso-8859-1')

class recibos(models.Model):
    _name = 'recibos'
    _description = u'Recibos'
    _inherit = ['mail.thread']
    _rec_name = 'concepto'

    _track = {
        'concepto': {
            'recibos.mt_concepto_change': lambda self, cr, uid, obj, ctx=None: True,
        },
        'fecha': {
            'recibos.mt_fecha_change': lambda self, cr, uid, obj, ctx=None: True,
        },
        'importe': {
            'recibos.mt_importe_change': lambda self, cr, uid, obj, ctx=None: True,
        },
        'cobrado': {
            'recibos.mt_cobrado_change': lambda self, cr, uid, obj, ctx=None: True,
        },
        'pagado': {
            'recibos.mt_pagado_change': lambda self, cr, uid, obj, ctx=None: True,
        },
    }

    _mail_post_access = 'read'
    
    #API VIEJA
    #_columns = {
    #    'concepto': fields.char(_(u'Concepto'), size=500, required=True),
    #    'fecha': fields.date(_(u'Fecha'), required=True),
    #    'importe': fields.float(_(u'Importe'), required=True),
    #    'cobrado': fields.float(_(u'Cobrado'), required=True),
    #    'pagado': fields.boolean(_(u'Pagado')),
    #    'product_id': fields.many2one('product.product', _(u'Vivienda')),
    #    'pendiente': fields.function(_get_importe_pendiente, type='float', digits=(12, 2), string=_(u'Pendiente')),
    #}
    
    #_defaults = {
    #    'cobrado': 0,
    #}

    #API NUEVA - odoo8
    concepto = fields.Char(string='Concepto', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    importe = fields.Float(string='Importe Factura', required=True)
    cobrado = fields.Float(string='Importe Cobrado', required=True, default=0.0)
    pagado = fields.Boolean(string='Pagado Propietario', default=False)
    
    account_id = fields.Many2one('account.analytic.account', string='Contrato')

    pendiente = fields.Float(string='Importe Pendiente de Cobrar', store=False, compute='_get_importe_pendiente')
    account_product = fields.Char(string='Vivienda', store=True, compute='_get_account_product')
    account_product_owner = fields.Char(string='Propietario', store=False, compute='_get_account_product_owner')
    account_product_tenant = fields.Char(string='Inquilino', store=False, compute='_get_account_product_tenant')

    is_pendiente_cobrar = fields.Boolean(string='¿Esta Pendiente de cobrar?', store=False, compute='_is_pendiente_cobro')
    is_pendiente_pagar = fields.Boolean(string='¿Esta Pendiente de pagar a propiertario?', store=False, compute='_is_pendiente_pago')

    @api.one
    @api.depends('importe', 'cobrado')
    def _get_importe_pendiente(self):
       self.pendiente = self.importe - self.cobrado


    @api.one
    @api.depends('account_id')
    def _get_account_product(self):
        self.account_product = self.account_id.product.name


    @api.one
    @api.depends('account_id')
    def _get_account_product_owner(self):
        self.account_product_owner = self.account_id.product.owner.name


    @api.one
    @api.depends('account_id')
    def _get_account_product_tenant(self):
        self.account_product_tenant = self.account_id.partner_id.name


    @api.one
    @api.depends('importe', 'cobrado')
    def _is_pendiente_cobro(self):
        if ((self.importe - self.cobrado) > 0):
            self.is_pendiente_cobrar = 1
        else:
            self.is_pendiente_cobrar = 0


    @api.one
    @api.depends('importe', 'cobrado', 'pagado')
    def _is_pendiente_pago(self):
        if ((self.importe - self.cobrado) == 0 and self.pagado == 0) :
            self.is_pendiente_pagar = 1
        else:
            self.is_pendiente_pagar = 0



    #def marcar_como_pagado(self, cr, uid, ids, context = None):
    #    osv.logging.log(100, "[Recibos] marcar_como_pagado:recibos:recibo (%s)" % (uid))
        
        # Modelos
    #    mMedia = self.pool.get('recibos')
        
        # Ejecucion
    #    mMedia.write(cr, uid, ids, {'pagado': True}, context)
    

    # -------------------------------------------------------
    # Mail gateway
    # -------------------------------------------------------
    #def message_get_suggested_recipients(self, cr, uid, ids, context=None):
    #	return super(recibos, self).message_get_suggested_recipients(cr, uid, ids, context=context)




