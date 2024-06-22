from odoo import models, fields


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'

    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
    visit_id = fields.Many2one(comodel_name='hospital.patient.visits')
    illness_id = fields.Many2one(comodel_name='hospital.illness')
    description = fields.Char(required=True,
                              string='Appointment for treatment')
    approved = fields.Boolean()
