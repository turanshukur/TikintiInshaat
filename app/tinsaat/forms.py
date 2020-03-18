from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name',
                  'email', 'subject', 'number', 'body']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control input_box', 'placeholder': 'Adınız *', 'style': 'color: #333'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control input_box', 'placeholder': 'Soyadınız *', 'style': 'color: #333'}),
            'email': forms.TextInput(attrs={'class': 'form-control input_box', 'placeholder': 'email adresiniz *', 'style': 'color: #333'}),
            'subject': forms.TextInput(attrs={'class': 'form-control input_box', 'placeholder': 'Mövzu *', 'style': 'color: #333'}),
            'number': forms.TextInput(attrs={'class': 'form-control input_box', 'placeholder': 'Nömrəniz *', 'style': 'color: #333'}),
            'body': forms.Textarea(attrs={'class': 'form-control input_box', 'placeholder': 'Mətn *', 'style': 'color: #333'})
        }
