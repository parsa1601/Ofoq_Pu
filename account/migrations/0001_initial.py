# Generated by Django 3.1 on 2020-09-07 17:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='ایمیل')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='تلفن همراه')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='نام کاربری')),
                ('first_name', models.CharField(max_length=50, unique=True, verbose_name='نام')),
                ('last_name', models.CharField(max_length=50, unique=True, verbose_name='نام خانوادگی')),
                ('birth_month', models.CharField(blank=True, choices=[('فروردین', 'فروردین'), ('اردیبهشت', 'اردیبهشت'), ('خرداد', 'خرداد'), ('تیر', 'تیر'), ('مرداد', 'مرداد'), ('شهریور', 'شهریور'), ('مهر', 'مهر'), ('آبان', 'آبان'), ('آذر', 'آذر'), ('دی', 'دی'), ('بهمن', 'بهمن'), ('اسفند', 'اسفند')], max_length=10, null=True, verbose_name='ماه تولد')),
                ('birth_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1300)], verbose_name='سال تولد')),
                ('birth_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)], verbose_name='روز تولد')),
                ('city', models.CharField(max_length=30, verbose_name='شهر محل سکونت')),
                ('education', models.CharField(choices=[('دبستان', 'دبستان'), ('پایه هفتم', 'پایه هفتم'), ('پایه هشتم', 'پایه هشتم'), ('پایه نهم', 'پایه نهم'), ('پایه دهم', 'پایه دهم'), ('پایه یازدهم', 'پایه یازدهم'), ('پایه دوازدهم', 'پایه دوازدهم'), ('دانشجوی کارشناسی', 'دانشجوی کارشناسی'), ('دانشجوی کارشناسی ارشد', 'دانشجوی کارشناسی ارشد'), ('دانشجوی دکتری', 'دانشجوی دکتری'), ('شاغل', 'شاغل')], max_length=30, verbose_name='پایه/مقطع تحصیلی')),
                ('field', models.CharField(max_length=50, verbose_name='رشته تحصیلی')),
                ('organization', models.CharField(max_length=50, verbose_name='نام مدرسه/دانشگاه/محل کار')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('is_vip', models.BooleanField(default=False, verbose_name='کاربر ویژه (می تواند تمام مقالات را بخواند)')),
                ('is_admin', models.BooleanField(default=False, verbose_name='کاربر ادمین باشد')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال است')),
                ('is_staff', models.BooleanField(default=False, verbose_name='کاربر می تواند وارد صفحه ادمین شود')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='کاربر می تواند به تمام محتواهای سایت دسترسی داشته و آنها را تغییر دهد')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='NotArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='پیام به ادمین')),
                ('response', models.TextField(blank=True, null=True, verbose_name='پاسخ ادمین')),
                ('date', models.DateTimeField(verbose_name='تاریخ درخواست')),
                ('type', models.CharField(choices=[('درخواست ارتقاء به کاربر ویژه', 'درخواست ارتقاء به کاربر ویژه'), ('انتقاد یا پیشنهاد', 'انتقاد یا پیشنهاد'), ('دیگر', 'دیگر')], max_length=30, verbose_name='نوع پیام')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'درخواست',
                'verbose_name_plural': 'درخواست ها و پیشنهادات',
            },
        ),
        migrations.CreateModel(
            name='ArticleRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='پیام به ادمین')),
                ('response', models.TextField(blank=True, null=True, verbose_name='پاسخ ادمین')),
                ('date', models.DateTimeField(verbose_name='تاریخ درخواست')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان (حداکثر 100 کاراکتر)')),
                ('summary', models.TextField(max_length=300, verbose_name='چکیده پیشنهادی متن (حداکثر 300 کاراکتر)')),
                ('file', models.FileField(upload_to='', verbose_name='متن خود را در قالب فایل word یا pdf آپلود کنید')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس اول (اختیاری)')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس دوم (اختیاری)')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس سوم (اختیاری)')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس چهارم (اختیاری)')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس پنجم (اختیاری)')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='منتشر می شود')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'درخواست انتشار مقاله',
                'verbose_name_plural': 'درخواست های انتشار مقاله',
            },
        ),
    ]
