from django import forms
from shopping.models import *


class ShoppingItemForm(forms.ModelForm):
    class Meta:
        models = ShoppingItem
        fields = ('item_name')