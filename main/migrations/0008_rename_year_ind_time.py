# Generated by Django 3.2.9 on 2022-02-17 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_ind_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ind',
            old_name='year',
            new_name='time',
        ),
    ]
