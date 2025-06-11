# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryManagementSystem(http.Controller):
#     @http.route('/library_management_system/library_management_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_management_system/library_management_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_management_system.listing', {
#             'root': '/library_management_system/library_management_system',
#             'objects': http.request.env['library_management_system.library_management_system'].search([]),
#         })

#     @http.route('/library_management_system/library_management_system/objects/<model("library_management_system.library_management_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_management_system.object', {
#             'object': obj
#         })

