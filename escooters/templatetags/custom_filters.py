from django import template

register = template.Library()


@register.filter
def filter_available(value):
    if value:
        return "В наличии"
    else:
        return "Нет в наличии"


@register.filter
def ordered_comments(value):
    return value.order_by('-created_day')
