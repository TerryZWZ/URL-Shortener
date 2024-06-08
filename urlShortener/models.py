from django.db import models

# Shortened URL
class ShortURL(models.Model):
    Original_URL = models.URLField(max_length = 700)
    Short_URL = models.CharField(max_length = 100)
    Time_Created = models.DateTimeField()

    def __str__(self):
        return self.Original_URL