from django.contrib import admin
from . import models

admin.site.register(models.cart)
admin.site.register(models.order)
admin.site.register(models.order_products)
admin.site.register(models.product)
admin.site.register(models.category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()