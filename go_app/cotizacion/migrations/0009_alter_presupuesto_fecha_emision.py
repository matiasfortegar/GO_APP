# Generated by Django 3.2.25 on 2024-08-25 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0008_alter_presupuesto_aprobado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='fecha_emision',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
