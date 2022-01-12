from django.db import models


class University(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="uni_student")

    def __str__(self):
        return self.first_name + " " + self.last_name
