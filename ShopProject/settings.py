"""
Django settings for ShopProject project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import django_heroku
from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wzm!-gpx0&*xgpkbvbted&_s%i+9)wb=twv$yd-c7cx6lte853'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['https://madukashop-production.up.railway.app',
#                  'https://madukashop-production.up.railway.app/admin/login/']
# CSRF_TRUSTED_ORIGINS = ['https://madukashop-production.up.railway.app/admin/login/']

CSRF_TRUSTED_ORIGINS = [
    'https://madukaonline.co.ke',
    # 'http://localhost:3000'
]
# Application definition


INSTALLED_APPS = [
    'shopapp',
    'ShopUser',
    'cms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'django.contrib.humanize',

    'phonenumber_field',
    # 'CustomUser',
    'django_filters',
    'rest_framework',
    
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_seo_js',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django_seo_js.middleware.EscapedFragmentMiddleware',  # If you're using #!
    'django_seo_js.middleware.UserAgentMiddleware',# If you want to detect by user agent
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    # "django.middleware.common.CommonMiddleware",
]



ROOT_URLCONF = 'ShopProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'ShopProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': '1cHGQ3TnjKfL8gWocriA',
#         'HOST': 'containers-us-west-40.railway.app',
#         'PORT': '6298',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }


"""===============================Start of Production database configuration=============================="""

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'mashop',

        'USER': 'postgres',

        'PASSWORD': 'madukaat2023',

        'HOST': 'mashop.ckp6xx54qapt.eu-central-1.rds.amazonaws.com',

        'PORT': '5432',

    }

}


"""=====================================End of Product database configuration============================================== """


"""============================Start of Local Database Configuration========================================================"""

# DATABASES = {
#     'default': {

#         'ENGINE': 'django.db.backends.postgresql',

#         'NAME': 'MadukaShop',

#         'USER': 'postgres',

#         'PASSWORD': '33016460d',

#         'HOST': 'localhost',

#         'PORT': '5432',
        

#     }

# }


""" =============================End of Local Database Configuration==================================== """

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/images/'


MEDIA_ROOT = BASE_DIR / 'static/images'

""" =============================Production AWS Storages================================= """


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_QUERYSTRING_AUTH = False

AWS_ACCESS_KEY_ID = 'AKIA53IMYZT7SVG7XVSR'
AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'maduka-shop'




"""============================End of production AWS settings=========================== """




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {

        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}


AUTH_USER_MODEL = 'ShopUser.CustomUser'



CORS_ALLOW_CREDENTIALS: True

CORS_ALLOWED_ORIGINS = [
    'https://madukaonline.co.ke',
]




REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}


SIMPLE_JWT = {
  # It will work instead of the default serializer(TokenObtainPairSerializer).
  "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.MyTokenObtainPairSerializer",
  # ...
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
 
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

