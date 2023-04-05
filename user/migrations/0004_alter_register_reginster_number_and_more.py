# Generated by Django 4.1.7 on 2023-04-01 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='reginster_number',
            field=models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='Invalid Register_number', message='Length has to be 12', regex='^\\d{12}$')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='year_of_passing',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(code='Invalid Register_number', message='Length has to be 4', regex='^\\d{4}$')]),
        ),
    ]
