# Generated by Django 3.2.4 on 2021-07-03 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='middle_name',
        ),
    ]
