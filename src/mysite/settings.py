from pathlib import Path
import os # 추가한 부분

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yk)2$z9!d2hu0jq)j61+_&k8^*#o-0f9setlbx2(52jby1vuj2'
# SECURITY WARNING: don't run with debug turned on in production!

## True로 세팅하면 개발모드, False로 세팅하면 운영모드
## False인 운영모드인 경우 아래 ALLOWED_HOSTS 리스트에 반드시
## 서버의 IP나 도메인을 지정해야 함
## True인 개발 모드인 경우는 'localhost', '127.0.0.1'로 간주함
DEBUG = True

ALLOWED_HOSTS = ['*']

# ALLOWED_HOSTS = '*'

# Application definition
## 새로운 앱이 만들어 지면 이 자리에 등록해야 함!

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #추가한 부분(, 반드시 추가)
    'bookmark.apps.BookmarkConfig',
    'blog.apps.BlogConfig',
    'taggit.apps.TaggitAppConfig',
    'taggit_templatetags2',
    'polls.apps.PollsConfig',
    'photo.apps.PhotoConfig',
    'widget_tweaks',
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'
    
## 프로젝트의 템플릿 파일이 위치할 디렉토리를 지정 (N V T == MVC)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')], ## os패키지를 임포트해야함
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # 리프레쉬하면 db폴더가 만들어짐
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr' # 'en-us'

TIME_ZONE = 'Asia/Seoul' # 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True # 타임존을 사용할 지 여부를 결정


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
## 장고가 자동으로 만든 static들의 경로
STATIC_URL = '/static/'
## 우선적으로 사용할 임의의 경로

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

## 추가
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

TAGGIT_CASE_INSENSITIVE = True
TAGGIT_LIMIT = 50

DISQUS_SHORTNAME = 'chlgus0719mysite'
DISQUS_MY_DOMAIN = 'https://192.168.0.238'

