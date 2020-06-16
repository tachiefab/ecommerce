from django.conf.urls import url, include
from django.contrib import admin
from .views import UserDetailAPIView, UserProductAPIView

app_name= 'accounts'

urlpatterns = [
    url(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<username>\w+)/products/$', UserProductAPIView.as_view(), name='product-list'),
]