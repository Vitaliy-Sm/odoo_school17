from odoo import api, fields, models


class ChangePersonalDoctor(models.TransientModel):
    _name = 'hospital.doctor.change.wizard'
    _description = 'Wizard to change personal doctor in batch'

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        required=True,
    )
    patient_ids = fields.Many2many(
        comodel_name='hospital.patient',
        required=True,
    )

    def change_doctor(self):
        self.patient_ids.personal_doctor_id = self.doctor_id

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if self.env.context.get('active_ids'):
            res['patient_ids'] = [(6, 0, self.env.context.get('active_ids'))]
        return res
