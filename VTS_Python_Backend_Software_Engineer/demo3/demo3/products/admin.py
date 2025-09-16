from django.contrib import admin
from django.utils import timezone
from .models import Category,Product 
from django.contrib import admin
from .models import Product,Category, Cart, CartItem, Order

admin.site.site_header = "E-commerce Admin"
admin.site.site_title = "LocalStore Admin Portal"
admin.site.index_title = "Welcome to the e-commerce Admin"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = (
        "id", "name", "price", "stock", "category", "user",
        "created_at", "updated_at"
    ) 
    list_editable = ("price", "stock")
    search_fields = ("name", "description", "category__name", "user__username")
    list_filter = ("category", "user", "created_at", "updated_at")
    ordering = ("-created_at",)
    list_per_page = 10
    readonly_fields = ("created_at", "updated_at") 

    actions = ["set_out_of_stock", "set_in_stock"]

    def set_out_of_stock(self, request, queryset):
        updated = queryset.update(stock=0)
        self.message_user(request, f"{updated} product(s) marked as Out of Stock.")
    set_out_of_stock.short_description = "Mark Out of Stock"

    def set_in_stock(self, request, queryset):
        updated = queryset.update(stock=10)  
        self.message_user(request, f"{updated} product(s) marked as In Stock (10).")
    set_in_stock.short_description = "Mark as In Stock (10)"
 

from django.contrib import admin
from .models import Category


class ChapterInline(admin.StackedInline):
    model = Product
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "product_count")
    search_fields = ("name", "description")
    ordering = ("name",)
    list_per_page = 20 
    inlines = [ChapterInline]
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = "Total Products"
 



class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    fields = ("product", "quantity")
    autocomplete_fields = ("product",) 


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "total_items","total_prices")
    list_filter = ("created_at", "user")
    search_fields = ("user__username", "id")
    ordering = ("-created_at",)
    inlines = [CartItemInline]

    def total_prices(self,obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())
    total_prices.sort_description = "Total Prices"

    def total_items(self, obj):
        return obj.items.count()
    total_items.short_description = "Items in Cart"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "cart", "total_price", "status", "created_at")
    list_filter = ("status", "created_at", "user")
    search_fields = ("user__username", "cart__id")
    ordering = ("-created_at",)
    list_editable = ("status",)
    autocomplete_fields = ("cart", "user")
    readonly_fields = ("total_price",)  

    actions = ["mark_as_shipped", "mark_as_completed", "mark_as_cancelled","create_orders_for_all_carts"]

    # Auto calculate total_price
    def save_model(self, request, obj, form, change):
        cart_items = obj.cart.items.all()
        total = sum(item.product.price * item.quantity for item in cart_items)
        obj.total_price = total
        super().save_model(request, obj, form, change)

    def mark_as_shipped(self, request, queryset):
        updated = queryset.update(status="shipped")
        self.message_user(request, f"{updated} order(s) Shipped.")
    mark_as_shipped.short_description = "Orders as Shipped"

    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status="completed")
        self.message_user(request, f"{updated} order(s) Completed.")
    mark_as_completed.short_description = "Orders as Completed"

    def mark_as_cancelled(self, request, queryset):
        updated = queryset.update(status="cancelled")
        self.message_user(request, f"{updated} order(s) Cancelled.")
    mark_as_cancelled.short_description = "Orders as Cancelled"
 
    def create_orders_for_all_carts(self, request, queryset=None):
        created_count = 0 
        carts_without_order = Cart.objects.filter(order__isnull=True)
        for cart in carts_without_order:
            if cart.items.exists():   
                total = sum(item.product.price * item.quantity for item in cart.items.all())
                Order.objects.create(
                    user=cart.user,
                    cart=cart,
                    total_price=total,
                    status="pending",
                    created_at=timezone.now()
                )
                created_count += 1
        self.message_user(request, f"{created_count} order(s) created for all carts.")
    create_orders_for_all_carts.short_description = "Create orders for all carts (ignore selection)"