from django import forms
from django.forms import fields
from .models import recipe

class ItemDetail(forms.ModelForm):
    class Meta:
        model = recipe
        fields = "__all__"
        widgets = {'ingredient': forms.Textarea(), 'How_to_make': forms.Textarea(),
                   'created_by': forms.HiddenInput()}