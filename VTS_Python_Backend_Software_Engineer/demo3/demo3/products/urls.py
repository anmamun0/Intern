from django.urls import path
from . import views
from .views import ProductListView,CartView,ClearCartView,AddToCartView,PlaceOrderView,ProductCreateView,ProductUpdateView

urlpatterns = [
    path("product/add/", ProductCreateView.as_view(), name="product_add"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),

    path("products/", ProductListView.as_view(), name="product_list"),
    path("cart/", CartView.as_view(), name="view_cart"),
    path("add-to-cart/<int:product_id>/", AddToCartView.as_view(), name="add_to_cart"),
    path("place-order/", PlaceOrderView.as_view(), name="place_order"),
    path('clear-cart/', ClearCartView.as_view(), name='clear_cart'),
]
