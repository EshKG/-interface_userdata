# Generated by Django 5.0.6 on 2024-06-18 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_users_exp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='exp_date',
        ),
    ]
