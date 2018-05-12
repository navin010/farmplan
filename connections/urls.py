from django.urls import re_path
from connections import views

app_name = 'connections'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^table/$', views.table, name='table'),

]
