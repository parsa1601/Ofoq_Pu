from django.db import models
from utilities.jalali_utils import jalali_convert

class AudioFile(models.Model):
    title = models.CharField(
                            'عنوان',
                            max_length=800
                            )
    creator = models.CharField(
                            'ایجادکننده',
                            max_length=100
                            )
    date = models.DateTimeField(
                            'تاریخ انتشار:'
                            )
    file_url = models.FileField(
                                'آپلود فایل',
                                upload_to='archive/audios/'
                                )

    def jalali_publish(self):
        return jalali_convert(self.date)
    jalali_publish.short_description = 'تاریخ انتشار'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'فایل صوتی'
        verbose_name_plural = 'فایل های صوتی'