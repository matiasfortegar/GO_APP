from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
           try:
                #registrar usuario
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('tareas')
           
           except:
            return render(request, 'signup.html',{
                'form' : UserCreationForm,
                "error" : 'Usuario ya existe'
            })
        
        return render(request, 'signup.html',{
            'form' : UserCreationForm,
            "error" : 'Contraseña no cohincide'
        })

def tareas(request):
   return render(request, 'tareas.html')

def cerrar_sesion(request):
   logout(request)
   return redirect('home')

def iniciar_sesion (request):
   if request.method == 'GET':
      return render(request, 'login.html',{
        'form' : AuthenticationForm
      })
   else:
      user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
      if user is None:
         return render(request, 'login.html',{
            'form' : AuthenticationForm,
            'error' : 'Clave o usuario incorrecto'
         })
      else:
         login(request, user)
         return redirect('home')