# Generated by Django 4.0.3 on 2022-03-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=30, verbose_name='Фамилие')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
                ('tg_account_id', models.IntegerField(blank=True, null=True, verbose_name='Telegram Id')),
                ('phone', models.TextField(blank=True, null=True, verbose_name='Телефон номер')),
            ],
            options={
                'verbose_name': 'Охранник',
                'verbose_name_plural': 'Охранники',
            },
        ),
    ]