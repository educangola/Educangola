
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os
import dj_database_url
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3o1kdr_xi3whqs618fafoy@!(^bj*d04plqzwsa8@iyrvr97vf'

DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'localflavor',
    'channels',
    # Apps customizados
    'instituicoes',
    'cursos',
    'noticias',
    'usuarios',
    'core',
    'biblioteca',
    'forum',
    'hackathons',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ANGOLA_EDUCA.urls'

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

WSGI_APPLICATION = 'ANGOLA_EDUCA.wsgi.application'
ASGI_APPLICATION = 'ANGOLA_EDUCA.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_educangola',  
        'USER': 'admin_muquissi',  
        'PASSWORD': 'Django1234',  
        'HOST': 'localhost',  
        'PORT': '5432', 
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'Africa/Luanda'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('pt-br', _('Português')),
    ('en', _('Inglês')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Direção dos arquivos estáticos (CSS, JS)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'erros.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'muquissicarlos@gmail.com'  
EMAIL_HOST_PASSWORD = 'uruj ywep dyee sfmg'  # Substitua com a senha de aplicativo gerada
DEFAULT_FROM_EMAIL = 'muquissicarlos@gmail.com'

JAZZMIN_SETTINGS = {
    "site_title": "Painel Administrativo",
    "site_header": "Educangola",
    "site_brand": "Dashboard",
    "site_logo": "assets/img/Artboard 1.png",  
    "welcome_sign": "Bem-vindo ao Painel",
    "copyright": "© 2024 Educangola",
    
    "show_sidebar": True,
    "navigation_expanded": True,
    
    "icons": {
        "usuarios.Usuario": "fas fa-user",  
        "auth.Group": "fas fa-users",  
        "auth.User": "fas fa-user",   
        "instituicoes.Categoria": "fas fa-tags",  
        "instituicoes.Instituicao": "fas fa-university", 
        "instituicoes.SeguirInstituicao": "fas fa-heart", 
        "instituicoes.Curso": "fas fa-chalkboard-teacher", 
        "instituicoes.Inscricao": "fas fa-clipboard-check", 
        "instituicoes.PerfilInstituicao": "fas fa-building",  
        "instituicoes.Postagem": "fas fa-newspaper", 
        "instituicoes.DadosUpload": "fas fa-upload", 
        "biblioteca.CategoriaBiblioteca": "fas fa-tags", 
        "biblioteca.Biblioteca": "fas fa-book-reader",
        "biblioteca.Livro": "fas fa-book", 
        "biblioteca.UsuarioBiblioteca": "fas fa-user-circle", 
        "biblioteca.Emprestimo": "fas fa-bookmark",  
        "biblioteca.Tese": "fas fa-graduation-cap", 
        "biblioteca.ConsultoriaTCC": "fas fa-chalkboard-teacher",  
        "biblioteca.EmprestimoTese": "fas fa-book-open",
        "hackathons.Hackathon": "fas fa-trophy",  
        "hackathons.Participante": "fas fa-user-friends",  
        "hackathons.Equipe": "fas fa-users",  
        "hackathons.Desafio": "fas fa-flag-checkered", 
        "hackathons.Submissao": "fas fa-upload", 
        "hackathons.Avaliacao": "fas fa-star", 
        "forum.Forum": "fas fa-comments",  
        "forum.Postagem": "fas fa-file-alt",  
        "forum.Comentario": "fas fa-comment", 
        "mentoria.Mentor": "fas fa-user-tie",  
        "mentoria.Mentee": "fas fa-user-graduate", 
        "mentoria.SessaoMentoria": "fas fa-calendar-alt", 
        "mentoria.Feedback": "fas fa-comment-dots",  
        "mentoria.Agendamento": "fas fa-clock",  


    },
    
   
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Documentação", "url": "https://docs.djangoproject.com", "new_window": True},
    ],
    "user_avatar": None,  
    "search_model": ["auth.User", "instituicoes.Curso"],
}


# settings.py

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)], 
        },
    },
}
