# Generated by Django 2.2.6 on 2019-11-15 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0009_auto_20191115_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='idioma',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='promocionado',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='ventas',
        ),
    ]