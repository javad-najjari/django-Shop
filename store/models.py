from django.db import models
from extensions.utils import persian_numbers_converter
from accounts.models import User


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE, related_name='branches', verbose_name='والد')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='آدرس دسته بندی')
    image = models.ImageField(upload_to='%Y/%m/%d', verbose_name='تصویر', null=True, blank=True)

    def __str__(self):
        return self.title



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته بندی')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(null=True, blank=True, verbose_name='قیمت')
    date = models.DateField(auto_now_add=True, verbose_name='تاریخ')
    time = models.TimeField(auto_now_add=True, verbose_name='ساعت')
    photo = models.ImageField(upload_to='%Y/%m/%d', verbose_name='تصویر')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='آدرس محصول')

    def __str__(self):
        return self.title
    
    def short_content(self):
        return self.description[:50]
    
    def show_price(self):
        price_to_str = str(int(self.price))
        right_price = ''
        for num, i in zip(price_to_str[::-1], range(1, len(price_to_str)+1)):
            right_price += num
            if i % 3 == 0 and i != len(price_to_str):
                right_price += ','
        return persian_numbers_converter(right_price[::-1])
    show_price.short_description = 'قیمت'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='user_comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comments')
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='reply_comments', null=True, blank=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(verbose_name='متن کامنت')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
    
    def __str__(self):
        return f'{self.author} - {self.body[:30]}'
    
