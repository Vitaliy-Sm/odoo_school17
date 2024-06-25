from odoo import models, fields, api


class IllnessCategory(models.Model):
    _name = "hospital.illness.category"
    _description = "Illness Category"
    _parent_name = "parent_id"
    _parent_store = True
    rec_name = 'complete_name'
    _rec_order = 'complete_name'

    name = fields.Char(index=True, required=True)
    complete_name = fields.Char(
        recursive=True,
        compute='_compute_complete_name',
        store=True)
    parent_id = fields.Many2one(
        comodel_name='hospital.illness.category',
        string='Parent Category',
        index=True,
        ondelete='cascade')
    parent_path = fields.Char(unaccent=False, index=True)
    child_id = fields.One2many(
        comodel_name='hospital.illness.category',
        inverse_name='parent_id',
        string='Child Categories')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = \
                    f'{category.parent_id.name} / {category.name}'
            else:
                category.complete_name = category.name
