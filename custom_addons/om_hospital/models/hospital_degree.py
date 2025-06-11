import odoo
from odoo import api, models, fields

class HospitalDegree(models.Model):
    """class defining Hospital degree details"""

    _name= "hospital.degree"
    _description = "Degrees"


    name  = fields.Char(string="Degrees", help="Degrees of the staff")

    