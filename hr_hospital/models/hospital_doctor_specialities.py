from odoo import models, fields


class HospitalDoctorSpecialities(models.Model):
    _name = 'hospital.doctor.specialities'
    _description = 'Medical specialities'

    name = fields.Char(required=True)
