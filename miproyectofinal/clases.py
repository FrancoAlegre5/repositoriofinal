from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo de usuario de Django

# Modelo para representar los blogs
class Blog(models.Model):
    title = models.CharField(max_length=200)  # Título del blog
    subtitle = models.CharField(max_length=200)  # Subtítulo del blog
    body = models.TextField()  # Cuerpo del blog
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor del blog, utilizando el modelo de usuario de Django
    date = models.DateTimeField(auto_now_add=True)  # Fecha de publicación del blog
    image = models.ImageField(upload_to='blog_images/')  # Imagen asociada al blog

    def __str__(self):
        return self.title  # Representación legible del objeto en el administrador de Django

# Modelo para representar perfiles de usuario
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona el perfil con un usuario
    description = models.TextField(blank=True)  # Descripción del usuario
    website = models.URLField(blank=True)  # Enlace a la página web del usuario
    image = models.ImageField(upload_to='profile_images/', blank=True)  # Imagen de perfil del usuario

    def __str__(self):
        return self.user.username  # Representación legible del perfil en el administrador de Django
