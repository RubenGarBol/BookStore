# Generated by Django 2.2.6 on 2019-11-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0014_auto_20191115_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='sinopsis',
            field=models.CharField(max_length=200),
        ),
    ]