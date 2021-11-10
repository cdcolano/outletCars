# Generated by Django 3.2.8 on 2021-11-10 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoría',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('modelo', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('cv', models.IntegerField()),
                ('km', models.BigIntegerField()),
                ('combustible', models.CharField(max_length=50)),
                ('categoría', models.ManyToManyField(to='outletCarsApp.Categoría')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outletCarsApp.marca')),
            ],
        ),
    ]