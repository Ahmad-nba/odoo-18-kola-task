# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    name = fields.Char(
        string='Request Reference',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('purchase.request')
    )
    request_date = fields.Date(
        string='Request Date',
        default=fields.Date.context_today
    )
    requested_by = fields.Many2one(
        'res.users',
        string='Requested By',
        default=lambda self: self.env.user
    )
    description = fields.Text(string='Description')
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('to_approve', 'To Approve'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('done', 'Done'),
        ],
        string='Status',
        default='draft'
    )

    def action_submit(self):
        self.write({'state': 'to_approve'})

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_reject(self):
        self.write({'state': 'rejected'})

    def action_done(self):
        self.write({'state': 'done'})
