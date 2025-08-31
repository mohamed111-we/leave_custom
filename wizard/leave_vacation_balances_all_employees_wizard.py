from odoo import models, fields, _
from odoo.exceptions import UserError
import logging


class LeaveReportBalancesWizard(models.TransientModel):
    _name = 'leave.report.balances.wizard'
    _description = 'Leave Report Balances Wizard'

    employee_ids = fields.Many2many('hr.employee', string='Employees')
    leave_type_ids = fields.Many2many('hr.leave.type', string='Leave Types')

    def action_generate_report(self):
        self.ensure_one()

        report_domain = []
        if self.employee_ids:
            report_domain.append(('employee_id', 'in', self.employee_ids.ids))
        if self.leave_type_ids:
            report_domain.append(('holiday_status_id', 'in', self.leave_type_ids.ids))

        leaves = self.env['hr.leave'].search(report_domain)

        if not leaves:
            raise UserError(_("No leave records found."))

        print("==== Leave Report ====")
        for leave in leaves:
            print("Employee: %s | Type: %s | From: %s | To: %s | Days: %s | State: %s" %
                  (leave.employee_id.name,
                   leave.holiday_status_id.name,
                   leave.date_from,
                   leave.date_to,
                   leave.number_of_days,
                   leave.state))
        print("==== End of Report ====")

        return {
            'name': _('Leave Report'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr.leave',
            'view_mode': 'list,form',
            'domain': report_domain,
            'target': 'current',
        }
