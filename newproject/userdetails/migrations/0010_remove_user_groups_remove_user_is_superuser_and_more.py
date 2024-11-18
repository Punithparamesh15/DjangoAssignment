# Generated by Django 5.1.2 on 2024-11-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0009_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=150),
        ),
    ]
