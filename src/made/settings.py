import os


def dirup( path, steps ):
    d = path
    for i in range(steps):
        int(i) # suppress warning
        d = os.path.abspath( os.path.dirname(d) )

    return d


def subpath(path, entry):
    return os.path.abspath(os.path.join(path, entry))


ROOT_DIR = dirup(__file__, 3)

subroot = lambda x: subpath(ROOT_DIR, x)

SECRET_KEY = 'should be redefined in production'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    )

ROOT_URLCONF = 'made.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
]

WSGI_APPLICATION = 'made.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': subroot('db/db.sqlite3'),
    }
}

LANGUAGE_CODE = 'ru-Ru'  # set to appropriate one

TIME_ZONE = 'Europe/Moscow'  # set to appropriate one

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = subroot('static_content/media/')

MEDIA_URL = '/media/'

STATIC_ROOT = subroot('static_content/static/')

STATIC_URL = '/static/'

MAIN_LOG_FILE = subroot('logs/made_project.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'regular': {
            'format': '%(levelname)s %(asctime)-15s Process "%(processName)s": %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
         'null': {
            'level': 'INFO',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'regular'
        },
        'file':{
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': MAIN_LOG_FILE,
            'formatter': 'regular'
        },
    },
    'loggers': {
        'main': {
            'handlers': ['console', 'file',],
            'level': 'DEBUG',
        }
    }
}

# AUTH_USER_MODEL = 'accounts.User'

# EMAIL_HOST = "smtp.yandex.ru"
# EMAIL_PORT = "587"
# EMAIL_HOST_USER = "example@yandex.ru"
# EMAIL_HOST_PASSWORD = "example"
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = 'example@yandex.ru'
# EMAIL_USE_TLS = True
