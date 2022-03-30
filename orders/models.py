from django.db import models
from accounts.models import User
from store.models import Product
from extensions.utils import persian_numbers_converter




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user} ----> {self.product}'
    

    def new_price(self):
        price_to_str = str(self.number * self.product.price)
        right_price = ''
        for num, i in zip(price_to_str[::-1], range(1, len(price_to_str)+1)):
            right_price += num
            if i % 3 == 0 and i != len(price_to_str):
                right_price += ','
        return persian_numbers_converter(right_price[::-1])
    new_price.short_description = 'قیمت'
    
