from django.shortcuts import render, redirect
from django.views import View
from orders.models import Order
from orders.forms import CartAddForm
from store.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import User



class CartAddView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        form = CartAddForm(request.POST)
        product = Product.objects.get(id=product_id)
        user = request.user
        if form.is_valid():
            if Order.objects.filter(user=user, product=product).exists():
                order = Order.objects.get(user=user, product=product)
                order.number += form.cleaned_data['quantity']
                order.save()
            else:
                Order.objects.create(user=user, product=product, number=form.cleaned_data['quantity'])
        return redirect('orders:user_card')


class CartRemoveView(LoginRequiredMixin, View):
    def get(self, request, order_id, remove_full):
        order = Order.objects.get(id=order_id)
        if order != None and request.user.id == order.user.id:
            if order.number == 1 or remove_full == 'True':
                order.delete()
            else:
                order.number -= 1
                order.save()
            return redirect('orders:user_card')
        else:
            messages.error(request, 'There is no order with these specifications ')


class MyCard(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        orders = Order.objects.filter(user=user)
        return render(request, 'orders/card.html', {'orders':orders})
    