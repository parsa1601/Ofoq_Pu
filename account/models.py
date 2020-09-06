from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, city, education, organization, password=None):
        if not username:
            raise ValueError('داشتن نام کاربری الزامی است!')
        if not first_name:
            raise ValueError('وارد کردن نام الزامی است!')
        if not last_name:
            raise ValueError('وارد کردن نام خانوادگی الزامی است!')
        if not city:
            raise ValueError('وارد کردن شهر محل سکونت الزامی است!')
        if not education:
            raise ValueError('وارد کردن پایه/مقطع تحصیلی الزامی است!')
        if not organization:
            raise ValueError('وارد کردن مدرسه/دانشگاه/محل کار الزامی است!')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            city=city,
            education=education,
            organization=organization,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, city, education, organization, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            city=city,
            education=education,
            organization=organization,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.is_vip = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField('ایمیل', blank=True, max_length=100)
    phone = models.PhoneNumberField('تلفن همراه', blank=True)
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
    birth_year = models.IntegerField(
        'سال تولد',
        validators=[
            MinValueValidator(1300),
        ]
    )
    birth_day = models.IntegerField(
        'روز تولد',
        validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ]
    )
    city = models.CharField('شهر محل سکونت', max_length=30)
    EDUCATION_CHOICE = (
        ('دبستان','دبستان'),
        ('پایه هفتم','پایه هفتم'),
        ('پایه هشتم','پایه هشتم'),
        ('پایه نهم','پایه نهم'),
        ('پایه دهم','پایه دهم'),
        ('پایه یازدهم','پایه یازدهم'),
        ('پایه دوازدهم','پایه دوازدهم'),
        ('دانشجوی کارشناسی','دانشجوی کارشناسی'),
        ('دانشجوی کارشناسی ارشد','دانشجوی کارشناسی ارشد'),
        ('دانشجوی دکتری','دانشجوی دکتری'),
        ('شاغل','شاغل')
    )
    education = CharField('پایه/مقطع تحصیلی', choices=EDUCATION_CHOICE)
    organization = CharField('نام مدرسه/دانشگاه/محل کار', max_length=50)
    date_joined = models.DateTimeField('تاریخ عضویت', auto_now_add=True)
    is_vip = models.BooleanField('کاربر ویژه (می تواند تمام مقالات را بخواند)', default=false)
    is_admin = models.BooleanField('کاربر ادمین باشد', default=False)
    is_active = models.BooleanField('فعال است', default=true)
    is_staff = models.BooleanField('کاربر می تواند وارد صفحه ادمین شود', default=false)
    is_superuser = models.BooleanField(
        'کاربر می تواند به تمام محتواهای سایت دسترسی داشته و آنها را تغییر دهد',
        default=false
    )

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'city', 'education', 'organization']

    def __str__(self):
        return self.username

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True