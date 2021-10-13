from django.db import models


# Create your models here.
class bus(models.Model):
    img = models.ImageField(upload_to='gallery')
    name = models.CharField(max_length=250)
    destination = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)
