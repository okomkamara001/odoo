# -*- coding: utf-8 -*-
import odoo
from datetime import datetime, timedelta, date
from odoo import api, models, fields
from odoo.api import ondelete


class Borrows(models.Model):
    _name = 'books.borrows'
    _inherit = ['mail.thread']
    _description = 'books.borrows'
    _rec_name = 'name_id'

    reference = fields.Char(string='Reference', default='New')
    name_id = fields.Many2one('books.author', string="Name", required=False, ondelete='restrict')
    book_id = fields.Many2one('books.data', string='Book')
    start_borrow = fields.Datetime(string="Start Borrow")
    email = fields.Char(string='Email Borrower', size=256, related='name_id.email', readonly=True)
    phone_number = fields.Char(string="Phone Number", related='name_id.phone_number', readonly=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'Ongoing'),
                              ('done', 'Done'), ('cancel', 'Cancelled'), ], default='draft', tracking=True)
    end_borrow = fields.Datetime(string="End Borrow", store='True')

    daily_price = fields.Float(string="Day Price", related='book_id.price')
    color = fields.Integer()
    duration = fields.Integer()
    received_date = fields.Datetime()
    delay_duration = fields.Float(string="Delay Duration", readonly=True)
    # delay_penalties_id = fields.Many2one('delay.penalities', string="Delay Penalties")
    borrows_duration = fields.Float(string="Borrows Duration")
    sub_total = fields.Integer(compute='_compute_sub_s_total', store=True)
    total_money = fields.Float(compute='_compute_total', store=True, string="Total Money")
    # book_copy_id = fields.Many2one('book.copies', string="Copies")
    book_copy_list_id = fields.Many2one('book.copies')
    note = fields.Text(string='Note')

    @api.model_create_multi
    def create(self, vals_list):
        print('odoo idtlabs', vals_list)

        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('books.borrows')

        return super().create(vals_list)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'
            # print("button is clicked", self, rec)
            # print('referece..', self.reference)
            # print("note..", self.note)

    def action_done(self):
        for rec in self:
            rec.state = 'done'
            # print("button is clicked", self, rec)
            # print('referece..', self.reference)
            # print("note..", self.note)

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
            # print("button is clicked", self, rec)
            # print('referece..', self.reference)
            # print("note..", self.note)
    # print("button is clicked", self, rec)
    # print('referece..', self.reference)
    # print("note..", self.note)
    # partner_id = fields.Many2one('res.partner', string='Partner')
    # place = fields.Char(related="book_copy_id.place")

    # @api.model_create_multi
    # def create(self, vals_list):
    #     print('odoo idtlabs', vals_list)
    #
    #     for vals in vals_list:
    #         if not vals.get('reference') or vals['reference'] == 'New':
    #             vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
    #
    #     return super().create(vals_list)
    #
    # def action_confirm(self):
    #     for rec in self:
    #
    #         rec.state = 'confirmed'
    #         # print("button is clicked", self, rec)
    #         # print('referece..', self.reference)
    #         # print("note..", self.note)
    #
    # def action_ongoing(self):
    #     for rec in self:
    #
    #         rec.state = 'ongoing'
    #         # print("button is clicked", self, rec)
    #         # print('referece..', self.reference)
    #         # print("note..", self.note)
    #
    # def action_done(self):
    #     for rec in self:
    #
    #         rec.state = 'done'
    #         # print("button is clicked", self, rec)
    #         # print('referece..', self.reference)
    #         # print("note..", self.note)
    #
    # def action_cancel(self):
    #     for rec in self:
    #
    #         rec.state = 'cancel'
    #         # print("button is clicked", self, rec)
    #         # print('referece..', self.reference)
    #         # print("note..", self.note)

