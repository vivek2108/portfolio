from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/')


