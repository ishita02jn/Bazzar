from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Removes all values of arg from the given string"""
    return value*arg