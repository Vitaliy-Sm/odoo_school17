from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients'
    _inherit = 'hospital.person'

    name = fields.Char()
