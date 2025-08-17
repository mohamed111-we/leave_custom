from odoo import models, _, fields
from odoo.exceptions import UserError

class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    holiday_status_id = fields.Many2one('hr.leave.type', string="Time Off Type")
    name = fields.Char(string="Description")
    date_from = fields.Datetime(string="Start Date")
    date_to = fields.Datetime(string="End Date")
    duration_display = fields.Char(string="Duration")
    state = fields.Selection([
        ('confirm', 'To Approve'),
        ('refuse', 'Refused'),
        ('validate1', 'Second Approval'),
        ('validate', 'Approved'),
        ('cancel', 'Cancelled'),
    ], string='Status', store=True, tracking=True, copy=False, readonly=False, default='confirm')



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


    def re_caculate(self):
        for rec in self:
            pass



    # def unlink(self):
    #     for leave in self:
    #         if leave.state == 'validate':
    #             raise UserError(_("لا يمكن حذف إجازة تمت الموافقة عليها."))
    #
    #     self.check_access_rights('unlink')
    #     self.check_access_rule('unlink')
    #
    #     for record in self:
    #         self._cr.execute("DELETE FROM %s WHERE id = %%s" % self._table, (record.id,))
    #
    #         record.invalidate_recordset()
    #
    #     self._cr.commit()
    #
    #     return True
