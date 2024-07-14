from odoo import _, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctors'
    _inherit = 'hospital.person'

    speciality_ids = fields.Many2many(
        comodel_name='hospital.doctor.speciality',
    )
    is_intern = fields.Boolean(
        string='Intern',
    )
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
    patient_ids = fields.One2many(
        comodel_name='hospital.patient',
        inverse_name='personal_doctor_id',
        string='Patients',
    )
    visit_history_ids = fields.One2many(
        comodel_name='hospital.patient.visit',
        inverse_name='doctor_id',
    )

    def action_new_visit(self):
        return {
            'name': _('Create Visit'),
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.patient.visit',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_doctor_id': self.id},
        }

    def action_open_diagnosis_to_approve(self):
        domain = [('approved', '=', False),
                  ('visit_id.doctor_id.mentor_id', '=', self.id)]

        return {
            'name': _('Diagnosis to approve'),
            'view_mode': 'tree,form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.diagnosis',
            'type': 'ir.actions.act_window',
            'domain': domain,
        }
