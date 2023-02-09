from django import forms
from .models import food_table

class Forms_add(forms.ModelForm):
    class Meta:
        model =food_table
        fields=['items','description','price','Img_items']