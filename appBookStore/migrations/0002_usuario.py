# Generated by Django 2.2.6 on 2019-11-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
                ('nombre', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
