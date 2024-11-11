from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.course.title}"
