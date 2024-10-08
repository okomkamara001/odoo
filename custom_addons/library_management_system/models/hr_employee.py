from odoo import api, models, fields


class Employee(models.Model):
    _inherit = "hr.employee"

    department = fields.Char(string="Department")
    location = fields.Char(string="Branch/Location")
    academic_experience = fields.Char(string="Academic Experience")
    start_date = fields.Date(string="Start Date")
    expire = fields.Boolean(string="Expire")
    institution = fields.Char(string="Institution")
    institution_location = fields.Selection([("freetown", "Freetown"), ('bo', 'Bo'),
                                             ('makeni', 'Makeni'), ('lunsar', 'Lunsar')], string="Location")
    diploma = fields.Char(string="Diploma")
    field_of_study = fields.Char(string="Field of study")
    comment = fields.Text(string="Activities of association")
