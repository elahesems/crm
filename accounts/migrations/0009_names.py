# Generated by Django 3.0.8 on 2020-07-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_order_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
