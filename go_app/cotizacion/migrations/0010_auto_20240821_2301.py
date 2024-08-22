# Generated by Django 3.2.25 on 2024-08-22 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0009_alter_presupuesto_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='presupuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mas_productos', to='cotizacion.presupuesto'),
        ),
        migrations.AlterModelTable(
            name='presupuesto',
            table='cotizacion_presupuesto',
        ),
    ]
