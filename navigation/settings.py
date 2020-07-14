# coding: utf8
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.contrib.messages import constants as message_constants
"""
Django settings for navigation project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^ol2c9_7cv(awauraw5z3bong2ya1=gzewue6bez*nzu^iq1nf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'widget_tweaks',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'navigation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'navigation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DBNAME' ] or '',
        'USER': os.environ['DBUSER'] or '',
        'PASSWORD': os.environ['DBPASSWORD'] or '',
        'HOST': os.environ['DBHOST'] or '127.0.0.1',
        'PORT': os.environ['DBPORT'] or '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# 支持中文
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'

# 时区修改
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False

USE_TZ = True

MESSAGE_TAGS = {
    message_constants.SUCCESS: 'alert alert-success',
    message_constants.ERROR: 'alert alert-danger',
}


# suit在admin里设置时间的一个小bug。需要把时间格式指定一下
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


STATIC_URL = '/static/'

# 支持静态文件

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# STATICFILES_FINDERS = (
#   'django.contrib.staticfiles.finders.FileSystemFinder',
#   'django.contrib.staticfiles.finders.AppDirectoriesFinder',)

# django版本的原因需要添加的


TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# django-suit配置相关信息

SUIT_CONFIG = {
    'ADMIN_NAME': u'导航系统内部管理',
    'LIST_PER_PAGE': 10,
    'MENU': ({'label': u'导航管理',
              'app': 'app',
              'icon': 'icon-cog',
              'models': ('UrlGroup',
                         'UrlInfor')},
             {'label': u'用户管理',
              'app': 'app',
              'icon': 'icon-user',
              'models': ('auth.User',
                         'auth.Group')}
             ),

    # 每一个字典表示左侧菜单的一栏
    # label表示name，app表示上边的install的app，models表示用了哪些models
}
