from rest_framework import serializers

from .models import BlogCategorie, Blog, BlogsComment


class BlogCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategorie
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogsCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsComment
        fields = '__all__'

