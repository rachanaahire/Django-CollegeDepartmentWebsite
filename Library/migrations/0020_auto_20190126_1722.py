# Generated by Django 2.1.4 on 2019-01-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0019_auto_20190126_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exampaper',
            name='exam_paper',
            field=models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Exam Paper Year & Month'),
        ),
        migrations.AlterField(
            model_name='exampaper',
            name='summary',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='Subject & Summary'),
        ),
        migrations.AlterField(
            model_name='exampaper',
            name='upload_exam_paper',
            field=models.FileField(default=True, max_length=200, upload_to='ExamPapers/'),
        ),
    ]