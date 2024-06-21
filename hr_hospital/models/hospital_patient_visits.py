from odoo import models, fields


class HospitalVisits(models.Model):
    _name = 'hospital.patient.visits'
    _description = 'Patient visits'

    name = fields.Char()
