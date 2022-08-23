from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import BlogCategorie, Blog, BlogsComment
from .serializers import BlogCategorieSerializer, BlogSerializer, BlogsCommentsSerializer


class CategoriesView(generics.RetrieveAPIView):
    queryset = BlogCategorie.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogCategorieSerializer(queryset, many=True)
        return Response(serializer.data)


class BlogView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)


class BlogsCommentsView(generics.RetrieveAPIView):
    queryset = BlogsComment.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BlogsCommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogsCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Your comment is under modaration. Admin will publish it soon.'})