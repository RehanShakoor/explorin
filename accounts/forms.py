from django import forms
from .models import Post,EditProfile

class ImageForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'

class EditForm(forms.ModelForm):
    class Meta:
        model=EditProfile
        fields='__all__'        
        
