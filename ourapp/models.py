from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.name

class Department(models.Model):
    Department = models.CharField(max_length=60)
    School = models.ForeignKey(School, on_delete=models.CASCADE)

class Faculty(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

class Degree(models.Model):
    Degree = models.CharField(max_length=60)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

class Passing(models.Model):
    passing = models.BooleanField(default=False)

class Student(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    Degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True)
    Passing = models.ForeignKey(Passing, on_delete=models.CASCADE, null=True)
    date_of_graduation = models.DateField(default=datetime.today)

    def __str__(self):
        return self.first_name
