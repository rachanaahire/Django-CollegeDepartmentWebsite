# Generated by Django 2.1.4 on 2019-02-21 15:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20190221_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poststudent',
            name='user',
            field=models.ForeignKey(max_length=100, on_delete='Uploaded By', to=settings.AUTH_USER_MODEL),
        ),
    ]
