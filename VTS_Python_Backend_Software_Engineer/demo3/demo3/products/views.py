from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .forms import CartItemForm
from .models import Product, Cart, CartItem,Order

from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, TemplateView, View 
from django.views.generic.edit import FormView
  
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("dashboard")

    def get_queryset(self): 
        return Product.objects.filter(user=self.request.user)












class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "product_forms"

    def get_queryset(self):
        
        products = Product.objects.all()
        return [(product, CartItemForm()) for product in products]
 
class CartView(LoginRequiredMixin, TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = self.request.user.cart
        return context

 
class ClearCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        cart = request.user.cart
        cart.items.all().delete()
        return redirect("view_cart")
 



class AddToCartView(LoginRequiredMixin, FormView):
    form_class = CartItemForm
    template_name = "add_to_cart.html" 

    def form_valid(self, form):
        product_id = self.kwargs["product_id"]
        product = get_object_or_404(Product, id=product_id)

        quantity = form.cleaned_data["quantity"]
        description = form.cleaned_data.get("description", "")

        cart, _ = Cart.objects.get_or_create(user=self.request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart,
            product=product,
            defaults={"quantity": quantity, "description": description},
        )

        if not created:
            cart_item.quantity += quantity
            if description:
                cart_item.description = description
            cart_item.save()

        return redirect("view_cart")

    def form_invalid(self, form):
        return redirect("product_list")



class PlaceOrderView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        cart = request.user.cart
        if not cart.items.exists():
            return redirect("product_list")

        total = sum(item.product.price * item.quantity for item in cart.items.all())
        order = Order.objects.create(user=request.user,cart=cart,total_price=total,status="pending")
        cart.items.all().delete()
        return render(request, "order_success.html", {"order": order})
    
    def get(self, request, *args, **kwargs):
        return redirect("product_list")
