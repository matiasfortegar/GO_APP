from django.http import JsonResponse
from django.db import transaction, IntegrityError
from django.shortcuts import redirect
from cotizacion.models import Presupuesto as CotizacionPresupuesto, Producto as CotizacionProducto
from trabajos.models import TrabPresupuesto, TrabProducto

def duplicar_presupuesto(presupuesto_id):
    presupuesto_original = CotizacionPresupuesto.objects.using('default').get(id=presupuesto_id, aprobado=True)
    
    if presupuesto_original.aprobado:
        try:
            with transaction.atomic(using='trabajos_db'):
                nuevo_presupuesto = TrabPresupuesto.objects.using('trabajos_db').create(
                    empresa=presupuesto_original.empresa,
                    nombre=presupuesto_original.nombre_trabajo,
                    detalle=presupuesto_original.detalle,
                    fecha_ok=presupuesto_original.fecha_ok,
                    usuario=presupuesto_original.usuario,
                )

                productos = CotizacionProducto.objects.filter(presupuesto=presupuesto_original)
                for producto in productos:
                    TrabProducto.objects.using('trabajos_db').create(
                        presupuesto=nuevo_presupuesto,
                        nombre=producto.nombre_producto,
                        cantidad=producto.cantidad,
                        cantidad_pliego=producto.cantidad_pliego,
                        medida_ancho=producto.medida_ancho,
                        medida_alto=producto.medida_alto,
                        papel=producto.papel,
                        terminacion=producto.terminacion,
                        detalle_producto=producto.detalle_producto,


                        # Copia otros campos aquí si es necesario
                    )

            return JsonResponse({"status": "success", "message": "Presupuesto duplicado exitosamente."})
        except IntegrityError as e:
            return JsonResponse({"status": "error", "message": f"Error al duplicar: {e}"})
        
    return JsonResponse({"status": "error", "message": "El presupuesto no está aprobado."})

# Función que aprueba el presupuesto y llama a duplicar_presupuesto
def aprobar_presupuesto(request, presupuesto_id):
    presupuesto = CotizacionPresupuesto.objects.get(id=presupuesto_id)
    presupuesto.aprobado = True
    presupuesto.save()
    
    # Llama a la función duplicar_presupuesto después de aprobar
    duplicar_presupuesto(presupuesto_id) 

    return redirect('nombre_de_la_vista')
