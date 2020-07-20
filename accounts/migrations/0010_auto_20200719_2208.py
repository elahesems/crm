# Generated by Django 3.0.8 on 2020-07-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='names',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
