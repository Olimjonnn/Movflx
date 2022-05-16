from django.urls import path
from .views import *

urlpatterns = [
    path("", Index, name="index"),
    path("contact/", Contact, name="contact"),
    path("blog/", Blog, name="blog"),
    path("movie/", Movie, name="movie"),
    path("movie-details/ <int:pk>/", MovieDetails, name="movie-details"),
    path("blog-details/ <int:pk>/", BlogDetails, name="blog-details"),
]
