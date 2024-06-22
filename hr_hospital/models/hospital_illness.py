from odoo import models, fields


class HospitalIllness(models.Model):
    _name = 'hospital.illness'
    _description = 'List of illnesses'

    name = fields.Char()
    category_id = fields.Many2one('hospital.illness.category')
