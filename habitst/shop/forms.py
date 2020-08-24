from django import forms
from .models import Order,Item

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'amount']
        widgets = {
            'name': forms.TextInput(attrs = {'readonly': 'readonly'}),
            'amount': forms.TextInput(attrs = {'readonlu': 'readonly'}),
        }
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','desc','amount','photo']
     