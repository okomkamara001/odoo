# -*- coding: utf-8 -*-

import odoo
from odoo import api, models, fields


class BooksReceived(models.Model):
    _name = 'books.received'
    _description = 'Books Received'

    borrow_id = fields.Many2one('books.borrows', string="Books")
    # end_date = fields.Date(string="End Date", related='borrow_id.end_borrow')
    received_date = fields.Date()
    delay_duration = fields.Integer()
    delay_penalties = fields.Float()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
