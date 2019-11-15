# Generated by Django 2.2.6 on 2019-11-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0015_auto_20191115_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='sinopsis',
        ),
        migrations.AddField(
            model_name='libro',
            name='sinopsis_max',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='libro',
            name='sinopsis_min',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
