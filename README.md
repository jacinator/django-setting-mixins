# django-setting-mixins

This library is to help with passing Django settings through to objects
as key-word arguments. I saw this being done enough that I thought it
could be helpful.

The core of django-setting-mixins is `setting_mixin_factory`. This
function takes the name of the key-word(s) and optionally the name of
the setting and the default value. It returns a mixin class that will
include that key-word paired with the setting or default value.

## A single setting

If you are only referencing a single Django setting there are two ways
to use the factory.

```python
LanguageCode = setting_mixin_factory(
    'language_code',
    setting='LANGUAGE_CODE',
    default='en-ca',
)


class WithLanguageCode(LanguageCode, WithoutLanguageCode):
    # This approach is very reusable. If this setting and default pair
    # is one that you'll use a lot this is a good approach.

    pass


class WithLanguageCode(setting_mixin_factory('language_code'), WithoutLanguageCode):
    # This approach is a bit more concise, but it's less reusable. This
    # is a good option if you have a lot of one-off references to your
    # Django settings.
    
    # You could still pass in the `setting` and `default` as key-words
    # to the factory, but the can get line length quite long.

    language_code_setting = 'LANGUAGE_CODE'
    language_code_default = 'en-ca'
```

## Multiple settings

The `setting_mixin_factory` will help you with multiple settings as
well. However, it only takes one set of key-word `setting` and
`default` arguments. As a result if you provide more than one setting
key-word name to the factory it won't let you use the `setting` and
`default` values.

```python
class WithInternationalCodes(setting_mixin_factory('language_code', 'country_code'), WithoutInternationalCodes):
    # As you can see, using multiple codes starts getting a bit long.
    # At this point you might prefer not to use the factory. This
    # approach also isn't the DRYest since you'll need to repeat all
    # these lines next time.

    language_code_setting = 'LANGUAGE_CODE'
    language_code_default = 'en-ca'
    country_code_setting = 'COUNTRY_CODE'
    country_code_default = 'CA'


class InternationalCodes(setting_mixin_factory('language_code', 'country_code')):
    # This approach saves the values in a subclassed mixin that can be
    # re-referenced by multiple subclasses.

    language_code_setting = 'LANGUAGE_CODE'
    language_code_default = 'en-ca'
    country_code_setting = 'COUNTRY_CODE'
    country_code_default = 'CA'


class WithInternationalCodes(InternationalCodes, WithoutInternationalCodes):
    pass
```
