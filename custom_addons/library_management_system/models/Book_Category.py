# -*- coding: utf-8 -*-

import odoo
from odoo import api, models, fields


class BookCategory(models.Model):
    '''
        class category content name of category books
        '''
    _name = 'books.category'
    _description = 'books category'

    name = fields.Char(string="Category")
    sequence = fields.Integer(default=10)
