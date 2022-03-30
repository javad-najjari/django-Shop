from django.urls import path
from .views import (
    product_category_list, product_detail, list_category, all_products, about, add_reply
)



app_name = 'store'
urlpatterns = [
    path('', product_category_list, name='home'),
    path('detail/<int:product_id>', product_detail, name='detail'),
    path('list/<slug:slug>', list_category, name='list'),
    path('all-list', all_products, name='all'),
    path('about/', about, name='about'),
    path('reply/<int:product_id>/<int:comment_id>', add_reply, name='add_reply'),
]
