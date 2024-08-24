# Generated by Django 3.2.25 on 2024-08-24 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0005_alter_producto_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto',
            name='precios',
        ),
        migrations.AlterField(
            model_name='precio',
            name='valor',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='terminacion',
            field=models.CharField(choices=[('nada', 'Nada'), ('troquel', 'Troquel'), ('laminado', 'Laminado'), ('corte', 'Corte')], max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='valor',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
