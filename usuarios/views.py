from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, AuthenticationForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Tu cuenta ha sido creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('_login')
        else: 
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

@login_required
def profile(request):
    # return(request, 'hola')
    return render(request, 'profile.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
