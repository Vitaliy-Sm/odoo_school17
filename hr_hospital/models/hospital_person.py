from odoo import _, fields, models


class HospitalPersonMixin(models.AbstractModel):
    _name = 'hospital.person'
    _description = 'Person mixin'

    active = fields.Boolean(
        default=True,
    )
    name = fields.Char(
        required=True,
    )
    full_name = fields.Char(
        string='Full name',
    )
    phone = fields.Char()
    photo = fields.Binary()
    gender = fields.Selection(
        default='male',
        required=True,
        selection=[
            ('male', _('Male')),
            ('female', _('Female')), ],
    )
