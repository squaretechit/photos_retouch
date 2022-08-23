from django.contrib import admin

from .models import Service, ServiceSlider, ServicePortfolio, ServiceGallerie, ServiceCalculator


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    fields = (('date', 'service_simble'), ('name', 'url'), 'description')
    prepopulated_fields = {"url":("name",)}


@admin.register(ServiceCalculator)
class ServiceCalculatorAdmin(admin.ModelAdmin):
    list_display = ('service', 'date', 'price_form', 'price_to')
    fields = (('date', 'pricing_image'), 'service', ('price_form', 'price_to'), 'work_process')


@admin.register(ServiceSlider)
class ServiceSliderAdmin(admin.ModelAdmin):
    list_display = ('service', 'date')


@admin.register(ServicePortfolio)
class ServiceSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'date')
    fields = ('date', 'service', 'title', ('before_image', 'after_image'), 'description')


@admin.register(ServiceGallerie)
class ServiceGallerieAdmin(admin.ModelAdmin):
    list_display = ('service', 'date')
    fields = ('date', 'service', 'image')
