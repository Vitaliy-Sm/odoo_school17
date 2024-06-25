from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctors'
    _inherit = 'hospital.person'

    specialities_id = fields.Many2many(
        comodel_name='hospital.doctor.specialities',
    )
    is_intern = fields.Boolean(default=False, string='Intern')
    mentor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        domain="[('is_intern', '=', False)]",
    )
