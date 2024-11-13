from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Student
 

def students_list(request: HttpRequest) -> HttpResponse:
    template = 'school/students_list.html'
    context = {'student': Student.objects}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    for student in Student.objects.all():
        print(student.teachers.all()[0])

    return render(request, template, context)
