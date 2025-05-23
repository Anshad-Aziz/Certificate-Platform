# certificate_platform/settings.py
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'your-secret-key-here'  # Change this to a secure random value in production
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Update with domain in production
AUTH_USER_MODEL = 'authentication.CustomUser'
SITE_URL = 'http://127.0.0.1:8000' 
# Application definition
INSTALLED_APPS = [
    'authentication',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Project apps
    'subscriptions',
    'template_manager',
    'candidates',
    'certificates',
    'verification',
    'dashboard',
    'admin_panel',
    # Third-party apps
    'django_filters',  # For search/filter functionality
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

ROOT_URLCONF = 'certificate_platform.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Project-level templates (e.g., base.html)
        'APP_DIRS': True,  # Enable app-specific templates
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

WSGI_APPLICATION = 'certificate_platform.wsgi.application'

# Database configuration (MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'certificate_platform',
        'USER': 'root',  
        'PASSWORD': 'Anshad@2003',  
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}




# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'  # Adjust to your preferred timezone (e.g., 'America/New_York')
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directory for static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For collectstatic in production

# Media files (Uploaded files: logos, templates, QR codes, PDFs)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom settings for the project
LOGIN_URL = '/auth/login/'  # Redirect unauthenticated users to login
LOGIN_REDIRECT_URL = '/dashboard/'  # Redirect after login
LOGOUT_REDIRECT_URL = '/auth/login/'  # Redirect after logout

# Email configuration (for bonus auto-email feature)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Example: Gmail SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'anshadaziz99@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'Anshad@2003'  # Replace with your email password

# Site URL for QR codes
SITE_URL = 'http://localhost:8000'  # Update to production domain

# Messages framework styling (for Bootstrap alerts)
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

