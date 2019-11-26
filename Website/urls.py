"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from User.views import *
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from Library.views import *
from posts.views import *
from comments.views import *
from todo.views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('success/', success, name='success'),
    path('library/books/', book_view, name='library_books'),
    path('logout/',user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('books/', book_home, name='books'),
    path('all_notices/', all_notice_home, name='all_notice'),
    path('all_bsc_notices/', all_bsc_notice, name='all_bsc_notice'),
    path('all_msc_notices/', all_msc_notice, name='all_msc_notice'),
    path('exampapers/', exampaper_home, name='exampapers'),
    path('syllabus/', syllabus_home, name='syllabus'),
    path('library/all_notices/', all_notice, name='library_all_notice'),
    path('library/timetables/', timetable, name='library_timetable'),
    path('library/exampapers/', exampaper, name='library_exampaper'),
    path('library/syllabus/', syllabus, name='library_syllabus'),
    path('department/', department, name='department'),
    path('about/department/', library_department, name='library_department'),
    path('faculty/', faculty, name='faculty'),
    path('about/faculty/', library_faculty, name='library_faculty'),
    path('alumni/', alumni, name='alumni'),
    path('about/alumni/', library_alumni, name='library_alumni'),
    path('contact/', mail, name='contact'),
    path('profile_gallery/', library_gallery, name='library_gallery'),
    path('gallery/', gallery, name='gallery'),
    path('admission/', admission, name='admission'),
    path('about/admission/', library_admission, name='library_admission'),
    path('editprofile/', editprofile, name='editprofile'),
    path('viewprofile/', viewprofile, name='viewprofile'),
    path('change-password/', change_password, name='change_password'),
    path('comments/', all_comment, name='comment'),
    #To-do
    path('user/ToDo/', todo, name='todo'),
    path('user/add_list/', todo_add, name='addlist'),
    path('delete/<list_id>', delete, name='delete'),
    path('cross_off/<list_id>', cross_off, name='cross_off'),
    path('uncross/<list_id>', uncross, name='uncross'),
    #Posts
    path('demopost/', post_details, name='demoposts'),
    path('all_post/', temp_allpost, name='posts'),
    path('create_post/', post_create, name='create_post'),
    url(r'^(?P<id>\d+)/$', post_details, name='post_details'),
    path('allStudentsPost/', allpoststudents, name='studentposts'),
    url(r'^post_details_student/(?P<id>\d+)/$', post_details_student, name='post_details_student'),
    url(r'^allStudentsPost/(?P<id>\d+)/delete/$', post_delete, name='post_delete_details'),
    url(r'^comments/(?P<id>\d+)/$', comment_thread, name='thread'),
    url(r'^(?P<id>\d+)/delete/$', comment_delete, name='comment_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