#
#     def action_report(self):
#         # function to report wornning
#         return self.env.ref('report_borrows_warning_id').report_action(self)
#
#     @api.onchange('start_borrow', 'end_borrow')
#     def states_test(self):
#         # when sdate <= today <= edate state=running else state=draft
#         sdate = self.start_borrow
#         edate = self.end_borrow
#         today = datetime.now()
#         if sdate and edate:
#             if sdate <= today <= edate:
#                 self.state = 'running'
#             else:
#                 self.state = 'draft'
#         else:
#             self.state = 'draft'
#
#     @api.onchange('borrows_duration')
#     def _onchange_borrows_duration(self):
#         #
#         if self.borrows_duration and self.start_borrow:
#             start_date = fields.Datetime.from_string(self.start_borrow)
#             new_end_date = start_date + timedelta(days=self.borrows_duration)
#             self.end_borrow = new_end_date
#
#     @api.onchange('start_borrow', 'end_borrow')
#     def _onchange_da_tes(self):
#         '''
#                 to calculate period of borrows Duration based on start deta and end date
#         '''
#         if self.start_borrow and self.end_borrow:
#             delta = self.end_borrow - self.start_borrow
#             if delta.days < 0:
#                 nod = 0
#             else:
#                 nod = delta.days
#             self.borrows_duration = nod
#         else:
#             self.borrows_duration = 0
#
#     @api.onchange('book_copy_id')
#     def _onchange_book_copy_id(self):
#         # function depend on book_copies
#         # if customer take copy available can change in the model book_copies state = borrowed
#         if self.book_copy_id and self.book_copy_id.state == 'available':
#             self.book_copy_id.state = 'borrowed'
#
#     @api.depends('start_borrow', 'duration')
#     def _get_end_date_(self):
#         '''
#         This method is decorated with @api.depends('start_borrow', 'duration'), which means it will be automatically triggered and recompute the field end_borrow whenever the start_borrow or duration fields are modified.
# It iterates over each record (r) in the current recordset (self).
# Inside the loop, it checks if both start_borrow and duration fields are set (if not (r.start_borrow and r.duration)).
# If either start_borrow or duration is not set, it sets the end_borrow field to the value of start_borrow and continues to the next record (continue).
# If both start_borrow and duration are set, it calculates the duration in days as a timedelta object using the timedelta function and subtracting one second (duration = timedelta(days=r.duration, seconds=-1)).
# Finally, it sets the end_borrow field by adding the duration to the start_borrow (r.end_borrow = r.start_borrow + duration).
#         '''
#         for r in self:
#             if not (r.start_borrow and r.duration):
#                 r.end_borrow = r.start_borrow
#                 continue
#             duration = timedelta(days=r.duration, seconds=-1)
#             r.end_borrow = r.start_borrow + duration
#
#     def _set_end_date(self):
#         for r in self:
#             if not (r.start_borrow and r.duration):
#                 continue
#
#             r.duration = (r.end_borrow - r.start_borrow).days + 1
#
#     def action_ended(self):
#
#         """
#          Perform the action of change the borrow to the 'ended' state.
#        """
#         self.received_date = datetime.now().strftime('%Y-%m-%d')
#         self.state = 'ended'
#         self.book_copy_id.state = 'available'
#
#
#
#
#     def action_draft(self):
#         # button to reset to draft
#         for rec in self:
#             rec.state = 'draft'
#
#
#     @api.onchange('book_id')
#     def _onchange_book_id(self):
#         '''  Perform a search to find available copies of the selected book
#             Return a domain filter to restrict the available options for the book_copy_id field
#         '''
#         book_copies = self.env['book.copies'].search(
#             [("book_id", "=", self.book_id.id), ('state', '=', 'available')]).ids
#         self.book_copy_id = False
#         self.book_copy_list_id = [(6, 0, book_copies)]
#
#
#
#
#
#     @api.onchange('end_borrow', 'received_date')
#     def onchange_dates(self):
#         '''
#         to calculate delay_duration based on end_borrow and received_date
#          delay_duration = received_date - end_borrow
#         '''
#         if self.end_borrow and self.received_date:
#             delta = self.received_date - self.end_borrow
#             if delta.days < 0:
#                 nod = 0
#             else:
#                 nod = delta.days
#             self.delay_duration = nod
#         else:
#             self.delay_duration = 0
#
#     @api.depends('daily_price', 'borrows_duration')
#     def _compute_sub_s_total(self):
#         '''
#         to calculate sub_total based on (daily_price) and (borrows_duration)
#         daily_price * borrows_duration =sub_total
#         '''
#         for rec in self:
#             sub_total = 0.0
#             if rec.borrows_duration and rec.daily_price:
#                 sub_total = rec.borrows_duration * rec.daily_price
#             rec.sub_total = sub_total
#
#
#
#     @api.depends('sub_total', 'delay_penalties_id')
#     def _compute_total(self):
#         '''
#         to calculate total money of period borrowed user
#         based on sub_total and delay_penalties
#         '''
#         for rec in self:
#             total_money = 0.0
#             if rec.sub_total and rec.delay_penalties_id:
#                 total_money = rec.sub_total + rec.delay_penalties_id
#             rec.total_money = total_money
#
#     # cron jop
#     def update_delayed_status(self):
#         # cron job every day to check state =running $ end_borrow < date today  change state from running to delayed
#         today = date.today()
#         running_borrows = self.env['books.borrows'].search([('state', '=', 'running'), ('end_borrow', '<', today)])
#         for rec in running_borrows:
#             if rec:
#                 rec.state = 'delayed'
#
# #
# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#
#     borrow_ids = fields.One2many('books.borrows', 'name_id', string='Books')
