from django.conf.urls import url
from home.views import HomeView
from . import views
from django.urls import path

urlpatterns = [
    #url(r'^$',HomeView.as_view(),name='home')
    path('#', HomeView.post),
]