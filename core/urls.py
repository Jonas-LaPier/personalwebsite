from django.urls import path
from . import views

urlpatterns = [
    path("", views.about, name="about"), path("cv/", views.cv, name="cv"),
    path("blog/", views.blog, name="blog"), path("blog/<slug:slug>/", views.post_detail, name="post_detail"),
]

