from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    url(r'^view/$', views.test, name='test'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail') #글 내용
]
