from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from stdimage.models import StdImageField

# Create your models here.

class Category(models.Model):
    cat_name = models.TextField()

    def __str__(self):
        return self.cat_name

class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    category_post = models.ForeignKey(Category, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = StdImageField(upload_to= '%Y/%m/%d/',variations={'thumbnail': {'width': 640, 'height': 480}})
    FEATURED_POST = (
        ('featured', 'Featured Post'),
        ('not', 'Not Featured'),
    )
    featured_post = models.CharField(max_length=256, choices=FEATURED_POST, default='not')
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    # image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="475")
    # image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="464")

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    email = models.EmailField(max_length=256)
    message = models.TextField()
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.message