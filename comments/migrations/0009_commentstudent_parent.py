# Generated by Django 2.1.4 on 2019-02-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_auto_20190222_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentstudent',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='comments.CommentStudent'),
        ),
    ]