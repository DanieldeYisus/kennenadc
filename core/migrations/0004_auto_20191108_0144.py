# Generated by Django 2.2.6 on 2019-11-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191108_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='tipo_contacto',
            field=models.CharField(choices=[('Venta', 'Venta'), ('Compra', 'Compra')], max_length=1),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='tipo_contacto',
            field=models.CharField(choices=[('Venta', 'Venta'), ('Compra', 'Compra')], max_length=1),
        ),
    ]