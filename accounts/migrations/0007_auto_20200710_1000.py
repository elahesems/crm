# Generated by Django 3.0.8 on 2020-07-10 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200708_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='data_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='data_created',
            new_name='date_created',
        ),
    ]
