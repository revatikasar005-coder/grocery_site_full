import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grocery_site_full.settings')
application = get_wsgi_application()
