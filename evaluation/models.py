from django.db import models

class Training(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class Instructor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=True)
    expectation = models.CharField(max_length=50, null=True, blank=True)
    courseware = models.CharField(max_length=50, null=True, blank=True)
    instructor_assessment = models.CharField(max_length=50, null=True, blank=True)
    general_evaluation = models.CharField(max_length=50)
    others = models.TextField(null=True, blank=True)
