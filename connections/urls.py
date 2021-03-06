from django.urls import re_path
from connections import views

app_name = 'connections'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^requests_table/$', views.requests_table, name='requests_table'),
    re_path(r'^approved_table/$', views.approved_table, name='approved_table'),
    re_path(r'^rejected_table/$', views.rejected_table, name='rejected_table'),
    re_path(r'^request_connection/$', views.request_connection, name='request_connection'),
    re_path(r'^modify_connection/(?P<slug>[-\w]+)/$', views.modify_connection, name='modify_connection'),
    re_path(r'^delete_connection/(?P<slug>[-\w]+)/$', views.delete_connection, name='delete_connection'),
    re_path(r'^approve_connection/(?P<slug>[-\w]+)/$', views.approve_connection, name='approve_connection'),

]
