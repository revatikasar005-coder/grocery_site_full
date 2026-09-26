from django import template
from datetime import datetime

register = template.Library()

@register.filter
def jdDate(value):
    """Format datetime to date"""
    if isinstance(value, datetime):
        return value.strftime("%d-%m-%Y")
    return value

@register.filter
def jdTime(value):
    """Format datetime to time"""
    if isinstance(value, datetime):
        return value.strftime("%H:%M:%S")
    return value
