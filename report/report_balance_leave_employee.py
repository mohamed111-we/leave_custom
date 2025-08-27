from odoo import fields, models, tools

class ReportBalanceLeaveEmployee(models.Model):
    _name = 'report.leave.balance.employee'
    _description = 'Leave Balance Report Employee'
    _auto = False

    emp_id = fields.Many2one('hr.employee', string="Employee", readonly=True)
    gender = fields.Char(string='Gender', readonly=True)
    department_id = fields.Many2one('hr.department', string='Department', readonly=True)
    country_id = fields.Many2one('res.country', string='Nationality', readonly=True)
    job_id = fields.Many2one('hr.job', string='Job', readonly=True)
    leave_type_id = fields.Many2one('hr.leave.type', string='Leave Type', readonly=True)
    allocated_days = fields.Integer(string='Allocated Balance')
    taken_days = fields.Integer(string='Taken Leaves')
    balance_days = fields.Integer(string='Remaining Balance')
    company_id = fields.Many2one('res.company', string="Company")

    def init(self):
        tools.drop_view_if_exists(self._cr, 'report_leave_balance_employee')
        self._cr.execute("""
            CREATE or REPLACE view report_leave_balance_employee as (
                SELECT row_number() over(ORDER BY e.id) as id,
                    e.id AS emp_id,
                    e.gender as gender,
                    e.country_id as country_id,
                    e.department_id as department_id,
                    e.job_id as job_id,
                    lt.id AS leave_type_id,
                    SUM(al.number_of_days) AS allocated_days,
                    SUM(CASE WHEN l.state ='validate' THEN l.number_of_days ELSE 0 END) AS taken_days,
                    SUM(al.number_of_days) - SUM(CASE WHEN l.state = 'validate' THEN l.number_of_days ELSE 0 END) AS balance_days,
                    e.company_id as company_id
                FROM hr_employee e
                JOIN hr_leave_allocation al ON al.employee_id = e.id
                JOIN hr_leave_type lt ON al.holiday_status_id = lt.id
                LEFT JOIN hr_leave l ON l.employee_id = e.id AND l.holiday_status_id = lt.id
                WHERE e.active = True
                GROUP BY e.id, lt.id
            )
        """)
