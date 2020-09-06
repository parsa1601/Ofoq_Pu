from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self):
        pass

class Account(AbstractBaseUser):
    email = models.EmailField('ایمیل', blank=True, max_length=100)
    username = models.CharField('نام کاربری', unique=True, max_length=50)
    first_name = models.CharField('نام', max_length=50)
    last_name = models.CharField('نام خانوادگی', max_length=50)
    MONTH_CHOICES = (
        ('فروردین','فروردین'),
        ('اردیبهشت','اردیبهشت'),
        ('خرداد','خرداد'),
        ('تیر','تیر'),
        ('مرداد','مرداد'),
        ('شهریور','شهریور'),
        ('مهر','مهر'),
        ('آبان','آبان'),
        ('آذر','آذر'),
        ('دی','دی'),
        ('بهمن','بهمن'),
        ('اسفند','اسفند'),
    )
    birth_month = models.CharField('ماه تولد', choises=MONTH_CHOICES)
    birth_year = models.IntegerField('سال تولد')
    birth_day = models.IntegerField('روز تولد',
        validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ]
    )
    date_joined = models.DateTimeField('تاریخ عضویت', auto_now_add=True)
    is_vip = models.BooleanField('کاربر ویژه (می تواند تمام مقالات را بخواند)', default=false)
    is_admin = models.BooleanField('کاربر ادمین باشد', default=False)
    is_active = models.BooleanField('فعال است', default=true)
    is_staff = models.BooleanField('کاربر می تواند وارد صفحه ادمین شود', default=false)
    is_superuser = models.BooleanField(
        'کاربر می تواند به تمام محتواهای سایت دسترسی داشته و آنها را تغییر دهد',
        default=false
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True