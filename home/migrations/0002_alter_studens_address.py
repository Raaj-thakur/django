# Generated by Django 5.0 on 2024-01-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studens',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
