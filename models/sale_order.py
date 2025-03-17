from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_picking(self):
        """Ensure that Sale Order tags are copied to the Delivery Order"""
        res = super()._prepare_picking()
        if self.tag_ids:
            res["sale_order_tags"] = [(6, 0, self.tag_ids.ids)]
        return res
