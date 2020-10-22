from django.contrib import admin

# Register your models here.
from .models import Student, StudentInfo

admin.sites.reverse(Student)
admin.sites.reverse(StudentInfo)