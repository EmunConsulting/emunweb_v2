from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'ኢመይል', 'required': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'ናይ ኣካውንት ስም', 'required': 'required'}),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'ፓስዎርድ', 'required': 'required'}),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'ደጊምካ ፓስዎርድ ጸሓፍ', 'required': 'required'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'ናይ ኣካውንት ስም', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'placeholder': 'ኢመይል', 'required': 'required'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'ፓስዎርድ', 'required': 'required'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'ደጊምካ ፓስዎርድ ጸሓፍ', 'required': 'required'})



