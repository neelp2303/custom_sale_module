from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductCategory(models.Model):
    _inherit = "product.category"

    _sql_constraints = [
        ("unique_category_name", "unique(name)", "Category name must be unique!"),
    ]

    @api.constrains("name")
    def _check_unique_category_name(self):
        for record in self:
            existing_category = self.env["product.category"].search(
                [("name", "=", record.name), ("id", "!=", record.id)]
            )
            if existing_category:
                raise ValidationError("Category name must be unique!")
