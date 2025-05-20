from django import forms
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    cnf_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['user_name', 'user_email']

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')

        if not user_name:
            raise forms.ValidationError("Username is required.")
        
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', user_name):
            raise forms.ValidationError('Username must be 3-20 characters and can contain letters, numbers, and underscores.')
        
        return user_name
    
    def clean_user_email(self):
        user_email = self.cleaned_data.get('user_email')

        if not user_email:
            raise forms.ValidationError("Email is required.")
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', user_email):
            raise forms.ValidationError('Please enter a valid email address.')
        
        if User.objects.filter(user_email=user_email).exists():
            raise forms.ValidationError('Email already exists.')
        
        return user_email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not password:
            raise forms.ValidationError("Password is required.")
        
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$', password):
            raise forms.ValidationError('Password must be at least 8 characters and include at least one letter and one number.')
        
        return password
    
    def clean_cnf_password(self):
        password = self.cleaned_data.get('password')
        cnf_password = self.cleaned_data.get('cnf_password')

        if not cnf_password:
            raise forms.ValidationError("Confirm Password is required.")
        
        if password != cnf_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cnf_password
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user