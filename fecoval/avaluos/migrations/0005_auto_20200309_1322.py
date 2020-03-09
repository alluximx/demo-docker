# Generated by Django 2.2.10 on 2020-03-09 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaluos', '0004_remove_mancomunado_curp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datoscliente',
            name='cliente',
        ),
        migrations.AddField(
            model_name='avaluo',
            name='datos_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='avaluos.DatosCliente'),
        ),
    ]
