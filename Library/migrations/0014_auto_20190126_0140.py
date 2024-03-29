# Generated by Django 2.1.4 on 2019-01-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0013_auto_20190126_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='access',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=100, null=True, verbose_name='Access to'),
        ),
        migrations.AddField(
            model_name='exampaper',
            name='access',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=100, null=True, verbose_name='Access to'),
        ),
        migrations.AddField(
            model_name='notice',
            name='access',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=100, null=True, verbose_name='Access to'),
        ),
        migrations.AddField(
            model_name='syllabu',
            name='access',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=100, null=True, verbose_name='Access to'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='access',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=100, null=True, verbose_name='Access to'),
        ),
    ]
