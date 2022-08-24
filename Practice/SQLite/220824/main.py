import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

genre = Genre()
genre.title = '액션'
genre.save()

genre = Genre()
genre.title = '드라마'
genre.save()