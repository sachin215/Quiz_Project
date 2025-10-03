import os
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dinga.settings') # Setup Django 
django.setup()
from first_page.models import  Question

for i in Question.objects.all()[51:]:
    i.category='SQL'
    i.save()