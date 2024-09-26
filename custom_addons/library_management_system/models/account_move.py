from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'



    author_id = fields.Many2one('books.author', string="Authors")

