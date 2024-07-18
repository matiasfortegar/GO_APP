# Generated by Django 3.2.25 on 2024-07-10 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=255)),
                ('nombre_trabajo', models.CharField(max_length=255)),
                ('cantidad', models.PositiveIntegerField()),
                ('cantidad_pliego', models.PositiveIntegerField()),
                ('medida_ancho', models.FloatField()),
                ('medida_alto', models.FloatField()),
                ('papel', models.CharField(max_length=255)),
                ('terminacion', models.CharField(choices=[('troquel', 'Troquel'), ('laminado', 'Laminado'), ('corte', 'Corte')], max_length=50)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('aprobado', models.BooleanField(default=False)),
                ('fecha_emision', models.DateField()),
                ('fecha_ok', models.DateField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoAdicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=255)),
                ('cantidad', models.PositiveIntegerField()),
                ('cantidad_pliego', models.PositiveIntegerField()),
                ('medida_ancho', models.FloatField()),
                ('medida_alto', models.FloatField()),
                ('papel', models.CharField(max_length=255)),
                ('terminacion', models.CharField(choices=[('troquel', 'Troquel'), ('laminado', 'Laminado'), ('corte', 'Corte')], max_length=50)),
                ('presupuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mas_productos', to='app_back_end.presupuesto')),
            ],
        ),
    ]
