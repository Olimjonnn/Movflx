# Generated by Django 3.2.9 on 2022-02-11 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcmovies',
            name='link',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upcmovies',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]