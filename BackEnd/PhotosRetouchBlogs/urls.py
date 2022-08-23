from django.urls import path
from . views import CategoriesView, BlogView, BlogsCommentsView

urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('blogs/', BlogView.as_view(), name='blogs'),
    path('blogs-comments/', BlogsCommentsView.as_view(), name='blogs_comments'),
]
