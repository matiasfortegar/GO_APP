# Generated by Django 3.2.25 on 2024-07-18 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_back_end', '0006_auto_20240710_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='presupuesto',
        ),
        migrations.DeleteModel(
            name='Presupuesto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
