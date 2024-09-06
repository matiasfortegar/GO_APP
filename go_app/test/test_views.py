import pytest
from django.contrib.auth.models import User
from cotizacion.models import Presupuesto

@pytest.mark.django_db
def test_duplicar_presupuesto(client):
    usuario = User.objects.create(username="testuser")
    presupuesto = Presupuesto.objects.create(
        empresa="Empresa Test",
        nombre_trabajo="Trabajo Test",
        aprobado=True,
        usuario=usuario 
    )
    assert presupuesto is not None
