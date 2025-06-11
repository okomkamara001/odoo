import odoo
from odoo import api, models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    patient_ids = fields.One2many("hospital.system", "partner_id")

