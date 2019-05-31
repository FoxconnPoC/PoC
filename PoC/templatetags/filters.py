from django import template
import pdb

register = template.Library()

@register.filter
def gkey(h, key):
    return h[key]
