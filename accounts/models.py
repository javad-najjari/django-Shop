from django.db import models
from django.contrib.auth.models import AbstractUser
from extensions.utils import persian_numbers_converter



class User(AbstractUser):
    def total_price(self):
        total = 0
        right_price = ''
        for order in self.orders.all():
            total += (order.number * order.product.price)
        total = str(total)
        for num, i in zip(total[::-1], range(1, len(total) + 1)):
            right_price += num
            if i % 3 == 0 and i != len(total):
                right_price += ','
        return persian_numbers_converter(right_price[::-1])
    