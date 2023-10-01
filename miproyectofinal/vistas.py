from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from .forms import BlogForm  # Importar los formularios necesarios

# Vista para la página de inicio
def home(request):
    # Aquí puedes recuperar los últimos blogs y renderizar la página de inicio
    return render(request, 'home.html')

# Vista para listar todos los blogs
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

# Vista para ver detalles de un blog
def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

# Vista para la página "Acerca de mí"
def about(request):
    return render(request, 'about.html')

# Vista para el registro de usuarios
def signup(request):
    # Implementa la lógica de registro de usuarios aquí
    return render(request, 'registration/signup.html')

# Vista para la página de inicio de sesión
def login_view(request):
    # Implementa la lógica de inicio de sesión aquí
    return render(request, 'registration/login.html')

# Vista para el perfil del usuario (requiere inicio de sesión)
@login_required
def profile(request):
    # Implementa la lógica para mostrar y editar el perfil del usuario aquí
    return render(request, 'registration/profile.html')

# Vista para la funcionalidad de mensajería (requiere inicio de sesión)
@login_required
def messages(request):
    # Implementa la funcionalidad de mensajería aquí
    return render(request, 'messages.html')

from django.shortcuts import render, redirect
from .models import Blog, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import BlogForm, SignupForm, UserProfileForm
from django.contrib import messages

# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')

# Vista para listar todos los blogs
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

# Vista para ver detalles de un blog
def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

# Vista para la página "Acerca de mí"
def about(request):
    return render(request, 'about.html')

# Vista para el registro de usuarios
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# Vista para la página de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'registration/login.html')

# Vista para el perfil del usuario (requiere inicio de sesión)
@login_required
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'registration/profile.html', {'form': form})

# Vista para la funcionalidad de mensajería (requiere inicio de sesión)
@login_required
def messages(request):
    # Implementa la lógica de mensajería aquí
    return render(request, 'messages.html')

from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request, recipient_id):
    recipient = User.objects.get(pk=recipient_id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    
    return render(request, 'messages/send_message.html', {'form': form, 'recipient': recipient})

@login_required
def inbox(request):
    received_messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messages/inbox.html', {'received_messages': received_messages})

from django.shortcuts import render, redirect
from .forms import UserProfileForm  # Asegúrate de importar el formulario correcto

def profile(request):
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos de la solicitud POST
        form = UserProfileForm(request.POST, instance=request.user.profile)
        
        if form.is_valid():
            # Guardar los cambios en el modelo de perfil del usuario
            form.save()
            return redirect('profile')  # Redirigir a la página de perfil después de guardar
            
    else:
        # Si la solicitud no es POST, simplemente crea una instancia del formulario vacío
        form = UserProfileForm(instance=request.user.profile)
    
    return render(request, 'profile.html', {'form': form})
