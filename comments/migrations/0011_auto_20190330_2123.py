# Generated by Django 2.1.4 on 2019-03-30 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0010_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentstudent',
            name='post',
            field=models.ForeignKey(default=1, on_delete='Post', to='posts.PostStudent'),
        ),
    ]
