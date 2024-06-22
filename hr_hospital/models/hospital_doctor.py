from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctors'
    _inherit = 'hospital.person'

    name = fields.Char()
