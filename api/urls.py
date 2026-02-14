from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:id>/', views.studentDetailView),

    #class based view
    path('employees/', views.Employees.as_view()),
    path('employees/<int:id>/', views.EmployeeDetail.as_view()),
]