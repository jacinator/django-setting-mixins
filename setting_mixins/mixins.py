from django.conf import settings

__all__ = ('BaseSettingMixin',)


class BaseSettingMixin:
    """The basic handler for the setting mixin factory.

    Provide the most basic methods for getting values from the Django
    settings.
    """

    _setting_names = ()

    def __init__(self, *args, **kwargs):
        for name in self._setting_names:
            kwargs.setdefault(name, self.get_setting(name))
        super().__init__(*args, **kwargs)

    def get_setting(self, name):
        return getattr(
            settings,
            getattr(self, f'{name}_setting'),
            getattr(self, f'{name}_default'),
        )
