from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from . import seguridad as security
# Create your views here.

seguridad = security.Seguridad()

def home(request):
    context = {}
    context['registrado'] = False
    context['user'] = ''
    return render(request, 'mysite/home.html', context)

def register(request):
    context = {}
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            passwordValidate = userObj['passwordValidate']
            if not seguridad.usuarioYaRegistrado(email):
                #User.objects.create_user(username, email, password)
                #user = authenticate(username = username, password = password)
                # aqui va es registrar usuario y luego render a home si los datos estan bien
                #login(request, user)
                #return HttpResponseRedirect('/')
                usuarioValido = seguridad.registrarUsuario(username,email,password,passwordValidate)
                context['registrado'] = True
                context['user'] = username
                if usuarioValido:
                    return render(request, 'mysite/home.html',context)
                else:
                    # Deberia mandarlo a home con un mensaje de error
                    return ''
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'mysite/register.html', {'form' : form})

def login_user(request):

    email = request.POST['email']
    password = request.POST['password']
    user = seguridad.ingresarUsuario()
    if user:
        context['registrado'] = True
        context['user'] = user
        return render(request, 'mysite/home.html',context)
    
     # Le paso la variable al template como un diccionario, si es true entonces muestra logout
     # sino lo demas el cambio es en home
