from pyexpat import model
from re import T
from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class ClientReview(models.Model):
    client_name = models.CharField(max_length=255)
    client_picture = models.ImageField(default='default.png', upload_to='review_client_pictures', help_text="106 x 106 pixels")
    review = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.client_name)


class OurTeam(models.Model):
    date = models.DateTimeField(default=timezone.now)
    member_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    picture = models.ImageField(default='default.png', upload_to='team_pictures', help_text="270 x 300 pixels")

    def __str__(self):
        return str(self.member_name)


class SubscriptionEmail(models.Model):
    email = models.EmailField(max_length=70)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.email)


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    phone_number = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return str(self.name)


class QuoteForm(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    services = models.TextField()
    message = models.TextField(blank=True)
    filelink = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.client_name)


class QuoteFormImage(models.Model):
    quote = models.ForeignKey(QuoteForm, on_delete=models.CASCADE)
    email = models.EmailField()
    images = models.ImageField(default='default.png', upload_to='quote_images')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Client Name: {self.quote.client_name}, Client Email: {self.quote.client_name}"
