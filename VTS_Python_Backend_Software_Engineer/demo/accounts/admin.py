from django.contrib import admin
from .models import Product, Category
from django.http import HttpResponse
import csv

class ProductInline(admin.TabularInline):
    model = Product
    extra = 2

@admin.action(description="Mark selected products as published")
def make_published(modeladmin, request, queryset):
    queryset.update(stock=0)

@admin.action(description="Export selected products to CSV")
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Price'])
    for obj in queryset:
        writer.writerow([obj.id, obj.name, obj.price])
    return response

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    list_display = ('id', 'name', 'price', 'stock', 'is_in_stock')
    search_fields = ('name',)
    list_filter = ('category','name')
    ordering = ('-price',)
    list_editable = ('price', 'stock')
    actions = ['mark_out_of_stock', 'apply_discount',make_published,export_to_csv]
    readonly_fields = ('created_at', 'updated_at')

    # Action 1
    def mark_out_of_stock(self, request, queryset):
        updated = queryset.update(stock=0)
        self.message_user(request, f"{updated} product(s) marked as out of stock.")
    mark_out_of_stock.short_description = "Mark selected %(verbose_name_plural)s as Out of Stock"


    def apply_discount(self, request, queryset):
        for product in queryset:
            product.price = product.price * 10
            product.save()
        self.message_user(request, "10% discount applied successfully.")
    apply_discount.short_description = "Apply 10%% Discount to selected %(verbose_name_plural)s"


    # Custom column
    def is_in_stock(self, obj):
        return obj.stock > 0
    is_in_stock.boolean = True
    is_in_stock.short_description = "Available?"

    # Auto-assign user
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [ProductInline]


# Branding Admin
admin.site.site_header = "My Company Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to My Dashboard"
