from django.db import models


# Create your models here.
class Note(models.Model):
    description = models.TextField()

    def get_excerpt(self, char):
        return self.description[:char]