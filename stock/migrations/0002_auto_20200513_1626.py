# Generated by Django 3.0.3 on 2020-05-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='body_txt',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='stock',
            name='short_txt',
            field=models.TextField(default='-'),
        ),
    ]
