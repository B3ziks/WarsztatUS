# Generated by Django 3.2.8 on 2021-12-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=128, verbose_name='Imię')),
                ('last_name', models.CharField(default='', max_length=256, verbose_name='Nazwisko')),
                ('birth_date', models.DateField(null=True, verbose_name='Data urodzenia')),
                ('description', models.TextField(blank=True, default='', max_length=1024, null=True, verbose_name='Opis')),
                ('image', models.ImageField(blank=True, null=True, upload_to='employee/', verbose_name='Zdjęcie')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
    ]
