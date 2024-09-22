from django import forms
from .models import Tweet, User
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'other_fields': forms.TextInput(attrs={'class': 'form-control'}),
            # Add other fields similarly
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        