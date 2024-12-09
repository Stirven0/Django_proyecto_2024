from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, CustomAuthenticationForm

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
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        print('entrandoa "from_login"')
        remember_me = form.cleaned_data.get('remember_me', False)
        
        if remember_me:
            print('se recordara por una semana')
            self.request.session.set_expiry(604800) # 1 semana
        else:
            print('La sesión expirará al cerrar el navegador')
            self.request.session.set_expiry(0) # La sesión expirará al cerrar el navegador
            
        messages.success(self.request, "Inicio de sesión exitoso")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Usuario y/o contraseña incorrectos")
        return super().form_invalid(form)
