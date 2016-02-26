"""blog Models Configuration."""
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    blog 어플리케이션의 Post Model Class.

    author          : 작성자(models.ForeignKey 타입)
    title           : 글 제목(models.CharField 타입)
    text            : 글 내용(models.TextField)
    created_date    : 글 생성일자(models.DateTimeField 타입)
    published_date  : 글 출판일자(models.DateTimeField 타입)
    """

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Post의 publish_date 생성."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Post의 title 값 반환."""
        return self.title
