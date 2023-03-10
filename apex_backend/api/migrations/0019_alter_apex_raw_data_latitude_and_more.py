# Generated by Django 4.0 on 2022-12-19 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_deployment_site_directory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apex_raw_data',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='apex_raw_data',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='apex_raw_data',
            name='time_stamp',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=21, null=True),
        ),
    ]
