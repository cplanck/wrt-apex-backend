# Generated by Django 4.0 on 2022-12-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_apex_raw_data_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apex_raw_data',
            name='filename',
            field=models.CharField(default='', max_length=200),
        ),
    ]