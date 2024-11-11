from django import forms
from .models import Student, Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'lastname', 'age',]


