# Generated by Django 3.2.8 on 2022-01-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20220111_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(default='Klient', max_length=128, unique=True, verbose_name='Nazwa'),
        ),
    ]
