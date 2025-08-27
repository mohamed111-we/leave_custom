from odoo import models, fields
from odoo.exceptions import UserError


class LeaveReportBalancesWizard(models.TransientModel):
    _name = 'leave.report.balances.wizard'
    _description = 'Leave Report Balances Wizard'

    employee_ids = fields.Many2many(
        'hr.employee',
        string='Employees',
        required=True
    )
    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')
    report_type = fields.Selection([
        ('pdf', 'PDF'),
        ('xlsx', 'XLSX'),
    ], string='Report Type', default='pdf')
    state_filter = fields.Selection([
        ('validate', 'Approved'),
        ('all', 'All Statuses'),
        ('confirm', 'To Approve'),
        ('refuse', 'Refused'),
    ], string='Leave Status', default='validate')


    def action_generate_report(self):
        self.ensure_one()
        domain = [('employee_id', 'in', self.employee_ids.ids)]
        print('domain for employee=====>> ', domain)

        if self.state_filter != 'all':
            domain.append(('state', '=', self.state_filter))

        if self.date_from:
            domain.append(('date_from', '<=', self.date_to))

        if self.date_to:
            domain.append(('date_to', '>=', self.date_from))

        leaves = self.env['hr.leave'].search(domain)
        print('domain========================>> ',domain)

        if not leaves:
            raise UserError("No leaves found for the selected criteria.")
