from django.db import models

class PDF(models.Model):
    title = models.CharField(
                            'عنوان',
                            max_length=800
                            )
    author = models.CharField(
                            'نویسنده',
                            max_length=100
                            )
    date = models.DateField(
                            'تاریخ انتشار:'
                            )
    file_url = models.FileField(
                                'آپلود فایل',
                                upload_to='archive/audios/'
                                )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نشریه'
        verbose_name_plural = 'نشریات'