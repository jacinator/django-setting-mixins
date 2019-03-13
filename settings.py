INSTALLED_APPS = (
    'setting_mixins',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SECRET_KEY = 'secret_key_for_testing'
