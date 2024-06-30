from datetime import datetime, time

from odoo import models, fields, _, api
from odoo.exceptions import UserError


class HospitalVisits(models.Model):
    _name = 'hospital.patient.visits'
    _description = 'Patient visits'

    active = fields.Boolean(default=True)
    name = fields.Char(compute='_compute_name', readonly=True)
    status = fields.Selection(
        default='planned',
        selection=[
            ('planned', _('Planned')),
            ('completed', _('Completed')),
            ('canceled', _('Canceled')), ])

    planned_visit_date = fields.Datetime()
    visit_date = fields.Datetime()
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        index=True,
    )
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        index=True,
    )
    diagnosis_ids = fields.One2many(
        comodel_name='hospital.diagnosis',
        inverse_name='visit_id',)

    @api.depends('visit_date', 'doctor_id', 'patient_id', 'planned_visit_date')
    def _compute_name(self):
        for rec in self:
            if rec.visit_date:
                rec.name = '%s - %s : %s' % (
                    rec.patient_id.name,
                    rec.doctor_id.name,
                    rec.visit_date.strftime('%d/%m/%Y %H:%M:%S'))
            elif rec.planned_visit_date:
                rec.name = '%s - %s : %s' % (
                    rec.patient_id.name,
                    rec.doctor_id.name,
                    rec.planned_visit_date.strftime('%d/%m/%Y %H:%M:%S'))
            else:
                rec.name = ''

    @api.onchange('doctor_id', 'visit_date')
    def _onchange_doctor_date(self):
        res = {}
        if self.visit_date:
            res['warning'] = {
                'title': _('Error!'),
                'message':
                    _('Can`t change Doctor or Visit date if fill visit date.')}
        return res

    @api.ondelete(at_uninstall=False)
    def _unlink_except_with_diagnosis(self):
        if any(rec.diagnosis_ids for rec in self):
            raise UserError(
                _('Can`t delete visit with a diagnosis.')
            )

    @api.constrains('active')
    def constrains_active(self):
        for obj in self:
            if not obj.active and any(rec.diagnosis_ids for rec in self):
                raise UserError(_('Can`t archive visit with diagnosis'))

    @api.constrains('planned_visit_date')
    def check_time_date(self):
        for rec in self:
            start_date = datetime.combine(
                rec.planned_visit_date.date(),
                time(0, 0, 0))
            end_date = datetime.combine(
                rec.planned_visit_date.date(),
                time(23, 59, 59))
            result = self.env['hospital.patient.visits'].search([
                ('doctor_id', '=', rec.doctor_id.id),
                ('patient_id', '=', rec.patient_id.id),
                ('planned_visit_date', '>=', start_date),
                ('planned_visit_date', '<=', end_date),
                ('id', '!=', rec.id),
            ])
            if result:
                raise UserError(_('Choose another day'))
