# Generated by Django 4.2.7 on 2024-02-08 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0006_permisoespecial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisoespecial',
            name='description',
        ),
        migrations.AddField(
            model_name='permisoespecial',
            name='codigo',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='permisoespecial',
            name='descripcion',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='permisoespecial',
            name='nombre',
            field=models.TextField(default=''),
        ),
    ]
