
from django.conf.urls import url
from django.contrib import admin

from analytics.views import analytics_view
from blogs.views import BlogListView, BlogDetailView
from survey.views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^analytics/$', analytics_view, name='analytics'),
    url(r'^blogs/$', BlogListView.as_view(), name='list'),
    url(r'^blogs/(?P<pk>\d+)/$', BlogDetailView.as_view(), name='detail'),
    url(r'^survey/', index)
]
