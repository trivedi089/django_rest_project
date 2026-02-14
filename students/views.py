from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from students.models import Student


# Create your views here.
def students(request):
    data = list(Student.objects.all().values())
    print(data)
    return JsonResponse(data, safe=False)