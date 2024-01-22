
from django.db import models

class ImageText(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
