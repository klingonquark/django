"""
Projekt URLs
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("token", obtain_auth_token, name="get-token"),
    path('admin/', admin.site.urls),
    path("events/", include("events.urls")),
    path("api/events/", include("events.api.urls")),
    path('accounts/', include('django.contrib.auth.urls')),

    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="v2"),
        name="schema",
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),


] + debug_toolbar_urls()
