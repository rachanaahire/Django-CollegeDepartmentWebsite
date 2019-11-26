from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from User.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail
from User import forms

# Create your views here.


def index(request):
    return render(request, "base.html", {})


def department(request):
    return render(request, "department.html", {})


def faculty(request):
    return render(request, "faculty.html", {})


def alumni(request):
    return render(request, "alumni.html", {})


def gallery(request):
    return render(request, "gallery.html", {})


def contact(request):
    return render(request, "contact.html", {})


def admission(request):
    return render(request, "admission.html", {})


def viewprofile(request):
    args= {'user': request.user}
    return render(request, "user/viewprofile.html", args)


def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/viewprofile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, "user/editprofile.html", args)


def library_department(request):
    return render(request, "library/department.html", {})


def library_faculty(request):
    return render(request, "library/faculty.html", {})


def library_alumni(request):
    return render(request, "library/alumni.html", {})


def library_gallery(request):
    return render(request, "library/gallery.html", {})


def library_admission(request):
    return render(request, "library/admission.html", {})


def user_login(request):
    context= {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username=username, password= password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))
        else:
            context["error"]= "Provide Valid Credentials!!!"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", {})


def success(request):
    context = {}
    context['user']= request.user
    return render(request, "success.html", {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def user_profile(request):
    args = {'user': request.user}
    return render(request, "user/profile.html", args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/viewprofile/')
        else:
            return redirect('/change-password/')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'user/change_password.html', args)


def mail(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        message = request.POST['message']
        send_mail('Contact Form',
                  'First name: '+fname+'\nLast Name: '+lname+'\n Message: '+message,
                  settings.EMAIL_HOST_USER,
                  ['rachanaahire98@gmail.com'],
                  fail_silently=False)

    return render(request,'contact.html')
