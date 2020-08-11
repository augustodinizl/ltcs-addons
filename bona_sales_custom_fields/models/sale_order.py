# -*- coding: utf-8 -*-
# © 2020 LTech CS
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# -*- coding: utf-8 -*-
from odoo import models, fields
class SaleOrder(models.Model):
	_inherit = 'sale.order'
	incorporadora = fields.Many2one('partner_invoice_id.parent_id', ondelete='set null')