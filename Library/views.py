from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Book, ExamPaper, TimeTable, Notice, Syllabu
from Library.forms import LibraryForm

# Create your views here.


def all_notice_home(request):
    form = LibraryForm
    obj = Notice.objects.filter(access="Public")
    context = {'form': form, 'obj': obj}
    return render(request, "all_notice.html", context)


def all_notice(request):
    form = LibraryForm
    obj = Notice.objects.all()
    context = {'form': form, 'obj': obj}
    return render(request, "library/all_notice.html", context)


def all_bsc_notice(request):
    form = LibraryForm
    obj = Notice.objects.filter(course= "BSC")
    context = {'form': form, 'obj':obj}
    return render(request, "library/all_bsc_notice.html", context)


def all_msc_notice(request):
    form = LibraryForm
    obj = Notice.objects.filter(course= "MSC")
    context = {'form': form, 'obj':obj}
    return render(request, "library/all_msc_notice.html", context)


def book_home(request):
    form = LibraryForm
    obj = Book.objects.filter(access="Public")
    context = {'form': form, 'obj': obj}
    return render(request, "books.html", context)


def book_view(request):
    form = LibraryForm
    obj = Book.objects.all()
    context = {'form': form, 'obj':obj}
    return render(request, "library/books.html", context)


def exampaper_home(request):
    form = LibraryForm
    obj = ExamPaper.objects.filter(access="Public")
    context = {'form': form, 'obj': obj}
    return render(request, "exampapers.html", context)


def exampaper(request):
    form = LibraryForm
    obj = ExamPaper.objects.all()
    context = {'form': form, 'obj': obj}
    return render(request, "library/exampapers.html", context)


def syllabus_home(request):
    form = LibraryForm
    obj = Syllabu.objects.filter(access="Public")
    context = {'form': form, 'obj': obj}
    return render(request, "syllabus.html", context)


def syllabus(request):
    form = LibraryForm
    obj = Syllabu.objects.all()
    context = {'form': form, 'obj': obj}
    return render(request, "library/syllabus.html", context)


def timetable(request):
    form = LibraryForm
    obj = TimeTable.objects.all()
    context = {'form': form, 'obj': obj}
    return render(request, "library/timetable.html", context)


