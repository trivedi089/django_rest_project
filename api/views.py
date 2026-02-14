from django.http import JsonResponse
from students.models import Student

# Create your views here.
def studentsView(request):
    data = list(Student.objects.all().values())
    print(data)
    return JsonResponse(data, safe=False)

