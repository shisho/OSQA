from django import template
import re

register = template.Library()

r_nofollow = re.compile('<a (?![^>]*nofollow)')
s_nofollow = '<a rel="nofollow" '

def nofollow(value):
    return r_nofollow.sub(s_nofollow, value)

register.filter(nofollow)