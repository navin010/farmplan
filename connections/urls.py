from django.urls import re_path
from connections import views

app_name = 'connections'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^show_table/$', views.show_table, name='show_table'),
    re_path(r'^request_connection/$', views.request_connection, name='request_connection'),
    #re_path(r'^change_connection/$', views.change_connection.as_view(), name='change_connection'),

]
