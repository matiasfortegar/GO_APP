from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from trabajos.forms import TrabajoPresupuestoForm, TrabajoProductoForm
from cotizacion.forms import PresupuestoForm, ProductoForm
from trabajos.models import OrdenTrabajo
from cotizacion.models import Presupuesto, Producto
from django.forms import inlineformset_factory


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
            return redirect('trabajos')
           
           except:
            return render(request, 'signup.html',{
                'form' : UserCreationForm,
                "error" : 'Usuario ya existe'
            })
        
        return render(request, 'signup.html',{
            'form' : UserCreationForm,
            "error" : 'Contraseña no cohincide'
        })

def trabajos(request):
   trabajos = OrdenTrabajo.objects.all()
   context = {'trabajos':trabajos}
   return render(request, 'trabajos.html', context)

def presupuestos(request):
   presupuestos = Presupuesto.objects.all()
   context = {'presupuestos':presupuestos}
   return render(request, 'presupuestos.html', context)


def agregar_productos(request, presupuesto_id):
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    ProductoFormSet = inlineformset_factory(Presupuesto, Producto, form=ProductoForm, extra=1)
    
    if request.method == 'POST':
        formset = ProductoFormSet(request.POST, instance=presupuesto)
        if formset.is_valid():
            formset.save()
            return redirect('/presupuestos/')
    else:
        formset = ProductoFormSet(instance=presupuesto)
    
    context = {'formset': formset, 'presupuesto': presupuesto}
    return render(request, 'agregar_productos.html', context)
   

def crear_presupuestos(request):
    form = PresupuestoForm()

    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            presupuesto = form.save() 
            return redirect('agregar_productos', presupuesto_id=presupuesto.id)
    context = {'form': form}
    return render(request, 'crear_presupuestos.html', context)


def crear_trabajo(request):
   return render(request, 'trabajos.html', {
      'form': TrabajoPresupuestoForm,
      'form': TrabajoProductoForm,
   })

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