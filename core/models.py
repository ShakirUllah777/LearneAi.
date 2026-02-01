from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    education = models.TextField()
    image = models.ImageField(upload_to='about/')
