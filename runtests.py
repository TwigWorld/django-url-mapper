import django

from django.conf import settings
from django.core.management import call_command

settings.configure(

    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'urlmapper'
    ),

    STATIC_URL='/',
    MIDDLEWARE_CLASSES=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
    ),
    ROOT_URLCONF='urlmapper.tests.urls',
    SITE_ID=1,

    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],

    URLMAPPER_KEYS=[
        'test_1',
        'test_2',
        'test_3',
        'test_4',
        'test_5'
    ],
    URLMAPPER_FUNCTIONS={
        'test_1': lambda: 'test_1_success',
        'test_2': lambda request: 'test_2_success'
    },
)
django.setup()

call_command('test')
