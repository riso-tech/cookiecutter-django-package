"""App Config for {{ cookiecutter.app_slug }} app."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class {{ cookiecutter.app_slug|replace('_', ' ')|title|replace(' ', '') }}sConfig(AppConfig):
    name = "{{ cookiecutter.app_slug }}"
    verbose_name = _("{{ cookiecutter.project_slug|replace('_', ' ')|title }}s")

    def ready(self):
        try:
            import {{ cookiecutter.app_slug }}.signals  # noqa F401
        except ImportError:
            pass
