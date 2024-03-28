from django.contrib import admin
from django.urls import path, include
from student.views import home_view

urlpatterns = [
	path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('student/', include('student.urls', namespace='student')),
]
