from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from products.models import Product, Cart, Order
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("dashboard")  

    def form_valid(self, form):
        response = super().form_valid(form)  
        login(self.request, self.object)     
        return response


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs): 
        
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()[:10]
 
        context["orders"] = Order.objects.filter(user=self.request.user).order_by("-created_at")[:5] 
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        context["cart"] = cart
 
        context["pending_orders"] = Order.objects.filter(user=self.request.user, status="pending")
        context["total_products"] = Product.objects.count()

        return context
