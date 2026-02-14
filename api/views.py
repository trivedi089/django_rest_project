from django.http import JsonResponse
from rest_framework import status

from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#decorator
@api_view(['GET', 'POST'])
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
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def studentDetailView(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)