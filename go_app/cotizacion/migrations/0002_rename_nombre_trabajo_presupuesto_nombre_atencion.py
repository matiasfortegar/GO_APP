# Generated by Django 3.2.25 on 2024-07-27 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presupuesto',
            old_name='nombre_trabajo',
            new_name='nombre_atencion',
        ),
    ]
