import odoo
from odoo import api, models, fields


class NursingPlan(models.Model):
    """Class holding nursing plan"""
    _name = 'nursing.plan'
    _description = "Nursing Plan"

    admission_id = fields.Many2one('hospital.inpatient',
                                   string='Patient',
                                   help='Name of the inpatient')
    date = fields.Datetime(string='Visit Time', help='Date and time of visit')
    status = fields.Char(string='Status',
                         help='Physical condition of the patient')
    notes = fields.Text(string='Note', help='You can add the notes here')
