# Generated by Django 4.0 on 2022-12-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_deployment_site_directory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment_site',
            name='directory_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
