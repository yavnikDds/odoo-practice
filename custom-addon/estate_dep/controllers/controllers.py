# -*- coding: utf-8 -*-
# from odoo import http


# class EstateDep(http.Controller):
#     @http.route('/estate_dep/estate_dep', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate_dep/estate_dep/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate_dep.listing', {
#             'root': '/estate_dep/estate_dep',
#             'objects': http.request.env['estate_dep.estate_dep'].search([]),
#         })

#     @http.route('/estate_dep/estate_dep/objects/<model("estate_dep.estate_dep"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate_dep.object', {
#             'object': obj
#         })

