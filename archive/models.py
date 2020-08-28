from django.db import models

class file(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    file_url = models.FileField(upload_to='archive/pdfs/' )

    def __str__(self):
        return self.title