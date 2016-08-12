# -*- encoding: utf-8 -*-
##############################################################################
#    product_update_price_wizard
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

from openerp import models, fields, api
from openerp import exceptions

class ProductUpdatePriceWizard(models.TransientModel):
    _name = 'product.update_price_wizard'
    _description = 'Update product price'

    pricelist = fields.Many2one('product.pricelist', string="Tarifa")

    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        if not (self.pricelist):
            raise exceptions.ValidationError('Debe seleccionar una tarifa')

        prods_obj = self.env['product.template']
        active_ids = self.env.context['active_ids'] or []
        all_prods = prods_obj.browse(active_ids)
        
        pricelist = self.env['product.pricelist'].browse(self.pricelist.id)

        for p in all_prods:
            precio = pricelist.price_get(prod_id=p.id, qty=1.0)
            #import pudb; pudb.set_trace()
            if precio:
                for k,v in precio.items():
                    p.write({'list_price': v})


