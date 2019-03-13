import setuptools

long_description = (
    "django-setting-mixins provides a mixin factory to reference "
    "Django settings and pass the values through to an object's "
    "__init__ method. If the setting can't be found it falls back to "
    "a default value."
)

setuptools.setup(
    name='django-setting-mixins',
    version='0.1.0',
    packages=['setting_mixins'],
    description='Factories to pass settings to objects as kwargs.',
    long_description=long_description,
    author='Jace Petkau',
    author_email='jacinator@outlook.com',
    url='https://github.com/jacinator/django-setting-mixins/',
    license='MIT',
    install_requires=[
        'Django>=2.1',
    ],
    extras_require={
        'testing': [
            'flake8>=3.7.7',
            'isort>=4.3.15',
            'coverage>=4.5.3',
        ],
    },
)
