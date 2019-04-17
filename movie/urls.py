from django.conf.urls import url
from .views import *
from home.models import User


app_name = "movie"
urlpatterns = [


        url(r'^movie_index/$', movie_index),
        url(r'^movie_create/$', movie_create),
        url(r'^(?P<id>\d+)/$', movie_detail,name="movie_detail"),
        url(r'^(?P<id>\d+)/movie_update/$', movie_update,name="movie_update"),
        url(r'^add_movie/$',add_multiple_movie),
        url(r'^favorite_movies/$',favorite_movie),
        url(r'^didnt_watch/$',didnt_watch),
        url(r'^watched/$',watched),
   ]

