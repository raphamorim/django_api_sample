from django.conf.urls import url

from game import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/$', views.category, name='category'),
]
