# Generated by Django 2.2.10 on 2020-03-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaluos', '0011_colegio_colegioavaluo_empresa_propuestatecnica_valuador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colegioavaluo',
            options={'verbose_name_plural': 'Colegios Avaluos'},
        ),
        migrations.AddField(
            model_name='propuestatecnica',
            name='aceptado',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='propuestatecnica',
            name='respuesta',
            field=models.TextField(blank=True, null=True, verbose_name='Respuesta'),
        ),
    ]
