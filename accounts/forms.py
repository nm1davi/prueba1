from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField

class MyUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label='Usuario', max_length=30)
    Mail = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username', 'Mail', 'password1', 'password2']
        help_texts = { key: '' for key in fields }
        
        
class MyUserEditForm(forms.Form):
    
    Mail = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput, required=False)
    Link = forms.URLField(label="Link", max_length=50, required=True)
    avatar = forms.ImageField(required=False)
    descripcion = RichTextFormField(required=False)
    
    