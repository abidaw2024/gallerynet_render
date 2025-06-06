from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('gallery:obras')
    return render(request, 'home.html')  # Renderiza la plantilla 'home.html'

def politicas_privacidad(request):
    return render(request, 'politicas_privacidad.html')  # O 'users/politicas_privacidad.html' si está en la app users

def terminos_condiciones(request):
    return render(request, 'terminos_condiciones.html')  # O 'users/terminos_condiciones.html' si está en la app users

def contacto(request):
    return render(request, 'contacto.html')

