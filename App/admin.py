from django.contrib import admin

# Register your models here.
from .models import Farmer, Product, DeliveryService, Buyer, Order

admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(DeliveryService)
admin.site.register(Buyer)
admin.site.register(Order)

