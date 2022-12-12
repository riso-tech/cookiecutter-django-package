from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("{{ cookiecutter.app_slug }}/", include("{{ cookiecutter.app_slug }}.urls")),
]
