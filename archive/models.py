from django.db import models

class file(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    file_upl = models.FileField()

    def __str__(self):
        return self.title