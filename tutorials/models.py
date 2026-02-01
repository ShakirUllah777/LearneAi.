from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='tutorials/')
    youtube_url = models.URLField()
