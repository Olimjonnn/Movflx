# Generated by Django 3.2.9 on 2022-02-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Main/')),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UpcMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='UpcMovies/')),
                ('name', models.CharField(max_length=200)),
                ('time', models.IntegerField()),
                ('year', models.IntegerField()),
                ('score', models.CharField(max_length=222)),
            ],
        ),
    ]