from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Comment


def all_comment(request):
    obj = Comment.objects.all()
    context = {'obj': obj}
    return render(request, "post/post.html", context)


def comment_thread(request, id):
    return render(request, "post/comment_thread.html", {})


def comment_delete(request, id):
    obj = Comment.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return render(request,'post/All_Post_Students.html')
    context = {
        "obj": obj
    }
    return render(request, "post/confirm_delete.html", context)