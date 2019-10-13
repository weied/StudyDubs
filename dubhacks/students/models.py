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

class Answer(models.Model):
    name = models.CharField(max_length=64)
    gpa = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    visual = models.IntegerField()
    auditory = models.IntegerField()
    kinect = models.IntegerField()

    def __str__(self):
        return self.name + '\n' + f'gpa: {self.gpa}' + '\n' + f'visual: {self.visual}'\
                + '\n' + f'auditory: {self.auditory}' + '\n' + f'kinect: {self.kinect}'
class Summary(models.Model):
    date = models.DateField()
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.date + f', rating: {self.rating}'
