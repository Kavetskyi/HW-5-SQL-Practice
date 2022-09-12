from django import template
from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu_items_nav.html")
def menu_items_all():
    menu_items_list = MenuItem.objects.all()
    return {"menu_items_list": menu_items_list}
