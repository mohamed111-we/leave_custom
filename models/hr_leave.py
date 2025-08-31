from odoo import models, _, fields
from odoo.exceptions import UserError

class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'


    def unlink(self):
        for leave in self:
            if leave.state == 'validate':
                raise UserError(_("An approved leave cannot be deleted."))
        self.check_access('unlink')
        for record in self:
            self._cr.execute("DELETE FROM %s WHERE id = %%s" % self._table, (record.id,))
            record.invalidate_recordset()
        self._cr.commit()
        return True


