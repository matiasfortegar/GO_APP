import pytest
from django.contrib.auth.models import User
from cotizacion.models import Presupuesto

@pytest.mark.django_db
def test_presupuesto_creacion():
    usuario = User.objects.create(username="testuser")
    presupuesto = Presupuesto.objects.create(
        empresa="Empresa Ejemplo",
        nombre_trabajo="Trabajo Ejemplo",
        aprobado=True,
        usuario=usuario 
    )
    assert presupuesto is not None
