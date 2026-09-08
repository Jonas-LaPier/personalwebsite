from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=220)),
                ("slug", models.SlugField(unique=True, help_text="Used in the post URL")),
                ("excerpt", models.TextField(blank=True, max_length=420)),
                ("body", models.TextField(help_text="Plain text. Blank lines create paragraphs.")),
                ("cover_image", models.ImageField(blank=True, upload_to="blog/")),
                ("status", models.CharField(choices=[("draft", "Draft"), ("published", "Published")], default="draft", max_length=12)),
                ("published_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-published_at", "-created_at"]},
        ),
        migrations.CreateModel(
            name="CVSection",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="SiteProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="Your Name", max_length=120)),
                ("tagline", models.CharField(default="Researcher, maker, and lifelong learner", max_length=220)),
                ("about", models.TextField(default="Write a short introduction here. Share what you do, what you care about, and what you are working toward.")),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("location", models.CharField(blank=True, max_length=120)),
                ("portrait", models.ImageField(blank=True, upload_to="profile/")),
                ("resume_file", models.FileField(blank=True, upload_to="documents/")),
                ("linkedin_url", models.URLField(blank=True)),
                ("github_url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="CVItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("organization", models.CharField(blank=True, max_length=200)),
                ("location", models.CharField(blank=True, max_length=120)),
                ("start_date", models.CharField(blank=True, help_text="For example: 2022", max_length=40)),
                ("end_date", models.CharField(blank=True, help_text="For example: Present", max_length=40)),
                ("description", models.TextField(blank=True)),
                ("link", models.URLField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("section", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="core.cvsection")),
            ],
            options={"ordering": ["order", "-id"]},
        ),
    ]
