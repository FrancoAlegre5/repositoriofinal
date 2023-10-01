from django.urls import path
from . import views  # Importar las vistas 

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('blogs/', views.blog_list, name='blog_list'),  # Ruta para listar todos los blogs
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Ruta para ver detalles de un blog
    path('about/', views.about, name='about'),  # Ruta para la página "Acerca de mí"
    path('accounts/signup/', views.signup, name='signup'),  # Ruta para el registro de usuarios
    path('accounts/login/', views.login_view, name='login'),  # Ruta para la página de inicio de sesión
    path('accounts/profile/', views.profile, name='profile'),  # Ruta para el perfil del usuario
    path('messages/', views.messages, name='messages'),  # Ruta para la funcionalidad de mensajería
]
from django.urls import path
from . import views

urlpatterns = [
    
    path('messages/send/<int:recipient_id>/', views.send_message, name='send_message'),
    path('messages/inbox/', views.inbox, name='inbox'),
]
