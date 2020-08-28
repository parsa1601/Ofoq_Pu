from django.db import models

class PDF(models.Model):
    Title = models.CharField(max_length=800)
    Author = models.CharField(max_length=100)
    Date = models.DateField(models.DateField('تاریخ انتشار:'))
    file_url = models.FileField(upload_to='archive/pdfs/')

    def __str__(self):
        return self.Title