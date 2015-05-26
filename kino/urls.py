from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'page.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^category/(?P<id>\d+).html$', 'blog.views.category_detail', name='category_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
