# Generated by Django 2.2.10 on 2020-03-20 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaluos', '0001_squashed_0021_auto_20200317_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cliente',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='adr',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
