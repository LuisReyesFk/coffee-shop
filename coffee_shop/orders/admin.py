from django.contrib import admin
from .models import Order, OrderProduct

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id_order',
        'user',
        'status',
        'total_price',
        'shipping_address',
        'payment_method',
        'tracking_number',
        'delivery_date',
        'created_at',
        'updated_at'
    )
    search_fields = ('user__username',)
    list_filter = ('status',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('user', 'status', 'total_price', 'shipping_address', 'payment_method')
        }),
        ('Tracking Information', {
            'fields': ('tracking_number', 'delivery_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Order, OrderAdmin)