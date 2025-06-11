import odoo

from odoo import models, fields, api


class odoo_controller(models.Model):
    _name = 'odoo.controller'
    _description = 'Patients'


    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of Birth", help="Date of birth of the patients")
    gender = fields.Selection([("male", "male"), ("female", "female"), ('other', 'Other')], string="Gender",
                              help="Gender of the patients")
    partner_id = fields.Many2one('res.partner', string="Partner")
    notes = fields.Text()

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

