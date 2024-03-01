from django import template

register = template.Library()



@register.filter
def persion_number(value):
    value = str(value)
    en_to_per = value.maketrans('0123456789','۰١٢٣٤٥٦٧٨٩')
    return value.translate(en_to_per)
