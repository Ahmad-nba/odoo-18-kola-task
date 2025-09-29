# -*- coding: utf-8 -*-
from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='purchase_order_vendor_rel',
        column1='order_id',
        column2='partner_id',
        string='Vendors',
        domain=[('supplier_rank', '>', 0)],
    )

    bid_ids = fields.One2many(
        comodel_name='rfq.bid',
        inverse_name='rfq_id',
        string='Supplier Bids',
    )

    def action_assign_winner(self, bid_id):
        """
        Assign the winning bid's partner as the order's vendor and try to confirm the PO.
        """
        bid = self.env['rfq.bid'].browse(bid_id)
        if not bid.exists() or not bid.partner_id:
            return False

        # Add the vendor to vendor_ids (many2many). Use (4, id) to add link without duplication.
        self.write({'vendor_ids': [(4, bid.partner_id.id)]})

        # Assign selected vendor as the order's partner
        self.write({'partner_id': bid.partner_id.id})

        # Try to confirm the order (may fail if required fields are missing)
        try:
            self.button_confirm()
        except Exception:
            # ignore confirmation errors so assignment remains
            pass

        return True
