# -*- coding: utf-8 -*-
from email.policy import default

import odoo
from odoo import api, fields, models
from datetime import datetime, timedelta

from odoo.tools.populate import compute

'''
Books_data is a model defined in an object-relational mapping (ORM) framework, 
which is often used in Python-based web applications, such as Odoo or Django.
 This class represents a table or collection in a database where information about books is stored.
The _name attribute is used to specify the internal name of the model. In this case, 
it is set to 'books.data',
 which means the table or collection name associated with this model will be 'books_data'.
'''


class Books_data(models.Model):
    _name = 'books.data'
    _inherit = ['mail.thread']
    _description = 'books.dat'
    # Basic Information
    name = fields.Char(string="Tittle", required=True, tracking=True)
    price = fields.Float(string="Price", tracking=True)
    image = fields.Image(string="Book Cover")

    # Book Details
    language = fields.Selection(
        [('en', 'English'), ('ar', 'Arabic'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German'), ],
        string='Language')
    description = fields.Text(string="Description")
    number_of_pages = fields.Integer(string="pages Book", tracking=True)
    author_ids = fields.Many2many('books.author', string="Author Name")
    copy_ids = fields.One2many('book.copies', 'book_id', string='Copies', ondelete='restrict')
    copy_count = fields.Integer(string='Copy Count')
    start_date = fields.Datetime(default=fields.Datetime.today)
    end_date = fields.Date(string="End Date", store=True,
                           compute='_get_end_date_', inverse='_set_end_date')
    color = fields.Integer(string="color")
    priority = fields.Selection([('0', 'normal'), ('1', 'low'),
                                 ('2', 'high'),
                                 ('3', 'very high')], string='priority')
    category_ids = fields.Many2one('books.category', string="Category Book")
    # miscellaneous
    version = fields.Char(string="Version")
    ispn = fields.Char(string="Isbn")
    invoice = fields.Many2one('account.move',string="Invoice")


    @api.depends('copy_ids')
    def _compute_copy_count(self):

        for book in self:
            book.copy_count = str(len(book.copy_ids))


    @api.depends('_get_end_date', '_set_end_date')
    def _get_end_date(self):
        """
                    Sets the end date based on the start date and duration.

                    This method calculates the end date by adding the duration (in days) to the start date.
                    The calculated end date is then assigned to the 'end_date' field of the record.

                    If either the start date or duration is not available, the function does nothing.

                    Note: This method assumes that the 'start_date' and 'duration' fields are already populated.
        """
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
            for r in self:
                if not (r.start_date and r.duration):
                    continue

                r.duration = (r.end_date - r.start_date).days + 1
    #
    #
    #
