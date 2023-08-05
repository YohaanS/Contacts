from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone']

    email = forms.EmailField(initial='example@gmail.com')

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'pattern': '[\d\-+]+',
                'title': 'Only digits, +, and - are allowed.',
                'placeholder': '+123-456-7890'  # Add your desired placeholder
            }
        )
    )