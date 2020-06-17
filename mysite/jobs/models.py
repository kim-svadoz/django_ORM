from django.db import models

# Create your models here.
class Person(models.Model) : 
    objects = models.Manager()
    name = models.CharField(max_length=150)
    past_job = models.TextField()

    def __str__(self):
        return f'{self.name}님의 전생은.. {self.past_job}'