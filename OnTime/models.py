from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    rating = models.IntegerField()
    email = models.EmailField()
    profession = models.CharField(max_length=40)
    image = models.ImageField()
    login = models.DateTimeField(auto_now=True)
    attendance = models.BooleanField(default=False)
    phone = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.first_name+' '+self.last_name

class face(models.Model):
    pface = models.CharField(max_length=40)
    dt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.pface

