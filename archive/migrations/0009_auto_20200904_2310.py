# Generated by Django 3.1 on 2020-09-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0008_auto_20200904_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='date',
            field=models.DateTimeField(verbose_name='تاریخ انتشار:'),
        ),
    ]