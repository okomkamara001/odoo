import datetime
import calendar

import odoo
from odoo import api, models, fields

from odoo.tools import date_utils
from odoo.http import request
from dateutil.relativedelta import relativedelta
from datetime import datetime


class Dashboard(models.Model):
    _name = 'books.borrows'
    _description = "Books Dashboard"

    _inherit = 'books.borrows'
#
#

    @api.model
    def get_main_data(self):
        all_borrows = self.env['books.borrows'].search([('state', '=', 'running'), ('state', '=', 'delayed')])
        return {
            'total_individual': len(all_borrows),
        }

    @api.model
    def get_filter_data(self, text_value):
        # all_borrows
        all_borrows = self.env['books.borrows'].search(
            [('state', '=', 'running'), ('partner_id.name', 'ilike', text_value)])
        return {
            'total_borrows': len(all_borrows)
        }



