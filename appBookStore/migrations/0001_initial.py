# Generated by Django 2.2.6 on 2019-11-05 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('bio', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('sinopsis', models.CharField(max_length=2000)),
                ('paginas', models.IntegerField()),
                ('precio', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=1)),
                ('ISBN', models.CharField(max_length=13)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Editorial')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Genero')),
            ],
        ),
        migrations.AddField(
            model_name='editorial',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Pais'),
        ),
        migrations.AddField(
            model_name='autor',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBookStore.Pais'),
        ),
    ]
