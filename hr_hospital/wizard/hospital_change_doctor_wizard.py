from odoo import fields, models


class ChangePersonalDoctor(models.TransientModel):
    _name = 'hospital.doctor.change.wizard'
    _description = 'Wizard to change personal doctor in batch'

    doctor_id = fields.Many2one('hospital.doctor', required=True)
    patient_ids = fields.Many2many('hospital.patient', required=True)

    def change_doctor(self):
        self.patient_ids.personal_doctor_id = self.doctor_id
