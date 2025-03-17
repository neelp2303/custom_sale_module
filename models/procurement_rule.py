from odoo import models, api, defaultdict


class ProcurementRule(models.Model):
    _inherit = "procurement.group"

    @api.model
    def _run_buy(self, procurements, partner):
        """Override _run_buy to split POs based on product categories."""
        grouped_procurements = defaultdict(list)

        # Group procurements by product category
        for procurement, rule in procurements:
            product_category = procurement.product_id.categ_id
            grouped_procurements[product_category].append((procurement, rule))

        po_vals_list = []
        for category, category_procurements in grouped_procurements.items():
            po_vals = self._prepare_purchase_order(category_procurements, partner)
            po_vals_list.append(po_vals)

        # Create separate POs per category
        purchase_orders = self.env["purchase.order"].create(po_vals_list)

        # Confirm all POs
        purchase_orders.button_confirm()
        return purchase_orders

    def _prepare_purchase_order(self, procurements, partner):
        """Prepare the purchase order values based on procurements."""
        first_procurement = procurements[0][0]
        return {
            "partner_id": partner.id,
            "order_line": [
                (0, 0, self._prepare_po_line(procurement))
                for procurement, _ in procurements
            ],
        }

    def _prepare_po_line(self, procurement):
        """Prepare the purchase order line values."""
        return {
            "product_id": procurement.product_id.id,
            "product_qty": procurement.product_qty,
            "product_uom": procurement.product_uom.id,
            "price_unit": procurement.product_id.standard_price,
            "date_planned": procurement.date_planned,
        }
