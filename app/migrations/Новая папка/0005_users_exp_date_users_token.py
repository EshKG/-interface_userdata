# Generated by Django 5.0.6 on 2024-06-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_clients_fio_representative'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='exp_date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(default='', max_length=60),
        ),
    ]
