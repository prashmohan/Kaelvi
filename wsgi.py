from django.core.handlers.wsgi import WSGIHandler
import os
import pinax.env
import sys
sys.path.append('/var/www/Kaelvi')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Kaelvi.settings'

# setup the environment for Django and Pinax
pinax.env.setup_environ(__file__)


# set application for WSGI processing
application = WSGIHandler()
