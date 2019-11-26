from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save, post_delete


# Create your models here.


class Student(AbstractBaseUser):
    Name = models.CharField('Name', max_length=20, null=True)
    Surname = models.CharField('Surname', max_length=10, null=True)
    username = models.CharField('username', max_length=20, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True, null=True)
    joined = models.DateTimeField(auto_now_add=True)
    rollno = models.PositiveSmallIntegerField('Roll Number', unique=True, null=True)
    phoneno = models.PositiveSmallIntegerField('Phone Number', unique=True, null=True)
    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username


class Teacher(AbstractBaseUser):
    Name = models.CharField('Name', max_length=10)
    Surname = models.CharField('Surname', max_length=10)
    username = models.CharField('username', max_length=20, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    phoneno = models.PositiveSmallIntegerField('Phone Number', unique=True)
    password = models.CharField('password', max_length=10)
    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        student = Student.objects.create(username=kwargs['instance'])


post_save.connect(create_profile, sender=User)


