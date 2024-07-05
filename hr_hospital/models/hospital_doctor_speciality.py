from odoo import fields, models


class HospitalDoctorSpeciality(models.Model):
    _name = 'hospital.doctor.speciality'
    _description = 'Medical specialities'

    name = fields.Char(
        required=True,
    )
