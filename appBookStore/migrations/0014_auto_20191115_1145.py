# Generated by Django 2.2.6 on 2019-11-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0013_auto_20191115_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='fecha',
            field=models.IntegerField(default=0),
        ),
    ]
