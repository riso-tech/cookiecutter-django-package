"""Register Models for Admin Interface."""
from django.conf import settings
from django.contrib import admin

if "django_admin" in settings.INSTALLED_APPS:
    from django_admin.admin import site  # noqa: F401
else:
    site = admin.site
