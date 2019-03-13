from django.utils.translation import gettext_lazy as _

from .exceptions import MissingSettingNames, MultipleSettingDefaults
from .mixins import BaseSettingMixin

__all__ = ('setting_mixin_factory',)


def setting_mixin_factory(*names, setting='', default='', **kwargs):
    """Create a setting mixin from the provided name(s) and kwargs.

    Take a series of setting names and create a mixin that already
    handles all of those names. If only one setting name is provided,
    then the setting label and default may also be passed into the
    factory.
    """

    if len(names) == 0:
        raise MissingSettingNames(_(
            'setting_mixin_factory() expects to receive the name of '
            'at least one setting. Please provide the keyword that '
            'the setting value will be assigned to.'
        ))

    if len(names) > 1 and (setting != '' or default != ''):
        raise MultipleSettingDefaults(_(
            'When setting_mixin_factory() is called with %(count)s '
            "setting names it doesn't expect to handle the setting "
            'label and default as well.'
        ) % {"count": len(names)})

    for name in names:
        kwargs.update({
            f'{name}_default': default,
            f'{name}_setting': setting,
        })

    kwargs['_setting_names'] = names
    return type('SettingMixin', (BaseSettingMixin,), kwargs)
