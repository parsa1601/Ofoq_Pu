# Generated by Django 3.1 on 2020-08-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofoqSchool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_file',
            name='file_url',
            field=models.FileField(upload_to='archive/audios/'),
        ),
    ]
