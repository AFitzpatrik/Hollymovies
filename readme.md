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

#vytvoření superuživatele
''' bash
python manage.py createsuperuser
'''

### .env
slouží k ukládání citlivých informací (SECRTE_KEY, hesla, přístupové údaje..)

### Instalace
''' bash
pip install python-dotenv
''''
