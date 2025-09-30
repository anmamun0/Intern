from django import template

register = template.Library()

@register.filter
def dictkey(dict_data, key):
    return dict_data.get(key)
