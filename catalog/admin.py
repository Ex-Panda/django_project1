from django.contrib import admin

from catalog.models import Product, Category

# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'price', 'category_product',)
    list_filter = ('category_product',)
    search_fields = ('name_product', 'description_product',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category',)
