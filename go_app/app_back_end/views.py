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
from decimal import Decimal


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
    # Obtener el presupuesto y los productos asociados
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    productos = Producto.objects.filter(presupuesto=presupuesto)

    # Verificar que el presupuesto y los productos fueron encontrados
    print("Presupuesto a duplicar: ", presupuesto)
    print("Productos asociados encontrados: ", productos)

    if request.method == 'POST':
        # Crear una nueva OrdenTrabajo (duplicado de presupuesto)
        orden_trabajo = OrdenTrabajo.objects.create(
            empresa=presupuesto.empresa,
            nombre_trabajo=presupuesto.nombre_trabajo,
            detalle=presupuesto.detalle,
            usuario=presupuesto.usuario,
            presupuesto_original=presupuesto  # Enlace al presupuesto original
        )
        
        # Verificar que la OrdenTrabajo fue creada correctamente
        print("OrdenTrabajo creada: ", orden_trabajo)

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
            # Verificar que el producto fue duplicado
            print(f"Producto duplicado: {producto.nombre_producto} para {orden_trabajo.nombre_trabajo}")

        # Redirigir a la vista de trabajos después de duplicar
        return redirect('trabajos')

    # Contexto para mostrar los detalles del presupuesto en la plantilla
    context = {'presupuesto': presupuesto, 'productos': productos}
    return render(request, 'duplicar_presupuesto.html', context)



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

        duplicados = ProductoOrden.objects.filter(orden_trabajo=orden_trabajo)
        print(f"Productos duplicados: {duplicados.count()}")  # Comprobar en consola
        
        return redirect('trabajos')

    context = {'presupuesto': presupuesto, 'productos': productos}
    return render(request, 'duplicar_presupuesto.html', context)

"""



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
        productos = Producto.objects.filter(presupuesto=presupuesto)
        total = sum([producto.valor * producto.cantidad for producto in productos])
        tasa_iva = Decimal(0.19)
        iva = total * tasa_iva
        total_iva = total + iva 
        form = PresupuestoForm(instance=presupuesto)
        context = {
            'presupuesto': presupuesto,
            'form': form,
            'productos': productos,
            'total': total,
            'iva': iva,
            'total_iva': total_iva,
             }
        return render(request, 'presupuestos_detalle.html', context)
   
   else:
        try:
            presupuesto = get_object_or_404(Presupuesto, pk=presupuesto_id)
            form = PresupuestoForm(request.POST, instance=presupuesto)
            form.save()
            return redirect('presupuestos')
        except ValueError:
            productos = Producto.objects.filter(presupuesto=presupuesto)
            total = sum([producto.valor * producto.cantidad for producto in productos])
            iva = total * Decimal(0.19)
            total_con_iva = total + iva
            context = {
                'presupuesto': presupuesto,
                'form': form,
                'productos': productos,
                'total': total,
                'iva': iva,
                'total_con_iva': total_con_iva,
                'error': "Error al actualizar"
            }
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
def ver_presupuestos_aprobados(request):
    # Obtener todos los presupuestos aprobados
    presupuestos = Presupuesto.objects.filter(aprobado=True)
    
    context = {
        'presupuestos': presupuestos,
    }
    
    return render(request, 'presupuestos_aprobados.html', context)

@login_required
def editar_trabajo(request, trabajo_id):
    # Obtener el trabajo específico
    trabajo = get_object_or_404(OrdenTrabajo, pk=trabajo_id)
    productos = ProductoOrden.objects.filter(orden_trabajo=trabajo)

    if request.method == 'POST':
        form_presupuesto = TrabajoPresupuestoForm(request.POST, instance=trabajo)
        
        if form_presupuesto.is_valid():
            form_presupuesto.save()

        # Guardar cada producto individualmente
        for producto in productos:
            form_producto = TrabajoProductoForm(request.POST, instance=producto)
            if form_producto.is_valid():
                form_producto.save()

        return redirect('trabajos')

    else:
        form_presupuesto = TrabajoPresupuestoForm(instance=trabajo)

        productos_forms = [TrabajoProductoForm(instance=producto) for producto in productos]

    context = {
        'trabajo': trabajo,
        'productos': productos,  # Este es el QuerySet
        'form_presupuesto': form_presupuesto,
        'productos_forms': productos_forms,  # Lista de formularios para productos
    }
    
    return render(request, 'editar_trabajo.html', context)




@login_required
def crear_trabajo(request):
    trabajos = OrdenTrabajo.objects.all()  # Asegurarse de que esta línea esté obteniendo trabajos
    print(f"Trabajos duplicados encontrados: {trabajos.count()}")  # Verificación en consola

    context = {
        'trabajos': trabajos,  # Pasamos los trabajos a la plantilla
        'form_presupuesto': TrabajoPresupuestoForm(),
        'form_producto': TrabajoProductoForm(),
    }
    
    return render(request, 'trabajos.html', context)


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