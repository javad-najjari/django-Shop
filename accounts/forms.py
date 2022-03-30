from django import forms
from .models import User
from django.core.exceptions import ValidationError




class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('این ایمیل از قبل وجود دارد')
        return email
    

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('این نام کاربری از قبل وجود دارد')
        return username
    
    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('رمز عبورها باید مشابه هم باشند')
        


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))