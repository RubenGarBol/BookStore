# Generated by Django 2.2.6 on 2019-11-15 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0008_auto_20191115_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MensajesContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('mensaje', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='promocionado',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='libro',
            name='ventas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Pais'),
        ),
        migrations.AlterField(
            model_name='deseado',
            name='libro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Libro'),
        ),
        migrations.AlterField(
            model_name='deseado',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Usuario'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='ubicacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Pais'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Genero'),
        ),
        migrations.AddField(
            model_name='libro',
            name='idioma',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Idioma'),
        ),
    ]