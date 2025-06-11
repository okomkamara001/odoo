import odoo
from odoo import api, models, fields


class DoctorSpecialization(models.Model):
    """class holding doctor's specializations"""

    _name = "doctor.specialization"
    _description = "Doctor's Specialization"
    _rec_name = 'specialization'

    specialization = fields.Char(string="Specialization",
                                 help='Specify the name of specialization')


