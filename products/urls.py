from django.conf.urls import url
from .views import (
    ProductAPIView, 
    ProductAPIDetailView,
    )

app_name= 'products'

urlpatterns = [
    url(r'^$', ProductAPIView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductAPIDetailView.as_view(), name='detail'),
]
