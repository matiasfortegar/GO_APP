# trabajos/views.py
from django.shortcuts import get_object_or_404, redirect, render
from cotizacion.models import Presupuesto
from trabajos.forms import TrabajoPresupuestoForm

def duplicar_presupuesto_formulario(request, presupuesto_id):
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    
    # Crear el formulario para Trabajopresupuesto
    trabajo_presupuesto_form = TrabajoPresupuestoForm(request.POST or None, initial={
        'nombre': presupuesto.nombre_trabajo,
        'empresa': presupuesto.empresa,
    })

    if trabajo_presupuesto_form.is_valid():
        trabajo_presupuesto = trabajo_presupuesto_form.save()

        # Duplicar los productos asociados
        for producto in presupuesto.producto_set.all(): # type: ignore
            producto.objects.create(
                nombre=producto.nombre,
                cantidad=producto.cantidad,
                precio=producto.precio,
                trabajo_presupuesto=trabajo_presupuesto
            )
        
        return redirect('nombre_de_la_vista_a_la_que_redirigir')

    return render(request, 'trabajos/duplicar_presupuesto.html', {
        'form': trabajo_presupuesto_form,
        'presupuesto': presupuesto,
    })

def ver_presupuesto(request, presupuesto_id):
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    return render(request, 'ver_presupuesto.html', {'presupuesto': presupuesto})