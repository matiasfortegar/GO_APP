# Generated by Django 3.2.25 on 2024-07-11 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_back_end', '0004_alter_precio_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio',
            name='valor',
            field=models.PositiveIntegerField(),
        ),
    ]
