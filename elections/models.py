# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"


class Candidate(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)  # e.g., President, Secretary
    manifesto = models.TextField()

    def __str__(self):
        return f"{self.student.full_name} - {self.position}"


class Vote(models.Model):
    voter = models.ForeignKey(Student, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.full_name} voted for {self.candidate.student.full_name}"
