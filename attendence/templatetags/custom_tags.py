from django import template
from datetime import datetime, timedelta

# from ..models import Attendance
register = template.Library()

@register.simple_tag
def current_month(format):
    today = datetime.today()
    return today.strftime(format)

@register.simple_tag
def prev_month(format):
    today = datetime.today()
    prev = (today.replace(day=1) - timedelta(1)).replace(day=1)
    return prev.strftime(format)
