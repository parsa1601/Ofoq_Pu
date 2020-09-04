from django.db import models


class Article(models.Model):
    author = models.CharField(
        'نویسنده',
        max_length=100
    )
    title = models.CharField(
        'عنوان مقاله',
        max_length=200
    )
    summary = models.TextField(
        'چکیده',
        max_length=300
    )
    pub_date = models.DateField('تاریخ انتشار')
    main_image = models.ImageField(
        'عکس اصلی',
        blank=True
    )
    content1 = models.TextField(
        'قسمت اول محتوا'
    )
    image1 = models.ImageField(
        'عکس اول',
        blank=True
    )
    content2 = models.TextField(
        'قسمت دوم محتوا',
        blank=True
    )
    image2 = models.ImageField(
        'عکس دوم',
        blank=True
    )
    content3 = models.TextField(
        'قسمت سوم محتوا',
        blank=True
    )
    image3 = models.ImageField(
        'عکس سوم',
        blank=True
    )
    content4 = models.TextField(
        'قسمت چهارم محتوا',
        blank=True
    )
    image4 = models.ImageField(
        'عکس چهارم',
        blank=True
    )
    content5 = models.TextField(
        'قسمت پنجم محتوا',
        blank=True
    )
    image5 = models.ImageField(
        'عکس پنجم',
        blank=True
    )

    def __str__(self):
        return self.title

    @classmethod
    def get_authors_articles(cls, username):
        return cls.objects.filter(author=username)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reply_id = models.IntegerField(default=-1)
    username = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField()