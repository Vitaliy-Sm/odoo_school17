from odoo import models, fields


class HospitalPersonMixin(models.AbstractModel):
    _name = 'hospital.person'
    _description = 'Person mixin'

    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
    full_name = fields.Char(string='Full name')
    phone = fields.Char(required=False)
    photo = fields.Binary(required=False)
    gender = fields.Selection(
        default='male',
        required=True,
        selection=[
            ('male', 'Male'),
            ('female', 'Female'), ])
