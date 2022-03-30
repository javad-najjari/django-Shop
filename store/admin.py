from django.contrib import admin
from .models import Product, Category, Comment



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'category']

admin.site.register(Product, ProductAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']

admin.site.register(Category, CategoryAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'is_reply']

admin.site.register(Comment, CommentAdmin)
