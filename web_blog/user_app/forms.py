from . import models
from django import forms


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['text']

        labels = {
            'text': '',
        }

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Agrega un comentario',
                                          'style': 'resize:none;'}),
        }
