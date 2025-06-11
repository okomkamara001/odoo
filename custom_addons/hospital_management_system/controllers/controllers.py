# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Hospital(http.Controller):
    # simple controller
    @http.route('/hospital/doctor', type='http', auth="public", website=True)
    def hospital_doctor(self, **kwargs):
        patients = request.env['hospital.system'].sudo().search([])
        print(patients)
        return request.render("hospital_management_system.patients_page", {
            'patients': patients
        })




# class HospitalManagementSystem(http.Controller):
#     @http.route('/hospital_management_system/hospital_management_system', type="http", auth='public', website=True)
#     def index(self, **kw):
#         return "Hello, world"
#
#     @http.route('/hospital_management_system/hospital_management_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_management_system.listing', {
#             'root': '/hospital_management_system/hospital_management_system',
#             'objects': http.request.env['hospital_management_system.hospital_management_system'].search([]),
#         })
#
#     @http.route('/hospital_management_system/hospital_management_system/objects/<model("hospital_management_system.hospital_management_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_management_system.object', {
#             'object': obj
#         })
