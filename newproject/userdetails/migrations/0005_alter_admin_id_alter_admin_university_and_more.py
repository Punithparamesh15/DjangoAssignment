# Generated by Django 5.1.2 on 2024-10-24 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0004_alter_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='admin',
            name='university',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='admin',
            name='year_of_passing',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
