"""
Django settings for foodlovers project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pusher import Pusher
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kh17=r**+g6zcq0z@################7fes$a$yz#&!y^%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_HTTPONLY = True
#X_FRAME_OPTIONS ='DENY'
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_BROWSER_XSS_FILTER = True


#PUSHER_APP_ID = "145081"
#PUSHER_KEY = "3d7b9976c49adb9da6f6"
#PUSHER_SECRET = "b2e3f7afd75f11c4c563"


#p=Pusher(app_id='145081', key='3d7b9976c49adb9da6f6', secret='b2e3f7afd75f11c4c563',ssl=True,
 # port=443)
#p.trigger('test_channel', 'my_event', {'message': 'hello world'})
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites',
	'appusers',
	'photobucket',
	'django_facebook',
    #'photologue',
     'sortedm2m',
	'social.apps.django_app.default',
    'friends',
    #'notification',
    'postman',
  #  'pusherable',
)

POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_NOTIFIER_APP = None

SITE_ID = 1
REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/home/' # The page you want users to arrive at after they successful log in
LOGIN_URL = '/login/'  # The page users are directed to if they are not logged in,
                                                                # and are trying to access pages requiring authentication

AUTH_USER_MODEL = 'appusers.MyUser'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
	 'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'foodlovers.urls'

WSGI_APPLICATION = 'foodlovers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
        'NAME': 'food',
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD':'himank',
        'PORT':3306 ,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

TEMPLATE_DIRS=(os.path.join(BASE_DIR,'templates'),)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
		'django_facebook.context_processors.facebook',
		'social.apps.django_app.context_processors.backends',
		'social.apps.django_app.context_processors.login_redirect',
		'django_facebook.context_processors.facebook',
		
)

AUTHENTICATION_BACKENDS = (
'social.backends.facebook.FacebookOAuth2',
'social.backends.google.GoogleOAuth2',
'social.backends.twitter.TwitterOAuth',
'django.contrib.auth.backends.ModelBackend',
'django_facebook.auth_backends.FacebookBackend',
'django.contrib.auth.backends.ModelBackend',
'social_auth.backends.facebook.FacebookBackend',
)
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_FACEBOOK_KEY ='##############'
SOCIAL_AUTH_FACEBOOK_SECRET ='3642##########1d320d7025e79cc7'
FACEBOOK_APP_ID='1#########6'
FACEBOOK_APP_SECRET='3##############37'


#EMAIL CONFIGURATION
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rkap95@gmail.com'
EMAIL_HOST_PASSWORD = '#####'
DEFAULT_FROM_EMAIL = 'rkap95@gmail.com'
DEFAULT_TO_EMAIL = 'coochy95@gmail.com'




