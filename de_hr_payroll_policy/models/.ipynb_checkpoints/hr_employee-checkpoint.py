# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HREmployee(models.Model):
    _inherit = 'hr.employee'
    
    leave_ded = fields.Boolean(string='Not Leave Deduction')
    stop_salary = fields.Boolean(string='Stop Salary')
