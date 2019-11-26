from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
from posts.models import Post
from User.models import *



class Comment(models.Model):
    user = models.CharField('Uploaded By', max_length=100)
    post = models.ForeignKey(Post, 'Post', null=False, blank=False, default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=True )


    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.user)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


class CommentStudent(models.Model):
    user = models.CharField('Uploaded By', max_length=100)
    post = models.ForeignKey(Post, 'Post', null=False, blank=False, default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=True )


    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.user)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True