from django import template
from blog.models import BlogCategory
register = template.Library()

@register.inclusion_tag("page/menu.html")
def menu():
    out = {}
    categories = BlogCategory.objects.all()
    out['cats'] = categories
    return out
