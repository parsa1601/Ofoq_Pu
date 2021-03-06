from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator

class MyAccountManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, city, education, field, organization, password=None):
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
        if not field:
            raise ValueError('وارد کردن رشته تحصیلی الزامی است!')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            city=city,
            education=education,
            field=field,
            organization=organization,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, city, education, field, organization,
                         password):
        user = self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            city=city,
            education=education,
            field=field,
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
    phone = models.CharField('تلفن همراه', blank=True, max_length=15)
    username = models.CharField('نام کاربری', unique=True, max_length=50)
    first_name = models.CharField('نام', unique=True, max_length=50)
    last_name = models.CharField('نام خانوادگی', unique=True, max_length=50)
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
    birth_month = models.CharField('ماه تولد', null=True, blank=True, choices=MONTH_CHOICES, max_length=10)
    birth_year = models.IntegerField(
        'سال تولد',
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1300),
        ]
    )
    birth_day = models.IntegerField(
        'روز تولد',
        null=True,
        blank=True,
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
    education = models.CharField('پایه/مقطع تحصیلی', choices=EDUCATION_CHOICE, max_length=30)
    field = models.CharField('رشته تحصیلی', max_length=50)
    organization = models.CharField('نام مدرسه/دانشگاه/محل کار', max_length=50)
    date_joined = models.DateTimeField('تاریخ عضویت', auto_now_add=True)
    is_vip = models.BooleanField('کاربر ویژه (می تواند تمام مقالات را بخواند)', default=False)
    is_admin = models.BooleanField('کاربر ادمین باشد', default=False)
    is_active = models.BooleanField('فعال است', default=True)
    is_staff = models.BooleanField('کاربر می تواند وارد صفحه ادمین شود', default=False)
    is_superuser = models.BooleanField(
        'کاربر می تواند به تمام محتواهای سایت دسترسی داشته و آنها را تغییر دهد',
        default=False
    )

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'city', 'education', 'organization', 'field']

    def __str__(self):
        return self.username

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Request(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField('پیام به ادمین', blank=True, null=True)
    response = models.TextField('پاسخ ادمین', blank=True, null=True)
    date = models.DateTimeField('تاریخ درخواست')


    class Meta:
        abstract = True


class ArticleRequest(Request):
    title = models.CharField('عنوان (حداکثر 100 کاراکتر)', max_length=100)
    summary = models.TextField('چکیده پیشنهادی متن (حداکثر 300 کاراکتر)', max_length=300)
    file = models.FileField('متن خود را در قالب فایل word یا pdf آپلود کنید')
    image1 = models.ImageField('عکس اول (اختیاری)', blank=True, null=True)
    image2 = models.ImageField('عکس دوم (اختیاری)', blank=True, null=True)
    image3 = models.ImageField('عکس سوم (اختیاری)', blank=True, null=True)
    image4 = models.ImageField('عکس چهارم (اختیاری)', blank=True, null=True)
    image5 = models.ImageField('عکس پنجم (اختیاری)', blank=True, null=True)
    is_accepted = models.BooleanField('منتشر می شود', default=False)


    class Meta:
        verbose_name = 'درخواست انتشار مقاله'
        verbose_name_plural = 'درخواست های انتشار مقاله'



class NotArticle(Request):
    TYPE_CHOICES = (
        ('درخواست ارتقاء به کاربر ویژه', 'درخواست ارتقاء به کاربر ویژه'),
        ('انتقاد یا پیشنهاد', 'انتقاد یا پیشنهاد'),
        ('دیگر', 'دیگر')
    )
    type = models.CharField('نوع پیام', choices=TYPE_CHOICES, max_length=30)


    class Meta:
        verbose_name = 'درخواست'
        verbose_name_plural = 'درخواست ها و پیشنهادات'