# Generated by Django 5.1.2 on 2024-11-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0011_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
