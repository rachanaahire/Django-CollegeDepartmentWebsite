from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from User.forms import EditProfileForm
from User import forms
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from posts.forms import *


# Create your views here.
from .models import Post
from comments.models import *
from comments.forms import *


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        user= request.POST.get("user")
        title = request.POST.get("title")
        content = request.POST.get("content")
        PostStudent.objects.create(user=user, title=title,content=content)
        messages.success(request, "Successfully Posted")
    #if form.is_valid():
        #instance = form.save(commit=False)
        #instance.save()
    context = {
        "form": form,

    }
    return render(request, "post/create_post.html", context)


def temp_post(request):
    return render(request, 'post/Posts.html', {})


def temp_allpost(request):
    obj = Post.objects.all()
    context = {'obj': obj}
    return render(request, 'post/All_Post.html', context)


def allpoststudents(request):
    if not request.user.is_staff or request.user.is_staff:
        obj = PostStudent.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        obj = obj.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__icontains=query)|
            Q(timestamp__icontains=query)
        ).distinct()
    context = {'obj': obj}
    return render(request, 'post/All_Post_Students.html', context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item </a>Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post/create_post.html", context)


def post_details(request, id=None):
    instance = get_object_or_404(Post, id=id)
    content_type = ContentType.objects.get_for_model(Post)
    obj_id = instance.id
    comments = Comment.objects.filter(content_type=content_type, object_id=obj_id)
    initial_data = {
        "content_type": content_type,
        "object_id": instance.id
    }
    form = CommentForm(request.POST or None, initial= initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            content = content_data,
            parent = parent_obj,
        )



    context = {
        "title":instance.title,
        "instance":instance,
        "comments": comments,
        "form": form,
        "obj_id": obj_id,
    }
    return render(request, "post/Posts.html", context)


def post_details_student(request, id=None):
    instance = get_object_or_404(PostStudent, id=id)
    content_type = ContentType.objects.get_for_model(PostStudent)
    obj_id = instance.id
    comments = CommentStudent.objects.filter(content_type=content_type, object_id=obj_id)
    initial_data = {
        "content_type": content_type,
        "object_id": instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = CommentStudent.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )

    context = {
        "title": instance.title,
        "instance": instance,
        "comments": comments,
        "form": form,
        "obj_id": obj_id,
    }
    return render(request, "post/post_details_student.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(PostStudent, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return render(request, 'post/All_Post_Students.html', {})
