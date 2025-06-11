import odoo
from odoo import api, models, fields


class BloodDonation(models.Model):
    """Class holding blood donation details"""
    _name = 'blood.donation'
    _description = 'Blood Donation'
    _rec_name = 'questions'

    questions = fields.Text(string='Contract Indications',
                            help='Contraindications of the blood donor')
    is_true = fields.Boolean(string='Is True',
                             help='True for contract indications')
    blood_bank_id = fields.Many2one('blood.bank',
                                    string='Blood Bank',
                                    help='Blood bank corresponding to the '
                                         'donor')
