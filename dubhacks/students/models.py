from django.db import models

# Create your models here.
class Option(models.Model):
    option = models.CharField(max_length=64)

    def __str__(self):
        return self.option

class Question(models.Model):
    question = models.CharField(max_length=64)
    notes = models.CharField(max_length=128, blank=True, default="")
    name = models.CharField(max_length=64, default="")
    options = models.ManyToManyField(Option, blank=True, related_name="question")

    def __str__(self):
        return self.question + ' ' + self.notes
