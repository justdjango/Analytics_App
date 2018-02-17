
from django.conf.urls import url
from django.contrib import admin

from blogs.views import BlogListView, BlogDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/$', BlogListView.as_view(), name='list'),
    url(r'^blogs/(?P<pk>\d+)/$', BlogDetailView.as_view(), name='detail'),
]
