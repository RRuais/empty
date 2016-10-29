from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/register$', views.register, name='register'),
    url(r'^users/show$', views.users, name='users'),
    url(r'^users/login$', views.login, name='login'),
    url(r'^users/logout$', views.logout, name='logout'),
    url(r'^users/delete/(?P<id>\w+)$', views.delete_users, name='delete_users'),
    url(r'^wall$', views.wall, name='wall'),
    url(r'^post_message$', views.post_message, name='post_message'),
    url(r'^messages/delete/(?P<id>\w+)$', views.delete_message, name='delete_message'),
    url(r'^comments/post/(?P<id>\w+)$', views.post_comment, name='post_comment'),
    url(r'^comments/delete/(?P<id>\w+)$', views.delete_comment, name='delete_comment'),
]
