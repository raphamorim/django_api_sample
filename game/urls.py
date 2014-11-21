from django.conf.urls import url

from game import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game/$', views.game, name='game'),
    url(r'^user/$', views.user, name='user'),
]
