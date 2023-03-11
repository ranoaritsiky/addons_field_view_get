# -*- coding: utf-8 -*-
# from odoo import http


# class AddonsUsingFieldViewGet(http.Controller):
#     @http.route('/addons_using_field_view_get/addons_using_field_view_get', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons_using_field_view_get/addons_using_field_view_get/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons_using_field_view_get.listing', {
#             'root': '/addons_using_field_view_get/addons_using_field_view_get',
#             'objects': http.request.env['addons_using_field_view_get.addons_using_field_view_get'].search([]),
#         })

#     @http.route('/addons_using_field_view_get/addons_using_field_view_get/objects/<model("addons_using_field_view_get.addons_using_field_view_get"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons_using_field_view_get.object', {
#             'object': obj
#         })
