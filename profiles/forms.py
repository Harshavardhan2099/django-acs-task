from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(
    widget=forms.ClearableFileInput(attrs={'accept': 'image/*'})  # Restrict to images only
    )
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'department', 'project_links', 'description', 'profile_image']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your department'
            }),
            'project_links': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your project links',
                'rows': 3
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a short description about yourself',
                'rows': 4
            }),
            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }
