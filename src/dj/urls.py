from django.contrib import admin
from django.urls import path

from analytics.views import analytics_view
from blogs.views import BlogListView, BlogDetailView
from survey.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('analytics/', analytics_view, name='analytics'),
    path('blogs/', BlogListView.as_view(), name='list'),
    path('blogs/<pk>/', BlogDetailView.as_view(), name='detail'),
    path('survey/', index)
]
