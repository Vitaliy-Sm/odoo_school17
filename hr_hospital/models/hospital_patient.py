from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patients'
    _inherit = 'hospital.person'

    personal_doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        index=True,
    )
    birthday_date = fields.Date(string='Date of Birth')
    age = fields.Integer(compute="_compute_age")
    passport = fields.Char()
    contact = fields.Char()

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
