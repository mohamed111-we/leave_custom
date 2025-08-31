{
    'name': 'Leave Management Custom',
    'version': '18.0.1.0',
    'summary': 'Custom module for managing employee leaves',
    'description': """
        This module provides custom functionality for managing employee leaves, 
        including leave requests, approvals, leave types, and tracking.
    """,
    'category': 'Human Resources',
    'author': 'Eng.Mathany Saad',
    'depends': ['base', 'hr_holidays', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/leave_vacation_balances_all_employees_wizard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'leave_custom/static/src/css/style.css',
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
