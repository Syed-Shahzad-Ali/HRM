# Generated by Django 5.2.1 on 2025-05-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
