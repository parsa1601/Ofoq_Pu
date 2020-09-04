from django.db import models

class Audio_File(models.Model):
    Title = models.CharField(
                            'عنوان',
                            max_length=800
                            )
    Creator = models.CharField(
                            'ایجادکننده',
                            max_length=100
                            )
    Date = models.DateField(
                            'تاریخ انتشار:'
                            )
    file_url = models.FileField(
                                'آپلود فایل',
                                upload_to='archive/audios/'
                                )

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'فایل صوتی'
        verbose_name_plural = 'فایل های صوتی'