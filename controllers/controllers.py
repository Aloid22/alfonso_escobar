# -*- coding: utf-8 -*-
# from odoo import http


# class AlfonsoEscobar(http.Controller):
#     @http.route('/alfonso_escobar/alfonso_escobar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alfonso_escobar/alfonso_escobar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alfonso_escobar.listing', {
#             'root': '/alfonso_escobar/alfonso_escobar',
#             'objects': http.request.env['alfonso_escobar.alfonso_escobar'].search([]),
#         })

#     @http.route('/alfonso_escobar/alfonso_escobar/objects/<model("alfonso_escobar.alfonso_escobar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alfonso_escobar.object', {
#             'object': obj
#         })
