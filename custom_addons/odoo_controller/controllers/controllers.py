from logging import exception

import odoo
from odoo import http
from odoo.http import request


class OdooController(http.Controller):
    @http.route('/odoo_controller/odoo_controller', type='http', auth='public', website=True)
    def index(self, **kw):
        try:
            sales_order = http.request.env['sale.order'].sudo().search([])
        except:
            return "<h1>Can't access API</h1>"

        return http.request.render('odoo_controller.index', {
            'sales': sales_order,
        })

    @http.route('/odoo_controller/<model("sale.order"):so>/', type='http', auth='public', website=True)
    def display_salesorder(self, so):
        print(so["name"])
        return http.request.render('odoo_controller.sales_order', {
            'saleorder': so,
        })

        # output = '<h1>:::Sale Order!:::</h1><ul>'

        # for sale in sales_order:
        #     output += '<li>' + sale['name'] + '</li>'
        #
        # output += '</ul>'
        # return output

#     @http.route('/odoo_controller/odoo_controller/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_controller.listing', {
#             'root': '/odoo_controller/odoo_controller',
#             'objects': http.request.env['odoo_controller.odoo_controller'].search([]),
#         })

#     @http.route('/odoo_controller/odoo_controller/objects/<model("odoo_controller.odoo_controller"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_controller.object', {
#             'object': obj
#         })
