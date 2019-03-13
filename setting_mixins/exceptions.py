__all__ = ('MissingSettingNames', 'MultipleSettingsWithDefaults',)


class MissingSettingNames(Exception):
    """The factory wasn't passed the names of any settings.

    The factory function expects to receive the name of at least one
    setting.
    """
    pass


class MultipleSettingsWithDefaults(Exception):
    """The factory was passed multiple names with kwargs.

    When the factory function is passed the names of multiple settings
    there shouldn't be a default value or a setting label also passed
    to the function. If we allowed this the same label and value would
    be set for each name.
    """
    pass
