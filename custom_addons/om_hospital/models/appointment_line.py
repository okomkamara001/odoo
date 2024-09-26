# -*- coding: utf-8 -*-

import odoo
from odoo import api, models, fields


class HospitalAppointmentLine(models.Model):
    _name = "hospital.appointment.line"
    _description = "Hospital Appointment Line"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment Line")

    product_id = fields.Many2one('product.product', string='Product', required=True)
    qty = fields.Float(string='Quantity')

