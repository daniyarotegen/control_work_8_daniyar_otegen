from django.contrib import admin
from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'rating', 'feedback')
    list_filter = ('product', 'author', 'rating')
    search_fields = ('product__name', 'author__username')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
