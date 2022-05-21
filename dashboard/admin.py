from django.contrib import admin
from .models import Product,Order
admin.site.site_header ="inventory"
class productAdmin(admin.ModelAdmin):
      list_display=('name','category','quantity')
      list_filter=('category',)

admin.site.register(Product,productAdmin)
admin.site.register(Order)
# Register your models here.
