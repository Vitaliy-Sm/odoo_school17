from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients'
    _inherit = 'hospital.person'

    personal_doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        index=True,
    )
    visit_history_ids = fields.One2many(
        comodel_name='hospital.patient.visits',
        inverse_name='patient_id',
    )

    birthday_date = fields.Date(string='Date of Birth')
    age = fields.Integer(compute="_compute_age")
    passport = fields.Char()
    contact = fields.Char()

    def action_open_visit_history(self):
        return {
            'name': _('Visit History'),
            'view_mode': 'tree',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.patient.visits',
            'type': 'ir.actions.act_window',
            'domain': [('patient_id', '=', self.id)],
        }

    def action_create_visit(self):
        return {
            'name': _('Create Visit'),
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.patient.visits',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_patient_id': self.id},
        }

    @api.depends('birthday_date')
    def _compute_age(self):
        for rec in self:
            if rec.birthday_date:
                rec.age = relativedelta(
                    date.today(),
                    date(
                        rec.birthday_date.year,
                        rec.birthday_date.month,
                        rec.birthday_date.day),
                ).years
            else:
                rec.age = False
