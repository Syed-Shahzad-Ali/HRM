# Generated by Django 5.2.1 on 2025-05-15 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_role', to='permissions.role'),
        ),
    ]
