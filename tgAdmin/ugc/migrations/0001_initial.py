# Generated by Django 4.0.3 on 2022-03-25 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название Компании')),
            ],
            options={
                'verbose_name': 'Компанию',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('surname', models.TextField(verbose_name='Фамилие')),
                ('patronymic', models.TextField(blank=True, null=True, verbose_name='Отчество')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ugc.companies')),
            ],
            options={
                'verbose_name': 'Сотрудника',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(verbose_name='Модель Автомобиля')),
                ('num_car', models.TextField(verbose_name='Номер Автомобиля')),
                ('color', models.TextField(blank=True, null=True, verbose_name='Цвет Автомобиля')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ugc.employees', verbose_name='Водитель')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
