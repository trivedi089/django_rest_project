from django.http import JsonResponse
from rest_framework import status

from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#decorator
@api_view(['GET'])
def studentsView(request):
    # data = list(Student.objects.all().values())
    # print(data)
    # return JsonResponse(data, safe=False)
    #Mthod based views
    if request.method == 'GET':
        #Get all the data from the student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

