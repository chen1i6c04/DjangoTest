from django.contrib import admin
from .models import Store
from .models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes')
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)


admin.site.unregister(Store)
admin.site.register(Store, StoreAdmin)
# Register your models here.
