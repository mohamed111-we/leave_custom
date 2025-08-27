from odoo import models, fields, api

class leaveCustom(models.AbstractModel):
    _name = 'report.leave_custom.leave_vacation_balances_all_employees'
    _description = 'leave Custom'

    @api.model
    def _get_report_values(self, docids, data=None):
        leaves = self.env['hr.leave'].browse(data.get('leaves', []))
        status_mapping = dict(self.env['hr.leave']._fields['state'].selection)

        return {
            'doc_ids': docids,
            'doc_model': 'leave.report.balances.wizard',
            'data': data,
            'leaves': leaves,
            'get_employee_name': lambda emp_id: self.env['hr.employee'].browse(emp_id).name,
            'state_filter_display': data.get('state_filter_display'),
            'get_status_display': lambda state: status_mapping.get(state, state),
        }

