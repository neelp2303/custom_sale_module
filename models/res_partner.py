from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        result = []
        for partner in self:
            ref = partner.ref if partner.ref else "NoRef"
            name = f"{partner.name} [{ref}]" if partner.name else "Unknown"
            result.append((partner.id, name))
        return result

    def _compute_display_name(self):
        """Modify the display name to include ref field"""
        for partner in self:
            if partner.ref:
                partner.display_name = f"{partner.name} [{partner.ref}]"
            else:
                partner.display_name = partner.name
