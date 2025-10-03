import json
import os
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dinga.settings') # Setup Django 
django.setup()
from first_page.models import Question, Choice
with open('quiz2.json') as f:
    data = json.load(f)

# for i in data['Questions'].values():
#     Question.objects.create(question_text=i,category='SQL')
n=len(Choice.objects.all())+1
for k,v in data['choice'].items() :
    # print(data['Questions'][k],v)
    Choice.objects.create(choice_id=int(k)+n,choice_text=v,answer=data['Answer'][k])
