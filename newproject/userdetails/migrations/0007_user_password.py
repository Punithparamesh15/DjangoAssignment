# Generated by Django 5.1.2 on 2024-11-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0006_alter_admin_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=150),
        ),
    ]
