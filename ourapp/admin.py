from django.contrib import admin
from .models import School, Department, Faculty, Degree, Passing, Student

# Register your models here.

admin.site.register(School)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Degree)
admin.site.register(Passing)
admin.site.register(Student)