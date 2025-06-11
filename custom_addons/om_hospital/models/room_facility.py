import odoo
from odoo import api, models, fields


class RoomFacility(models.Model):
    _name = "room.facility"
    _description = "Room Facility"


    name = fields.Char(string="Facilities", help="Name of room facility")