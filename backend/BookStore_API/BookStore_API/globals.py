from enum import Enum

PAYMENT_METHOD = (
    ('online', 'Online'),
    ('offline', 'Offline'),
)

STATUS_PAYMENT = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
)

STATUS_ORDER = (
    ('ordered', 'Ordered'),
    ('cancelled', 'Cancelled'),
    ('delivered', 'Delivered'),
)

ADDRESS_STATUS = (
    ('current', 'Current'),
    ('old', 'Old'),
)