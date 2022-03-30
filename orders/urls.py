from django.urls import path
from .views import CartAddView, MyCard, CartRemoveView



app_name = 'orders'
urlpatterns = [
    path('add/<int:product_id>', CartAddView.as_view(), name='add_order'),
    path('remove/<int:order_id>/<remove_full>', CartRemoveView.as_view(), name='remove_order'),
    path('card', MyCard.as_view(), name='user_card'),
]
