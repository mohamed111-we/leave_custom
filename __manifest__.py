{
    'name': 'Leave Management Custom',
    'version': '18.0.1.0',
    'summary': 'Custom module for managing employee leaves',
    'description': """
        This module provides custom functionality for managing employee leaves, 
        including leave requests, approvals, leave types, and tracking.
    """,
    'category': 'Human Resources',
    'author': 'Mohamed Yehya',
    'website': 'https://yourcompany.com',
    'depends': ['base','hr_holidays', 'hr'],
    'data': [
        'views/menu_leave_custom_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
