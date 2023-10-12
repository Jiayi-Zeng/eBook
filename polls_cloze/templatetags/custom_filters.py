from django import template

register = template.Library()

@register.filter(name='get_value_from_key')
def get_value_from_key(dictionary, key):
    return dictionary.get(str(key), 0)