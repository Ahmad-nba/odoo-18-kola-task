# -*- coding: utf-8 -*-
from odoo import models, fields


class RfqBid(models.Model):
    _name = 'rfq.bid'
    _description = 'Supplier Bid for RFQ'

    name = fields.Char(
        string='Bid Reference',
        required=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('rfq.bid')
    )
    rfq_id = fields.Many2one(
        comodel_name='purchase.order',
        string='Related RFQ',
        required=True,
        ondelete='cascade'
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Vendor',
        required=True,
        domain=[('supplier_rank', '>', 0)]
    )
    bid_amount = fields.Float(string='Bid Amount', required=True)
    notes = fields.Text(string='Notes')
    state = fields.Selection(
        [
            ('submitted', 'Submitted'),
            ('review', 'Under Review'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        ],
        string='Status',
        default='submitted'
    )

    def action_set_review(self):
        self.write({'state': 'review'})

    def action_accept(self):
        self.write({'state': 'accepted'})
        if self.rfq_id:
            self.rfq_id.action_assign_winner(self.id)

    def action_reject(self):
        self.write({'state': 'rejected'})
