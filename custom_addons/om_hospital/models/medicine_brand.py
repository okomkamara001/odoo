
import odoo
from odoo import api, models, fields

class MedicineBrand(models.Model):
    """Model holding all medicine brands"""
    _name = 'medicine.brand'
    _description = 'Medicine Brand'

    name = fields.Char(string="Brand", help='Name of the brand')
    medicine_ids = fields.One2many('product.template',
                                   'medicine_brand_id',
                                   string='Medicine',
                                   help='All medicines belongs to this brand')