from odoo import models, fields
from collections import defaultdict


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @staticmethod
    def _group_by_category(po_lines):
        category_dict = defaultdict(list)
        for line in po_lines:
            if line.product_id.categ_id:
                category_dict[line.product_id.categ_id.id].append(line)
        return category_dict

    def action_confirm(self):
        category_dict = self._group_by_category(self.order_line)
        for category_id, lines in category_dict.items():
            new_po = self.copy(default={"order_line": []})
            new_po.order_line = [(6, 0, [line.id for line in lines])]
        return super(PurchaseOrder, self).action_confirm()
