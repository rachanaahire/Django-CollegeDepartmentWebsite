# Generated by Django 2.1.4 on 2019-02-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]
