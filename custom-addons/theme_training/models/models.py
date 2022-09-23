from odoo import models

class ThemeOriginal(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_original_post_copy(self, mod):
        # This method is called after the copy of the views.
        # You can put your own code here.
        pass