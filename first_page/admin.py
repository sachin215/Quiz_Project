from django.contrib import admin
from first_page.models import   Question,Choice,User_Registry

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User_Registry)