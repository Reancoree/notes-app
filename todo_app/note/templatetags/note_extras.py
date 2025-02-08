from django import template

register = template.Library()


@register.inclusion_tag('note/tags/show_notes.html')
def show_notes(notes):
    return {'notes': notes}
