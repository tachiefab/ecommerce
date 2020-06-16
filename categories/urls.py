from django.conf.urls import url
from .views import CategoryAPIView

app_name= 'categories'

urlpatterns = [
    url(r'^$', CategoryAPIView.as_view(), name='list'),
]
