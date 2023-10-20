# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alfonso_escobar(models.Model):
    _name = 'alfonso_escobar.task'
    _description = 'alfonso_escobar.alfonso_escobar'
    
    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    fecha = fields.Date()
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
