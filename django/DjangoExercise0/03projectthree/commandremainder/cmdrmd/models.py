from django.db import models

# Create your models here.
class CmdRemainder(models.Model):
    text = models.TextField()

    # predefinded method with constructor "self"
    def __str__(self):
        return self.text
