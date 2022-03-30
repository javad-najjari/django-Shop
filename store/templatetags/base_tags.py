from django import template
from ..forms import ProductSearchForm


register = template.Library()


@register.inclusion_tag('store/partials/hover.html')
def hover_navbar(request, title, app, link, more_class=None):
    return {
        'request': request,
        'title': title,
        'link': link,
        'link_url': '{}:{}'.format(app, link),
        'more_class': more_class,
    }


@register.inclusion_tag('store/partials/search.html')
def search_box():
    context = {
        'search_box': ProductSearchForm,
    }
    return context
    