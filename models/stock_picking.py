from odoo import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # Define a Many2many field for tags from Sale Order
    sale_order_tags = fields.Many2many(
        "crm.tag",  # Adjust this model if necessary
        "stock_picking_sale_order_tag_rel",  # Unique relation table
        "picking_id",
        "tag_id",  # Unique column names
        string="Sale Order Tags",
    )

    # Ensure stock.picking has its own tag_ids field (if needed)
    tag_ids = fields.Many2many(
        "crm.tag",  # Adjust this model if necessary
        "stock_picking_tag_rel",  # Unique relation table
        "picking_id",
        "tag_id",  # Unique column names
        string="Tags",
    )

    def _prepare_procurement_group_vals(self):
        vals = super()._prepare_procurement_group_vals()
        vals["sale_order_tags"] = [(6, 0, self.tag_ids.ids)]  # Copy Tags
        return vals

    def _update_picking_tags(self):
        """Copy tags from Sale Order to Delivery Order."""
        for picking in self:
            if picking.origin:
                sale_order = self.env["sale.order"].search(
                    [("name", "=", picking.origin)], limit=1
                )
                if sale_order:
                    picking.sale_order_tags = [(6, 0, sale_order.tag_ids.ids)]

    def write(self, values):
        """Ensure tags are updated on change."""
        res = super().write(values)
        self._update_picking_tags()
        return res

    def action_done(self):
        res = super(StockPicking, self).action_done()
        for picking in self:
            if picking.sale_id and picking.state == "done":
                template = self.env.ref(
                    "your_module.mail_template_delivery_notification"
                )
                if template and picking.sale_id.user_id.email:
                    template.send_mail(picking.id, force_send=True)
        return res
