from odoo import fields, models, _


class CreateDiagnosisReport(models.TransientModel):
    _name = 'hospital.diagnosis.report.wizard'
    _description = 'Diagnosis list report'

    doctor_ids = fields.Many2many(
        comodel_name='hospital.doctor',
        string="Doctor")
    illness_ids = fields.Many2many(
        comodel_name='hospital.illness',
        string="Illness")
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    def action_create_report(self):
        domain = [("create_date", ">=", str(self.start_date)),
                  ("create_date", "<=", str(self.end_date))]
        if self.doctor_ids:
            domain.append(("visit_id.doctor_id", "in", self.doctor_ids.ids))
        if self.illness_ids:
            domain.append(("illness_ids", "in", self.illness_ids.ids))

        return {
            'name': _('Diagnosis List Report'),
            'view_mode': 'tree',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.diagnosis',
            'type': 'ir.actions.act_window',
            'domain': domain,
            'context': {
                'group_by': 'illness_id',
            }
        }
