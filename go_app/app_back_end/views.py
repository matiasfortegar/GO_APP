from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from trabajos.forms import TrabajoPresupuestoForm, TrabajoProductoForm
from cotizacion.forms import PresupuestoForm, ProductoForm
from trabajos.models import OrdenTrabajo, ProductoOrden
from cotizacion.models import Presupuesto, Producto
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required


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
            "error" : 'Contraseña no coincide'
        })

@login_required
def trabajos(request):
    # Filtrar solo los presupuestos aprobados
    presupuestos_aprobados = Presupuesto.objects.filter(aprobado=True)
    context = {'presupuestos': presupuestos_aprobados}
    return render(request, 'trabajos.html', context)

"""
    def trabajos(request):
        presupuestos_aprobados = Presupuesto.objects.filter(aprobado=True)
        context = {'presupuestos': presupuestos_aprobados}
        return render(request, 'trabajos.html', context)
"""
@login_required
def duplicar_presupuesto(request, presupuesto_id):
    # Obtener el presupuesto y sus productos asociados
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    productos = Producto.objects.filter(presupuesto=presupuesto)
    
    # Si el formulario se ha enviado
    if request.method == 'POST':
        # Crear la Orden de Trabajo duplicada
        orden_trabajo = OrdenTrabajo.objects.create(
            empresa=presupuesto.empresa,
            nombre_trabajo=presupuesto.nombre_trabajo,
            detalle=presupuesto.detalle,
            usuario=presupuesto.usuario,
            presupuesto_original=presupuesto
        )
        
        # Duplicar los productos asociados al presupuesto
        for producto in productos:
            ProductoOrden.objects.create(
                orden_trabajo=orden_trabajo,
                nombre_producto=producto.nombre_producto,
                cantidad=producto.cantidad,
                cantidad_pliego=producto.cantidad_pliego,
                medida_ancho=producto.medida_ancho,
                medida_alto=producto.medida_alto,
                papel=producto.papel,
                terminacion=producto.terminacion,
                valor=producto.valor,
                detalle_producto=producto.detalle_producto
            )
        
        return redirect('trabajos')
    context = {'presupuesto': presupuesto, 'productos': productos}
    return render(request, 'duplicar_presupuesto.html', context)


@login_required
def presupuestos(request):
   presupuestos = Presupuesto.objects.all()
   context = {'presupuestos':presupuestos}
   return render(request, 'presupuestos.html', context)

@login_required
def agregar_productos(request, presupuesto_id):
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    ProductoFormSet = inlineformset_factory(Presupuesto, Producto, form=ProductoForm, extra=1)
    
    if request.method == 'POST':
        formset = ProductoFormSet(request.POST, instance=presupuesto)
        if formset.is_valid():
            formset.save()
            return redirect('presupuestos')
    else:
        formset = ProductoFormSet(instance=presupuesto)
    
    context = {'formset': formset, 'presupuesto': presupuesto}
    return render(request, 'agregar_productos.html', context)

@login_required
def presupuestos_detalle(request, presupuesto_id):
   if request.method =='GET':
        presupuesto = get_object_or_404(Presupuesto, pk=presupuesto_id)
        form = PresupuestoForm(instance=presupuesto)
        context = {'presupuesto': presupuesto, 'form': form}
        return render(request, 'presupuestos_detalle.html', context)
   else:
        try:
            presupuesto = get_object_or_404(Presupuesto, pk=presupuesto_id)
            form = PresupuestoForm(request.POST, instance=presupuesto)
            form.save()
            return redirect('presupuestos')
        except ValueError:
           context = {'presupuesto': presupuesto, 'form': form, 'error': "Error al actulizar"}
           return render(request, 'presupuestos_detalle.html', context)

@login_required
def crear_presupuestos(request):
    form = PresupuestoForm()

    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            presupuesto = form.save() 
            return redirect('agregar_productos', presupuesto_id=presupuesto.id)
    context = {'form': form}
    return render(request, 'crear_presupuestos.html', context)

@login_required
def crear_trabajo(request):
   return render(request, 'trabajos.html', {
      'form': TrabajoPresupuestoForm,
      'form': TrabajoProductoForm,
   })

@login_required
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