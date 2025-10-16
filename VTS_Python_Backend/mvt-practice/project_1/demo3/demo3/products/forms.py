from django import forms

from .models import Product

from django import forms
from .models import Product,CartItem

product_form_input_attrs = {
    "class": "w-full border border-gray-300 rounded-lg px-4 py-2 text-gray-800 "
             "focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400 transition"
}
add_tocard_attrs ={
 "class": "border rounded px-3 py-1 w-full",
                "placeholder": "Quantity",
}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock", "category"]
        widgets = {
            "name": forms.TextInput(attrs={**product_form_input_attrs, "placeholder": "Enter product name"}),
            "description": forms.Textarea(attrs={**product_form_input_attrs, "rows": 4, "placeholder": "Enter product description"}),
            "price": forms.NumberInput(attrs={**product_form_input_attrs, "placeholder": "Enter price"}),
            "stock": forms.NumberInput(attrs={**product_form_input_attrs, "placeholder": "Enter stock quantity"}),
            "category": forms.Select(attrs={**product_form_input_attrs}),
        }
        

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ["quantity", "description"]
        widgets = {
            "quantity": forms.NumberInput(attrs={**add_tocard_attrs,"placeholder":"Quantity"}),
            "description": forms.TextInput(attrs={**add_tocard_attrs,"placeholder":"Description"})
        }

