# Generated by Django 3.2.4 on 2021-06-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_customer_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='e_mail',
            field=models.EmailField(max_length=150),
        ),
    ]