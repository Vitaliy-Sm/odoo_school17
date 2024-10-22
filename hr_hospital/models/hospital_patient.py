from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients'
    _inherit = 'hospital.person'

    personal_doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        index=True,
    )
    visit_history_ids = fields.One2many(
        comodel_name='hospital.patient.visit',
        inverse_name='patient_id',
    )
    birthday_date = fields.Date(
        string='Date of Birth',
    )
    age = fields.Integer(
        compute="_compute_age",
    )
    passport = fields.Char()
    contact = fields.Char()
    last_visit_status = fields.Char(
        compute="_compute_last_visit_status",
    )

    @api.depends('visit_history_ids')
    def _compute_last_visit_status(self):
        for rec in self:
            if rec.visit_history_ids:
                rec.last_visit_status = rec.visit_history_ids[-1].status
            else:
                rec.last_visit_status = ''

    def action_open_visit_history(self):
        return {
            'name': _('Visit History'),
            'view_mode': 'tree',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.patient.visit',
            'type': 'ir.actions.act_window',
            'domain': [('patient_id', '=', self.id)],
        }

    def action_create_visit(self):
        return {
            'name': _('Create Visit'),
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.patient.visit',
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
