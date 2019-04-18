
from django.contrib import admin


from .models import Product,Offer

class ProductImp(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
class OfferImp(admin.ModelAdmin):
    list_display = ('code', 'description')



admin.site.register(Product, ProductImp)
admin.site.register(Offer, OfferImp)
