from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'brand', 'is_active']
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_editable = ['price', 'is_active']



admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Color)
admin.site.register(models.RAM)
admin.site.register(models.Storage)
admin.site.register(models.Warranty)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductVisit)
admin.site.register(models.ProductGallery)
admin.site.register(models.ProductComment)
