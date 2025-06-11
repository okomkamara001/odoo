import odoo
from odoo import api, models, fields


class ResUsers(models.Model):
    """Inherited to prevent creating patients while creating users"""
    _inherit = "res.user"

    @api.model_create_multi
    def create(self, vals_list):
        """Override to add patient_seq to the partners created from users"""
        users = super().create(vals_list)
        for user in users:
            user.partner_id.patient_seq = 'User'
        return users
