from django import forms
from .models import Student

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('roll_no', 'name', 'std', 'birthdate')

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('roll_no', 'name', 'std', 'birthdate')