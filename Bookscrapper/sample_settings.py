# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''  # ==> set secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ''  # ==> set DEBUG specification True or Not

ALLOWED_HOSTS = []  # ==> if you run project on production environment , you should fill this section


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# if you use sqlite3 :
DATABASES = {
    "default": {
        "ENGINE": "",
        "NAME": "",
    }
}

# if using others :
DATABASES = {
    "default": {
        "ENGINE": "",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}