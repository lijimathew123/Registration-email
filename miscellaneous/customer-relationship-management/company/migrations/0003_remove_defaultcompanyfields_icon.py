# Generated by Django 4.1.13 on 2024-03-14 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_defaultcompanyfields_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defaultcompanyfields',
            name='icon',
        ),
    ]
