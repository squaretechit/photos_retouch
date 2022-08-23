from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class BlogCategorie(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    url = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    title = models.CharField(max_length=500)
    url = models.SlugField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    descriptions = RichTextUploadingField(blank=True, null=True)
    feature_picture = models.ImageField(default='default.png', upload_to='blog_feature_pictures', help_text="1200 x 628 pixels")
    category = models.ForeignKey(BlogCategorie, related_name="blog_category", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title)


class BlogsComment(models.Model):
    blog = models.ForeignKey(Blog, related_name="blog_comment_blog", on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    comment = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
