import odoo
from odoo import api, models, fields


class EmployeeDepartment(models.Model):
    _inherit = "hr.department"

    name = fields.Char(string="Department")