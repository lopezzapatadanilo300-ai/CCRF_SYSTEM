from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def miles(value):
    try:
        return intcomma(int(value)).replace(',', '.')
    except:
        return value