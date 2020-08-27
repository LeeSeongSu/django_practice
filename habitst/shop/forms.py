from django import forms
from .models import Order,Item
from .mixins import IamportBaseForm


class PayForm(IamportBaseForm):
    template_name = 'shop/_iamport.html'
    params_names = ['merchant_uid', 'name', 'amount']
    imp_fn_name = 'request_pay'

    class Meta:
        model = Order
        fields = ['imp_uid']
        widgets = {
        'imp_uid': forms.HiddenInput,
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','desc','amount','photo','date_select'] 
        widgets = {
               'date_select': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
             
        }

   