from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse

urlpatterns = [
    path("healthz/", lambda request: JsonResponse({"status": "ok"})),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
