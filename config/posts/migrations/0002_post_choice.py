# Generated by Django 3.1.1 on 2020-10-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='choice',
            field=models.CharField(choices=[('a', 'all'), ('b', 'brand'), ('c', 'img-man'), ('d', 'creative'), ('e', 'web'), ('f', 'print-mat')], default='a', max_length=1),
        ),
    ]
