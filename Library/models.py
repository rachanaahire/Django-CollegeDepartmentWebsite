from django.db import models
from User.models import Teacher

# Create your models here.

COURSE_CHOICES= (
        ('BSC', 'BSC'),
        ('MSC', 'MSC'),
    )
CLASS_CHOICES= (
        ('First Year', 'First Year'),
        ('Second Year', 'Second Year'),
        ('Third Year', 'Third Year'),
    )
SEM_CHOICES= (
        ('First Semester', 'First Semester'),
        ('Second Semester', 'Second Semester'),
        ('Third Semester', 'Third Semester'),
        ('Fourth Semester', 'Fourth Semester'),
        ('Fifth Semester', 'Fifth Semester'),
        ('Sixth Semester', 'Sixth Semester')
    )

CHOICES= (
    ('Public', 'Public'),
    ('Private', 'Private')
)


class Book(models.Model):
    uploaded_by = models.ForeignKey(Teacher,'Uploaded by')
    book_name = models.CharField('Book Name', max_length=100)
    summary = models.CharField('Summary', max_length=160, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    course = models.CharField('Select Course', max_length=100, choices=COURSE_CHOICES, blank=True, null=True)
    select_class = models.CharField('Select Class', max_length=100, choices=CLASS_CHOICES, null=True, blank=True)
    semester = models.CharField('Select Semester', max_length=100, choices=SEM_CHOICES, null=True, blank=True)
    access= models.CharField('Access to', max_length=100, choices=CHOICES, null=True)
    upload_book = models.FileField(upload_to='Ebooks/', default= True)

    def __str__(self):
        hello = '{0.book_name}, {0.summary}, {0.course}, {0.select_class}, {0.semester}'
        return hello.format(self)


class Syllabu(models.Model):
    uploaded_by = models.ForeignKey(Teacher,'Uploaded by')
    syllabus = models.CharField('Syllabus Year', max_length=20, unique=True, db_index=True)
    summary = models.CharField('Summary', max_length=160,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    course = models.CharField('Select Course', max_length=100, choices=COURSE_CHOICES, blank=True, null=True)
    select_class = models.CharField('Select Class', max_length=100, choices=CLASS_CHOICES, null=True, blank=True)
    semester = models.CharField('Select Semester', max_length=100, choices=SEM_CHOICES, null=True, blank=True)
    access = models.CharField('Access to', max_length=100, choices=CHOICES, null=True)
    upload_syllabus = models.FileField(upload_to='Syllabus/', default= True)

    def __str__(self):
        hello = '{0.syllabus}, {0.summary}, {0.course}, {0.select_class}'
        return hello.format(self)


class Notice(models.Model):
    uploaded_by = models.ForeignKey(Teacher,'Uploaded by')
    notice = models.CharField('Notice', max_length=30, unique=True, db_index=True)
    summary = models.CharField('Summary', max_length=160,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    course = models.CharField('Select Course', max_length=100, choices=COURSE_CHOICES, blank=True, null=True)
    select_class = models.CharField('Select Class', max_length=100, choices=CLASS_CHOICES, null=True, blank=True)
    semester = models.CharField('Select Semester', max_length=100, choices=SEM_CHOICES, null=True, blank=True)
    access= models.CharField('Access to', max_length=100, choices=CHOICES, null=True)
    upload_notice = models.FileField(upload_to='Notices', default= True)

    def __str__(self):
        hello = '{0.notice}, {0.summary}'
        return hello.format(self)


class ExamPaper(models.Model):
    uploaded_by = models.ForeignKey(Teacher,'Uploaded by')
    exam_paper = models.CharField('Exam Paper Year & Month', max_length=20, unique=True, db_index=True)
    summary = models.CharField('Subject & Summary', max_length=160,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    course = models.CharField('Select Course', max_length=100, choices=COURSE_CHOICES, blank=True, null=True)
    select_class = models.CharField('Select Class', max_length=100, choices=CLASS_CHOICES, null=True, blank=True)
    semester = models.CharField('Select Semester', max_length=100, choices=SEM_CHOICES, null=True, blank=True)
    access= models.CharField('Access to', max_length=100, choices=CHOICES, null=True)
    upload_exam_paper = models.FileField(upload_to='ExamPapers/', max_length=200, default= True)

    def __str__(self):
        hello = '{0.exam_paper}, {0.summary}, {0.course}, {0.select_class}, {0.semester}'
        return hello.format(self)


class TimeTable(models.Model):
    uploaded_by = models.ForeignKey(Teacher,'Uploaded by')
    time_table = models.CharField('Description', max_length=30, unique=True, db_index=True)
    summary = models.CharField('Summary', max_length=160,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    course = models.CharField('Select Course', max_length=100, choices=COURSE_CHOICES, blank=True, null=True)
    select_class = models.CharField('Select Class', max_length=100, choices=CLASS_CHOICES, null=True, blank=True)
    semester = models.CharField('Select Semester', max_length=100, choices=SEM_CHOICES, null=True, blank=True)
    upload_timetable = models.FileField(upload_to='TimeTables/', default= True)

    def __str__(self):
        hello = '{0.time_table}, {0.summary}'
        return hello.format(self)








