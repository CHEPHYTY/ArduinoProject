from django.urls import path, include
from .views import postUNOdata

urlpatterns = [path("postdata/", postUNOdata)]
