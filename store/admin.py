from django.contrib import admin
from .models import Category, Product, Favourite, Cart, Order, OrderItem


# ------------------------------
# Category Admin
# ------------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


# ------------------------------
# Product Admin
# ------------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'favourite_flag', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'favourite_flag')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    list_editable = ('price', 'favourite_flag', 'is_featured')  # Inline edit in admin list view


# ------------------------------
# Favourite Admin
# ------------------------------
@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at',)


# ------------------------------
# Cart Admin
# ------------------------------
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'product__name')


# ------------------------------
# OrderItem Inline (inside Order Admin)
# ------------------------------
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


# ------------------------------
# Order Admin
# ------------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)
    inlines = [OrderItemInline]  # Show items inside order page


# ------------------------------
# OrderItem Admin
# ------------------------------
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    search_fields = ('product__name', 'order__id')

