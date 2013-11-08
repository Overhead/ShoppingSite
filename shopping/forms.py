from django import forms
from shopping.models import *


class ShoppingItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ('item_name', )