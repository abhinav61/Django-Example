from django.urls import path, re_path
from App import views

#Template tagging
app_name = 'App'

urlpatterns = [
    re_path(r'^relative/$',views.relative,name = 'relative'),
    re_path(r'^other/$',views.other,name = 'other'),
]
