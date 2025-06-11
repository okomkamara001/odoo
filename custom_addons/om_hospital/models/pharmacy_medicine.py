import odoo
from odoo import api, models, fields

class PharmacyMedicine(models.Model):
    """class holding pharmacy medicine details"""

    _name = "pharmacy.medicine"
    _description = "Pharmacy Medicine"
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.template',
                                 string='Medicine',
                                 help='Name of medicine',
                                 domain="[('medicine_ok', '=', True)]")
    pharmacy_id = fields.Many2one('hospital.pharmacy',
                                  string='Pharmacy',
                                  help='Name of pharmacy')
    # qty_available = fields.Float(related='product_id.qty_available',
    #                              string='Available Quantity',
    #                              help='The quantity of product available')
    list_price = fields.Float(related='product_id.list_price', string='Price',
                              help='Price of the medicine')