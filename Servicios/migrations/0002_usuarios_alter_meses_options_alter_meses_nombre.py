# Generated by Django 4.0.6 on 2022-08-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=8)),
                ('habilitar', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='meses',
            options={},
        ),
        migrations.AlterField(
            model_name='meses',
            name='nombre',
            field=models.CharField(blank=True, editable=False, max_length=40, null=True),
        ),
    ]