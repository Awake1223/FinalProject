# Generated by Django 5.1.3 on 2024-12-18 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
