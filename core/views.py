from django.shortcuts import get_object_or_404, render
from .models import BlogPost, CVSection

def about(request): return render(request, "core/about.html")
def cv(request): return render(request, "core/cv.html", {"sections": CVSection.objects.prefetch_related("items")})
def blog(request): return render(request, "core/blog.html", {"posts": BlogPost.objects.filter(status="published")})
def post_detail(request, slug):
    return render(request, "core/post_detail.html", {"post": get_object_or_404(BlogPost, slug=slug, status="published")})

