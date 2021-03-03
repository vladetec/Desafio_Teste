
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # User Management
    path("accounts/", include("allauth.urls")),
    # Local
    path("", include("apps.urls", namespace="apps")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)