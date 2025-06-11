import odoo
from odoo import api, models, fields


class PrescriptionLine(models.Model):
    """Class holding prescription line details"""
    _name = 'prescription.line'
    _description = 'Prescription Lines'
    _rec_name = 'prescription_id'

    prescription_id = fields.Many2one('hospital.prescription',
                                      string='Prescription',
                                      help='Name of the prescription')
    medicine_id = fields.Many2one('product.template', domain=[
        '|', ('medicine_ok', '=', True), ('vaccine_ok', '=', True)],
                                  string='Medicine', required=True,
                                  help='Medicines or vaccines')
    quantity = fields.Integer(string='Quantity', required=True,
                              help="The number of medicines for the time "
                                   "period")
    no_intakes = fields.Float(string='Intakes', required=True,
                              help="How much medicine want to take")
    time = fields.Selection(
        [('once', 'Once in a day'), ('twice', 'Twice in a Day'),
         ('thrice', 'Thrice in a day'), ('morning', 'In Morning'),
         ('noon', 'In Noon'), ('evening', 'In Evening')], string='Time',
        required=True,
        help='The interval for medicine intake')
    note = fields.Selection(
        [('before', 'Before Food'), ('after', 'After Food')],
        string='Before/ After Food',
        help='Whether the medicine to be taken before or after food')
    inpatient_id = fields.Many2one('hospital.inpatient',
                                   string='Inpatient',
                                   help='The inpatient corresponds to the '
                                        'prescription line')
    outpatient_id = fields.Many2one('hospital.outpatient',
                                    string='Outpatient',
                                    help='The outpatient corresponds to the '
                                         'prescription line')
    hospital_patient_id = fields.Many2one('hospital.patient',
                                          string='Patient',
                                          help='The outpatient corresponds to the '
                                               'prescription line',
                                          related='outpatient_id.patient_id')
