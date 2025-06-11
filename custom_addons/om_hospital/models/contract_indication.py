import odoo
from odoo import api, models, fields


class ContraIndication(models.Model):
    """Class holding the contra indications details"""
    _name = 'contract.indication'
    _description = 'Contra Indication'
    _rec_name = 'blood_donation_question'

    blood_donation_question = fields.Text(string='Contra Indications',
                                          help='Contra indications of the '
                                               'blood donor')
