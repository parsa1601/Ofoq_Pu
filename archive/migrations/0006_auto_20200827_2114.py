# Generated by Django 3.1 on 2020-08-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_auto_20200827_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_url',
            field=models.FileField(upload_to='archive/pdfs/'),
        ),
    ]