ZDE JE POPIS PROJEKTU
## Sylabus
### 27. května 2025
 - Úvod projektu
 - Vytvoření projektu

## Django
### Instalace

''' bash
pip install django
pip freeze > requirements.txt
django-admin startproject <nazev_projektu> .
'''

### Struktura projektu
- 'hollymovies' - složka projektu (obsahuje informace o celém projektu
  - '__init__.py' - je zde jen proto, aby daná složka byla package
  - 'asgi.py' - nebudeme potřebovat
  - 'settings.py' - nastavení projektu
  - 'urls.py' - zde jsou nastavené url adresy
  - 'wsgi.py' - nebudeme potřebovat
  - 'manage.py' - hlavní skript pro práci s projektem (spouštění serveru, testů, migrací, ...)

### Spuštění serveru
''' bash
python manage.py runserver
'''

### Vytvoření superuživatele
'''bash
python manage.py createsuperuser
'''

### .env
slouží k ukládání citlivých informací (SECRET_KEY, hesla, přístupové údaje..)

### Instalace
''' bash
pip install python-dotenv
pip freeze > requirements.txt
''''

Vytvoříme soubor s názvem ".env" v kořenovém adresáři projektu

Do souboru 'settings.py' vložíme:
'''python
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure-@#0uqgasfgasdffxcvxc@4#y-hgaf4d65f4asdfsd2^j5o5ddk7x)')

### .gitignore
Správny projekt má nastavení pro ignorované soubory v git repozitáři v souboru '.gitignore'.

'''git
/.idea
*.pyc
/db.sqlite3
/.env
'''

### Aplikace
### Vytvoření
'''bash
python manage.py startapp <název_aplikace>
'''

### Struktura aplikace
- 'viewer' - složka aplikace
  - 'migrations' - složka obsahující migrační skripty
  - '__init__.py' - je tu zde jen proto, aby daná složka byla package
  - 'admin.py' - nastavení administrační stránky
  - 'apps.py' - nastavení aplikace - nebudeme upravovat
  - 'models.py' - zde bude definice modelů (databáze)
  - 'tests.py' - zde budou views(funkcionalita)


### Registrace aplikace
Do souboru 'settings.py' musíme novou aplikaci zaregistrovat do seznamu

"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'viewer',
]

### Vytvoření superuživatele
'''bash
python manage.py createsuperuser
''''