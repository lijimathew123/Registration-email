# Generated by Django 4.1.13 on 2024-03-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldtype',
            name='icon',
            field=models.ImageField(blank=True, default='', upload_to='field_icons'),
        ),
    ]
