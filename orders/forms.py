from django import forms
from .models import Order, OrderItem
from users.models import Profile

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'postal_code', 'city', 'address']