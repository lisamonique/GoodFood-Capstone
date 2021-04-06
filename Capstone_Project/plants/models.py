from django.db import models

# Create your models here.

class Food(models.Model):
    text = models.CharField(max_length=200)
    parsed = models.CharField(max_length=200)
    hints = models.CharField(max_length=200)
    _links = models.CharField(max_length=200)
    labels = models.CharField(max_length=50)
    image = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.text
