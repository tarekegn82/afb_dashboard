from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, label='I am a')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned = super().clean()
        pw = cleaned.get('password')
        pw2 = cleaned.get('password2')
        if pw and pw2 and pw != pw2:
            self.add_error('password2', "Passwords don't match")
        return cleaned
