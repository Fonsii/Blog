from . import models
from django import forms


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%'}),
        }
