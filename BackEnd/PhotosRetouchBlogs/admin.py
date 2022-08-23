from django.contrib import admin

from .models import BlogCategorie, Blog, BlogsComment


@admin.register(BlogCategorie)
class BlogCategorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'url')
    fields = ('name','url','date')
    prepopulated_fields = {"url":("name",)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'category')
    fields= ['date', ('title', 'url'), ('category', 'feature_picture'), 'descriptions']
    prepopulated_fields = {"url":("title",)}


@admin.register(BlogsComment)
class BlogsCommentsAdmin(admin.ModelAdmin):
    list_display = ('blog', 'date', 'name', 'email')
    fields= ('blog', 'date', 'name', 'email', 'published', 'comment')
