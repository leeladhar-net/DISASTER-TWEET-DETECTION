# Generated by Django 4.1.9 on 2023-06-01 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0010_tweety_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweety',
            name='name',
        ),
    ]
