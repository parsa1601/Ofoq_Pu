from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    pub_date = models.DateField('تاریخ انتشار:')
    main_image = models.ImageField(
        upload_to='static/articles/images',
        blank=True
    )
    content1 = models.CharField(max_length=4000)
    image1 = models.ImageField(
        upload_to='static/articles/images',
        blank=True
    )
    content2 = models.CharField(
        max_length=4000,
        blank=True
    )
    image2 = models.ImageField(
        upload_to='static/articles/images',
        blank=True
    )
    content3 = models.CharField(
        max_length=4000,
        blank=True
    )
    image3 = models.ImageField(
        upload_to='static/articles/images',
        blank=True
    )
    content4 = models.CharField(
        max_length=4000,
        blank=True
    )
    image4 = models.ImageField(
        upload_to='static/articles/images',
        blank=True
    )
    content5 = models.CharField(
        max_length=4000,
        blank=True
    )
    image5 = models.ImageField(
        upload_to='static/articles/images',
        blank=True
    )

    def __str__(self):
        return self.title

    @classmethod
    def get_authors_articles(cls, username):
        return cls.objects.filter(author=username)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reply_id = models.IntegerField(default=-1)
    username = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField()