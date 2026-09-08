from django.db import models
from django.urls import reverse
from django.utils import timezone

class SiteProfile(models.Model):
    name = models.CharField(max_length=120, default="Your Name")
    tagline = models.CharField(max_length=220, default="Researcher, maker, and lifelong learner")
    about = models.TextField(default="Write a short introduction here. Share what you do, what you care about, and what you are working toward.")
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    portrait = models.ImageField(upload_to="profile/", blank=True)
    resume_file = models.FileField(upload_to="documents/", blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    def __str__(self): return self.name

    @classmethod
    def get_solo(cls):
        return cls.objects.first() or cls.objects.create()

class CVSection(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order", "id"]
    def __str__(self): return self.title

class CVItem(models.Model):
    section = models.ForeignKey(CVSection, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.CharField(max_length=40, blank=True, help_text="For example: 2022")
    end_date = models.CharField(max_length=40, blank=True, help_text="For example: Present")
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order", "-id"]
    def __str__(self): return self.title

class BlogPost(models.Model):
    STATUS = [("draft", "Draft"), ("published", "Published")]
    title = models.CharField(max_length=220)
    slug = models.SlugField(unique=True, help_text="Used in the post URL")
    excerpt = models.TextField(max_length=420, blank=True)
    body = models.TextField(help_text="Plain text. Blank lines create paragraphs.")
    cover_image = models.ImageField(upload_to="blog/", blank=True)
    status = models.CharField(max_length=12, choices=STATUS, default="draft")
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta: ordering = ["-published_at", "-created_at"]
    def __str__(self): return self.title
    def get_absolute_url(self): return reverse("post_detail", args=[self.slug])
    def save(self, *args, **kwargs):
        if self.status == "published" and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
