from django.db import models

# Create your models here.
class OpenSourceCourses(models.Model):
    instructor = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)


    def __str__(self):
        return self.title
