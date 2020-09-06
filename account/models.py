from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Account(AbstractBaseUser):
    email = models.EmailField('ایمیل', blank=True, max_length=100)
    username = models.CharField('نام کاربری', unique=True, max_length=50)
    first_name = models.CharField('نام', max_length=50)
    last_name = models.CharField('نام خانوادگی', max_length=50)
    date_joined = models.DateTimeField('تاریخ عضویت', auto_now_add=True)
    is_vip = models.BooleanField('کاربر ویژه (می تواند تمام مقالات را بخواند)', default=false)
    is_admin = models.BooleanField('کاربر ادمین باشد', default=False)
    is_active = models.BooleanField('فعال است', default=true)
    is_staff = models.BooleanField('کاربر می تواند وارد صفحه ادمین شود', default=false)
    is_superuser = models.BooleanField(
        'کاربر می تواند به تمام محتواهای سایت دسترسی داشته و آنها را تغییر دهد',
        default=false
    )
