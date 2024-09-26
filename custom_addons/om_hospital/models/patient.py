
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description = "Hospital Master"

    name = fields.Char(string="Name", required=True, tracking= True)
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection([("male", "male"), ("female", "female")], string="Gender")
    tag_ids = fields.Many2many("patient.tag", "patient_tag_rel", "patient_id", "tag_id", string="Tags")
    is_minor = fields.Boolean(string="Minor")
    guardian = fields.Char(string="Guardian")
    weight = fields.Float(string="Weight")

    @api.ondelete(at_uninstall=False)
    def _check_patient_appointments(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError(_('The appointment exist, You cannot delete the patient now!'))


    # def unlink(self):
    #     # any operation can be performed here
    #     for rec in self:
    #         domain = [('patient_id', '=', rec.id)]
    #         appointments = self.env['hospital.appointment'].search(domain)
    #         if appointments:
    #             raise UserError(_('The appointment exist' '\nYou cannot delete the patient now: %s' % rec.name))
    #     return super().unlink()
