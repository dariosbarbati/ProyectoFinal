# Generated by Django 4.0.6 on 2022-08-31 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('descripcion', models.CharField(max_length=40)),
                ('habilitar', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Meses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=40, null=True)),
                ('precio', models.FloatField()),
                ('pagado', models.BooleanField(default=False)),
                ('fecha', models.DateField()),
                ('aleatorio', models.CharField(blank=True, max_length=40, null=True)),
                ('MesesServicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MesesServicio', to='Servicios.servicios')),
            ],
            options={
                'verbose_name': 'Mes',
                'verbose_name_plural': 'Meses',
            },
        ),
    ]
