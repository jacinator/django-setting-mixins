from django import test

from .exceptions import MissingSettingNames, MultipleSettingsWithDefaults
from .factories import setting_mixin_factory
from .mixins import BaseSettingMixin


def test_setting_mixin(mixin, **attrs):
    """Create a testable version of the setting mixin.

    The setting mixin passes through kwargs to an expected `super`
    object. When that object doesn't exist it causes errors. This
    function takes the mixin in question and adds that `super` object
    so that the mixin can be tested.
    """

    # The __init__ method for the parent object, so that it will accept
    # kwargs and store them so they can be tested.
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    # Create the parent object for testing the setting mixin and return
    # the subclass of the mixin and the parent.
    parent = type('TestSettingMixin', (), {'__init__': __init__})
    return type('SettingMixin', (mixin, parent), attrs)


BaseSettingMixin = test_setting_mixin(
    BaseSettingMixin,
    _setting_names=('country', 'website'),
    country_default='Erebor',
    country_setting='COUNTRY',
    website_default='www.erebor.net',
    website_setting='WEBSITE',
)


@test.override_settings(COUNTRY='Khazad Dum')
class BaseSettingMixinTestCase(test.TestCase):

    @test.override_settings(WEBSITE='www.khazad-dum.net')
    def test_get_settings(self):
        self.assertDictEqual(BaseSettingMixin().kwargs, {
            'country': 'Khazad Dum',
            'website': 'www.khazad-dum.net',
        })

    def test_get_defaults(self):
        self.assertDictEqual(BaseSettingMixin().kwargs, {
            'country': 'Khazad Dum',
            'website': 'www.erebor.net',
        })


FactorySettingMixin = test_setting_mixin(
    setting_mixin_factory('country', 'website'),
    country_default='Erebor',
    country_setting='COUNTRY',
    website_default='www.erebor.net',
    website_setting='WEBSITE',
)


@test.override_settings(COUNTRY='Khazad Dum')
class FactorySettingMixinTestCase(test.TestCase):

    @test.override_settings(WEBSITE='www.khazad-dum.net')
    def test_get_settings(self):
        self.assertDictEqual(FactorySettingMixin().kwargs, {
            'country': 'Khazad Dum',
            'website': 'www.khazad-dum.net',
        })

    def test_get_setting_method(self):
        self.assertEqual(FactorySettingMixin().get_setting('country'), 'Khazad Dum')

    def test_get_defaults(self):
        self.assertDictEqual(FactorySettingMixin().kwargs, {
            'country': 'Khazad Dum',
            'website': 'www.erebor.net',
        })

    def test_error_no_settings(self):
        with self.assertRaisesMessage(MissingSettingNames, (
            'setting_mixin_factory() expects to receive the name of '
            'at least one setting. Please provide the keyword that '
            'the setting value will be assigned to.'
        )):
            setting_mixin_factory()

    def test_error_has_kwargs(self):
        with self.assertRaisesMessage(MultipleSettingsWithDefaults, (
            'When setting_mixin_factory() is called with 2 setting '
            "names it doesn't expect to handle the setting label and "
            'default as well.'
        )):
            setting_mixin_factory(
                'country', 'website',
                setting='COUNTRY',
                default='Erebor',
            )


SingleSettingMixin = test_setting_mixin(
    setting_mixin_factory(
        'country',
        setting='COUNTRY',
        default='Erebor',
    ),
)


@test.override_settings(COUNTRY='Khazad Dum')
class SingleSettingMixinTestCase(test.TestCase):

    def test_get_setting(self):
        self.assertDictEqual(SingleSettingMixin().kwargs, {
            'country': 'Khazad Dum'
        })


class InheritedSettingMixinTestCase(test.TestCase):

    def test_inherited_class(self):
        class InheritedSettingMixin(SingleSettingMixin):
            pass
