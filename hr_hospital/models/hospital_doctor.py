from odoo import models, fields, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctors'
    _inherit = 'hospital.person'

    specialities_ids = fields.Many2many(
        comodel_name='hospital.doctor.specialities',
    )
    is_intern = fields.Boolean(default=False, string='Intern')
    mentor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        domain="[('is_intern', '=', False)]",
    )

    intern_ids = fields.One2many(
        comodel_name='hospital.doctor',
        inverse_name='mentor_id',
        string='Interns',
        readonly=True,
    )

    def action_new_visit(self):
        return {
            'name': _('Create Visit'),
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.patient.visits',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_doctor_id': self.id},
        }
