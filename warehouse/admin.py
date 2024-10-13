from django.contrib import admin
from warehouse.models import Godown, Item


class GodownAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent_godown']
    search_fields = ['name']
    list_filter = ['parent_godown']
    ordering = ['name']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'name', 'quantity',
                    'category', 'price', 'status', 'godown']
    search_fields = ['name', 'category', 'brand']
    list_filter = ['category', 'status', 'godown']
    ordering = ['name']


# Register the models with their corresponding admin classes
admin.site.register(Godown, GodownAdmin)
admin.site.register(Item, ItemAdmin)
