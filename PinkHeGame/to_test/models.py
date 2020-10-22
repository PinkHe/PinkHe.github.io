from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    tel = models.CharField(max_length=11)
    addr = models.CharField(max_length=120)

class Student(models.Model):
    name = models.CharField(max_length=10)
    info = models.OneToOneField(StudentInfo, on_delete=models.CASCADE)



stu = Student() 
meta = StudentInfo()