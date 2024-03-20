# Generated by Django 4.1.13 on 2024-03-15 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_defaultcustomerfields_icon'),
        ('company', '0003_remove_defaultcompanyfields_icon'),
        ('Leads', '0003_remove_defaultleadfields_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
