# Generated by Django 4.0 on 2022-12-17 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_remove_customer_city_remove_customer_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='contact',
        ),
    ]
