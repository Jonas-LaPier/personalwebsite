from django.contrib import admin
from .models import BlogPost, CVItem, CVSection, SiteProfile

admin.site.site_header = "Personal Site Editor"
admin.site.site_title = "Site Editor"

@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    fieldsets = (("Introduction", {"fields": ("name", "tagline", "about", "portrait")}),
                 ("Contact & links", {"fields": ("email", "location", "linkedin_url", "github_url", "resume_file")}))
    def has_add_permission(self, request): return not SiteProfile.objects.exists()

class CVItemInline(admin.StackedInline):
    model = CVItem
    extra = 1

@admin.register(CVSection)
class CVSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    inlines = [CVItemInline]

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "published_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "excerpt", "body")
    prepopulated_fields = {"slug": ("title",)}

