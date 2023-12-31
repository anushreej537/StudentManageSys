from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=255)

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    fees = models.IntegerField()
    duration = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.course_name

class Addstudent(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    mobileno = models.IntegerField()
    address = models.TextField()
    degree = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)


class Addteacher(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    work = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    mobileno = models.IntegerField()