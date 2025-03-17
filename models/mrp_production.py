from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def write(self, vals):
        if "product_qty" in vals:
            for record in self:
                if record.state in ["confirmed", "progress"]:  # Adjust states if needed
                    raise api.UserError(
                        "You cannot change the quantity of a confirmed manufacturing order."
                    )
        return super(MrpProduction, self).write(vals)
