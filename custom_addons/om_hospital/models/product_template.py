import odoo
from odoo import api, models, fields


class ProductTemplate(models.Model):
    """Inherited to add more fields and functions"""
    _inherit = "product.template"

    medicine_ok = fields.Boolean(string='Medicine', help='True for medicines')
    vaccine_ok = fields.Boolean(string="Vaccine", help='True for vaccines')
    pharmacy_id = fields.Many2one('hospital.pharmacy',
                                  string='Pharmacy',
                                  help='Name of the pharmacy')
    medicine_brand_id = fields.Many2one('medicine.brand',
                                        string='Brand',
                                        help='Indicates the brand of medicine '
                                             'or vaccine')

    @api.model
    def action_get_medicine_data(self):
        """Returns medicine list to the pharmacy dashboard"""
        medicines = []
        for rec in self.env['product.template'].sudo().search(
                [('medicine_ok', '=', True)]):
            medicines.append(
                [rec.name, rec.list_price, rec.qty_available, rec.image_1920, rec.id])
        return medicines

    @api.model
    def action_get_vaccine_data(self):
        """Returns vaccine list to the pharmacy dashboard"""
        vaccines = []
        for rec in self.env['product.template'].sudo().search(
                [('vaccine_ok', '=', True)]):
            vaccines.append(
                [rec.name, rec.list_price, rec.qty_available, rec.image_1920])
        return vaccines
