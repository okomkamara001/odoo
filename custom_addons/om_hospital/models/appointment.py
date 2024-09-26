from email.policy import default

from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread']
    _description = "Hospital Appointment"
    _rec_names_search = ['reference', 'patient_id']
    _rec_name = 'patient_id'

    reference = fields.Char(string='Reference', default='New')
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=False, ondelete='restrict')
    date_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'Ongoing'),
                              ('done', 'Done'), ('cancel', 'Cancelled'), ], default='draft', tracking=True)
    appointment_line_ids = fields.One2many('hospital.appointment.line', 'appointment_id', string="Line")
    total_qty = fields.Float(compute='_compute_total_qty', string='Total Quantity', store=True)
    date_of_birth = fields.Date(string="DOB", related='patient_id.date_of_birth', store=True)

    @api.model_create_multi
    def create(self, vals_list):
        print('odoo idtlabs', vals_list)

        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')

        return super().create(vals_list)

    @api.depends('appointment_line_ids', 'appointment_line_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            print(rec.appointment_line_ids.mapped('qty'))
            # total_qty = 0
            # print(rec.appointment_line_ids)
            # for line in rec.appointment_line_ids:
            #     print("Line value", line.qty)
            #     total_qty += line.qty
            rec.total_qty = sum(rec.appointment_line_ids.mapped('qty'))

    def _compute_display_name(self):
        for rec in self:
            print("value is", f"[{rec.reference}] {rec.patient_id.name}")
            rec.display_name = f"[{rec.reference}] {rec.patient_id.name}"

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
            # print("button is clicked", self, rec)
            # print('referece..', self.reference)
            # print("note..", self.note)

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'
            # print("button is clicked", self, rec)
            # print('referece..', self.reference)
            # print("note..", self.note)

    def action_done(self):
        for rec in self:
            rec.state = 'done'
            # print("button is clicked", self, rec)
            # print('referece..', self.reference)
            # print("note..", self.note)

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
            # print("button is clicked", self, rec)
            # print('referece..', self.reference)
            # print("note..", self.note)
