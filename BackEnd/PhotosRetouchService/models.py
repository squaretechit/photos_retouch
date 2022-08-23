from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class Service(models.Model):
    name = models.CharField(max_length=255)
    url = models.SlugField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    description = RichTextUploadingField(
        blank=True, null=True, help_text="43 words 303 characters")
    service_simble = models.ImageField(
        default='default.png', upload_to='services_simble', help_text="124 x 124 pixels")

    def __str__(self):
        return str(self.name)


class ServiceCalculator(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    price_form = models.FloatField(default=00.00)
    price_to = models.FloatField(default=00.00)
    pricing_image = models.ImageField(
        upload_to='pricing_images', help_text="600 x 320 pixels, before and after image")
    work_process = models.TextField()

    def __str__(self):
        return str(self.service)


class ServiceSlider(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    slider_image = models.ImageField(
        default='default.png', upload_to='services_slider_images', help_text="2400 x 750 pixels")

    def __str__(self):
        return str(self.service)


class ServicePortfolio(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = models.TextField()
    before_image = models.ImageField(
        default='default.png', upload_to='portfolio_images', help_text="460 x 600 pixels")
    after_image = models.ImageField(
        default='default.png', upload_to='portfolio_images', help_text="460 x 600 pixels")

    def __str__(self):
        return str(self.title)


class ServiceGallerie(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        default='default.png', upload_to='services_gallery_images', help_text="770 x 432 pixels")

    def __str__(self):
        return str(self.service)
