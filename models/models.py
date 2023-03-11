# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class addons_using_field_view_get(models.Model):
#     _name = 'addons_using_field_view_get.addons_using_field_view_get'
#     _description = 'addons_using_field_view_get.addons_using_field_view_get'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
