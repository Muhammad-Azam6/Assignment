# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
class Course(models.Model):

    _name='eacademy.course'
    _description = 'Eacademy'

    name = fields.Char(string='Course Name')
    description = fields.Text('Description', help='add course Description here')
    name_seq = fields.Char(string='Number' , required=True, copy=False, readonly=True, index=True,
                           default=lambda self: ('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', ('New')) == ('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'eacademy.course') or ('New')
            result = super(Course, self).create(vals)
            return result










