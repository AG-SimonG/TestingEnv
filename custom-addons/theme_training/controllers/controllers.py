# -*- coding: utf-8 -*-
# from odoo import http


# class ThemeTraining(http.Controller):
#     @http.route('/theme_training/theme_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_training/theme_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_training.listing', {
#             'root': '/theme_training/theme_training',
#             'objects': http.request.env['theme_training.theme_training'].search([]),
#         })

#     @http.route('/theme_training/theme_training/objects/<model("theme_training.theme_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_training.object', {
#             'object': obj
#         })
