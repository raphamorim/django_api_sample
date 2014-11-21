from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gameApi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^v1/', include('game.urls')) ,
    url(r'^admin/', include(admin.site.urls)),
)
