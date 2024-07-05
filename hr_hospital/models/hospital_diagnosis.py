from odoo import fields, models


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'

    active = fields.Boolean(
        default=True,
    )
    name = fields.Char(
        required=True,
    )
    visit_id = fields.Many2one(
        comodel_name='hospital.patient.visit',
    )
    illness_id = fields.Many2one(
        comodel_name='hospital.illness',
    )
    description = fields.Char(
        required=True,
        string='Appointment for treatment',
    )
    approved = fields.Boolean(
        string='Approved by mentor',
    )
