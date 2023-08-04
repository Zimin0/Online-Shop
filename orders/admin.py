from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'date', 'stage_status')

admin.site.register(Order, OrderAdmin)