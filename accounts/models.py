from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class MasDatosUsuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares", null=True, blank= True)
    Link = models.URLField(max_length=120, null=True)
    descripcion = RichTextField(null=True)
    
def __str__(self):
        return {self.user}