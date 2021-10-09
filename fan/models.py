from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()
    list_display = ['name', 'hero_set', 'vilan']
    serch=['firstname','lastname']




    def __str__(self):
        return self.name


class Rail(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=123)
    phone=models.IntegerField(default=+91)
    date=models.DateField()
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return self.email



class Pnna(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122,default='')
    phone = models.CharField(max_length=122,default='')


    def __str__(self):
        return self.name



