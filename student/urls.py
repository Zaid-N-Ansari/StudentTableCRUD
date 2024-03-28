from django.urls import path
from .views import create, read, update, delete, delete_student_record

app_name = 'student'

urlpatterns = [
	path('create/', create, name='create'),
	path('read/', read, name='read'),
	path('update/<int:roll_no>', update, name='update'),
	path('delete/<int:roll_no>', delete, name='delete'),
	path('delete_student_record/<int:roll_no>', delete_student_record, name='delete_student_record'),
]
