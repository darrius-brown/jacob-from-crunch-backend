# Generated by Django 4.1.7 on 2023-03-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jacob', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='description',
        ),
        migrations.AddField(
            model_name='exercise',
            name='bodypart',
            field=models.CharField(default='bodypart', max_length=100),
        ),
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.CharField(default='category', max_length=100),
        ),
    ]
