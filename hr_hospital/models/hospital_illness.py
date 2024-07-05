from odoo import fields, models


class HospitalIllness(models.Model):
    _name = 'hospital.illness'
    _description = 'List of illnesses'

    name = fields.Char()
    category_id = fields.Many2one(
        comodel_name='hospital.illness.category',
    )
