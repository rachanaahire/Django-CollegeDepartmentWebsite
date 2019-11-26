from django.db import models
from django.contrib.auth.models import User
from User.models import Teacher, Student
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify


# Create your models here.


class PostManager(models.Manager):
    def active(self,*args,**kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish_lte=timezone.now())


class Post(models.Model):
    user = models.ForeignKey(Teacher,'Uploaded By',default=1)
    title = models.CharField(max_length=120)
    image = models.FileField(upload_to='Post', null=True, blank=True)
    content = models.TextField(max_length=2000)
    link = models.TextField(null=True, blank=True)
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title


class PostStudent(models.Model):
    user = models.CharField('Uploaded By', max_length=100)
    title = models.CharField(max_length=120)
    image = models.FileField(upload_to='Post', null=True, blank=True)
    content = models.TextField(max_length=2000, null=False)
    link = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp","-updated"]



