from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'image']

# Explicación:
# - Importamos `forms` de Django y el modelo `Blog` de nuestra aplicación.
# - Definimos una clase `BlogForm` que hereda de `forms.ModelForm`.
# - Utilizamos la clase `Meta` para especificar el modelo al que está asociado el formulario (`model = Blog`)
#   y los campos que queremos incluir en el formulario (`fields = ['title', 'subtitle', 'body', 'image']`).
#   Estos campos son los que se mostrarán en el formulario para la creación y edición de blogs.

from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Requerido. Ingrese un correo válido.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Explicación:
# - Importamos `forms` de Django y `UserCreationForm` de `django.contrib.auth.forms`.
# - Creamos una clase `SignupForm` que hereda de `UserCreationForm`. Esto proporciona un formulario predefinido
#   para el registro de usuario con campos como `username`, `password1`, y `password2`.
# - Agregamos un campo adicional `email` al formulario utilizando `email = forms.EmailField(max_length=200)`.
# - En la clase `Meta`, especificamos el modelo al que está asociado el formulario (`model = User`)
#   y los campos que se mostrarán en el formulario de registro.

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['description', 'website', 'image']

# Explicación:
# - Importamos `forms` de Django y el modelo `UserProfile` de nuestra aplicación.
# - Definimos una clase `UserProfileForm` que hereda de `forms.ModelForm`.
# - Usamos la clase `Meta` para especificar el modelo al que está asociado el formulario (`model = UserProfile`)
#   y los campos que queremos incluir en el formulario para la edición del perfil de usuario (`fields = ['description', 'website', 'image']`).

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nombre', 'descripcion', 'imagen', 'otros_campos']  # Ajustar los campos según tu modelo de perfil
