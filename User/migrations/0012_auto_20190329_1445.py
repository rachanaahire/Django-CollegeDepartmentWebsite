# Generated by Django 2.1.5 on 2019-03-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_auto_20190216_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Name',
            field=models.CharField(max_length=20, null=True, verbose_name='Name'),
        ),
    ]
