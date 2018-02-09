from django.conf.urls import url

from backend.views import *

urlpatterns = [
    url(r'^banners', banners, name='backend_banners_index'),
]