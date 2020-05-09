from django.forms import ModelForm
from App_Login.models import User, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm


# forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(
        required = True,
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required = True,
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder':'Password Confirmation'})
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
