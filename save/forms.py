from django import forms
from .models import List, Items

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title',)


class ItemsForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ('item',)